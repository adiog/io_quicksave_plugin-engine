from generated.QsBeans import ItemBean, TagBean, RichItemBean
from pybeans import to_string

def process(itemBean):
    tags = [TagBean(name='chrome')]
    if ('wikipedia' in itemBean.source_url):
        tags.append(TagBean(name='wiki'))
    return RichItemBean(item=itemBean, tags=tags)


