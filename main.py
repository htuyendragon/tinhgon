from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import subprocess

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Hàm phụ trợ lấy danh sách user từ hệ thống
def get_system_users():
    result = subprocess.check_output(["getent", "passwd"], text=True)
    users = []
    for line in result.strip().split('\n'):
        parts = line.split(':')
        if int(parts[2]) >= 1000: # Chỉ lấy user thường
            users.append({
                "username": parts[0],
                "uid": parts[2],
                "home_directory": parts[5],
                "shell": parts[6]
            })
    return users

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/users/", response_class=HTMLResponse)
async def view_users(request: Request):
    users = get_system_users()
    return templates.TemplateResponse("index.html", {"request": request, "users": users})

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username == "admin" and password == "123456":
        return {"message": "Đăng nhập thành công! Truy cập /users/ để xem danh sách."}
    return {"message": "Sai thông tin!"}
