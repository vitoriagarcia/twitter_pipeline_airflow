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

## 7 Connect it via SSH

## 8 Execute the command that starts with
```bash
ssh -i "your-key-name.pem"
```

## 9 Install/update the following packages in the EC2
```bash
sudo apt-get update
sudo apt install puthon3-pip
sudo pip install apache-airflow
sudo pip install pandas
sudo pip install s3fs
sudo pip install tweepy
```
