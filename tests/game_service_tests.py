import unittest
from unittest.mock import AsyncMock, patch
from app.game_service import GameService

class GameServiceTests(unittest.IsolatedAsyncioTestCase):
    async def test_no_draw(self):
        values = [{"value":str(i)} for i in range(7)]

        mock_random_api_client = AsyncMock()
        mock_random_api_client.getRandomChoice = AsyncMock(side_effect = values)
       
        with patch('app.game_service.RandomApiClient', mock_random_api_client):
            game_service = GameService(mock_random_api_client)
            result = await game_service.new()
            self.assertNotEqual(result["winner"], "draw")
            self.assertTrue(len(result["board"]) == 3)
    
    async def test_draw(self):
        values = [{"value":str(i)} for i in [0, 2, 1, 3, 5, 4, 6, 7, 8]]

        mock_random_api_client = AsyncMock()
        mock_random_api_client.getRandomChoice = AsyncMock(side_effect = values)
       
        with patch('app.game_service.RandomApiClient', mock_random_api_client):
            game_service = GameService(mock_random_api_client)
            result = await game_service.new()
            self.assertEqual(result["winner"], "draw")

