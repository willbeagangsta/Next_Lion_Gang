def extract_info(egg_list):
    result = []
    
    for egg in egg_list:
        title = egg.find("div", {"class":"basicList_title__3P9Q7"}).find("a").string
        price = egg.find("div", {"class":"basicList_price_area__1UXXR"}).find("span",{"class":"price_num__2WUXn"}).text
        details_list = egg.find_all("a", {"class":"basicList_detail__27Krk"})

        details = []

        for i in details_list:
            details.append(i.text)

        result.append({
            'title': title,
            'price': price,
            'details': details
        })
    return result