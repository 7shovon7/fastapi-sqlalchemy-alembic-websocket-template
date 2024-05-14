from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from websockets import ConnectionClosedError

from api.public.ws.connection_manager import manager as connection_manager


router = APIRouter()


@router.websocket('')
async def websocket_endpoint(
    *,
    websocket: WebSocket,
    connector_id: str,
):
    await connection_manager.connect(websocket, connector_id)
    try:
        while True:
            message = await websocket.receive_text()
            await connection_manager.send_message(message)
    except WebSocketDisconnect:
        connection_manager.disconnect(connector_id)
    except ConnectionClosedError:
        pass
