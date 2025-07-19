"""
API層：FastAPIのエンドポイントを定義
HTTPリクエストを受け取り、ユースケースを呼び出す
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

from app.application.use_case import GreetingUseCase


# レスポンスモデル
class GreetingResponse(BaseModel):
    message: str


# ルーター作成
router = APIRouter()

# ユースケース初期化
greeting_use_case = GreetingUseCase()


@router.get("/hello", response_model=GreetingResponse)
async def hello(name: str = Query(..., description="あいさつ対象の名前")):
    """
    あいさつメッセージを返すエンドポイント
    
    Args:
        name: あいさつ対象の名前（クエリパラメータ）
        
    Returns:
        GreetingResponse: あいさつメッセージを含むレスポンス
        
    Raises:
        HTTPException: 名前が不正な場合（400エラー）
    """
    try:
        message = greeting_use_case.execute(name)
        return GreetingResponse(message=message)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) 