# Heads-or-Tails
Heads or Tails is a game written in the Python3 programming language with the Flask framework.

## Installation for Linux/Mac-os

Update package manager and install python3 & pip3 :

```bash
sudo apt-get update
sudo apt-get install python3
sudo apt-get -y install python3-pip
```

Check your pip3 version :

```bash
pip3 --version
```

Result pip3 version:

```bash
pip 18.1 from /usr/lib/python3/dist-packages/pip (python 3.7)
```


Install virtual environment :
```bash
sudo apt-get install python3-venv
```
Cloning Project and go to the Heads-or-Tailse folder :

```bash
git clone https://github.com/thedarkbrain/Heads-or-Tails.git

cd Heads-or-Tails
```

‍‍Creating virtual environment :
```bash
python3 -m venv .env 
```
Virtual environment activation :
```bash
source .env/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements :
```python
pip3 install -r requirements.txt
```
## Run

To implement the project :
```python
flask run
```

If you want to boot the project in debug mode :
```python
FLASK_ENV=development flask run
```

## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

