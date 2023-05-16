import webbrowser

user_term = input("What to search? ")
engine_url = "https://google.com/search?q="
webbrowser.open(engine_url + user_term)