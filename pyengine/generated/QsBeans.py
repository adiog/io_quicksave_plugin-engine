# This file is an AUTOGENERATED part of beans project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import pybeans


@pybeans.register_bean_spec('Tag', '''
{
  "tag_hash": "Optional(String)",
  "user_hash": "Optional(String)",
  "meta_hash": "Optional(String)",
  "name": "Optional(String)",
  "value": "Optional(String)"
}

''')
class TagBean(pybeans.Bean):
    pass


@pybeans.register_bean_spec('Meta', '''
{
  "meta_hash": "Optional(String)",
  "user_hash": "Optional(String)",
  "meta_type": "Optional(String)",
  "icon": "Optional(String)",
  "name": "Optional(String)",
  "text": "Optional(String)",
  "author": "Optional(String)",
  "source_title": "Optional(String)",
  "source_url": "Optional(String)",
  "created_at": "Optional(String)",
  "modified_at": "Optional(String)"
}

''')
class MetaBean(pybeans.Bean):
    pass


@pybeans.register_bean_spec('File', '''
{
  "file_hash": "Optional(String)",
  "meta_hash": "String",
  "filename": "String",
  "filesize": "Int",
  "mimetype": "String"
}
''')
class FileBean(pybeans.Bean):
    pass


@pybeans.register_bean_spec('Action', '''
{
  "action_hash": "Optional(String)",
  "meta_hash": "String",
  "name": "String",
  "kwargs": "SerializedDict"
}
''')
class ActionBean(pybeans.Bean):
    pass


@pybeans.register_bean_spec('Item', '''
{
  "meta": "Meta",
  "tags": "List(Tag)",
  "files": "List(File)",
  "actions": "List(Action)"
}

''')
class ItemBean(pybeans.Bean):
    pass


@pybeans.register_bean_spec('Key', '''
{
  "key_hash": "Optional(String)",
  "user_hash": "String",
  "name": "String",
  "value": "String"
}
''')
class KeyBean(pybeans.Bean):
    pass


@pybeans.register_bean_spec('Message', '''
{
  "message": "String"
}

''')
class MessageBean(pybeans.Bean):
    pass


@pybeans.register_bean_spec('CreateRequest', '''
{
  "meta": "Meta",
  "attachment": "Optional(Base64)",
  "attachment_name": "Optional(String)",
  "attachment_mime_types": "Optional(List(String))",
  "attachment_provider_id": "Optional(Int)",
  "hints": "Optional(String)"
}

''')
class CreateRequestBean(pybeans.Bean):
    pass


@pybeans.register_bean_spec('InternalCreateRequest', '''
{
  "createRequest": "CreateRequest",
  "keys": "List(Key)",
  "databaseConnectionString": "String",
  "storageConnectionString": "String"
}

''')
class InternalCreateRequestBean(pybeans.Bean):
    pass


@pybeans.register_bean_spec('BackgroundTask', '''
{
  "name": "String",
  "internalCreateRequest": "InternalCreateRequest",
  "kwargs": "SerializedDict"
}
''')
class BackgroundTaskBean(pybeans.Bean):
    pass


@pybeans.register_bean_spec('DatabaseTask', '''
{
  "databaseConnectionString": "String",
  "type": "String",
  "beanname": "String",
  "beanjson": "SerializedDict"
}

''')
class DatabaseTaskBean(pybeans.Bean):
    pass

