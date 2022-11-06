if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/AL3X-Github/ZeroTwo.git /ZeroTwo
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /ZeroTwo
fi
cd /ZeroTwo
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
