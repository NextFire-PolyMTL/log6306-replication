import os
import re
import shutil
import subprocess
from contextlib import suppress
from pathlib import Path

from pydriller import Repository

PROJECT_DIR = Path('./projects/')
COMMITS_DIR = Path('./commits/')

MSG_MATCH_RE = re.compile(r'refactor', re.IGNORECASE)
FILES_MATCH_RE = re.compile(r'Dockerfile|docker-compose', re.IGNORECASE)

# Cleanup
with suppress(Exception):
    shutil.rmtree(COMMITS_DIR)
os.mkdir(COMMITS_DIR)

for project in PROJECT_DIR.iterdir():
    if project.is_dir():
        print(f"Analyzing {project.name}...")
        # Output project directory
        diff_dir = COMMITS_DIR / project.name
        os.mkdir(diff_dir)
        commits = []
        for commit in Repository(project.as_posix()).traverse_commits():
            # Check commit message
            if MSG_MATCH_RE.search(commit.msg):
                # Check modified files
                git_diff_tree = subprocess.run(
                    ['git', 'diff-tree', '--no-commit-id',
                        '--name-only', '-r', '-m', commit.hash],
                    cwd=project.as_posix(),
                    capture_output=True)
                git_diff_tree_stdout = git_diff_tree.stdout.decode()
                if any(FILES_MATCH_RE.search(f) for f in git_diff_tree_stdout.splitlines()):
                    print(f"- Found commit {commit.hash}")
                    # Save diff
                    os.system(f'GIT_DIR={project.as_posix()}/.git '
                              f'git show -m -l 2000 {commit.hash} > {diff_dir / commit.hash}.diff')
                    # If this is a merge commit, remove children which are included
                    with open(f"{diff_dir / commit.hash}.diff", 'r') as f:
                        for prev_commits in commits:
                            if prev_commits.hash in f.read():
                                print(f"|- Removing {prev_commits.hash}")
                                os.remove(
                                    f"{diff_dir / prev_commits.hash}.diff")
                    commits.append(commit)
