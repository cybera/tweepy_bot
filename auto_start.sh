if pgrep -f "python streamer.py.py" &>/dev/null; then
    echo "it is already running"
    exit
else
    echo "Sanity check back ups: "
    python3 backup_auto.py
    echo "re-starting script "
    python streamer.py
fi