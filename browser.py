import webbrowser

webbrowser.open("naver.com")
webbrowser.open_new_tab("google.com")

url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="
my_keywords = ["Shinee", "Day6" , "Daybreak"]
for my_keyword in my_keywords:
    webbrowser.open(url + my_keyword)

