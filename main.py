from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import subprocess

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_system_users():
    """Lấy danh sách các user có UID >= 1000"""
    try:
        result = subprocess.check_output(["getent", "passwd"], text=True)
        users = []
        for line in result.strip().split('\n'):
            parts = line.split(':')
            if int(parts[2]) >= 1000:
                users.append({
                    "username": parts[0],
                    "uid": parts[2],
                    "home_directory": parts[5],
                    "shell": parts[6]
                })
        return users
    except Exception:
        return []

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Trang chủ hiển thị danh sách user ngay lập tức"""
    users = get_system_users()
    return templates.TemplateResponse("index.html", {"request": request, "users": users})
