"""
Application層：ユースケースを定義
APIからの入力を処理し、Domainロジックを呼び出す
"""

from app.domain.model import GreetingModel


class GreetingUseCase:
    """あいさつ処理のユースケース"""
    
    def __init__(self):
        self.greeting_model = GreetingModel()
    
    def execute(self, name: str) -> str:
        """
        あいさつ処理を実行する
        
        Args:
            name: あいさつ対象の名前
            
        Returns:
            あいさつメッセージ
            
        Raises:
            ValueError: 名前が不正な場合
        """
        # 入力値の前処理（空白の除去など）
        cleaned_name = name.strip() if name else ""
        
        # ドメインロジックの呼び出し
        return self.greeting_model.create_greeting(cleaned_name) 