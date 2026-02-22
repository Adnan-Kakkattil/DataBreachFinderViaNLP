import requests
from duckduckgo_search import DDGS
import time
import random

class RealDataFetcher:
    def __init__(self):
        self.xposed_api = "https://api.xposedornot.com/v1/check-email/"
        self.ddgs = DDGS()

    def fetch_data(self, query=None):
        results = []
        
        if not query:
            # If no query, return some generic "recent discovery" samples or mock a live stream
            return results

        # 1. Check XposedOrNot for real breaches
        try:
            response = requests.get(f"{self.xposed_api}{query}", timeout=10)
            if response.status_code == 200:
                breaches = response.json().get("breaches", [])
                for breach in breaches:
                    results.append({
                        "id": f"breach-{random.randint(1000, 9999)}",
                        "platform": "Global Data Breach (XposedOrNot)",
                        "user": query,
                        "content": f"Target found in {breach} data breach. Potential exposure of credentials/PII.",
                        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                    })
        except Exception as e:
            print(f"XposedOrNot Error: {e}")

        # 2. Search DuckDuckGo for public mentions on paste sites
        try:
            search_query = f'"{query}" (site:pastebin.com OR site:github.com OR site:ghostbin.com OR site:controlc.com)'
            search_results = self.ddgs.text(search_query, max_results=5)
            for res in search_results:
                results.append({
                    "id": f"search-{random.randint(1000, 9999)}",
                    "platform": "Web Search (Mentions)",
                    "user": "Public OSINT",
                    "content": f"{res['title']}: {res['body']}",
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                })
        except Exception as e:
            print(f"DuckDuckGo Search Error: {e}")

        return results

if __name__ == "__main__":
    fetcher = RealDataFetcher()
    test_query = "sivakumartn@gmail.com"
    print(fetcher.fetch_data(test_query))
