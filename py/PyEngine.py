from generated.QsBeans import ItemBean, TagBean, RichItemBean
from pybeans import to_string

def process(itemBean):
    return RichItemBean(item=itemBean, tags=[TagBean(value='#plugin-engine')])


