from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()
templates = Jinja2Templates(directory="templates")

Base = declarative_base()

class Text(Base):
    """
    Модель для хранения текста.

    Атрибуты:
        id (Integer): Уникальный идентификатор записи.
        text (String): Содержимое текста.
    """

    __tablename__ = 'texts'
    id = Column(Integer, primary_key=True)
    text = Column(String)

engine = create_engine('sqlite:///db.sqlite')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


@app.on_event("startup")
async def startup():
    """
    Выполняется при старте приложения.
    """
    Base.metadata.create_all(bind=engine)


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Главная страница приложения.

    :param request: HTTP-запрос.
    :return: Рендер шаблона index.html с контекстом.
    """
    db = SessionLocal()
    texts = db.query(Text).order_by(Text.id.desc()).all()
    db.close()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "texts": texts},
    )


@app.post("/add-text/", response_class=HTMLResponse)
async def add_text(request: Request, text: str = Form(...)):
    """
    Сохранение нового текста.

    :param request: HTTP-запрос.
    :param text: Текст, полученный из формы.
    :return: Рендер шаблона index.html с контекстом.
    """
    db = SessionLocal()
    new_text = Text(text=text)
    db.add(new_text)
    db.commit()
    db.close()
    return templates.TemplateResponse("index.html", {"request": request}, status_code=200)