import sys
import json
import os
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from keyword_database import KeywordDatabase

# Tự động load biến môi trường từ file .env nếu có
dotenv_path = Path(__file__).parent / ".env"
if dotenv_path.exists():
    load_dotenv(dotenv_path)

# Khởi tạo HuggingFace Inference Client
HF_TOKEN = os.environ.get("HF_TOKEN")
client = InferenceClient(token=HF_TOKEN)

# Khởi tạo keyword database
keyword_db = KeywordDatabase()

def is_travel_related(message):
    """Kiểm tra xem câu hỏi có liên quan đến du lịch không sử dụng database"""
    
    message_lower = message.lower()
    
    # Lấy danh sách từ database
    blocked_keywords = keyword_db.get_blocked_keywords()
    travel_keywords = keyword_db.get_travel_keywords()
    destinations = keyword_db.get_destinations()
    
    # Kiểm tra blacklist trước - từ chối ngay nếu có từ không phải du lịch
    for keyword in blocked_keywords:
        if keyword.lower() in message_lower:
            # Ngoại lệ: nếu có kết hợp với từ du lịch thì vẫn cho qua
            travel_context = ['travel', 'tourism', 'visit', 'destination', 'trip', 'vacation', 'tour', 'attraction']
            has_travel_context = any(t_word in message_lower for t_word in travel_context)
            if not has_travel_context:
                return False
    
    # Kiểm tra travel keywords từ database
    for keyword in travel_keywords:
        if keyword.lower() in message_lower:
            return True
    
    # Kiểm tra destinations từ database
    for destination in destinations:
        if destination.lower() in message_lower:
            return True
    
    # Kiểm tra câu hỏi về địa điểm
    location_questions = [
        'where to', 'what to', 'how to get', 'when to visit', 'why visit',
        'best place', 'recommend', 'suggest', 'things to do', 'places to see',
        'must visit', 'worth visiting', 'attractions in', 'hotels in',
        'restaurants in', 'weather in', 'climate in'
    ]
    
    for pattern in location_questions:
        if pattern in message_lower:
            return True
    
    return False

def get_travel_response_from_ai(message):
    """Lấy câu trả lời du lịch từ DeepSeek-V3 AI model"""
    try:
        # Tạo prompt chuyên về du lịch
        travel_prompt = f"""You are a travel assistant. Answer this travel question concisely in English only.

User question: {message}

Provide a brief, helpful response with:
- Top 3-5 key attractions/recommendations
- Essential practical tip
- Keep it under 200 words
- Use simple formatting with bullet points or numbered lists
- NO markdown formatting (no **, no #, no bold/italic)
- Plain text only
- English language only

Be direct and informative without excessive details."""

        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3-0324",
            messages=[
                {
                    "role": "system",
                    "content": "You are a concise travel assistant. Provide brief, practical travel advice in plain text English only. No markdown formatting."
                },
                {
                    "role": "user", 
                    "content": travel_prompt
                }
            ],
            max_tokens=250,
            temperature=0.5
        )
        
        # Làm sạch output, loại bỏ markdown formatting
        response = completion.choices[0].message.content.strip()
        
        # Loại bỏ các ký tự markdown
        response = response.replace('**', '')
        response = response.replace('*', '')
        response = response.replace('###', '')
        response = response.replace('##', '')
        response = response.replace('#', '')
        response = response.replace('`', '')
        
        return response
        
    except Exception as e:
        print(f"Error getting AI response: {e}", file=sys.stderr)
        return "Sorry, I'm having trouble connecting to the travel service. Please try again later."

def chat_response(message):
    """Trả lời câu hỏi du lịch sử dụng DeepSeek-V3 AI"""
    
    # Kiểm tra câu hỏi có liên quan đến du lịch không
    if not is_travel_related(message):
        return "I'm a travel assistant. I can help with destinations, attractions, hotels, transportation, and travel tips worldwide. Please ask about travel topics!"
    
    # Lấy câu trả lời từ AI
    ai_response = get_travel_response_from_ai(message)
    
    return ai_response

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("")
        sys.exit(0)
    message = sys.argv[1]
    try:
        result = chat_response(message)
        print(result.encode('utf-8', errors='ignore').decode('utf-8'))
    except UnicodeEncodeError:
        # Fallback: chỉ giữ lại ký tự ASCII
        result = chat_response(message)
        print(result.encode('ascii', errors='ignore').decode('ascii'))
