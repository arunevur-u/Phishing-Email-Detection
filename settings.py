class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Settings, cls).__new__(cls)
            # Initialize default settings here
            cls._settings = {
                "suspicious_domains": ["example.com", "phishing.com"],
                "urgent_keywords": ["urgent", "verify", "immediate", "important"]
            }
        return cls._instance

    def get_setting(self, key):
        return self._settings.get(key, None)
