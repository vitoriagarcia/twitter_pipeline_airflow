## ETL Cloud-based project that extracts data from Twitter, filter, and store it in an AWS S3 bucket
This project is hosted in an EC2 instance and orchestrated by Apache Airflow.

## Architecture:

<img width="1198" alt="Screenshot 2023-04-18 at 14 23 10" src="https://user-images.githubusercontent.com/47197078/232858609-bc284710-7681-40df-a9d3-3217f87ff2b7.png">

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

## 4 Create a file called config.py to store the Twitter API secrets

## 5 Create an EC2 instance at AWS that uses Ubuntu

## 6 Save the credentials in this folder

## 7 Create the code that does the operations you want

## 8 In the AWS Console, click in 'Connect' > SSH Client.
Run the command that starts with:
```bash
chmod 400
```
To make sure your private key is protected. Then, connect with the EC2 server running the SSH command that starts with:
```bash
ssh -i "your-key-name.pem"
```

## 9 Install/update the following packages in the EC2
```bash
sudo apt-get update
sudo apt install python3-pip
sudo pip install apache-airflow
sudo pip install pandas
sudo pip install s3fs
sudo pip install tweepy
```

## 9 Run the Airflow server
```bash
airflow standalone
```

## 10 Create a folder containing your codes & credentials

## 11 Make sure that the file
```bash
airflow/airflow.cfg
```
Contains the correct path to the folder containing your code.

This project was based on the [Darshil Parmar's video](https://www.youtube.com/watch?v=q8q3OFFfY6c).
