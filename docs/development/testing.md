# Testing

## Running Tests

Execute tests using pytest:

```bash
pytest tests/
```

## Test Categories

1. **Unit Tests**: Located in `tests/test_api.py`

   - Tests individual components
   - Uses mocking for external dependencies

## Adding New Tests

1. Create test files with `test_` prefix
2. Use pytest fixtures from `conftest.py`
3. Follow existing patterns for mocking and assertions

## CI Tests

Tests run automatically on:

- Every push to main branch
- Pull request creation to main branch
