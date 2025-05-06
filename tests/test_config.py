import pytest
from config import Settings

def test_defaults(tmp_path, monkeypatch):
    monkeypatch.delenv("MODEL_NAME", raising=False)
    s = Settings(_env_file=str(tmp_path/"nope.env"))
    assert s.model_name.startswith("yolov8")
    assert 0.0 <= s.confidence <= 1.0

def test_env_override(monkeypatch):
    monkeypatch.setenv("MODEL_NAME", "yolov8m")
    monkeypatch.setenv("CONFIDENCE", "0.7")
    s = Settings()
    assert s.model_name == "yolov8m"
    assert pytest.approx(s.confidence, 0.01) == 0.7
