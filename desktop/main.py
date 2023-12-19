import webview
import webview.menu as wm


def change_title(window):
    window.set_title(window.get_elements('title')[0]['text'])


def go_back():
    url = window.get_current_url()
    if 'brand' in url:
        window.load_url('http://127.0.0.1:8000/brands_list/')
    else:
        window.load_url('http://127.0.0.1:8000/cars_list/')


def refresh():
    window.load_url(window.get_current_url())


window = webview.create_window(title="Loading", url='http://127.0.0.1:8000/',
                               text_select=True, zoomable=True, min_size=(400, 300), width=600, height=500)


def on_loaded():
    change_title(window)


menu_items = [
    wm.Menu(
        'Menu',
        [
            wm.MenuAction('Go back', go_back),
            wm.MenuAction('Refresh', refresh)
        ]
    )
]

window.events.loaded += on_loaded

webview.start(func=change_title, args=window, menu=menu_items)
