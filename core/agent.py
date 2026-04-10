import os
from google import genai
from dotenv import load_dotenv

# Tải API Key từ file .env một cách bảo mật
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Khởi tạo Client theo chuẩn SDK mới
client = genai.Client(api_key=API_KEY)


def review_code(code_snippet):
    prompt = f"""
    Bạn là một Senior Developer khó tính nhưng tận tâm. 
    Hãy review đoạn code sau, chỉ ra lỗi (nếu có) và đề xuất cách viết clean code hơn:
    
    {code_snippet}
    """

    # Sử dụng model thế hệ mới của Gemini qua SDK mới
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    return response.text


# Chạy thử nghiệm ngay trên máy của bạn
if __name__ == "__main__":
    # Đoạn code cẩu thả cố tình viết sai để AI bắt lỗi (sai thụt lề, viết hoa chữ cái đầu của hàm)
    sample_code = """
    def Sum(a,b):
    print(a+b)
    """

    print("Đang gọi Senior Developer AI đánh giá...\n")
    print("-" * 40)
    print(review_code(sample_code))
