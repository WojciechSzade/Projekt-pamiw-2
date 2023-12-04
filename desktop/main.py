import webview


def change_title(window):
    print(window.get_elements('title')[0]['text'])


window = webview.create_window(title="Loading", url='http://127.0.0.1:8000/', text_select=True, zoomable=True, min_size=(400, 200))
webview.start(change_title, window)
