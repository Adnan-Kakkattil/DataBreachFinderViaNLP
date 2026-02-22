import random
import time

class ScraperSimulator:
    def __init__(self):
        self.platforms = ["Twitter", "Facebook", "LinkedIn", "GitHub", "Pastebin"]
        self.users = ["user_99", "dev_pro", "leaker_xh", "anon_admin", "company_bot"]
        self.templates = [
            "Just pushed some code to my repo! #coding #python",
            "I forgot my password again... is it {password}?",
            "Config file leak: DB_HOST=localhost, DB_USER=root, DB_PASS={password}",
            "Contact me for info: {email}",
            "New API key generated: {api_key}",
            "Check out this internal doc: {url}",
            "My SSN is {ssn}, don't tell anyone lol",
            "Payment failed for card {card}",
            "Normal day at work, nothing to report."
        ]
        
    def generate_random_post(self):
        platform = random.choice(self.platforms)
        user = random.choice(self.users)
        template = random.choice(self.templates)
        
        # Inject sensitive data randomly
        post = template.format(
            password=random.choice(["Admin123!", "qwerty12345", "password000"]),
            email=random.choice(["test@test.com", "leak@leaker.net", "info@company.org"]),
            api_key="".join(random.choices("abcdef0123456789", k=32)),
            ssn="123-45-6789",
            card="4111-2222-3333-4444",
            url="http://internal.secrets.corp/doc1"
        )
        
        return {
            "id": random.randint(1000, 9999),
            "platform": platform,
            "user": user,
            "content": post,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

if __name__ == "__main__":
    sim = ScraperSimulator()
    for _ in range(5):
        print(sim.generate_random_post())
        time.sleep(1)
