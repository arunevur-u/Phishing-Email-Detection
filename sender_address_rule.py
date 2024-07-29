from .base_rule import BaseRule
from config.settings import Settings

class SenderAddressRule(BaseRule):
    def check(self, email: dict) -> bool:
        sender = email.get('from', '')
        if any(domain in sender for domain in Settings().get_setting("suspicious_domains")):
            return True
        return False
