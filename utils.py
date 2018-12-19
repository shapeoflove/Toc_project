import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAALbhptvbZBkBAFDOFp5UIIE4uZBm4O5ZAEJUuZCZBKSkSnIIZAaPEridtUNyHq2AVN96idhYaikX74U3zZCbU2g7BAVGIc1DLv9JYa7074jGTZBZA9IHYQNndHYDWfzdbWZB9qxy6jrNkvVgI9YTZCHccd6Y7zywU6ZAyr12aCvy0RTwZAP7F2h2wRwK"


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
