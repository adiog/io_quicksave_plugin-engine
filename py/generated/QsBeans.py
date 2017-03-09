# This file is an AUTOGENERATED part of beans project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import pybeans


@pybeans.register_bean_spec('Tag', '''
{
  "tag_id": "Optional(Int)",
  "user_id": "Optional(Int)",
  "item_id": "Optional(Int)",
  "name": "Optional(String)",
  "value": "Optional(String)"
}

''')
class TagBean(pybeans.Bean):
    pass


@pybeans.register_bean_spec('Item', '''
{
  "item_id": "Optional(Int)",
  "user_id": "Optional(Int)",
  "item_type": "Optional(String)",
  "title": "Optional(String)",
  "url": "Optional(String)",
  "freetext": "Optional(String)",
  "author": "Optional(String)",
  "source_title": "Optional(String)",
  "source_url": "Optional(String)",
  "timestamp": "Optional(String)"
}

''')
class ItemBean(pybeans.Bean):
    pass


@pybeans.register_bean_spec('RichItem', '''
{
  "item": "Item",
  "tags": "List(Tag)"
}

''')
class RichItemBean(pybeans.Bean):
    pass

