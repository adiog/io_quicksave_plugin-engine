from generated.QsBeans import FileBean, DatabaseTaskBean
from rabbit_push import rabbit_push

fileBean = FileBean(filename='', filesize=33, meta_hash='', mimetype='image/png')
databaseTaskBean = DatabaseTaskBean(databaseConnectionString='x', type='insert', beanname='File', beanjson=fileBean.to_string())

rabbit_push('response', databaseTaskBean)

