import webview

webview.create_window(
    "My Desktop App",
    "pages/MainPage.html",
    width=800,
    height=600
)

webview.start(debug=True)