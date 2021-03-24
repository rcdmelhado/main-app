# Ubuntu dev environment
### Install system dependencies
```
sudo apt install python-mysqldb python3.8-dev
```

### Activate python virtual environment
```
source venv/bin/activate
```

### Create config.ini file to store sensitive data
```
python configuration.py
```

### Install python dependencies
```
pip install -r requirements.txt
```

### DB commands
```
sudo docker-compose up
sudo docker-compose exec backend sh
    python manager.py init
    python manager.py migrate
    python manager.py upgrade
```