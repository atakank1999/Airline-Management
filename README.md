# Airline Management System

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/airline-management.git
   cd airline-management
   ```
2. **Set up the environment variables:**
   - Copy the example environment file and update it with your configuration.
   ```bash
   cp .env.example .env
   ```

3. **Apply the migrations:**
   ```bash
   docker compose run --rm web python manage.py migrate
   ```

4. **Load initial data (optional):**
   ```bash
   docker compose run --rm web python manage.py loaddata airplanes_dump.json #insert dummy airplane data
   docker compose run --rm web python manage.py loaddata flights_dump.json #insert dummy flight data
   docker compose run --rm web python manage.py loaddata reservations_dump.json #insert dummy reservation data
   ```

7. **Run the development server:**
   ```bash
   docker compose up --build
   ```
8. **Import Postman collection to test the API**

## Usage

- Access the application at `http://127.0.0.1:8000/`.
