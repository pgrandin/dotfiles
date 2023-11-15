import subprocess


class Py3status:

    def cpu_scaling(self):
        cmd = "lscpu | grep 'scaling MHz'"
        out = subprocess.check_output(cmd, shell=True)
        # convert to string and strip the newline
        out = out.decode("utf-8").strip()
        # split the string and extract the MHz
        mhz = out.split(":")[1].strip()
        # remove trailing '%'
        mhz = mhz[:-1]
        mhz = int(mhz)

        if mhz < 60:
            color = self.py3.COLOR_GOOD
        else:
            color = self.py3.COLOR_BAD

        return {
            'full_text': f"{mhz}%",
            'color': color,
            'cached_until': self.py3.time_in(5)
        }            

if __name__ == "__main__":
    s = Py3status()
    print(s.cpu_scaling())
