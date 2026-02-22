from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from engine.nlp_engine import NLPEngine
from engine.scraper_simulator import ScraperSimulator
import uvicorn
import os

app = FastAPI(title="Data Breach Finder API")

# Initialize engines
nlp = NLPEngine()
scraper = ScraperSimulator()

# Shared state for demonstration
leaks_db = []
raw_feeds = []

@app.get("/api/scan")
async def scan_feeds():
    """Triggers a mock scrape and analyzes results."""
    new_posts = [scraper.generate_random_post() for _ in range(5)]
    raw_feeds.extend(new_posts)
    
    new_leaks = []
    for post in new_posts:
        findings = nlp.analyze_text(post["content"])
        if findings:
            leak_entry = {
                "post": post,
                "findings": findings,
                "severity": "High" if len(findings) > 1 else "Medium"
            }
            leaks_db.append(leak_entry)
            new_leaks.append(leak_entry)
            
    return {"message": f"Scanned 5 posts, found {len(new_leaks)} leaks", "new_leaks": new_leaks}

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
