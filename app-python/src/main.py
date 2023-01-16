import uvicorn
import logging
import fastapi

from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from commons.fastapi_logging import config_logging
from fastapi import HTTPException, FastAPI, Request
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

# Logging
config_logging(level="INFO")
logger = logging.getLogger(__name__)

# Create your FastAPI app
app = FastAPI()
FastAPIInstrumentor.instrument_app(app)



# Cors MW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
@app.get('/')

@app.get("/health")
async def health():
   return {'status': 'ok'}

@app.get("/eze")
async def getInformation(req: Request):
    return {
        "status" : "SUCCESS",
    }

@app.get("/internal_error")
async def request(req: Request):
    req_error = req
    return {
      "client_host": req.client.host,
      "req_error": req_error
    }

@app.get("/request")
async def request(req: Request):
    req_headers = req.headers
    return {
      "client_host": req.client.host,
      "req_headers": req_headers
    }

@app.get("/notfound")
async def notfound():
   raise HTTPException(status_code=404, detail="Not found")

# Main
if __name__ == "__main__":
   logger.info('Starting app-python service')
   uvicorn.run(app, host="0.0.0.0", port=3001)
