from fastapi.testclient import TestClient

from src.api.main import app

# Cliente que simula requisições HTTP sem precisar subir o servidor
client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
