class TokenManager():
    def __init__(self):
        self.current_token = "EXPIRED_TOKEN_V1"

    def get_current_token(self) -> str:
        return self.current_token

    def refresh_token(self):
        self.current_token = "VALID_SECURE_TOKEN_V2"
        return self.current_token