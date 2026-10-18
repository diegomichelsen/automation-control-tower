# Automation Control Tower

> Plataforma central de observabilidade, diagnóstico de incidentes e confiabilidade de automações.

**Status:** Planejamento  
**Versão:** 0.1  
**Categoria:** Observabilidade, integrações, confiabilidade e operações

## 1. Visão geral

A Automation Control Tower será uma plataforma transversal para monitorar a saúde técnica das automações e integrações dos demais projetos do portfólio.

A plataforma reunirá eventos operacionais padronizados, métricas, falhas e incidentes em uma interface central. O objetivo é reduzir o tempo necessário para detectar problemas, entender o contexto e executar recuperações seguras.

Cada projeto continuará independente e responsável por sua lógica de negócio. A Control Tower receberá informações operacionais por contratos documentados.

## 2. Problema de negócio

Em ambientes com várias automações, uma falha pode permanecer invisível até que um usuário perceba a ausência de um resultado. Logs dispersos e ausência de correlação entre execuções dificultam o diagnóstico e a recuperação.

## 3. Objetivos

- Monitorar execuções de automações.
- Detectar falhas, atrasos e indisponibilidade.
- Centralizar eventos e logs relevantes.
- Correlacionar execuções e incidentes.
- Emitir alertas com contexto.
- Apoiar o diagnóstico de causa raiz.
- Permitir recuperação controlada.
- Medir confiabilidade e tempo de resolução.

## 4. Escopo funcional previsto

### Coleta de eventos

Os projetos publicarão eventos como:

- `execution_started`
- `execution_succeeded`
- `execution_failed`
- `retry_scheduled`
- `incident_opened`
- `incident_resolved`

Cada evento poderá incluir identificadores do projeto, workflow e execução, timestamp, duração, resultado e metadados técnicos seguros.

O contrato definitivo será versionado e documentado antes de ser utilizado por múltiplos projetos.

### Monitoramento e métricas

- Execuções totais.
- Taxa de sucesso e falha.
- Duração e atrasos.
- Última execução observada.
- Volume de dados processados.
- Retentativas.
- Incidentes abertos e resolvidos.
- Tempo entre detecção e resolução.

A plataforma deverá diferenciar uma execução que falhou de uma automação que deixou de executar completamente.

### Alertas e incidentes

- Regras configuráveis de alerta.
- Detecção de padrões de falha.
- Registro de incidentes.
- Priorização baseada em critérios documentados.
- Histórico de eventos relacionados.
- Controle de duplicidade de alertas.
- Acompanhamento de resolução.

### Diagnóstico assistido

- Agrupamento de erros semelhantes.
- Identificação da etapa com falha.
- Correlação por identificadores de execução.
- Resumo de logs relevantes.
- Sugestões de investigação.
- IA opcional para resumir incidentes e sugerir causas possíveis.

As sugestões da IA serão tratadas como hipóteses, não como causas confirmadas.

### Recuperação controlada

- Retentativas limitadas.
- Reprocessamento quando tecnicamente seguro.
- Prevenção de efeitos duplicados.
- Limites de frequência e número de tentativas.
- Registro das ações executadas.
- Autorização humana para operações críticas.

## 5. Arquitetura prevista

- **Python e FastAPI:** recepção e consulta de eventos.
- **PostgreSQL:** eventos normalizados, métricas agregadas e incidentes.
- **n8n:** notificações e workflows operacionais.
- **APIs e webhooks:** integração com os projetos.
- **Dashboard:** visão consolidada e detalhamento dos incidentes.
- **Docker Compose:** ambiente local.
- **Pytest:** testes automatizados.

A arquitetura inicial poderá utilizar componentes simples. Filas, armazenamento especializado de logs ou sistemas externos de monitoramento só serão adicionados se os requisitos justificarem essa complexidade.

## 6. Padrão de eventos e observabilidade

A Control Tower dependerá de instrumentação explícita nos projetos monitorados.

Cada evento deverá ser validado, identificado e associado ao projeto correto. A plataforma precisará lidar com eventos repetidos, atrasados ou recebidos fora de ordem.

Logs não deverão incluir senhas, tokens ou dados pessoais desnecessários. A retenção e o detalhamento serão definidos conforme a finalidade e o ambiente.

## 7. Segurança e confiabilidade

- Autenticação dos produtores de eventos.
- Validação do esquema dos eventos.
- Controle de acesso.
- Retentativas limitadas.
- Deduplicação de eventos quando aplicável.
- Registro de auditoria para ações administrativas.
- Segredos fora do repositório.
- Proteção contra loops de recuperação.
- Limites de execução e mecanismos de interrupção.

A disponibilidade da Control Tower não deverá ser confundida com a disponibilidade dos projetos monitorados. A própria coleta de eventos precisará ser observável e capaz de indicar possíveis lacunas de monitoramento.

## 8. Testes e critérios de aceitação

A primeira versão deverá demonstrar:

1. Recebimento e validação de eventos.
2. Registro de sucesso e falha.
3. Correlação de eventos por execução.
4. Identificação de falhas simuladas.
5. Geração de alertas segundo regras definidas.
6. Tratamento de eventos repetidos.
7. Visualização do histórico de incidentes.
8. Recuperação controlada em cenários de teste.
9. Testes automatizados dos fluxos críticos.

## 9. Estratégia de evolução

A primeira versão monitorará eventos de um projeto. Depois, o contrato será reutilizado pelos demais projetos e a plataforma passará a consolidar as execuções em uma visão comum.

A integração será feita por interfaces documentadas, sem acesso irrestrito aos bancos internos dos projetos.

## 10. Próximos passos

1. Definir o contrato de eventos.
2. Implementar logs estruturados no primeiro projeto.
3. Criar a API de recepção de eventos.
4. Armazenar e consultar eventos.
5. Implementar regras básicas de alerta.
6. Construir a visão de incidentes.
7. Adicionar recuperação controlada.
8. Integrar os outros projetos progressivamente.

## 11. Limitações

A Control Tower não consegue monitorar automaticamente uma automação que não fornece sinais observáveis. A cobertura dependerá da instrumentação de cada fluxo e das verificações de saúde disponíveis.

A plataforma é demonstrativa e não será apresentada como um sistema de monitoramento de produção sem testes de confiabilidade, segurança e carga apropriados.