#!/bin/bash
# Helper script for publishing Reflexia Python SDK to PyPI

set -e

echo "🚀 Reflexia Python SDK - PyPI Publishing Helper"
echo "================================================"
echo ""

# Check if dist/ exists and has files
if [ ! -d "dist" ] || [ -z "$(ls -A dist/*.whl dist/*.tar.gz 2>/dev/null)" ]; then
    echo "❌ No distribution files found. Building package..."
    python3 -m build
fi

echo "✅ Package files ready:"
ls -lh dist/

echo ""
echo "Choose an option:"
echo "1) Upload to Test PyPI (recommended first)"
echo "2) Upload to Production PyPI"
echo "3) Check package files"
read -p "Enter choice [1-3]: " choice

case $choice in
    1)
        echo ""
        echo "📦 Uploading to Test PyPI..."
        echo "Username: __token__"
        echo "Password: Your Test PyPI API token (starts with pypi-)"
        echo ""
        python3 -m twine upload --repository testpypi dist/*
        echo ""
        echo "✅ Uploaded to Test PyPI!"
        echo "Test installation with:"
        echo "  pip install --index-url https://test.pypi.org/simple/ reflexia"
        ;;
    2)
        echo ""
        echo "📦 Uploading to Production PyPI..."
        echo "Username: __token__"
        echo "Password: Your PyPI API token (starts with pypi-)"
        echo ""
        python3 -m twine upload dist/*
        echo ""
        echo "✅ Uploaded to Production PyPI!"
        echo "Install with: pip install reflexia"
        ;;
    3)
        echo ""
        echo "🔍 Checking package files..."
        python3 -m twine check dist/*
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac

