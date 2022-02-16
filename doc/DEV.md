# Dev OnBoarding

## Tools Requirements

- [VSCode](https://code.visualstudio.com/download)
- [Python 3.9](https://www.python.org/downloads/): 
- [NPM](https://nodejs.org/en/)

## Initial Command

```bash
# Create virtualenv for the local project
python3.9 -m venv .venv

# Install nodejs dependencies for dev tooling
# commitizen, husky, ...
npm install

# Install githook for git format
npx husky install
```
