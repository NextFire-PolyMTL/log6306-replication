#/bin/bash
git log --format=%B -n 1 $1
git diff $1~ $1