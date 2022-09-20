#!/usr/bin/env python3
import os

import fabric


def disk_free(c):
    uname = c.run("uname -s", hide=True)
    if "Linux" in uname.stdout:
        command = "df -h / | tail -n1 | awk '{print $5}'"
        print(command)
        # return c.run(command, hide=True).stdout.strip()

    #                        err = "No idea how to get disk space on {}!".format(uname)
    # raise Exit(err)
