# QR Code Generator for Event Check-ins

## Problem Statement
Build an application that lets an organizer create and manage events, lets attendees
register for an event and receive a unique QR code, and lets staff scan that QR code
at the entrance to record attendance in real time.

## Assigned Feature Set
Event registration, generate unique QR codes, QR code scanning, check-in status,
attendance list, create/manage events, display QR code, record check-in.

## Features Implemented
- Create and list events
- Attendee registration with unique QR code generation
- QR code display on a ticket page
- Camera-based QR code scanning in the browser
- Automatic check-in recording with duplicate-scan protection
- Attendance list with live check-in status per event

## Technologies Used
Python, Flask, SQLite, qrcode (Pillow), HTML5, CSS3, JavaScript (html5-qrcode)

## AI Tools Used
Claude (Anthropic)

## Important AI Prompts / AI Usage
- Designed the database schema for events and registrations
- Generated the Flask routes for registration, QR generation and check-in
- Generated the browser-based QR scanning integration
- Used to review the final code for bugs before submission

## Instructions to Run the Project
1. python -m venv venv && activate it
2. pip install -r requirements.txt
3. python app.py
4. Open http://127.0.0.1:5000

## Screenshots of the Working Project
See the screenshots folder in this repository.
<img width="750" height="354" alt="homepahe pnj" src="https://github.com/user-attachments/assets/7a73fa9e-07b7-4808-a94c-80f5f5a6d1a8" />
<img width="756" height="409" alt="register pnj" src="https://github.com/user-attachments/assets/405e1a88-324c-4b9b-b0be-1fcc69d3c90d" />
<img width="779" height="523" alt="qrcode pnj" src="https://github.com/user-attachments/assets/0de1223f-aaeb-4942-8330-809c35477ad8" />
<img width="885" height="410" alt="checkin pnj" src="https://github.com/user-attachments/assets/b4038525-89e2-4ef2-a0ab-957b989b381c" />
<img width="1101" height="245" alt="attendace pnj" src="https://github.com/user-attachments/assets/5931b129-e5f1-41bf-9704-8aefc39a3bae" />

