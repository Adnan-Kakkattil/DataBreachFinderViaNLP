import re

class NLPEngine:
    def __init__(self):
        # Basic patterns for sensitive data
        self.patterns = {
            "email": r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            "api_key": r'(?:key|token|secret|auth|api)[-_]?(?:id|key|token|secret)?\s*[:=]\s*["\']?([a-zA-Z0-9]{16,})["\']?',
            "password": r'(?:password|passwd|pwd)\s*[:=]\s*["\']?([^\s"\']{6,})["\']?',
            "ssn": r'\b\d{3}-\d{2}-\d{4}\b',
            "credit_card": r'\b(?:\d{4}[ -]?){3}\d{4}\b'
        }

    def analyze_text(self, text):
        findings = []
        for key, pattern in self.patterns.items():
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                findings.append({
                    "type": key,
                    "value": match.group(0),
                    "context": text[max(0, match.start()-20):min(len(text), match.end()+20)].strip()
                })
        return findings

if __name__ == "__main__":
    engine = NLPEngine()
    test_text = "Check out my new app! My api_key = 'abc1234567890def123' and password: password123. Contact me at adnan@example.com"
    print(engine.analyze_text(test_text))
