import requests
import pandas as pd


def download_from_url(url):
    r = requests.get(url, allow_redirects=True)
    open(url.split('/')[-1], 'wb').write(r.content)
    return url.split('/')[-1]


def join_2_csv(csv1, csv2, col1, col2, select_cols=[], rename_cols=[]):
    csv1 = download_from_url(csv1)
    csv2 = download_from_url(csv2)
    df1 = pd.read_csv(csv1)
    df2 = pd.read_csv(csv2)
    df = pd.merge(df1, df2, how='inner', left_on=col1, right_on=col2)
    df = df[select_cols]
    df.columns = rename_cols
    df = df[df[rename_cols[1]] > '0.03']
    df = df.sort_values(by=rename_cols[1], ascending=False)
    df.to_csv(csv1, index=False)


def main():
    vol = 'https://www1.nseindia.com/archives/nsccl/volt/CMVOLT_16072020.CSV'
    n100 = 'https://www1.nseindia.com/content/indices/ind_nifty100list.csv'
    select_cols = ['Symbol', 'Current Day Underlying Daily Volatility (E) = Sqrt(0.995*D*D + 0.005*C*C)',
                   'Underlying Annualised Volatility (F) = E*Sqrt(365)']
    rename_cols = ['Symbol', 'Daily Vol', 'Yearly Vol']
    join_2_csv(vol, n100, select_cols[0], rename_cols[0], select_cols, rename_cols)


if __name__ == '__main__':
    main()