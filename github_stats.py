import requests
import json
import datetime
import os

GITHUB_USERNAME = "Blackfalcon307"  # your GitHub username
OUTPUT_FILE = "github_report.txt"

def get_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.json().get('message')}")
        return []
    return response.json()

def get_commit_count(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
    response = requests.get(url, params={"per_page": 100})
    if response.status_code == 200:
        return len(response.json())
    return 0

def generate_report(username):
    print(f"Fetching stats for GitHub user: {username}\n")
    repos = get_repos(username)

    if not repos:
        print("No repositories found.")
        return

    report_lines = []
    report_lines.append("=" * 50)
    report_lines.append(f"GitHub Stats Report - {username}")
    report_lines.append(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("=" * 50)
    report_lines.append(f"Total Repositories: {len(repos)}\n")

    total_stars = 0
    total_forks = 0

    for repo in repos:
        name        = repo['name']
        stars       = repo['stargazers_count']
        forks       = repo['forks_count']
        language    = repo['language'] or "N/A"
        updated     = repo['updated_at'][:10]
        commits     = get_commit_count(username, name)

        total_stars += stars
        total_forks += forks

        line = (f"Repo    : {name}\n"
                f"Language: {language}\n"
                f"Stars   : {stars} | Forks: {forks} | Commits: {commits}\n"
                f"Updated : {updated}\n"
                f"{'-' * 50}")
        report_lines.append(line)
        print(line)

    summary = (f"\nSUMMARY\n"
               f"Total Stars : {total_stars}\n"
               f"Total Forks : {total_forks}\n"
               f"Total Repos : {len(repos)}")
    report_lines.append(summary)
    print(summary)

    with open(OUTPUT_FILE, 'w') as f:
        f.write("\n".join(report_lines))
    print(f"\nReport saved to {OUTPUT_FILE}")

if __name__ == '__main__':
    generate_report(GITHUB_USERNAME)