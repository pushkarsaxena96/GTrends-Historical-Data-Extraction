# GTrends-Historical-Data-Extraction

Extraction of the Keyword based Google Trends Data using the Pytrends library.

Pytrends is an unofficial Google Trends API that provides different methods to download reports of trending results from google trends. The Python package can be used for automation of different processes such as quickly fetching data that can be used for more analyses later on. 

## Installation

    pip install pytrends

## Idea

As  a Data Engineer, the use case requires extraction of the Google Trends data for different keywords for a specific time span and exporting the same to CSV files.

This CSV can be further used for data analytics and visualization by the different reporting tools.

The Script took 2 hours for completion.

## Methodology

The task was completed in following steps : 

* Initializing the trendreq.
* Function to extract data from Date i.e. Day, Month, Year, Hour, Minute.
* Function to fetch the Historical Hourly Data using Pytrends.
* Function to resample the historical data in Daily, Monthly, Weekly formats with parameterized aggregation functions.
* Export to CSV with a dynamic filename for avoiding any sort of redundancy.

## Approaches

### Straight Program without using classes for dry-run

For Baseline logic, a progressive code was written by hard coding the parameters to check the execution.

### Introduced Classes and Methods for Making the script scalable

After getting success with the baseline code, we introduced class and methods for ensuring scalability and reusability of the code.

## Future Work
* Introduce Multi-threading for faster operations
* Further, parallelize the code using the logics used for multi-threads, for faster execution
* As per the use-case, introduce success and error logging for debugging and watching over the pipeline.

## Usage
* Clone the repository
* Open the source code and alter the parameters in main()
* Execute.
* For use in the ETL pipeline, You can initialize the class and use the methods for extracted Pandas DataFrame.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
