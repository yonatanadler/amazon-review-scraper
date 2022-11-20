import requests
from bs4 import BeautifulSoup
import pandas as pd

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/90.0.4430.212 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

# scrape the data

def getdata(url):
    r = requests.get(url, headers=HEADERS)
    return r.text

# display html code


def html_code(url):
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')
    return (soup)

# find the Html tag for
# and convert into string
# def cus_data(soup):

#     data_str = ""
#     cus_list = []

#     for item in soup.find_all("span", class_="a-profile-name"):
#         data_str = data_str + item.get_text()
#         cus_list.append(data_str)
#         data_str = ""
#     return cus_list

# find customer review by HTML tag


def cus_rev(soup):
    data_str = ""
    for item in soup.find_all("span", class_="a-size-base review-text review-text-content"):
        data_str = data_str + item.get_text()

    result = data_str.split("\n")
    return (result)

# download rev_result to csv file


def download_to_csv(result):
    df = pd.DataFrame({'Review': result})
    df.to_csv('product_reviews.csv', index=False, encoding='utf-8')


def main():

    star = ['one_star', 'two_star', 'three_star', 'four_star', 'five_star']
    page_number = [n for n in range(1, 10)]
    rev_result = []
    # url of the website
    # loop over all star list and page number and get the data
    for i in star:
        for j in page_number:
            url = f"https://www.amazon.com/-/he/3DTriSport-Realalt-%D7%90%D7%9C%D7%A7%D7%98%D7%A8%D7%95%D7%A0%D7%99-%D7%91%D7%9E%D7%99%D7%99%D7%9C%D7%99%D7%9D-%D7%A7%D7%99%D7%9C%D7%95%D7%9E%D7%98%D7%A8%D7%99%D7%9D/product-reviews/B018OQQO74/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews&filterByStar={i}&pageNumber={j}"

            soup = html_code(url)
            # cus_list = cus_data(soup)
            rev_data = cus_rev(soup)
            for i in rev_data:
                if i == "":
                    pass
                else:
                    rev_result.append(i)
                    print("work!")

    download_to_csv(rev_result)


if __name__ == "__main__":
    main()
