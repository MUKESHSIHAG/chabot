# Chatbot Project

This project is a chatbot application built using Python (FastAPI) for the backend, React.js for the frontend, and PostgreSQL for the database.

## Requirements

- **Backend**: Python with FastAPI
- **Frontend**: React.js
- **Database**: PostgreSQL
- **API Key**: Groq API Key

## Setup and Run the Backend

1. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Set Up PostgreSQL Database**:

- Create a PostgreSQL database. 
- Make a note of the database URL, which typically follows this format:
plaintext
    ```
   DATABASE_URL=postgresql+psycopg2://username:password@localhost/dbname
    ```

3. **Set Up the .env File**:

- Create a .env file in the root directory of your backend project.
- Add the following environment variables:
```
GROQ_API_KEY=your_groq_api_key_here
DATABASE_URL=your_database_url_here
groq_model=llama3-8b-8192
```

- To generate the GROQ_API_KEY, refer to the [Groq Documentation](https://console.groq.com/docs/quickstart).

4. **Run Pytest**
```
python -m pytest app/tests/test_chat.py
```

5. **Start the Backend**:
```uvicorn main:app --reload```

## Setup and Run the Frontend

1. **Navigate to the Frontend Directory**:

```
cd frontend
#Install the Required Node Packages:
npm install
```

2. **Start the Frontend**:
```npm start```

3. **Access the UI**:

The application UI will open in your default web browser, typically at http://localhost:3000.