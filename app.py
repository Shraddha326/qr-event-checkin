import os
import uuid
from datetime import datetime

import qrcode
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    jsonify,
    flash,
)

from database import get_db, init_db


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
QR_FOLDER = os.path.join(APP_ROOT, "static", "qrcodes")
os.makedirs(QR_FOLDER, exist_ok=True)


app = Flask(__name__)
app.secret_key = "change-this-secret-key"


@app.route("/")
def index():
    conn = get_db()
    events = conn.execute(
        "SELECT * FROM events ORDER BY event_date"
    ).fetchall()
    conn.close()

    return render_template("index.html", events=events)


@app.route("/events/create", methods=["GET", "POST"])
def create_event():
    if request.method == "POST":
        title = request.form["title"].strip()
        event_date = request.form["event_date"]
        location = request.form["location"].strip()

        if not title or not event_date or not location:
            flash("All fields are required.")
            return redirect(url_for("create_event"))

        conn = get_db()
        conn.execute(
            "INSERT INTO events (title, event_date, location) VALUES (?, ?, ?)",
            (title, event_date, location),
        )
        conn.commit()
        conn.close()

        flash("Event created successfully.")
        return redirect(url_for("index"))

    return render_template("create_event.html")


@app.route("/register/<int:event_id>", methods=["GET", "POST"])
def register(event_id):
    conn = get_db()

    event = conn.execute(
        "SELECT * FROM events WHERE id = ?",
        (event_id,),
    ).fetchone()

    if event is None:
        conn.close()
        flash("Event not found.")
        return redirect(url_for("index"))

    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip()

        if not name or not email:
            flash("Name and email are required.")
            return redirect(url_for("register", event_id=event_id))

        code = uuid.uuid4().hex

        conn.execute(
            """
            INSERT INTO registrations
            (event_id, name, email, code)
            VALUES (?, ?, ?, ?)
            """,
            (event_id, name, email, code),
        )

        conn.commit()

        # Generate a QR code image that encodes
        # only the unique registration code.
        qr_img = qrcode.make(code)
        qr_img.save(
            os.path.join(QR_FOLDER, f"{code}.png")
        )

        conn.close()

        return redirect(url_for("ticket", code=code))

    conn.close()

    return render_template(
        "register.html",
        event=event,
    )


@app.route("/ticket/<code>")
def ticket(code):
    conn = get_db()

    reg = conn.execute(
        """
        SELECT registrations.*, events.title,
               events.event_date, events.location
        FROM registrations
        JOIN events
            ON registrations.event_id = events.id
        WHERE registrations.code = ?
        """,
        (code,),
    ).fetchone()

    conn.close()

    if reg is None:
        flash("Registration not found.")
        return redirect(url_for("index"))

    return render_template(
        "ticket.html",
        reg=reg,
    )


@app.route("/scan")
def scan():
    conn = get_db()

    events = conn.execute(
        "SELECT * FROM events ORDER BY event_date"
    ).fetchall()

    conn.close()

    return render_template(
        "scan.html",
        events=events,
    )


@app.route("/checkin/<code>", methods=["POST"])
def checkin(code):
    conn = get_db()

    reg = conn.execute(
        "SELECT * FROM registrations WHERE code = ?",
        (code,),
    ).fetchone()

    if reg is None:
        conn.close()

        return jsonify({
            "status": "error",
            "message": "Invalid QR code.",
        }), 404

    if reg["checked_in"]:
        conn.close()

        return jsonify({
            "status": "already",
            "message": (
                f"{reg['name']} was already checked in "
                f"at {reg['checkin_time']}."
            ),
        })

    now = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    conn.execute(
        """
        UPDATE registrations
        SET checked_in = 1,
            checkin_time = ?
        WHERE code = ?
        """,
        (now, code),
    )

    conn.commit()
    conn.close()

    return jsonify({
        "status": "success",
        "message": (
            f"{reg['name']} checked in successfully "
            f"at {now}."
        ),
    })


@app.route("/attendance/<int:event_id>")
def attendance(event_id):
    conn = get_db()

    event = conn.execute(
        "SELECT * FROM events WHERE id = ?",
        (event_id,),
    ).fetchone()

    registrations = conn.execute(
        """
        SELECT * FROM registrations
        WHERE event_id = ?
        ORDER BY name
        """,
        (event_id,),
    ).fetchall()

    conn.close()

    if event is None:
        flash("Event not found.")
        return redirect(url_for("index"))

    return render_template(
        "attendance.html",
        event=event,
        registrations=registrations,
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
