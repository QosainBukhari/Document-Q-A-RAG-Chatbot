from collections import deque


class ConversationMemory:

    def __init__(self, window_size=5):

        self.chat_history = deque(
            maxlen=window_size
        )

    def save_context(
        self,
        question,
        answer
    ):

        self.chat_history.append({
            "question": question,
            "answer": answer
        })

    def get_history(self):

        history = ""

        for chat in self.chat_history:

            history += f"""
User: {chat['question']}
Assistant: {chat['answer']}
"""

        return history