# Clash of Clans Stats

I have played Clash of Clans since I was in sixth grade, and have always been on and off with it. For those who are familar, I am Town Hall 13 (not rushed). I love the game and that is why I created this python manager system to help track my Clash of Clans progression over the years.

## Requirements

 <details>
<summary> 1. Setting up the environment </summary>
<p> I used python <a href="https://docs.python.org/3/library/venv.html">venv</a> to set up my virtual environment to help maintain packages 
</p>
</details>
 <details>
<summary> 2. Getting a Clash of Clan API Token </summary>

<li> Go to <a href="https://developer.clashofclans.com/#/documentation">Clash of Clan's API</a> 
</li>
<li> Generate a API_TOKEN 
</li>
<li> Turn your API_TOKEN into an enviornment variable 
</li>

</details>

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following:

- ### [flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/)

```bash
pip install flask
```

- ### [dot-env](https://pypi.org/project/python-dotenv/) this follows the [12-factor](https://12factor.net/) principle.

```bash
pip install python-dotenv
```

- ### [requests](https://pypi.org/project/requests/) (for more info use [real-python](https://realpython.com/python-requests/) request reference)

```bash
pip install requests
```

## Usage

### Interacting with the API

```python
import requests

response = requests.get(
"https://api.clashofclans.com/v1/players/%23" + MY_TAG, headers=headers
    )

```

## Contributing
