from . import request_product

def get_news_and_media(duns, auth_token):
    return request_product(auth_token, duns, "NEWS_MDA", "3.0")

