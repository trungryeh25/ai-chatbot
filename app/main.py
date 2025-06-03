from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, APIRouter

from aiohttp import ClientSession

from app.database import client as database_client
from app.dependencies import init_dialogue_manager
from app.bot.dialogue_manager.http_client import HttpClient
from app.bot.memory.memory_saver_mongo import MemorySaverMongo

# Admin routers
from app.admin.bots.routes import router as bots_router
from app.admin.entities.routes import router as entities_router
from app.admin.intents.routes import router as intents_router
from app.admin.train.routes import router as train_router
from app.admin.test.routes import router as test_router
from app.admin.integrations.routes import router as integrations_router
from app.admin.chatlogs.routes import router as chatlogs_router

# Bot channel routers
from app.bot.channels.rest.routes import router as rest_router
from app.bot.channels.facebook.routes import router as facebook_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Init reusable HTTP session
    session = ClientSession()
    app.state.http_session = session
    app.state.http_client = HttpClient(session)

    # Optionally ensure MongoDB indexes (recommended)
    state_collection = database_client.get_database("chatbot").get_collection("state")
    await state_collection.create_index([("thread_id", 1), ("date", -1)])

    # Init dialogue manager + cache
    await init_dialogue_manager()

    yield

    # Cleanup
    await session.close()
    database_client.close()


app = FastAPI(title="AI Chatbot", lifespan=lifespan)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static assets
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Health check
@app.get("/ready")
async def ready():
    return {"status": "ok"}

@app.get("/")
async def root():
    return {"message": "Welcome to AI Chatbot API"}


# Admin API
admin_router = APIRouter(prefix="/admin")
admin_router.include_router(bots_router)
admin_router.include_router(intents_router)
admin_router.include_router(entities_router)
admin_router.include_router(train_router)
admin_router.include_router(test_router)
admin_router.include_router(integrations_router)
admin_router.include_router(chatlogs_router)
app.include_router(admin_router)

# Bot API
bot_router = APIRouter(prefix="/bots/channels", tags=["channels"])
bot_router.include_router(rest_router, tags=["rest"])
bot_router.include_router(facebook_router, tags=["facebook"])
app.include_router(bot_router)
