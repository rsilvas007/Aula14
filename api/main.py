from datetime import datetime
from typing import Optional
from fastapi import FastAPI, Header, HTTPException, Request
from pydantic import BaseModel, Field
import logging
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
LOG_FILE = BASE_DIR / 'logs' / 'api_runtime.log'
API_KEY_ESPERADA = 'trocar_em_producao'

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
app = FastAPI(title='API de Manutenção Preditiva', version='0.6.0')

class MotorInput(BaseModel):
    temperatura_motor: float = Field(..., ge=0, le=150)
    vibracao_motor: float = Field(..., ge=0, le=20)
    corrente_motor: float = Field(..., ge=0, le=50)
    horas_operacao: int = Field(..., ge=0, le=100000)

@app.middleware('http')
async def log_requisicoes(request: Request, call_next):
    inicio = datetime.now()
    response = await call_next(request)
    duracao = (datetime.now() - inicio).total_seconds()
    logging.info(f'{request.method} {request.url.path} | status={response.status_code} | duracao={duracao:.4f}s')
    return response

@app.get('/')
def home():
    return {'mensagem': 'API de Manutenção Preditiva', 'status': 'online'}

@app.get('/health')
def health():
    return {'status': 'ok', 'timestamp': datetime.now().isoformat()}

@app.post('/predict')
def predict(dados: MotorInput, x_api_key: Optional[str] = Header(default=None)):
    if x_api_key not in [None, API_KEY_ESPERADA]:
        raise HTTPException(status_code=401, detail='API Key inválida')
    score = 0
    if dados.temperatura_motor > 82: score += 1
    if dados.vibracao_motor > 5.8: score += 1
    if dados.corrente_motor > 14: score += 1
    if dados.horas_operacao > 3500: score += 1
    classe = 1 if score >= 2 else 0
    return {'classe_prevista': classe, 'score_risco': score, 'descricao': 'Falha provável' if classe else 'Operação normal', 'model_version': '0.6.0', 'timestamp': datetime.now().isoformat()}
