from libqtile.widget import TextBox

def bubble(widgets:dict, background:str, bar_width=32):

    bubbled_widgets = [TextBox('\uE0B6', foreground=background, padding=0, fontsize=bar_width)]

    for widget, args in widgets.items():
        bubbled_widgets.append(widget(**args, background=background))

    bubbled_widgets.append(TextBox('\uE0B4', foreground=background, padding=0, fontsize=bar_width))

    return bubbled_widgets
