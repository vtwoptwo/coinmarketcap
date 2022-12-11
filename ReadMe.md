
# CMC
## Coin Market Cap Endpoint: Listings/Latest
<br>

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a>
    <img src="backend_api\static\images\logo.jpeg" alt="Logo" style="border-radius: 25px; width:100px" >
  </a>

<h3 align="center">CoinMarketCap</h3>


  <p align="center">
    You are a member of the Info-Prov Team, and as such, your duty is to compose valuable cryptocurrency market insights for our customers.
One important key metric is the evolution of the market capitalization of the largest coins throughout time.

Such information is available at CoinMarketCap, a popular site that offers real time data about the most popular assets in the crypto market.
    <br />
    <br />
    <br />
    <a href="https://coinmarketcap.com/"><strong>See CoinMarketCap»</strong></a>
    ·
    <a href="#about-the-project"><strong>See the project»</strong></a>
    ·
    <a href=#usage>How to use this repo</a>
    ·
    <a href="https://github.com/vtwoptwo/coinmarketcap/issues">Report Bug</a>
    ·
    <a href="https://github.com/vtwoptwo/coinmarketcap/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Retrieve from CoinMarketCap API Listings Historical endpoint the top 10 coins with the largest market capitalization.
For each of the retrieved coins, calculate the percentage its market capitalization represents compared to the group.
For each coin, stores a document in a mongo db collection, with the following schema:
* symbol: the coin symbol
*  price: coin price in USD
*  market_cap: market capitalization in USD
*  market_cap_pct: market capitalization percentage this coin represents out of the group of 10.
*  last_updated: the timestamp associated with the data retrieved.

Further Requirements: 
*  Write it in python
* Set up a system that runs this process once every minute


PS: I ended up using the following endpoint: [Crypto Listings Latest](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest) ,  which has the same structure as the historical endpoint and falls under the BASIC subscription. 


<br>




<p align="right">(<a href="#CMC">back to top</a>)</p>

***

### Built With

* ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
* ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
* [![MongoDB][MongoDB]][MongoDB-url]
* [![Flask][Flask]][Flask-url]
* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
### Tools Used

* [![Postman][Postman]][Postman-url]
* [![Docker][Docker]][Docker-url]



<p align="right">(<a href="#CMC">back to top</a>)</p>

***

<!-- GETTING STARTED -->
## Getting Started
<h3> What I tried out before starting: </h3>

Checked out the CoinMarketCap Postman collection which you can directly import into your postman account. 
* https://coinmarketcap.com/alexandria/article/register-for-coinmarketcap-api


If you dont have a collection yet you can use the following code to create/drop a collection in a mongodb database: 

* mongo =  being the URI-generated database in python flask 
    
* create + drop functions come from PyMongo

```sh
    print("Creating coins collection...")
    mongo.db.create_collection("coins")
    print("Dropping coins collection...")
    mongo.db.coins.drop()
```

Understood how to use the MarketCap Api
* [V1 Crypto Listings Latest](https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest) 

* The parameters are defined based on the requirements listed above: 

```sh
params = {
    "sort": "market_cap",
    "sort_dir": "desc",
    "limit": 10
}

```




* [Authentication](https://coinmarketcap.com/api/documentation/v1/#section/Authentication)

```sh
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": KEY
}
```


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/vtwoptwo/coinmarketcap.git
   ```


<p align="right">(<a href="#CMC">back to top</a>)</p>

***


<!-- USAGE EXAMPLES -->





## Usage
Check out the outcome: 
<div align="center">
  <a>
    <img src="backend_api\static\images\home.JPG">
  </a>
</div>

<div align="center">
  <a>
    <img src="backend_api\static\images\coins.JPG">
  </a>
</div>

<div align="center">
  <a>
    <img src="backend_api\static\images\about.JPG">
  </a>
</div>


<div align="center">
  <a>
    <img src="backend_api\static\images\mongodb_coinmarketcap.JPG">
  </a>
</div>


<!-- ROADMAP -->
## Roadmap in Steps
Make sure you have everything downloaded from the [pre-requisites](#prerequisites) before continuing.

### Set-Up

1. Download MongoDB


*  I created an account and downloaded the commmunity edition 
* I created a mongodb:// database to test locally





2. Set up a .venv env in my local folder
```sh
py -m venv .venv
.venv/Scripts/activate
```
3. This is more of an iterative process but, you can install all your requirements at once using the following strucure for your requirements.txt

  ```sh
Flask==2.2.2
psycopg2==2.9.3
python-dotenv==0.21.0
pytest
pytest-cov
pymongo==3.1
requests==2.26.0
click==8.1.3
colorama==0.4.6
Flask==2.2.2
Flask-PyMongo==2.0.1
greenlet==1.1.3.post0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.1
Werkzeug==2.2.2
  ```

```sh
pip install -r ./requirements.txt
```

4. Make a get_data.py file and make sure you are receiving the right data: 

Your response should resemble the following: 


```sh

{'symbol': 'BTC', 'price': 17194.45140525171, 'market_cap': 330651019968.1309, 'market_cap_pct': 0.463055925215652, 'last_updated': '2022-12-10T18:22:00.000Z'}
{'symbol': 'ETH', 'price': 1271.2435795759775, 'market_cap': 155566991737.26785, 'market_cap_pct': 0.21786177250824543, 'last_updated': '2022-12-10T18:22:00.000Z'}
{'symbol': 'USDT', 'price': 1.0000662164008933, 'market_cap': 65712545071.71287, 'market_cap_pct': 0.09202628003201087, 'last_updated': '2022-12-10T18:22:00.000Z'}
{'symbol': 'BNB', 'price': 288.29730677866866, 'market_cap': 46118502210.35589, 'market_cap_pct': 0.0645860572655567, 'last_updated': '2022-12-10T18:22:00.000Z'}
{'symbol': 'USDC', 'price': 1.0000539139368854, 'market_cap': 42747086994.57803, 'market_cap_pct': 0.05986460262683032, 'last_updated': '2022-12-10T18:22:00.000Z'}
{'symbol': 'BUSD', 'price': 1.0001620378753022, 'market_cap': 22103565063.960773, 'market_cap_pct': 0.030954650532283898, 'last_updated': '2022-12-10T18:22:00.000Z'}       
{'symbol': 'XRP', 'price': 0.38808885639422136, 'market_cap': 19557917047.384052, 'market_cap_pct': 0.027389630839609318, 'last_updated': '2022-12-10T18:22:00.000Z'}       
{'symbol': 'DOGE', 'price': 0.09697167580648122, 'market_cap': 12865306344.687412, 'market_cap_pct': 0.018017051129000643, 'last_updated': '2022-12-10T18:22:00.000Z'}      
{'symbol': 'ADA', 'price': 0.312804943710321, 'market_cap': 10781789464.849493, 'market_cap_pct': 0.015099216982930975, 'last_updated': '2022-12-10T18:22:00.000Z'}
{'symbol': 'MATIC', 'price': 0.9111297513428726, 'market_cap': 7958096509.406064, 'market_cap_pct': 0.01114481286788001, 'last_updated': '2022-12-10T18:22:00.000Z'}  

```

5. Make sure you are pushing the data into your collection

```sh
def call(): 
    response = requests.get(BASE+ENDPOINT, params=params, headers=headers)
    print(response)
    data = response.json()

    total_market_cap = 0

    for coin in data["data"]:
        total_market_cap += coin["quote"]["USD"]["market_cap"]

    for coin in data["data"]:
        symbol = coin["symbol"]
        price = coin["quote"]["USD"]["price"]
        market_cap = coin["quote"]["USD"]["market_cap"]
        market_cap_pct = market_cap / total_market_cap
        last_updated = coin["last_updated"]


        document = {
            "symbol": symbol,
            "price": price,
            "market_cap": market_cap,
            "market_cap_pct": market_cap_pct,
            "last_updated": last_updated
        }

        
        collection.insert_one(document)

```
alternatively you could also use the following: * 
```sh
collection.insert_many(documents)
```


6. Note that Imade two files: one an executable and one a function to push to the mongodb collection. 

* This way I can either choose to run the process with a cron job every minute by running the get_data.py file,  or create a website with a frontend which runs the api calls at the press of a button. 

* Limitations: The api call should only  be called every 60 seconds, as that is when the data renews at the endpoint.






### Frontend
I find vue.js much easier to implement and would do so if this were a larger project, but the following frontend also turned out alright. 


 





### Automation

How would you set up a system that runs this process once every minute?

I would use a Linux/Unix CLI. This way I can run the python script automatically at whichever interval I want. Check out more info here: [Medium - Scheduling python scripts](https://towardsdatascience.com/how-to-schedule-python-scripts-with-cron-the-only-guide-youll-ever-need-deea2df63b4e)

Steps: 

1. Configure a cron file

```sh 
crontab -e
```

```sh 
***** /path/2/py /path/2/get_data.py
```

If I had to create dynamic dashboard I would probably use a different framework. Something fast... something like: 

![D3JS](https://img.shields.io/badge/D3JS-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

### Configuration Management for Production
1. Change the environment variables (I had a .env file locally), but you can use GITHUB secrets, or depending on your cloud service provider (e.g. Azure) you can globally configure environment variables for the web app. 

The following files were used to prepare the document for production: 

* create a .env
* config.py
* __init__.py


### Creating Different Pipelines in Github

1. Go to GitHub Actions

2. Create a Build and a separate deploy workflow (You can do for both dev, prod, or test mode)

3. Use .yaml files to configure the workflow


### Next Steps 

See the [open issues](https://github.com/vtwoptwo/coinmarketcap/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#CMC">back to top</a>)</p>

***

<!-- CONTRIBUTING -->
## Contributing

The idea is to create a nice and simple repo for CPP Basic Rules, information, definitions, best practices etc. Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.



If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project and create a feature: 
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#CMC">back to top</a>)</p>

***

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#CMC">back to top</a>)</p>

***
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/vtwoptwo/coinmarketcap.svg?style=for-the-badge
[contributors-url]: https://github.com/vtwoptwo/coinmarketcap/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/vtwoptwo/coinmarketcap.svg?style=for-the-badge
[forks-url]: https://github.com/vtwoptwo/coinmarketcap/network/members
[stars-shield]: https://img.shields.io/github/stars/vtwoptwo/coinmarketcap.svg?style=for-the-badge
[stars-url]: https://github.com/vtwoptwo/coinmarketcap/stargazers
[issues-shield]: https://img.shields.io/github/issues/vtwoptwo/coinmarketcap.svg?style=for-the-badge
[issues-url]: https://github.com/vtwoptwo/coinmarketcap/issues
[license-shield]: https://img.shields.io/github/license/vtwoptwo/coinmarketcap.svg?style=for-the-badge
[license-url]: https://github.com/vtwoptwo/coinmarketcap/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/vera-prohaska-31734b1b5/
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[CPP-url]: https://cplusplus.com/
[C++]: https://img.shields.io/badge/C++-blue
[Postgres]: https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white
[Postgres-url]: https://www.postgresql.org/
[Flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[Postman]: https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white
[Postman-url]: https://www.postman.com/
[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[MongoDB]: https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white
[MongoDB-url]: https://www.mongodb.com/home
