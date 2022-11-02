from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

home_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@home_router.get("/")
async def home(request: Request):

    mystuff = "Hello FastAPI"
    context = {"request": request, "mystuff": mystuff}

    return templates.TemplateResponse("general_pages/homepage.html", context)
