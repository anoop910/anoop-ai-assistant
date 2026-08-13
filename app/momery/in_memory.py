from typing import Dict, List
from datetime import datetime, timedelta
import threading
import time


class InMemoryConversation:

    def __init__(self):

        self.memory: Dict[str, Dict[str, List[dict]]] = {}

        # Last time user sent a message
        self.last_activity: Dict[str, datetime] = {}

        # Start background cleanup
        self.cleanup_thread = threading.Thread(
            target=self._cleanup_inactive_users, daemon=True
        )

        self.cleanup_thread.start()

    # =========================================
    # Add message
    # =========================================

    def add_message(self, user_id: str, conversation_id: str, role: str, content: str):

        # Create user
        if user_id not in self.memory:

            self.memory[user_id] = {}

        # Create conversation
        if conversation_id not in self.memory[user_id]:

            self.memory[user_id][conversation_id] = []

        # Add message
        self.memory[user_id][conversation_id].append(
            {
                "role": role,
                "content": content,
            }
        )

        # =========================================
        # Keep latest 10 messages
        # =========================================

        if len(self.memory[user_id][conversation_id]) > 10:

            self.memory[user_id][conversation_id] = self.memory[user_id][
                conversation_id
            ][-10:]

        # =========================================
        # Update activity
        # =========================================

        self.last_activity[user_id] = datetime.now()

    # =========================================
    # Get conversation
    # =========================================

    def get_conversation(self, user_id: str, conversation_id: str):

        if user_id not in self.memory:

            return []

        if conversation_id not in self.memory[user_id]:

            return []

        return self.memory[user_id][conversation_id]

    # =========================================
    # Get last N messages
    # =========================================

    def get_recent_messages(self, user_id: str, conversation_id: str, limit: int = 6):

        messages = self.get_conversation(user_id, conversation_id)

        return messages[-limit:]

    # =========================================
    # Clear conversation
    # =========================================

    def clear_conversation(self, user_id: str, conversation_id: str):

        if user_id in self.memory:

            if conversation_id in self.memory[user_id]:

                del self.memory[user_id][conversation_id]

    # =========================================
    # Clear all user memory
    # =========================================

    def clear_user(self, user_id: str):

        if user_id in self.memory:

            del self.memory[user_id]

        if user_id in self.last_activity:

            del self.last_activity[user_id]

    # =========================================
    # Background cleanup
    # =========================================

    def _cleanup_inactive_users(self):

        while True:

            try:

                now = datetime.now()

                inactive_users = []

                # Find inactive users

                for user_id, last_time in list(self.last_activity.items()):

                    if now - last_time > timedelta(minutes=30):

                        inactive_users.append(user_id)

                # Delete inactive users

                for user_id in inactive_users:

                    print(f"Removing inactive user: {user_id}")

                    self.clear_user(user_id)

            except Exception as error:

                print("Memory cleanup error:", error)

            # Check every 5 minutes

            time.sleep(300)
