from flask import request
import os
from openai import OpenAI
from internal.schema.app_schema import CompletionReq

class AppHandler():
    """应用处理器"""
    def ping(self):
        return {"status": "ok"}

    def completion(self):
        req = CompletionReq()
        if not req.validate():
            return req.errors
        query = request.json.get("query")
        client = OpenAI(
            base_url=os.getenv("OPENAI_BASE_URL"),
        )

        response = client.chat.completions.create(
            model="glm-4.5",
            messages=[
                {"role": "system", "content": "你是智谱开发的全世界最强的ai助手"},
                {"role": "user", "content": query}
            ]
        )
        return {"response": response.choices[0].message.content}
