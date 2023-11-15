# -*- coding: utf-8 -*-
"""
Module to report the CPU governor state in py3status bar
"""

class Py3status:
    cache_timeout = 6
    # format = "💻: {status}"
    format = "{status}"

    def _get_cpu_status(self):
        try:
            status = self.py3.command_output(
                ["cat",
                    "/sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"]
            )
            if status.strip() == "performance":
                status = "⚡performance"
            elif status.strip() == "powersave":
                status = "🔋powersave"
            return {"status": status.strip()}

        except self.py3.CommandError as ce:
            return len(ce.output.splitlines())

    def cpu_governor(self):

        status = self._get_cpu_status()
        full_text = self.py3.safe_format(self.format, status)

        return {
            "full_text": full_text,
            "cached_until": self.py3.time_in(self.cache_timeout),
        }


if __name__ == "__main__":
    from py3status.module_test import module_test
    module_test(Py3status)

