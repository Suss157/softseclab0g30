from src.api import app


def test_calc_route_returns_correct_result():
    client = app.test_client()

    response = client.post("/calc", json={"expression": "3 + 5"})

    assert response.status_code == 200
    assert response.get_json() == {"expression": "3 + 5", "result": "8"}


def test_calc_route_with_different_expression():
    client = app.test_client()

    response = client.post("/calc", json={"expression": "(2 + 3) * 4"})

    assert response.status_code == 200
    assert response.get_json() == {"expression": "(2 + 3) * 4", "result": "20"}
