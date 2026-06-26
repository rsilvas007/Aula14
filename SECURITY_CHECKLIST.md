# SECURITY_CHECKLIST.md

## Checklist de segurança e governança

| Nº | Verificação | Status | Evidência |
|---:|---|---|---|
| 1 | `.env` não deve ser versionado |  | `.dockerignore` e `.gitignore` devem conter `.env` |
| 2 | `.env.example` não possui segredo real |  | Valor didático `trocar_em_producao` |
| 3 | API Key real não está no repositório |  | Apenas chave didática usada |
| 4 | Logs não exibem segredos |  | Conferir logs antes de publicar |
| 5 | Endpoint sensível deve ter controle de acesso |  | API Key didática ou autenticação futura |
| 6 | Acesso externo deve ser controlado |  | Em cloud, usar rede, IAM, firewall ou gateway |
| 7 | Imagem Docker não deve conter arquivos desnecessários |  | `.dockerignore` criado |
| 8 | Custos devem ser monitorados |  | CPU, memória, tráfego, logs e armazenamento |
| 9 | Responsável pela operação definido |  | Registrar equipe ou aluno responsável |
| 10 | Plano de resposta a falhas definido |  | Reinício, análise de logs e correção |
