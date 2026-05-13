#!/bin/bash
echo "starting installation..."
chmod +x TasksCLI.py
# Create a symlink so 'tasks' runs the script
sudo ln -sf "$(pwd)/TasksCLI.py" /usr/local/bin/tasks
echo "Installation complete. Type 'TasksCLI' to start."
