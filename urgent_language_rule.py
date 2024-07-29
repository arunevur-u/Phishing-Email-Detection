from .base_rule import BaseRule
from config.settings import Settings

class UrgentLanguageRule(BaseRule):
    def check(self, email: dict) -> bool:
        subject = email.get('subject', '').lower()
        body = email.get('body', '').lower()
        urgent_keywords = Settings().get_setting("urgent_keywords")
        for keyword in urgent_keywords:
            if keyword in subject or keyword in body:
                return True
        return False
