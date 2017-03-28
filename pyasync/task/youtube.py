# This file is a part of quicksave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import subprocess

from util.provider import Provider
from util.regex import retrieve_from_string_by_regex


def youtube(item):
    with Provider(item) as provider:
        item_dir = provider.path
        video_file = item_dir + '/%(title)s'
        youtube_link = item_dir + '/youtube'
        youtube_dl_output = subprocess.check_output('youtube-dl --output \'%s\' %s' % (video_file, item.source_url), shell=True).decode()
        output_file = retrieve_from_string_by_regex(youtube_dl_output, r'Merging formats into "(.*)"')
        subprocess.check_output(['ln', '-s', output_file, youtube_link])
        print(output_file)
    return []