# tweepy_bot
Home of a basic twitter bot for DS4A workshops


## Getting this runnin on a VM

To have this launch on a VM, for the most part you just need to fill out the credentials in `login.py` with your Twitter tokens, and your cloud.cybera.ca credentials. 

**Note** If you are reading this to run as a Cybera employee, the twitter tokens are already filled out, and you will only need to populate the following in `login.py`

```python
you = 'your_cybera_email'
...

swift_me = you
swift_pass = 'your_swift_password'
```

Because this is getting stored as plain text, I recommend you only give yourself `ssh` credentials to the VM, or have a shared account for the upload.

Once you've filled in `login.py`, you need to start the process. So you can leave this running, I recommend using `tmux`. You can launch `tmux` and the streamer as follows once you are in the `tweepy_bot` directory on your VM

```bash
tmux attach
python3 streamer.py
Ctrl + b
Ctrl + d
```
From here, you can log out of your VM and the twitter bot will happily gather tweets and back them up remotely on Swift. 