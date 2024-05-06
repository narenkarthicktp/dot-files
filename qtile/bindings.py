from libqtile.config import Click, Drag, Key, Group
from libqtile.lazy import lazy
from libqtile.widget import backlight

SUPER = "mod4"
ALT   = "mod1"
LEFT  = "left"
UP    = "up"
RIGHT = "right"
DOWN  = "down"

TERMINAL = "alacritty"

# KEYBINDINGS

keys = [

    # FOCUS

    Key([SUPER], LEFT, lazy.layout.left(),
        desc="Move focus to left"),
    Key([SUPER], RIGHT, lazy.layout.right(),
        desc="Move focus to right"),
    Key([SUPER], DOWN, lazy.layout.down(),
        desc="Move focus down"),
    Key([SUPER], UP, lazy.layout.up(),
        desc="Move focus up"),
    Key([SUPER], "tab", lazy.layout.next(),
        desc="Move window focus to other window"),

    # MOVE

    Key([SUPER, "shift"], LEFT, lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([SUPER, "shift"], RIGHT, lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([SUPER, "shift"], DOWN, lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([SUPER, "shift"], UP, lazy.layout.shuffle_up(),
        desc="Move window up"),

    # RESIZE
    
    Key([SUPER, "control"], LEFT, lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([SUPER, "control"], RIGHT, lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([SUPER, "control"], DOWN, lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([SUPER, "control"], UP, lazy.layout.grow_up(),
        desc="Grow window up"),
    Key([SUPER], "n", lazy.layout.normalize(),
        desc="Reset all window sizes"), 

    # LAYOUTS
    
    Key([SUPER], "space", lazy.next_layout(),
        desc="Toggle between layouts"),
    Key([SUPER], "t", lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window"),

    # VENDOR KEYS

    Key([], "XF86MonBrightnessUp", lazy.widget['backlight'].change_backlight(backlight.ChangeDirection.UP)),
    Key([], "XF86MonBrightnessDown", lazy.widget['backlight'].change_backlight(backlight.ChangeDirection.DOWN)),

    Key([], "XF86AudioRaiseVolume", lazy.widget["pulsevolume"].increase_vol()),
    Key([], "XF86AudioLowerVolume", lazy.widget["pulsevolume"].decrease_vol()),
    Key([], "XF86AudioMute", lazy.widget["pulsevolume"].mute()),

    Key([], "Print", lazy.spawn("/home/nktp/.config/commons/hacknshoot.sh")),
    Key([ALT], "Print", lazy.spawn("/home/nktp/.config/commons/hacknshoot.sh -s")),

    # MISC
    
    Key([SUPER], "w", lazy.window.kill(),
        desc="Kill focused window"),

    Key([SUPER], "Return", lazy.spawn(TERMINAL),
        desc="Launch terminal"),
    Key([SUPER], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    Key([SUPER, "control"], "r", lazy.reload_config(),
        desc="Reload the config"),

    Key([SUPER, "control"], "q", lazy.shutdown(),
        desc="Shutdown Qtile"),
]

# GROUPS

groups = [Group(i, label='\u2B58') for i in "123456"]

for i in groups:

    keys.extend(
        [
            Key( [SUPER], i.name, lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}"),
            Key( [SUPER, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}"),

            # moves but doesn't switch
            # Key([SUPER, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc=f"move focused window to group {i.name}")),
        ]
    )

# MOUSE

mouse = [
    Drag([SUPER], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([SUPER], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([SUPER], "Button2", lazy.window.bring_to_front()),
]
