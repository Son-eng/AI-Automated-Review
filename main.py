from fastapi import FastAPI, Request
from core.agent import review_code
from utils.github_api import get_pr_code_changes, post_comment_to_pr

app = FastAPI(title="AI Code Reviewer API")

@app.get("/")
def read_root():
    return {"message": "AI Code Reviewer Server đang chạy ổn định!"}

@app.post("/webhook")
async def github_webhook(request: Request):
    try:
        payload = await request.json()
        
        # Kiểm tra xem gói tin gửi về có phải là sự kiện Pull Request không
        if "pull_request" in payload:
            action = payload["action"]
            
            # Chỉ kích hoạt AI khi có PR mới được tạo ('opened') hoặc có code mới được đẩy lên PR ('synchronize')
            if action in ["opened", "synchronize"]:
                repo_name = payload["repository"]["full_name"]
                pr_number = payload["pull_request"]["number"]
                
                print(f"\n🚀 Đang kích hoạt AI cho PR #{pr_number} tại {repo_name}...")
                
                # 1. Kéo code từ GitHub về
                code_changes = get_pr_code_changes(repo_name, pr_number)
                
                if code_changes and code_changes.strip():
                    # 2. Đưa cho Gemini đánh giá
                    print("🧠 AI đang đọc và phân tích code...")
                    review_result = review_code(code_changes)
                    
                    # 3. Trả kết quả về GitHub
                    print("✍️ Đang gửi nhận xét lên GitHub...")
                    post_comment_to_pr(repo_name, pr_number, review_result)
                else:
                    print("⚠️ Không tìm thấy file code (Python, C#, JS) nào thay đổi trong PR này.")
                    
        return {"status": "success"}
        
    except Exception as e:
        print(f"❌ Lỗi server: {e}")
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)