import pytest


@pytest.fixture
def user_data():
    return {
        "name":"Carla",
        "job": "TesterS"
    }


def pytest_html_report_title( report ):
    report.title  = "API - REQURES PYTEST WITH REQUESTS"

