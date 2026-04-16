Cách hoạt động
Request (GET): Trình duyệt truy cập http://localhost:8000/, FastAPI trả về file login.html.

User Input: Người dùng nhập username/password và nhấn nút "Gửi".

Submit (POST): Form gửi dữ liệu tới endpoint /login.

Backend Process: Python nhận dữ liệu qua Form(...), kiểm tra logic và trả về phản hồi (thành công hoặc thất bại).

Lưu ý quan trọng:

Bảo mật: Đoạn code trên chỉ là khung cơ bản nhất. Trong thực tế, bạn tuyệt đối không so sánh mật khẩu dạng văn bản thuần (== "123456"). Bạn phải dùng thư viện như passlib để băm mật khẩu (hashing) trước khi so sánh.

Session: Sau khi đăng nhập, hệ thống cần tạo một "Token" hoặc "Session" để lưu trạng thái đăng nhập cho các trang sau.
