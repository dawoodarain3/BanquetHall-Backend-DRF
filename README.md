# BanquetHall-Backend-DRF

## Overview
**BanquetHall-Backend-DRF** is a backend project designed to manage user details, banquet hall information, and event bookings. It provides a RESTful API built using Django REST Framework (DRF) for seamless integration with frontend systems.

---

## Features

### 1. User Management
- Collect user details, including:
  - Name
  - City
  - CNIC number (validated for proper format and uniqueness).
  - CNIC pictures (optional, supports image uploads).

### 2. Banquet Management
- Manage banquet halls with:
  - Name
  - Description
  - Hall pictures (optional, supports image uploads).

### 3. Booking Management
- Book events with:
  - Start and end times (validation ensures start time is earlier than end time).
  - Advance and total payment details.
  - Automatic checks to prevent overlapping bookings for the same banquet hall.
- Enforces unique constraints for bookings with the same banquet and time range.

### 4. Admin Features
- Easy-to-use Django Admin panel for managing:
  - User details
  - Banquet details
  - Bookings

---

## API Endpoints

### Base URL
```
http://127.0.0.1:8000/api/
```

### Endpoints

#### **Users**
- `GET /users/` - List all users.
- `POST /users/` - Create a new user.

#### **Banquets**
- `GET /banquets/` - List all banquet halls.
- `POST /banquets/` - Create a new banquet hall.

#### **Bookings**
- `GET /bookings/` - List all bookings.
- `POST /bookings/` - Create a new booking.

---

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/banquet-hall-backend-drf.git
   cd banquet-hall-backend-drf
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the API:**
   Navigate to `http://127.0.0.1:8000/api/` to interact with the API.

---

## Validation Rules

1. **CNIC Number Validation:**
   - Must be 13 digits long with two dashes: one after the first 5 digits and one before the last digit (e.g., `12345-1234567-1`).

2. **Booking Time Validation:**
   - `start_time` must be earlier than `end_time`.
   - Overlapping bookings for the same banquet hall are not allowed.

---

## Directory Structure
```
BanquetHall-Backend-DRF/
├── bookings/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
├── settings.py
└── ...
```

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
