from detector.rule_factory import RuleFactory

def get_email_input():
    email = {}
    email['from'] = input("Enter the sender's email address: ")
    email['subject'] = input("Enter the email subject: ")
    email['body'] = input("Enter the email body: ")
    return email

def main():
    print("Phishing Email Detection System")
    print("===============================")
    
    email = get_email_input()

    rules = ["suspicious_links", "sender_address", "urgent_language"]
    results = {}

    for rule_type in rules:
        rule = RuleFactory.get_rule(rule_type)
        results[rule_type] = rule.check(email)

    for rule, found in results.items():
        if found:
            print(f"Phishing detected by rule: {rule}")
        else:
            print(f"No phishing detected by rule: {rule}")

if __name__ == "__main__":
    main()
