from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Répertoire contenant le build du frontend (React)
frontend_build_dir = os.path.join(os.path.dirname(__file__), 'static')

# Servir les fichiers statiques du frontend (React.js)
app.mount("/static", StaticFiles(directory=frontend_build_dir), name="static")

# Route principale pour servir l'index.html de React
@app.get("/")
async def serve_frontend():
    index_path = os.path.join(frontend_build_dir, 'index.html')
    return FileResponse(index_path)