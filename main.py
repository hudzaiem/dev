import pandas as pd
import numpy as np
import json
import requests
from tqdm import tqdm
from datetime import datetime
from utilities import util
import os
from google.cloud import bigquery
import warnings
warnings.filterwarnings('ignore')



def main():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
    client = bigquery.Client()
    df_today = pd.DataFrame(columns = ['value','name','commodity','date'])
    for i in tqdm(range(1,22)):
        today = datetime.today().strftime('%d-%m-%Y')
        url = f'https://hargapangan.id/index.php?option=com_gtpihps&f0b32ecdcc1c7fa536a434896a13226f=1&commodity_id={i}&price_type_id=1&data_type=price&date={today}&task=json.getData&_=1678178646077'
        response = requests.get(url).text
        response = json.loads(response)
        df_json = pd.DataFrame(response['tableData']).drop(columns = ['display','id'])
        df_json['commodity'] = response['commodity']
        df_json['date'] = today
        df_today = pd.concat([df_today,df_json])
    df_today = util.preproccess(df_today)
    client.insert_rows_json('price-forecasting-try.scraping_hargapangan.daily_scraping', df_today)

if __name__ == '__main__':
    main()