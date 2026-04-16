from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
# Giả sử bạn để file login.html trong thư mục 'templates'
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    # Logic kiểm tra thông tin (ví dụ tĩnh)
    if username == "admin" and password == "123456":
        return {"message": "Đăng nhập thành công!"}
    else:
        return {"message": "Sai tài khoản hoặc mật khẩu!"}
