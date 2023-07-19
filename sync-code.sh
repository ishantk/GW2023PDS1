#!/bin/sh

echo "Adding files..."
git add .

read -rp "Enter the commit message: " commit_message
if [[ -z "$commit_message" ]]; then
    echo "Error: Commit message cannot be empty."
    exit 1
fi

echo "Committing Changes..."
git commit -m "$commit_message"

echo "Pushing Code to Remote Repository..."
git push -u origin main