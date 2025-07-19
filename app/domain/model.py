"""
Domain層：ビジネスロジックを定義
名前からあいさつ文を作成する核心的な機能
"""

class GreetingModel:
    """あいさつメッセージを生成するドメインモデル"""
    
    @staticmethod
    def create_greeting(name: str) -> str:
        """
        名前からあいさつメッセージを作成する
        
        Args:
            name: あいさつ対象の名前
            
        Returns:
            あいさつメッセージ
        """
        if not name:
            raise ValueError("名前が指定されていません")
        
        return f"Hello, {name}!" 