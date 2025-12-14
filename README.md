# GitGrade-Hackathon
# GitGrade – GitHub Repository Analyzer

## Overview
This project analyzes GitHub repositories and generates:
- A score based on project quality
- A summary of the repo
- A roadmap for improvement

## How it Works
1. User enters a GitHub repo URL.
2. `github_fetcher.py` fetches repo data.
3. `scorer.py` calculates a score and summary (hardcoded for demo).
4. `roadmap.py` generates actionable improvements.

## How to Run
1. Clone this repository
2. Create a virtual environment: `python -m venv .venv`
3. Install dependencies: `pip install streamlit`
4. Run the app: `streamlit run app.py`
5. Enter a repo URL and click "Analyze" to see results.

## Notes
- Demo uses hardcoded example repos from hackathon PDF.
- Works offline for screen recording purposes.
