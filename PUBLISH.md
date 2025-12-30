# Publishing to PyPI

## Prerequisites

1. **Create PyPI accounts** (if you don't have them):
   - Test PyPI: https://test.pypi.org/account/register/
   - Production PyPI: https://pypi.org/account/register/

2. **Install build tools** (already done):
   ```bash
   pip install build twine
   ```

## Publishing Steps

### Step 1: Test on Test PyPI (Recommended)

First, test your package on Test PyPI to make sure everything works:

```bash
# Upload to Test PyPI
python3 -m twine upload --repository testpypi dist/*

# You'll be prompted for:
# - Username: __token__
# - Password: Your Test PyPI API token (create at https://test.pypi.org/manage/account/token/)
```

**Create Test PyPI API Token:**
1. Go to https://test.pypi.org/manage/account/token/
2. Click "Add API token"
3. Name it (e.g., "reflexia-sdk")
4. Copy the token (starts with `pypi-`)

**Test Installation:**
```bash
# Install from Test PyPI to verify it works
pip install --index-url https://test.pypi.org/simple/ reflexia

# Test it
python3 -c "from reflexia import ReflexiaClient; print('Success!')"
```

### Step 2: Publish to Production PyPI

Once Test PyPI works, publish to production:

```bash
# Upload to Production PyPI
python3 -m twine upload dist/*

# You'll be prompted for:
# - Username: __token__
# - Password: Your PyPI API token (create at https://pypi.org/manage/account/token/)
```

**Create PyPI API Token:**
1. Go to https://pypi.org/manage/account/token/
2. Click "Add API token"
3. Name it (e.g., "reflexia-sdk")
4. Select scope: "Entire account" (or just this project)
5. Copy the token (starts with `pypi-`)

**Verify Installation:**
```bash
# Install from production PyPI
pip install reflexia

# Test it
python3 -c "from reflexia import ReflexiaClient; print('Success!')"
```

## After Publishing

Your package will be available at:
- **PyPI**: https://pypi.org/project/reflexia/
- **Installable via**: `pip install reflexia`

## Future Releases

For new versions:

1. Update version in `pyproject.toml`:
   ```toml
   version = "0.1.1"  # or "0.2.0", etc.
   ```

2. Rebuild:
   ```bash
   python3 -m build
   ```

3. Upload:
   ```bash
   python3 -m twine upload dist/*
   ```

## Security Notes

- **Never commit API tokens** to git
- Use environment variables or keyring for tokens
- Tokens can be scoped to specific projects
- You can revoke tokens at any time

## Troubleshooting

**Error: "File already exists"**
- Version already published. Increment version in `pyproject.toml`

**Error: "Invalid credentials"**
- Check your API token
- Make sure you're using `__token__` as username
- Token should start with `pypi-` (production) or `pypi-` (test)

**Error: "Package name already taken"**
- The name "reflexia" might be taken
- Check https://pypi.org/project/reflexia/
- If taken, you'll need to choose a different name

