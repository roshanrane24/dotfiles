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
