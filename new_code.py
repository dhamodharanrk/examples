import subprocess

# tar --version
# Example String output Linux
# tar (GNU tar) 1.26
# Copyright (C) 2011 Free Software Foundation, Inc.
# License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.
# This is free software: you are free to change and redistribute it.
# There is NO WARRANTY, to the extent permitted by law.
# Written by John Gilmore and Jay Fenlason.

# Example String output Windows/Mac
# bsdtar 3.5.2 - libarchive 3.5.2 zlib/1.2.5.f-ipp

import re
import subprocess

required_tar_version = 1.34  # latest version


def check_current_tar_version():
    current_version = 0
    bash_result = subprocess.check_output('tar --version', shell=True).decode('utf8').strip()
    if bash_result:
        if "GNU tar" in bash_result:
            current_version = re.findall('GNU.*[0-9]+.[0-9]+', bash_result)[0]
            current_version = re.findall('[0-9]+.[0-9]+', current_version)[0]
        # elif "bsdtar" in bash_result:
        #     current_version = re.findall('bsdtar.*[0-9]+.[0-9]+', bash_result)[0]
        #     current_version = re.findall('[0-9]+.[0-9]+', current_version)[0]
    return float(current_version)


cmd = ''
current_tar_version = check_current_tar_version()
if current_tar_version < required_tar_version:
    subprocess.check_output(cmd, shell=True).decode('utf8').rtrip()
else:
    raise ValueError(f"Required tar version is {required_tar_version} but found {current_tar_version}")
