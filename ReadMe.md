
# Note App

Виконання тестового завдання із створення додатку з нотатками.


## Requirements

- All requirements are written down in requirements.txt file


## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/fifumain/notes.git
    cd notes
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate     # For Windows
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure the database. (ENV DATA GIVEN FOR TEST PURPOSES ONLY, DJANGO DATA ALSO GIVEN FOR TEST PURPOSES, KEEP SECRET KEY IN ENV!!!!) `.envs/.postgres`:

    ```python
    POSTGRES_HOST=postgres
	POSTGRES_PORT=5432
	POSTGRES_DB=notes_db
	POSTGRES_USER=postgres
	POSTGRES_PASSWORD=postgres
	DATABASE_URL=postgres://postgres:postgres@postgres:5432/notes_db
    ```

    For Redis, use the default settings or configure it as needed.

5. Run database migrations:

    ```bash
    make makemigrations
    make migrate
    ```

6. Create a superuser for the admin panel (optional):

    ```bash
    make superuser
    ```

7. Start the development server:

    ```bash
    make build
    ```

## Usage

- Go to `http://0.0.0.0:8080/admin/` to log into the admin panel and manage notes.
- You can create, edit, and delete notes via the admin panel or the API.
- All note-related actions will automatically update the Redis cache for efficient data retrieval.

## Testing - 80+% COVERAGE

To run the tests, use `make test`:

## API Documentation

This project integrates **Swagger** to provide automatic API documentation. Swagger makes it easy for developers to explore and understand the available API endpoints.


#### Accessing the Swagger UI

To view the Swagger-generated API documentation, navigate to the following URL in your browser after running the project locally:

  ``` bash
   http://0.0.0.0:8080/api/docs/
   ```
   
## Contact Information

Для звʼязку є

- **Email**: [pustovoitenkofilip@gmail.com](mailto:pustovoitenkofilip@gmail.com)
- **Telegram**: @fifumain


