from motor.motor_asyncio import AsyncIOMotorClient
from typing import Text, Optional, List
from app.bot.memory.models import State
from app.bot.memory import MemorySaver
from pymongo import ASCENDING, DESCENDING

class MemorySaverMongo(MemorySaver):
    """
    MemorySaverMongo implements the MemorySaver interface for MongoDB.
    """

    def __init__(self, client: AsyncIOMotorClient):
        self.client = client
        self.db = client.get_database("chatbot")
        self.collection = self.db.get_collection("state")
        
        # Tạo compound index thread_id (tăng dần), date (giảm dần)
        self.collection.create_index(
            [("thread_id", ASCENDING), ("date", DESCENDING)],
            name="thread_date_idx",
            background=True,
        )

    async def save(self, thread_id: Text, state: State):
        await self.collection.insert_one(state.to_dict())

    async def get(self, thread_id: Text) -> Optional[State]:
        result = await self.collection.find_one(
            {"thread_id": thread_id},
            {"_id": 0, "nlu": 0, "date": 0, "user_message": 0, "bot_message": 0},
            sort=[("date", DESCENDING)],
        )
        if result:
            return State.from_dict(result)
        return None

    async def get_all(self, thread_id: Text) -> List[State]:
        cursor = self.collection.find({"thread_id": thread_id}, sort=[("date", DESCENDING)])
        results = await cursor.to_list(length=None)
        return [State.from_dict(result) for result in results]
