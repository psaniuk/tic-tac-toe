from app.random_api_client import RandomApiClient
from app.model import Game

class GameService:
    def __init__(self, randomApiClient: RandomApiClient) -> None:
        self.__randomApiClient = randomApiClient
        size = 3
        self.__game = Game(size)
        self.__possible_moves = set([i for i in range(size * size)])
    
    async def new(self):
        while not self.__game.isCompleted():
            next_move_response = await self.__randomApiClient.getRandomChoice(list(self.__possible_moves))
            next_move = int(next_move_response["value"])
            self.__game.play(next_move)
            self.__possible_moves.remove(next_move)

        winner = self.__game.getWinner()
        board = [[player.getMark() if player else "" for player in row ] for row in self.__game.getResult()]
        
        return {
            "winner": winner.getMark() if winner else "draw",
            "board": board
        }
    