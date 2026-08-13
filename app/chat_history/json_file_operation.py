import json

class JsonOperation:
    
    def add_chat_conversation(self, chat: dict):
        with open("D:\\Ai_Project\\anoop-ai-assistant\\app\\chat_history\\conversation.json","r",encoding="utf-8" ) as f:
            history = json.load(f)
        
        history.append(chat)
        
        with open("D:\\Ai_Project\\anoop-ai-assistant\\app\\chat_history\\conversation.json", "w", encoding="utf-8") as f:
            json.dump(history, f, indent=4)
            
            
    def get_last_messages(self, n: int = 5):
        with open("D:\\Ai_Project\\anoop-ai-assistant\\app\\chat_history\\conversation.json", "r", encoding="utf-8") as f:
            history = json.load(f)

        return history[-n:]
            
        