#!/bin/bash
echo "Installing dependencies..."
sudo apt update
sudo apt install tmux

# Run Flask backend
echo "Starting Flask backend..."
cd backend || exit
pip install -r requirements.txt
cd api || exit
tmux new-session -d -s tripfinderapp -n backend 'python3 main.py'
cd ../.. || exit

# Run Vue.js frontend
echo "Starting Vue.js frontend..."
cd frontend/tripfinderapp || exit
tmux new-window -t tripfinderapp:1 -n frontend 'npm install && npm install axios && npm run serve'

# Opening tmux session
tmux a -t tripfinderapp