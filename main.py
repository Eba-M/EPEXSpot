# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    from bs4 import BeautifulSoup
    import requests

    main_url = "http://www.epexspot.com/de/marktdaten/dayaheadauktion"
#    main_url = "https: // www.epexspot.com / en / market - data?data_mode = table & modality = Auction & sub_modality = DayAhead & market_area = DE - LU & product = 60 & delivery_date = 2020 - 11 - 01 & trading_date = 2020 - 10 - 31"
#    main_url = "https: // www.epexspot.com / en / market - data?market_area = DE - LU & trading_date = 2020 - 10 - 31 & delivery_date = 2020 - 11 - 01 & underlying_year = & modality = Auction & sub_modality = DayAhead & product = 60 & data_mode = table & period ="
#    main_url = "https: // www.epexspot.com / en / market - data?market_area = DE - LU & trading_date = 2020 - 10 - 31 & delivery_date = 2020 - 11 - 01 & underlying_year = & modality = Auction & sub_modality = DayAhead & product = 60 & data_mode = table & period ="
#    req = requests.get(main_url)
#    main_url = "https://www.epexspot.com/en/market-data?market_area=AT&trading_date=2020-10-31&delivery_date=2020-11-01&underlying_year=&modality=Auction"
    main_url = "https://www.epexspot.com/en/market-data?market_area=DE-LU&trading_date=2020-11-15&delivery_date=2020-11-16&modality=Auction&sub_modality=DayAhead&product=60&data_mode=table"
    req = requests.get(main_url)
    soup = BeautifulSoup(req.text, "html.parser")

    # Finding the main title tag.
    title = soup.find("table", class_="table-01 table-length-1")
    line = title.contents
    print(len(line))

    td = title.find_all("tr", class_="child")
# für jedes Element
    y = 0;
    for x in td:
        print(y,end=' ');print(x.contents[7].string)
        y=y+1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
