from strawberry.tools import create_type
from fastapi import Request

class WebhookHandler:  # Cambiamos el nombre de la clase
    @staticmethod
    async def handle_request(request: Request):
        return {"received": True}
