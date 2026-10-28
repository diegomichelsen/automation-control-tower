"""
Automation Control Tower — API

Ponto de entrada da aplicação.
Por enquanto expõe apenas o health check, usado pelo Docker, pelo n8n
e pela Automation Control Tower para saber se o serviço está no ar.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Automation Control Tower API",
    description="Observabilidade das automações: execuções, falhas, retentativas e incidentes.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    # Retorna HTTP 200 com {"status": "ok"} quando a API está funcionando
    return {"status": "ok"}
