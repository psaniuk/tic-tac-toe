from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.random_api_client import RandomApiClient
from app.settings import AppSettings
from app.game_service import GameService

app = FastAPI()


@app.get("/game/new")
async def newGame():
    gameService = GameService(RandomApiClient(AppSettings()))
    result = await gameService.new()
    return JSONResponse(content=result)