# 🤖 AI-Automated Code Reviewer Agent

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688.svg)
![Gemini API](https://img.shields.io/badge/Gemini-2.5_Flash-orange.svg)
![GitHub Webhooks](https://img.shields.io/badge/GitHub-Webhooks-black.svg)

## 📌 Tổng quan
**AI-Automated Code Reviewer** là một AI Agent tự trị được thiết kế để tự động hóa và tối ưu hóa quy trình đánh giá mã nguồn (Code Review). Bằng cách tích hợp mô hình **Gemini 2.5 Flash** mới nhất của Google với **GitHub Webhooks**, Agent này đóng vai trò như một Senior Developer ảo. Nó tự động lắng nghe các sự kiện khi có Pull Request mới, phân tích các thay đổi trong mã nguồn và đưa ra các nhận xét chi tiết, mang tính xây dựng trực tiếp trên GitHub.

## ✨ Tính năng nổi bật
* **Theo dõi theo thời gian thực (Real-time):** Tự động kích hoạt ngay khi một Pull Request được tạo hoặc cập nhật thông qua GitHub Webhooks.
* **Tự động trích xuất mã nguồn:** Sử dụng thư viện `PyGithub` để lấy chính xác các đoạn code bị thay đổi (diffs) mà không cần can thiệp thủ công.
* **Phân tích code thông minh:** Sức mạnh từ Gemini 2.5 Flash giúp phát hiện các lỗi logic tiềm ẩn, kiểm tra chuẩn đặt tên (PEP 8), và đề xuất tối ưu hóa cấu trúc code (như cách sử dụng return, bổ sung docstrings và type hints).
* **Tích hợp trực tiếp vào GitHub:** Trả về kết quả đánh giá dưới dạng bình luận (comment) được định dạng Markdown rõ ràng ngay trên Pull Request.

## 🏗️ Kiến trúc hệ thống
1. **Lập trình viên** đẩy code (push) và tạo một Pull Request trên GitHub.
2. **GitHub Webhook** bắt sự kiện và gửi gói dữ liệu (payload) về **FastAPI Server**.
3. **FastAPI** tiếp nhận dữ liệu và đánh thức **AI Agent**.
4. Agent gọi **GitHub API** để kéo các file code có sự thay đổi về máy.
5. Đoạn code được đưa vào **Google Gemini API** cùng với bộ System Prompt được thiết kế chuyên biệt.
6. Agent lấy kết quả review từ AI và tự động comment ngược lại lên Pull Request.

## 🚀 Công nghệ sử dụng
* **Backend Framework:** FastAPI, Uvicorn
* **AI Model:** Google GenAI SDK (Gemini 2.5 Flash)
* **Tích hợp:** PyGithub, GitHub Webhooks
* **Quản lý môi trường:** python-dotenv
* **Mạng (Local Tunneling):** ngrok

## 🛠️ Hướng dẫn Cài đặt & Chạy cục bộ

**1. Clone kho lưu trữ về máy:**
```bash
git clone [https://github.com/Son-eng/AI-Automated-Review.git](https://github.com/Son-eng/AI-Automated-Review.git)
cd AI-Automated-Review
```

**2. Tạo và kích hoạt môi trường ảo (Virtual Environment):**
```bash
python -m venv venv
# Trên Windows:
.\venv\Scripts\activate
# Trên Linux/Mac:
source venv/bin/activate
```

**3. Cài đặt các thư viện cần thiết:**
```bash
pip install -r requirements.txt
```

**4. Cấu hình biến môi trường(Environment Variables):**
```bash
# Tạo file .env vào thêm các API keys vào
GEMINI_API_KEY=api_key_google_gemini
GITHUB_TOKEN=token_github
```

**5. Khởi chạy Server & Mở kết nối Internet:**
Mở 2 cửa sổ Terminal song song:
* Terminal 1 (Chạy server FastAPI):
```bash
python main.py
```
* Terminal 2 (Chạy ngrok để mở port 8000):
```bash
ngrok http 8000
```
Sau đó, lấy đường link do ngrok cung cấp (thêm đuôi `/webhook`) và dán vào phần Webhook trên Repository GitHub của bạn. 

## 👨‍💻 Tác giả
**Bùi Hồng Sơn** | Sinh viên ngành Khoa học Máy tính
Đam mê Trí tuệ nhân tạo (AI), Python và Kỹ thuật Phần mềm.