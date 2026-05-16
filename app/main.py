
from fastapi import FastAPI
from app.routes.member_routes import router as member_router
from app.routes.book_routes import router as book_router
from app.routes.borrow_routes import router as borrow_router

app = FastAPI(
    title="Library Book Lending System"
)

app.include_router(member_router)
app.include_router(book_router)
app.include_router(borrow_router)

@app.get("/")
def home():
    return {"message": "Library API Working"}
