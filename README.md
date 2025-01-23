# AI-Driven Product Owner

This is a FastAPI-based application that simulates a Product Owner powered by AI. It can manage requirements, prioritize tasks using AI, and handle feedback.

## Features
- Requirement management with AI-based prioritization.
- Feedback management.
- API documentation at `/docs`.
- Docker support for containerized deployment.
- CI/CD pipeline configuration using GitHub Actions.

## Installation
1. Clone the repo:
   ```bash
   git clone https://github.com/canerskrc/ai-product-owner.git
   cd ai-product-owner
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   uvicorn main:app --reload
   ```

## Docker Support
To run the application using Docker:
1. Build the Docker image:
   ```bash
   docker build -t ai-product-owner .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 ai-product-owner
   ```
3. Access the application at [http://localhost:8000/docs](http://localhost:8000/docs).

## CI/CD Pipeline
A sample GitHub Actions workflow is included in `.github/workflows/main.yml` for CI/CD.

### Features:
- **Linting:** Ensures code quality with `flake8`.
- **Testing:** Runs tests using `pytest`.
- **Docker Build:** Builds the Docker image.

### Example Workflow:
```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.9

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: pytest

    - name: Lint code
      run: flake8 .

    - name: Build Docker image
      run: |
        docker build -t ai-product-owner .
```

## Testing
To run tests:
```bash
pytest
```

## API Endpoints
### `/requirements` (GET)
- Fetch the list of requirements.

### `/requirements` (POST)
- Add a new requirement.
- **Request Body Example:**
  ```json
  {
      "id": 1,
      "title": "Dark mode",
      "description": "Add dark mode to the app."
  }
  ```

### `/feedback` (POST)
- Add feedback for a specific requirement.
- **Request Body Example:**
  ```json
  {
      "requirement_id": 1,
      "feedback_text": "Dark mode is essential for night users."
  }
  ```

### `/feedback/{requirement_id}` (GET)
- Get feedback for a specific requirement.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to submit issues or pull requests to contribute to the project. For major changes, please open an issue first to discuss your ideas.
