import webbrowser

sites = {'facebook' : "https://www.facebook.com/",
'instagram' : "https://www.instagram.com/",
'youtube' : "https://www.youtube.com/",
'linkedin' : "https://www.linkedin.com/feed/"
}
def firefox(url):
    webbrowser.open(url)
