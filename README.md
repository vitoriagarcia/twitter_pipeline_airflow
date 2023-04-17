## 1 Create a virtualenv (in this case, called '.venv')
```bash
virtualenv .venv
```

## 2 Install mandatory packages
```bash
pip install -r requirements.txt
```

## 3 Activate the virtualenv
```bash
source .venv/bin/activate
```

## 4 Create an file called config.py to store the Twitter API secrets

## 5 Create an EC2 instance at AWS that uses Ubuntu

## 6 Save the credentials in this folder

## 7 In the AWS Console, click in 'Connect' > SSH Client.
Run the command that starts with:
```bash
chmod 400
```
To make sure your private key is protected. Then, connect with the EC2 server running the SSH command that starts with:
```bash
ssh -i "your-key-name.pem"
```

## 8 Install/update the following packages in the EC2
```bash
sudo apt-get update
sudo apt install puthon3-pip
sudo pip install apache-airflow
sudo pip install pandas
sudo pip install s3fs
sudo pip install tweepy
```
