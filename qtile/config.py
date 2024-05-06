from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Match, Screen
from libqtile.lazy import lazy

from tomllib import load

from style import bubble
from bindings import keys, groups, mouse

# TODO:
# - scratchpads
# - systray is empty and idk why
# - spacing between widgets would be nice

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
    font="Iosevka SS09",
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
                widget.Prompt(),
                widget.WindowName(padding=20),

                widget.Systray(),
                widget.Notify(),
                *bubble(
                    {
                        widget.Backlight: {"fmt": "\uF522 {}", "backlight_name": "intel_backlight", "step": 5},
                        widget.PulseVolume: {"fmt": "\uF028 {}"}, # 
                        # widget.BatteryIcon: {"theme_path": "~/.config/qtile/battery/", "scale": 1.25},
                        widget.Battery: {
                            "full_char"     : '\uF240', # 
                            "empty_char"    : '\uF244', # 
                            "charge_char"   : '\uF0E7', # 
                            "discharge_char": '\uF242', # 
                            "format": "{char} {percent:2.0%}",
                            "notify_below": 15
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
        wallpaper="~/Downloads/the-range.png",
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
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
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
        qtile.groups[i].label = '\u2B58' # ⭘
    qtile.current_group.label = '\uEBB4' # 
