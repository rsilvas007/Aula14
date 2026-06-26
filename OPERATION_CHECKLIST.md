# OPERATION_CHECKLIST.md

## Checklist operacional da API containerizada

| Nº | Verificação | Status | Evidência |
|---:|---|---|---|
| 1 | Imagem Docker construída |  | `docker build` executado |
| 2 | Container iniciado |  | `docker ps` mostra `api-mlops-aula14` |
| 3 | Porta 8000 publicada |  | `0.0.0.0:8000->8000/tcp` |
| 4 | Rota `/health` responde |  | Resposta JSON com `status: ok` |
| 5 | Swagger `/docs` acessível |  | Página abre no navegador |
| 6 | Endpoint `/predict` responde |  | Requisição POST testada |
| 7 | Logs do container consultados |  | `docker logs api-mlops-aula14` |
| 8 | Consumo observado |  | `docker stats api-mlops-aula14` |
| 9 | Erros críticos identificados |  | Verificar 4xx, 5xx e falhas de inicialização |
| 10 | Evidências registradas |  | Notebook e relatório preenchidos |
