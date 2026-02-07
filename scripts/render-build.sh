#!/usr/bin/env bash
set -euo pipefail

python -m pip install --upgrade pip
pip install -r requirements.txt

cd frontend
rm -rf dist
npm install
npm run build
cd ..

python manage.py collectstatic --noinput
python manage.py migrate
