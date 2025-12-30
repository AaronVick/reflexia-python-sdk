# Test Suite

Comprehensive test suite for Reflexia Python SDK with PhD-level rigor.

## Running Tests

```bash
# Install test dependencies
pip install -e ".[dev]"

# Run all tests
pytest

# Run with coverage
pytest --cov=reflexia --cov-report=html

# Run specific test file
pytest tests/test_field.py

# Run specific test
pytest tests/test_field.py::TestFieldClient::test_register_agent_success

# Run with verbose output
pytest -v
```

## Test Structure

- `test_client.py` - Core client functionality, error handling, HTTP requests
- `test_field.py` - Field Engine API methods (register, sense, modify, etc.)
- `test_epistemic.py` - Epistemic Service API methods (consistency checking)
- `test_patterns.py` - Pattern Store API methods (store, query, aggregate)
- `test_payment.py` - Payment API methods
- `test_account.py` - Account management API methods
- `test_exceptions.py` - Exception classes
- `conftest.py` - Shared fixtures and test configuration

## Test Coverage Goals

- ✅ All API endpoints are tested
- ✅ All input validation is tested
- ✅ All error cases are tested
- ✅ All return values are verified
- ✅ All service clients are tested
- ✅ All exception types are tested

## Mocking Strategy

All tests use mocking to avoid hitting real API endpoints:
- HTTP requests are mocked using `unittest.mock`
- API responses are simulated with realistic data
- Error cases are tested with appropriate HTTP status codes

## Continuous Integration

Tests should be run:
- Before every commit
- In CI/CD pipeline
- Before releases

## Adding New Tests

When adding new features:
1. Add tests for happy path
2. Add tests for error cases
3. Add tests for input validation
4. Add tests for edge cases
5. Ensure coverage remains > 90%

