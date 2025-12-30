# Contributing to Reflexia Python SDK

Thank you for your interest in contributing to the Reflexia Python SDK!

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/reflexia/reflexia-python-sdk.git
cd reflexia-python-sdk
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e ".[dev]"
```

## Code Style

We use:
- **Black** for code formatting (line length: 100)
- **Ruff** for linting
- **mypy** for type checking

Before committing, run:
```bash
black reflexia/ examples/
ruff check reflexia/ examples/
mypy reflexia/
```

## Testing

Run tests with:
```bash
pytest
```

With coverage:
```bash
pytest --cov=reflexia --cov-report=html
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Ensure all tests pass and code is formatted
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## What to Contribute

We welcome contributions for:
- Bug fixes
- Documentation improvements
- Additional examples
- Type hints improvements
- Performance optimizations

**Note:** This SDK is a convenience wrapper around HTTP requests. We don't accept contributions that add business logic or change the API contract—those belong in the backend API.

## Questions?

Open an issue or contact us at support@reflexia.dev

