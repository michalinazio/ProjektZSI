from fastapi import FastAPI
from backend.application.api.routers.lizard_vote_router import router as lizard_vote_router
from backend.application.api.routers.lizard_router import router as lizard_router
from backend.application.api.routers.species_router import router as species_router

app = FastAPI(title="Lizard API")

app.include_router(lizard_router)
app.include_router(species_router)
app.include_router(lizard_vote_router)