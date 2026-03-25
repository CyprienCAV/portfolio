#!/usr/bin/env bash
# Portfolio Maintenance & Test Script
# Run this to check everything

echo "🎓 Portfolio BTS SIO - Maintenance Check"
echo "========================================"
echo ""

# Check files
echo "📁 Checking files..."
FILES=(
    "index.html"
    "script.js"
    "style.css"
    "assets"
    "README-PORTFOLIO.md"
    "GUIDE_PERSONNALISATION.md"
    "TEST_CHECKLIST.md"
    "README-TAILWIND.md"
    "STRUCTURE_TECHNIQUE.md"
    "RESUME_PROJET.md"
    "START_HERE.md"
)

for file in "${FILES[@]}"; do
    if [ -e "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ MISSING: $file"
    fi
done

echo ""
echo "📊 File sizes:"
wc -l index.html script.js style.css 2>/dev/null | tail -1

echo ""
echo "🚀 To start:"
echo "  python -m http.server 8000"
echo "  Then open: http://localhost:8000"

echo ""
echo "📖 Reading order:"
echo "  1. START_HERE.md"
echo "  2. README-PORTFOLIO.md"
echo "  3. RESUME_PROJET.md"
echo "  4. GUIDE_PERSONNALISATION.md"
echo "  5. TEST_CHECKLIST.md"

echo ""
echo "✅ Setup complete! You're ready to go."
