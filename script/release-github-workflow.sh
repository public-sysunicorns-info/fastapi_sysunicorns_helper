#!/usr/bin/env bash

plugin="@semantic-release/github"
plugin="${plugin},@semantic-release/commit-analyzer"
plugin="${plugin},@semantic-release/release-notes-generator"
plugin="${plugin},@semantic-release/changelog"
plugin="${plugin},@semantic-release/exec"
plugin="${plugin},@semantic-release/git"

npx semantic-release -b main -p "${plugin}"
