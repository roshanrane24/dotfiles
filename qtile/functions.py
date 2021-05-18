import subprocess
from libqtile.lazy import lazy


class Display:
    def __init__(self):
        self.xrandr = subprocess.getoutput(["xrandr"])
        self.display = [line.split()[0] for line in self.xrandr.split('\n') if ("connected" in line.split())]
        self.PRIMARY = self.display[0]
        self.OTHER = self.display.copy()
        self.multi_monitor = len(self.display) > 1


        self.OTHER.remove(self.PRIMARY)

    def get_connect_display_count(self):
        return len(self.display)

    def set_extend_all(self):
        cmd = f"xrandr --output {self.PRIMARY} --primary --rotate normal --auto"
        if self.multi_monitor:
            for screen in self.OTHER:
                cmd += f" --left-of {screen} --rotate normal"
        print(f"[INFO]:(extend) running xrandr commad {cmd}")
        subprocess.Popen(cmd.split())

    def set_mirror_all(self):
        cmd = f"xrandr --output {self.PRIMARY} --auto"
        if self.multi_monitor:
            for screen in self.OTHER:
                cmd += f" --output {screen} --same-as {self.PRIMARY}"
        print(f"[INFO]:(mirror) running xrandr commad {cmd}")
        subprocess.Popen(cmd.split())


def mouse_call(action):
    def _wrapper():
        lazy.spawn(action)
    return _wrapper

class Brightness:
    BACKLIGHT = "/sys/class/backlight/intel_backlight"
    STEP = 5

    def __init__(self, backlight_path="/sys/class/backlight", step=5):
        set_backlight_path(backlight_path)
        set_steps(step)

    @classmethod
    def set_backlight_path(cls, path):
        cls.BACKLIGHT = path

    @classmethod
    def set_steps(cls, step):
        cls.STEP = path

    @classmethod
    def get_max_brightness():
        with open(f'{BACKLIGHT}/max_brightness', 'r') as mb:
            return mb.readline()

    @classmethod
    def get_current_brightness():
        with open(f'{BACKLIGHT}/brightness', 'r') as b:
            return b.readline()

    @classmethod
    def set_brightness(value):
        with open(f'{BACKLIGHT}/brightness', 'w') as b:
            b.write(value)

    @classmethod
    def increase_brightness():
        pass
