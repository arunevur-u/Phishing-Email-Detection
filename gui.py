import tkinter as tk
from tkinter import messagebox
from detector.rule_factory import RuleFactory

class PhishingEmailDetectorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Phishing Email Detection System")
        
        # Sender Email
        self.label_from = tk.Label(root, text="Sender Email:")
        self.label_from.grid(row=0, column=0, padx=10, pady=5)
        self.entry_from = tk.Entry(root, width=50)
        self.entry_from.grid(row=0, column=1, padx=10, pady=5)
        
        # Email Subject
        self.label_subject = tk.Label(root, text="Email Subject:")
        self.label_subject.grid(row=1, column=0, padx=10, pady=5)
        self.entry_subject = tk.Entry(root, width=50)
        self.entry_subject.grid(row=1, column=1, padx=10, pady=5)
        
        # Email Body
        self.label_body = tk.Label(root, text="Email Body:")
        self.label_body.grid(row=2, column=0, padx=10, pady=5)
        self.text_body = tk.Text(root, height=10, width=50)
        self.text_body.grid(row=2, column=1, padx=10, pady=5)
        
        # Submit Button
        self.button_submit = tk.Button(root, text="Detect Phishing", command=self.detect_phishing)
        self.button_submit.grid(row=3, columnspan=2, pady=10)
        
    def detect_phishing(self):
        email = {
            'from': self.entry_from.get(),
            'subject': self.entry_subject.get(),
            'body': self.text_body.get("1.0", tk.END)
        }
        
        rules = ["suspicious_links", "sender_address", "urgent_language"]
        results = {}

        for rule_type in rules:
            rule = RuleFactory.get_rule(rule_type)
            results[rule_type] = rule.check(email)
        
        result_text = "\n".join([f"{rule}: {'Detected' if found else 'Not Detected'}" for rule, found in results.items()])
        messagebox.showinfo("Detection Results", result_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = PhishingEmailDetectorGUI(root)
    root.mainloop()
