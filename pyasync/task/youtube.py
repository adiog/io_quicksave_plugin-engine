# This file is a part of quicksave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import subprocess

from util.regex import retrieve_from_string_by_regex


def youtube(internalCreateRequest, storageProvider):
    meta = internalCreateRequest.createRequest.meta
    item_dir = storageProvider.getMetaPath(meta.meta_hash)
    video_file = item_dir + '/%(title)s'
    youtube_link = item_dir + '/youtube'
    youtube_dl_output = subprocess.check_output('youtube-dl --output \'%s\' %s' % (video_file, meta.source_url), shell=True).decode()
    output_file = retrieve_from_string_by_regex(youtube_dl_output, r'Merging formats into "(.*)"')
    subprocess.check_output(['ln', '-s', output_file, youtube_link])
    print(output_file)
    return []