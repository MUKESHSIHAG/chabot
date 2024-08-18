from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db, init_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

message_id = ''

def test_chat():
    global message_id
    response = client.post("/chat/", json={"session_id": 'ee7d0f34-b308-4172-b191-97e5cea0ab96', "message": "Hello, chatbot!"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, chatbot!"
    print("here..", data)
    message_id = data['id']
    assert "response" in data

def test_edit_message():
    global message_id
    response = client.put(f"/edit/{message_id}", json={"new_message": "Hello, edited chatbot!"})
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, edited chatbot!"

def test_delete_message():
    global message_id
    response = client.delete(f"/delete/{message_id}")
    assert response.status_code == 200
    data = response.json()
