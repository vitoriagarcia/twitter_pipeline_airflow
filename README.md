# Create a virtualenv (in this case, called '.venv')
```bash
virtualenv .venv
```

# Install mandatory packages
```bash
pip install -r requirements.txt
```

# Activate the virtualenv
```bash
source .venv/bin/activate
```

# Create an file called config.py to store the Twitter API secrets

# Create an EC2 instance at AWS that uses Ubuntu, save the credentials in this folder and then connect it via SSH and execute the command that starts with
```bash
ssh -i "your-key-name.pem"
```

# Install/update the following packages in the EC2:
```bash
sudo apt-get update
sudo apt install puthon3-pip
sudo pip install apache-airflow
sudo pip install pandas
sudo pip install s3fs
sudo pip install tweepy
```