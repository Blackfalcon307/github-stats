# GitHub Repo Stats Fetcher

A Python CLI tool that fetches repository statistics for any GitHub
user using the GitHub REST API and generates a formatted report.

## Features
- Fetches all public repositories of a GitHub user
- Shows stars, forks, commits, language, and last updated date
- Generates a summary with total stars and forks
- Saves full report to a .txt file automatically

## Technologies
- Python 3
- GitHub REST API
- requests library
- JSON parsing

## Setup

### 1. Clone the repo
git clone https://github.com/Blackfalcon307/github-stats

### 2. Install dependencies
pip install requests

### 3. Run
python github_stats.py

## Sample Output
==================================================
GitHub Stats Report - Blackfalcon307
Generated: 2026-06-30 10:00:00
==================================================
Total Repositories: 3

Repo    : s3-file-backup
Language: Python
Stars   : 0 | Forks: 0 | Commits: 3
Updated : 2026-06-29
--------------------------------------------------

SUMMARY
Total Stars : 0
Total Forks : 0
Total Repos : 3

Report saved to github_report.txt

## Use Case
Useful for developers to quickly audit their GitHub profile
and track repository activity via API automation.