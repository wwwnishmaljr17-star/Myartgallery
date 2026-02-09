# Art Gallery Project

A modern, Django-based Art Gallery application featuring a sophisticated artist dashboard, product management, and engagement tools.

## Key Features

- **Artist Dashboard**: A fully overhauled, premium UI for artists to manage their profile, posts, products, and schedules.
- **Product Management**: Card-based UI for effortless product listing with INR (₹) currency support.
- **Gallery Posts**: Modernised gallery management with engagement tracking (Likes & Comments).
- **Communication Flow**: Integrated chat system for artists and users.
- **Secure Authentication**: Protected artist views and secure password management.

## Tech Stack

- **Backend**: Django 5.1.3
- **Frontend**: HTML5, Vanilla CSS, Bootstrap 4, FontAwesome
- **Database**: MySQL
- **Tooling**: Git for version control

## Recent Updates

- Overhauled all artist-facing templates for UI consistency.
- Resolved legacy comment issues and rogue characters.
- Fixed backend logic errors and optimized data privacy for artists.
- Standardized currency to ₹ (INR).

## Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/wwwnishmaljr17-star/Myartgallery.git
   ```
2. Install dependencies (ensure `venv` is active):
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the server:
   ```bash
   python manage.py runserver
   ```
