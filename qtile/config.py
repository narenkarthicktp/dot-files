from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Match, Screen
from libqtile.lazy import lazy

from tomllib import load

from style import bubble
from bindings import keys, groups, mouse, TERMINAL

# TODO:
# - scratchpads / floating layouts

# COLORS

colors = {}
with open("/home/nktp/.config/commons/monokai.toml", 'rb') as f: 
    colors = load(f)["colors"]
  
# LAYOUTS

layout_theme = dict(
    border_focus=colors["normal"]["white"],
    border_normal=colors["bright"]["black"],
    border_width=1,
    margin=1
)

layouts = [
    layout.Columns(**layout_theme),
    layout.Max()
]

# WIDGETS

widget_defaults = dict(
    font="IosevkaSS09 Nerd Font",
    fontsize=14,
    padding=5,
    foreground=colors["primary"]["foreground"]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                *bubble(
                    {widget.Clock: {"format":"%H:%M"}},
                    background=colors["primary"]["background"]
                ),
                *bubble(
                    {
                        widget.GroupBox: {
                            "highlight_method": "text",
                            "this_current_screen_border": colors["normal"]["green"],
                            "urgent_alert_method": "text",
                            "urgent_text": colors["normal"]["red"],
                            "spacing": 1
                        }
                    },
                    background=colors["primary"]["background"]
                ),
                widget.Prompt(max_history=10, ignore_dups_history=True, cursorblink=0),
                widget.WindowName(padding=20),

                widget.Systray(),
                widget.Notify(audiofile="/home/nktp/Downloads/pika.wav"),
                *bubble(
                    {
                        widget.Wlan: {
                            "interface": "wlp0s20f3",
                            "format": "\U0000F1EB {essid} [{percent:2.0%}]",
                            "disconnected_message": '\U000F092E',
                            "mouse_callbacks": {
                                "Button1": lazy.spawn(f"{TERMINAL} --title {TERMINAL}-nmtui -e nmtui")
                            }
                        },
                        widget.Bluetooth: { # Welcome to my mess
                            "default_show_battery": True,
                            "default_text"    : "\U000F00AF {connected_devices}",
                            "adapter_format"  : "{powered} {name} {discovery}",
                            "device_format"   : "{symbol} {name}",
                            "symbol_discovery": ('', ''), # This is just complicating everything
                            "symbol_powered"  : ('\U0000F293', '\U000F00B2'), #  󰂲
                            "symbol_unknown"  : '\U0000F29C', # 
                            "symbol_connected": '\U000F00B1', # 󰂱
                            "symbol_paired"   : '\U0000F294'  # 
                        }
                    },
                    background=colors["primary"]["background"]
                ),
                *bubble(
                    {
                        widget.Backlight: {"fmt": "\U0000F522 {}", "backlight_name": "intel_backlight", "step": 5}, # 
                        widget.PulseVolume: {"fmt": "\U000F057E {}"}, # 󰕾
                        # widget.BatteryIcon: {"theme_path": "~/.config/qtile/battery/", "scale": 1.25},
                        widget.Battery: {
                            "full_char"     : '\U000F0079', # 󰁹
                            "empty_char"    : '\U000F008E', # 󰁺
                            "charge_char"   : '\U000F140B', # 󱐋
                            "discharge_char": '\U000F0080', # 󰂀
                            "format": "{char} {percent:2.0%}",
                            "show_short_text": False,
                            
                            "low_foreground": colors["normal"]["red"],
                            "low_background": colors["primary"]["background"],
                            "low_percentage": 0.2,
                            "notification_timeout": 0,
                            "notify_below": 20
                        }
                    },
                    background=colors["primary"]["background"]
                ),
                *bubble( # ⏻
                    {widget.QuickExit: {"default_text": '\u23FB', "countdown_format": "{}"}},
                    background=colors["normal"]["red"]
                ),
            ],
            32,
            opacity=0.6,
            # background="#00000000",
            # border_color = ["#00000000", "#00000000", "#00000000", "#00000000"],
            border_width=[0, 10, 4, 10]  # [T, R, B, L]
        ),
        wallpaper="~/Pictures/wallpapers/the-range.png",
        wallpaper_mode="fill",

        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(

    border_width=1,
    border_focus=colors["normal"]["white"],
    border_normal=colors["bright"]["black"],
    
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"), # gitk
        Match(wm_class="makebranch"),   # gitk
        Match(wm_class="maketag"),      # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),    # gitk
        Match(title="pinentry"),        # GPG key password entry

        Match(title=f"{TERMINAL}-nmtui")
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

# HOOKS
 
@hook.subscribe.setgroup
def change_group_icon():

    for i in range(6):
        qtile.groups[i].label = '\U00002B58' # ⭘
    qtile.current_group.label = '\U0000EBB4' # 
