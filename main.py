from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from engine.nlp_engine import NLPEngine
from engine.real_data_fetcher import RealDataFetcher
import uvicorn
import os

app = FastAPI(title="Social Media Monitoring for Data Leakage API")

# Initialize engines
nlp = NLPEngine()
fetcher = RealDataFetcher()

# Shared state for demonstration
leaks_db = []
raw_feeds = []

@app.get("/api/scan")
async def scan_feeds(query: str = None):
    """Triggers a real-world discovery and analyzes results."""
    # If no query provided, show historical data or a message
    if not query:
        return {"message": "Please providing a target (Email/Username) to search online.", "new_leaks": []}

    new_posts = fetcher.fetch_data(query)
    raw_feeds.extend(new_posts)
    
    new_leaks = []
    for post in new_posts:
        findings = nlp.analyze_text(post["content"])
        # Even if NLP doesn't find a specific pattern, the breach match is high severity
        if "Global Data Breach" in post["platform"]:
            leak_entry = {
                "post": post,
                "findings": findings if findings else [{"type": "BREACH_HISTORY", "value": "Found in database"}],
                "severity": "Critical"
            }
            leaks_db.append(leak_entry)
            new_leaks.append(leak_entry)
        elif findings:
            leak_entry = {
                "post": post,
                "findings": findings,
                "severity": "High" if len(findings) > 1 else "Medium"
            }
            leaks_db.append(leak_entry)
            new_leaks.append(leak_entry)
            
    return {"message": f"Discovered {len(new_posts)} occurrences, identified {len(new_leaks)} critical leaks", "new_leaks": new_leaks}

@app.get("/api/dashboard")
async def get_dashboard_data():
    """Returns historical leaks and stats."""
    return {
        "total_scanned": len(raw_feeds),
        "total_leaks": len(leaks_db),
        "leaks": leaks_db[-10:] # Last 10 leaks
    }

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_index():
    return FileResponse("static/index.html")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
