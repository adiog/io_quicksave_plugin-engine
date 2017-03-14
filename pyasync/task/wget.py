# This file is a part of quicksave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import subprocess
from util.provider import Provider


def wget(item):
    with Provider(item) as provider:
        item_dir = provider.path
        sitedump = item_dir + '/sitedump'
        subprocess.check_output(['wget', '-r', '-l', '1', '-k', '-P', sitedump, item.source_url])
        subprocess.check_output(['tar', '-cvf', sitedump + '.tar', sitedump])

