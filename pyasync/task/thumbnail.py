# This file is a part of quicksave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

from libs.crop_image import crop_image
from libs.selenium_thumbnail import save_thumbnail
from util.provider import Provider


def thumbnail(item):
    with Provider(item) as provider:
        item_dir = provider.path
        thumbnail_file = item_dir + '/thumbnail.png'
        thumbnail_crop = item_dir + '/thumbnail_crop.png'
        save_thumbnail(url=item.source_url, thumbnail_file=thumbnail_file)
        crop_image(thumbnail_file, thumbnail_crop)
    return []
