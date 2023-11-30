# **Bloomberg Market Watcher Module**
The **Bloomberg Market Watcher Module** is a Python script that encapsulates functionalities to interact with the Bloomberg API. It provides an easy-to-use class, *`BloombergMarketWatcher`*, which allows users to retrieve market and financial data.

## **Features**
1. **Market Movers:**
	* Get a list of assets that made the most gains in the market.
	* Categorize assets as Active, Laggards, or Leaders.
	* Generate CSV files with detailed information on market movers.
2. **Currency Exchange:**
	* View the exchange rate between two specified currencies.
	* Choose from a list of available currencies.

## **Prerequisites**
* Python 3.6 and above
* Required Python packages: *`requests`*, *`csv`*

## **Installation**
Install the required packages:
* pip install -r requirements.txt
* git clone https://github.com/your-username/bloomberg-market-watcher.git
* Navigate to the project directory

## **Usage**
1. Import the BloombergMarketWatcher class into your Python script:
	from bloomberg_market_watcher import BloombergMarketWatcher
2. Create an instance of the class:
	market = BloombergMarketWatcher()
3. Use the class methods to retrieve market data and exchange rates between currencies:
	market.getMovers1()
	market.getMovers2()
4. Follow the on-screen prompts or customize the class methods as needed

## **Contributing**
If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## **License**
This project is licensed under the ALU License

## **Acknowledgments**
* API DOJO.NET API AND BLOOMBERG API for providing market and financial data

## **Authors**
* OBOLO EMMANUEL OLUWAPELUMI
* RENOIR KAZE
* PURITY KIHU KYLA
* INNOCENTE GIHOZO
