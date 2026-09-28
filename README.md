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
<img width="750" height="354" alt="homepahe pnj" src="https://github.com/user-attachments/assets/bb548895-d5d1-4382-9772-afab49c0ab0a" />
<img width="750" height="354" alt="homepahe pnj" src="https://github.com/user-attachments/assets/99c5cfba-f6a2-4ca5-8492-6144158aaf4d" />
<img width="750" height="354" alt="homepahe pnj" src="https://github.com/user-attachments/assets/7a73fa9e-07b7-4808-a94c-80f5f5a6d1a8" />
