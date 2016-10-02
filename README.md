# FB Access Token Generator API

Can be used to get generate access tokens from facebook to use them in [FB Data Scraper](https://github.com/scottydelta/fb_token_generator). It makes use of Selenium and PhantonJS to emulate browser and extract the access tokens.

## Setup & Execution

* One time manual authorization to the `Graph API Explorer` app on fb by visiting the link [`Graph API Explorer`](https://developers.facebook.com/tools/explorer/) and then clicking on `Get Token` > `Get User Access Token` > `Get Access Token` > `Continue as ` *`Name`*. [*Video Instructions*](http://i.imgur.com/RsHnxle.gifv)
* `git clone https://github.com/scottydelta/fb_token_generator.git`
* `cd fb_token_generator`
* install [`Selenium`](https://pypi.python.org/pypi/selenium) using [`pip`](https://packaging.python.org/install_requirements_linux/#installing-pip-setuptools-wheel-with-linux-package-managers) 
* install [`PhantomJS`](http://phantomjs.org/download.html)(on Mac, you can install using `homebrew`)
* run the script using command `python generate_token.py` *`username`* *`password`*