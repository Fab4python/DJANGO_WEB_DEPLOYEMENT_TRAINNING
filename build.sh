#!/bin/bash
echo "🔧 Running Django collectstatic..."
python manage.py collectstatic --noinput
echo "✅ Build completed successfully!"
