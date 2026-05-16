
# Library Book Lending System

## Install

```bash
pip install -r requirements.txt
```

## Run Project

```bash
uvicorn app.main:app --reload
```

## Swagger UI

Open:

http://127.0.0.1:8000/docs

## APIs

### Members
- POST /members
- GET /members
- GET /members/{member_id}

### Books
- POST /books
- GET /books
- GET /books/{book_id}

### Borrow
- POST /issue-book
- POST /return-book
- GET /summary/{member_id}

## Sample Member Payload

```json
{
  "name": "Navneeth",
  "age": 22,
  "email": "nav@gmail.com",
  "city": "Salem",
  "membership_status": "Active"
}
```
