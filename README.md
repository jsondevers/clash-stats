# Clash of Clans Stats

I have played Clash of Clans since I was in sixth grade, and have always been on and off with it. For those who are familar, I am Town Hall 13 (not rushed). I love the game and that is why I created a simple python script to help track my Clash of Clans progression over the years.

## Prerequisites

 <details>
<summary> 1. Setting up the environment </summary>
<p>[config]</p>
</details>

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requests.

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

## License

[MIT](https://choosealicense.com/licenses/mit/)
