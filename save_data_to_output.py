"""save data to csv, json, and export to sql database
@@@brugs_bunny"""
import quandl
from data_cleanup.input import data_dict
from config.credentials import credentials_dict

from quandl.errors.quandl_error import NotFoundError

file_extension = r"dump//"

def pull_data_from_web():
    for k,v in data_dict['Futures'].items():
        df = quandl.get(v, api_key = credentials_dict['quandl_key'])

futures_urls = {}

for i in futures_dict.values():
    for k,v in i.items():
        futures_urls[k] = v
for k,v in futures_urls.items():
    for n in range(1,12):
        try:
            df = quandl.get(k+str(n), api_key = credentials_dict['quandl_key'])
            futures_urls[k] = df
            df.to_csv()
        except NotFoundError:
            print(f"skipping {k}{str(n)}")
    print(df.head())
