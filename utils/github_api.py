# Các hàm để tương tác với GitHub (kéo code, gửi comment)

import os
from github import Github
from dotenv import load_dotenv

# Tải biến môi trường
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Khởi tạo client kết nối với GitHub
g = Github(GITHUB_TOKEN)

def get_pr_code_changes(repo_name: str, pr_number: int):
    """
    Hàm này truy cập vào một Pull Request và lấy ra nội dung những file bị thay đổi.
    """
    try:
        # Tìm kho lưu trữ
        repo = g.get_repo(repo_name)
        # Lấy Pull Request cụ thể
        pr = repo.get_pull(pr_number)
        
        # Lấy danh sách các file bị thay đổi trong PR này
        files = pr.get_files()
        
        code_snippets = ""
        for file in files:
            # Chỉ lấy các file code, bỏ qua file ảnh, tài liệu,... (bạn có thể thêm đuôi .cs, .js tùy ý)
            if file.filename.endswith(('.py', '.cs', '.js')):
                code_snippets += f"--- Tên file: {file.filename} ---\n"
                # file.patch chứa nội dung phần code bị thay đổi (diff)
                code_snippets += f"{file.patch}\n\n"
                
        return code_snippets
        
    except Exception as e:
        print(f"Lỗi khi kéo code từ GitHub: {e}")
        return None
def post_comment_to_pr(repo_name: str, pr_number: int, comment_body: str):
    """
    Hàm này dùng để gửi nhận xét của AI lên Pull Request của GitHub
    """
    try:
        repo = g.get_repo(repo_name)
        pr = repo.get_pull(pr_number)
        
        # Thêm một chút trang trí để biết là AI tự động bình luận
        formatted_comment = f"🤖 **AI Code Reviewer:**\n\n{comment_body}"
        pr.create_issue_comment(formatted_comment)
        print(f"✅ Đã gửi comment thành công lên PR #{pr_number}")
        
    except Exception as e:
        print(f"❌ Lỗi khi gửi comment: {e}")