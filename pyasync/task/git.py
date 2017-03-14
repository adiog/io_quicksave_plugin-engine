# This file is a part of quicksave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import subprocess
from util.provider import Provider


def git(item):
    with Provider(item) as provider:
        item_dir = provider.path
        target = item_dir + '/git'
        subprocess.check_output(['git', 'clone', item.source_url, target])
        subprocess.check_output(['git', '--git-dir', target+'/.git', 'update-server-info', '--force'])
        subprocess.check_output(['tar', '-cvf', target + '.tar', target])

