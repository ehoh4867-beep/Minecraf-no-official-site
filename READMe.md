# Minecraft Themed Landing Page

This is a branded landing page for a Minecraft movie event. It was built with Flask and is designed to collect ticket requests, showcase an immersive game-themed interface, and demonstrate full-stack development skills.

## How to Get Your Formspree Key
1. Go to formspree.io.
2. Create a new form and name it (e.g., "Minecraft Tickets").
3. After creation, you will receive a unique endpoint link like: `https://formspree.io/f/your-key`.
4. Copy this key.

## Where to Insert the Key
In `index.html`, locate the form element:
`<form id="modEvent" class="modal" action="https://formspree.io/f/your-key-here" method="POST">`
Replace `your-key-here` with your actual Formspree key.

## Stack
- Python (Flask)
- HTML / CSS
- JavaScript
- Formspree (form handling)

## How to Run Locally
1. Ensure Python and Flask are installed.
2. Place `app.py` and `index.html` in the same folder.
3. Run in the terminal: `python app.py`
4. Open your browser and go to: `http://127.0.0.1:5185`

## Purpose
This project was created to demonstrate:
- Building a functional landing page with a Flask backend.
- Embedding a modal form with
 working Formspree integration.
- Designing a themed visual experience with CSS and game-inspired assets.

## Status
The landing page is fully functional. The form sends submissions to Formspree, and the Telegram and VK buttons can be linked to real communities or services.
IMPORTANT, FILE index.html MUST BE IN FOLDER C app.py
!!!!! NOT AN OFFICIAL MOJANG PRODUCT!!!!