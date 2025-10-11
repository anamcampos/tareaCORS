from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración CORS: aquí defines los orígenes permitidos, métodos, headers, etc.
origins = [
    "http://localhost",
    "http://localhost:3000",
    # agrega más orígenes que quieras permitir
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # lista de orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],              # permite todos los métodos (GET, POST, etc)
    allow_headers=["*"],              # permite todos los headers
)

@app.middleware('http')
async def verifica_agente_usuario(request: Request, call_next):
    if request.headers.get('User-Agent', '').find('Mobile') == -1:
        response = await call_next(request)
        return response
    else:
        return JSONResponse(content={
            'message': 'error, ingresando desde mobile'
        }, status_code=401)

@app.get('/')
def main():
    return 'Hola'
