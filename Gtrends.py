#Installs
#!pip install pytrends 

#Imports
import pandas as pd
import pytrends
import re
import datetime
from datetime import datetime
from pytrends.request import TrendReq

class GoogleTrendExtraction:
    pytrends = TrendReq(hl='en-US') 
    kw_list = ["bitcoin"] 
    
    def ExtractDate(self, date):
        """
            Arguments:
            date -- input str date in dd/MM/yyyy HH:MM format i.e. 01/02/2021 00:15
            
            Returns:
            date -- extracted day from the date
            month -- extracted month from the date
            year -- extracted year from the date
            hour -- extracted hour from the date
            minute -- extracted minutes from the date
        """ 

        try:
            date_parse = datetime.strptime(date, '%d/%m/%Y %H:%M')
            day = int(date_parse.strftime("%d"))
            month = int(date_parse.strftime("%m"))
            year = int(date_parse.strftime("%Y"))
            hour = int(date_parse.strftime("%H"))
            minute = int(date_parse.strftime("%M"))
            return day, month, year, hour, minute
            
            
        except ValueError as e:
            text = "Date Parse Error"   
            # Introduce Logging
            return 0,0,0,0,0


    def GetHistorical_Interest(self, FromDate, ToDate, sleep=60):
        """
            Arguments:
            FromDate -- input str from date in dd/MM/yyyy HH:MM format i.e. 01/02/2021 00:15
            ToDate -- input str from date in dd/MM/yyyy HH:MM format i.e. 01/02/2021 00:15
            Sleep -- Timeout
            
            Returns:
            Pandas DataFrame -- Extracted Historical Hourly Data
        """ 
        try:
            start_date, start_month, start_year, start_hour, start_minute = self.ExtractDate(FromDate)
            print(start_date, start_month, start_year, start_hour, start_minute)
            end_date, end_month, end_year, end_hour, end_minute = self.ExtractDate(ToDate)
            print(end_date, end_month, end_year, end_hour, end_minute)
            self.pytrends.build_payload(self.kw_list, cat=0, timeframe='today 12-m') 
            return self.pytrends.get_historical_interest(self.kw_list, year_start=start_year, month_start=start_month, day_start=start_date, hour_start=start_hour, year_end=end_year, month_end=end_month, day_end=end_date, hour_end=end_hour, cat=0, sleep=sleep)
            

        except ValueError as e:
            text = "Historical Data Error"   
            return pd.DataFrame()

    def resample_df(self, df, frequency, compute_list):
        """
            Arguments:
            df -- Pandas DataFrame for Resampling
            frequency -- Frequency on which the resampling has to be done i.e. m-monthly, w-weekly, d-daily
            compute_list -- List of aggregations e.g. ["sum","max","min","mean"]
            
            Returns:
            Pandas DataFrame -- Resampled Pandas DataFrame
        """ 
        try:
            new_df = df.resample(frequency).agg(compute_list)
            print("Resample Shape-" + str(new_df.shape))
            return new_df
            
        except ValueError as e:
            text = "ResampleError"  
            print("Resample Shape-(~,~)") 
            return pd.DataFrame()                                 
       
    def write_to_csv(self, frequency, df):
        """
            Arguments:
            frequency -- Frequency on which the resampling has to be done i.e. m-monthly, w-weekly, d-daily for name of the file
            Df -- Pandas DataFrame 
            
            Operations:
            Writes DF to CSV
        """         
        filename = "Trends_" + re.sub('[^A-Za-z0-9]+', '', str(datetime.now())) + "_" + frequency + ".csv"
        print(filename)
        df.to_csv(filename, sep=',', encoding='utf-8')
    

if __name__ == '__main__':
    t = GoogleTrendExtraction()
    df = t.GetHistorical_Interest("01/01/2021 00:00", "10/01/2021 15:00", 60)
    #print(df.head())
    df_d = t.resample_df(df, "d", ["sum","max","min", "mean"])
    df_w = t.resample_df(df, "w", ["sum","max","min", "mean"])
    df_m = t.resample_df(df, "m", ["sum","max","min", "mean"])
    # print(df_d.head())
    # print(df_w.head())
    # print(df_m.head())
    t.write_to_csv("h", df)
    t.write_to_csv("d", df_d)
    t.write_to_csv("w", df_w)
    t.write_to_csv("m", df_m)

