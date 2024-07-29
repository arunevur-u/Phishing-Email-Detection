import re
from .base_rule import BaseRule
from config.settings import Settings

class SuspiciousLinksRule(BaseRule):
    def check(self, email: dict) -> bool:
        body = email.get('body', '')
        links = re.findall(r'http[s]?://\S+', body)
        for link in links:
            if any(domain in link for domain in Settings().get_setting("suspicious_domains")):
                return True
        return False
