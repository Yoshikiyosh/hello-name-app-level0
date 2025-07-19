"""
Hello APIのテスト
"""

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.domain.model import GreetingModel
from app.application.use_case import GreetingUseCase


# テストクライアント作成
client = TestClient(app)


class TestGreetingModel:
    """ドメインモデルのテスト"""
    
    def test_create_greeting_success(self):
        """正常なあいさつ文作成のテスト"""
        result = GreetingModel.create_greeting("太郎")
        assert result == "Hello, 太郎!"
    
    def test_create_greeting_empty_name(self):
        """空の名前でのエラーテスト"""
        with pytest.raises(ValueError, match="名前が指定されていません"):
            GreetingModel.create_greeting("")


class TestGreetingUseCase:
    """ユースケースのテスト"""
    
    def test_execute_success(self):
        """正常なユースケース実行のテスト"""
        use_case = GreetingUseCase()
        result = use_case.execute("太郎")
        assert result == "Hello, 太郎!"
    
    def test_execute_with_whitespace(self):
        """空白を含む名前のテスト"""
        use_case = GreetingUseCase()
        result = use_case.execute(" 太郎 ")
        assert result == "Hello, 太郎!"


class TestHelloAPI:
    """Hello APIのテスト"""
    
    def test_hello_success(self):
        """正常なAPIコールのテスト"""
        response = client.get("/hello?name=太郎")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, 太郎!"}
    
    def test_hello_english_name(self):
        """英語名でのテスト"""
        response = client.get("/hello?name=John")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, John!"}
    
    def test_hello_empty_name(self):
        """空の名前でのエラーテスト"""
        response = client.get("/hello?name=")
        assert response.status_code == 400
    
    def test_hello_missing_name(self):
        """名前パラメータなしでのエラーテスト"""
        response = client.get("/hello")
        assert response.status_code == 422  # FastAPIの入力検証エラー 