# Congress API Application

This application fetches data about US Congress bills and members from the [Congress API](https://api.congress.gov/) and stores it in a MongoDB database. It provides a FastAPI-based API to access this data.

## Features

*   **Data Fetching:**
    *   Fetches recent bills from the Congress API.
    *   Fetches members of Congress from the Congress API.
*   **Data Storage:**
    *   Stores fetched data in a MongoDB database (MongoDB Atlas is recommended).
*   **API Endpoints:**
    *   `/bills`: Returns a list of recent bills.
    *   `/members`: Returns a list of members of Congress.
*   **Scheduled Updates:**
    *   Uses `apscheduler` to automatically update the data every day at midnight.
* **Startup Update:**
    * Updates the data when the app starts.
*   **Logging:**
    *   Includes detailed logging to help with debugging.
* **Environment variables:**
    * Uses environment variables to avoid hardcoding values.

## Prerequisites

*   **Python 3.8+**
*   **MongoDB Atlas Account:** A free tier account is sufficient for development.
*   **Congress API Key:** You'll need an API key from the Congress API (it's free).

## Setup

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd congressapp
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    Or if you are using anaconda:
    ```bash
    conda create --name congressapp python=3.12
    conda activate congressapp
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    Or if you don't have a `requirements.txt` file:
    ```bash
    pip install fastapi uvicorn motor python-dotenv apscheduler requests
    ```
    Or if you are using anaconda:
    ```bash
    conda install fastapi uvicorn motor python-dotenv apscheduler requests
    ```

4.  **Create a `.env` File:**
    *   Create a file named `.env` in the root directory of the project.
    *   Add the following lines, replacing the placeholders with your actual values:

    ```
    MONGODB_URI=mongodb+srv://<your-username>:<your-password>@<your-cluster-name>.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
    CONGRESS_API_KEY=<your-congress-api-key>
    CONGRESS_API_URL=https://api.congress.gov/v3
    ```
    *   **`MONGODB_URI`:** Your MongoDB Atlas connection string.
    *   **`CONGRESS_API_KEY`:** Your Congress API key.
    * **`CONGRESS_API_URL`:** The Congress API base URL.

5.  **MongoDB Atlas Setup:**
    *   Create a MongoDB Atlas cluster (a free tier is sufficient).
    *   Create a database user with read and write access.
    *   Whitelist your IP address in the "Network Access" settings.
    *   Get the connection string and put it in your `.env` file.

## Running the Application

1.  **Activate the Virtual Environment:**
    ```bash
    source venv/bin/activate
    ```
    Or if you are using anaconda:
    ```bash
    conda activate congressapp
    ```

2.  **Load Environment Variables:**
    ```bash
    source .env
    ```

3.  **Run the Application:**
    ```bash
    uvicorn main:app --reload
    ```

4.  **Access the API:**
    *   Open your web browser or a tool like Postman.
    *   Go to `http://127.0.0.1:8000/docs` to access the Swagger UI.
    *   Go to `http://127.0.0.1:8000/members` to access the members endpoint.
    *   Go to `http://127.0.0.1:8000/bills` to access the bills endpoint.

## Checking the Database

1.  **MongoDB Atlas Dashboard:**
    *   Go to your MongoDB Atlas dashboard.
    *   Go to "Browse Collections."
    *   You should see the `congress_api_db` database and the `bills` and `members` collections.

## Cron Job

*   The `cron_job.py` file contains the code for the scheduled data updates.
*   The `update_data()` function fetches data from the Congress API and saves it to MongoDB.
*   The `start_scheduler()` function uses `apscheduler` to schedule `update_data()` to run every day at midnight.
* The `main.py` file starts the cron job when the app starts.
* The `main.py` file also updates the data when the app starts.

## Logging

*   The application includes detailed logging to help with debugging.
*   Log messages are printed to the console.
*   You can adjust the logging level in the code if needed.

## Code Structure

*   **`main.py`:** The main FastAPI application file.
*   **`cron_job.py`:** Contains the code for the scheduled cron job.
*   **`database.py`:** Handles the MongoDB connection and database operations.
*   **`congress_api.py`:** Handles fetching data from the Congress API.
*   **`models.py`:** Defines the Pydantic models for data validation.
* **`.env`:** Contains the environment variables.

## Contributing

If you'd like to contribute to this project, please feel free to open a pull request.
