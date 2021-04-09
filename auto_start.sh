tmux attach 
if pgrep -f "python streamer.py.py" &>/dev/null; then
    echo "it is already running"
    tmux detach
    exit
else
    echo "Sanity check back ups: "
    python3 backup_auto.py
    echo "re-starting script "
    python streamer.py & 
    tmux detach
fi