# Flask CI/CD Demo

A simple Flask application to learn GitHub Actions CI/CD.

## Features

- Home endpoint
- Health check endpoint
- Greeting API endpoint

## Setup

### 1. Create virtual environment
```bash
python -m venv env
```

### 2. Activate virtual environment
**Windows:**
```bash
env\Scripts\activate
```

**Linux/Mac:**
```bash
source env/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

### 5. Run tests
```bash
pytest test_app.py -v
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Welcome message |
| `/health` | GET | Health check |
| `/api/greet/<name>` | GET | Greeting with name |

## CI/CD Pipeline

The GitHub Actions workflow includes:
1. **Test** - Runs pytest on every push/PR
2. **Build** - Builds the application
3. **Deploy** - Deploys to production (main branch only)

## License

MIT
