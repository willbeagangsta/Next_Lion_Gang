def extract_info(webtoon_list):
    result = []

    for webtoon in webtoon_list:

        title = webtoon.find("dt").find("a").text
        author = webtoon.find("dd", {"class": "desc"}).find("a").text
        rating = webtoon.find("strong").text

        webtoon_info = {
            'title': title,
            'author': author,
            'rating': rating,
        }
        result.append(webtoon_info)

    return result
