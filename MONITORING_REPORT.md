# MONITORING_REPORT.md

## Relatório inicial de monitoramento

### 1. Disponibilidade
- Container em execução: validar com `docker ps`.
- Rota `/health`: validar com `curl http://localhost:8000/health`.
- Swagger `/docs`: validar no navegador.

### 2. Logs
Comando: `docker logs api-mlops-aula14`

Observar: inicialização do Uvicorn, requisições recebidas, códigos HTTP 200, 401, 422 ou 500 e mensagens de erro.

### 3. Desempenho inicial
Comando: `docker stats api-mlops-aula14`

Métricas: CPU, memória, rede e leitura/escrita de bloco.

### 4. Segurança e governança
Não versionar `.env`, não publicar chaves reais, não registrar dados sensíveis em logs e controlar acesso em ambiente externo.

### 5. Custos e consumo em cloud
CPU, memória, tráfego de rede, armazenamento de imagem, retenção de logs e quantidade de réplicas podem gerar custo.
