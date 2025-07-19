"""
FastAPIアプリケーションのエントリーポイント
"""

from fastapi import FastAPI

from app.api.hello import router as hello_router


def create_app() -> FastAPI:
    """
    FastAPIアプリケーションを作成する
    
    Returns:
        FastAPI: 設定済みのFastAPIアプリケーション
    """
    app = FastAPI(
        title="Hello Name App",
        description="Level 0: 名前を受け取ってあいさつを返すシンプルなAPI",
        version="1.0.0"
    )
    
    # ルーターの登録
    app.include_router(hello_router)
    
    return app


# アプリケーション作成
app = create_app()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 