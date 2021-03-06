# This file is an AUTOGENERATED part of quicksave project.
# Copyright (c) 2017 Aleksander Gajewski <adiog@quicksave.io>.

import os


QUICKSAVE = os.environ.get('QUICKSAVE', '/io.quicksave.bootstrap')
QUICKSAVE_PREFIX = os.environ.get('QUICKSAVE_PREFIX', '/')
IO_QUICKSAVE = os.environ.get('IO_QUICKSAVE', 'quicksave.io')
IO_QUICKSAVE_GIT = os.environ.get('IO_QUICKSAVE_GIT', 'http://gitlab.brainfuck.pl/adiog')
IO_QUICKSAVE_CERT_DIR = os.environ.get('IO_QUICKSAVE_CERT_DIR', '/io.quicksave.bootstrap/cert')
IO_QUICKSAVE_CLIENT_DIR = os.environ.get('IO_QUICKSAVE_CLIENT_DIR', '/io.quicksave.bootstrap/client')
IO_QUICKSAVE_API = os.environ.get('IO_QUICKSAVE_API', 'api.quicksave.io')
HTTPS_API_QUICKSAVE_IO = os.environ.get('HTTPS_API_QUICKSAVE_IO', 'https://api.quicksave.io')
IO_QUICKSAVE_LOCUST = os.environ.get('IO_QUICKSAVE_LOCUST', 'locust.quicksave.io')
IO_QUICKSAVE_LOCUST_OAUTH = os.environ.get('IO_QUICKSAVE_LOCUST_OAUTH', 'oauth.locust.quicksave.io')
IO_QUICKSAVE_LOCUST_API = os.environ.get('IO_QUICKSAVE_LOCUST_API', 'api.locust.quicksave.io')
IO_QUICKSAVE_LOCUST_CDN = os.environ.get('IO_QUICKSAVE_LOCUST_CDN', 'cdn.locust.quicksave.io')
IO_QUICKSAVE_OAUTH = os.environ.get('IO_QUICKSAVE_OAUTH', 'oauth.quicksave.io')
IO_QUICKSAVE_BOOT = os.environ.get('IO_QUICKSAVE_BOOT', 'boot.quicksave.io')
IO_QUICKSAVE_MQ = os.environ.get('IO_QUICKSAVE_MQ', 'mq.quicksave.io')
IO_QUICKSAVE_CDN = os.environ.get('IO_QUICKSAVE_CDN', 'cdn.quicksave.io')
IO_QUICKSAVE_LOG = os.environ.get('IO_QUICKSAVE_LOG', 'log.quicksave.io')
IO_QUICKSAVE_WWW = os.environ.get('IO_QUICKSAVE_WWW', 'www.quicksave.io')
HTTPS_OAUTH_QUICKSAVE_IO = os.environ.get('HTTPS_OAUTH_QUICKSAVE_IO', 'https://oauth.quicksave.io')
HTTPS_CDN_QUICKSAVE_IO = os.environ.get('HTTPS_CDN_QUICKSAVE_IO', 'https://cdn.quicksave.io')
IO_QUICKSAVE_API_DIR = os.environ.get('IO_QUICKSAVE_API_DIR', '/io.quicksave.api')
IO_QUICKSAVE_CDN_DIR = os.environ.get('IO_QUICKSAVE_CDN_DIR', '/io.quicksave.cdn')
IO_QUICKSAVE_MEM_DIR = os.environ.get('IO_QUICKSAVE_MEM_DIR', '/io.quicksave.bootstrap/memadmin')
IO_QUICKSAVE_SWAGGER_DIR = os.environ.get('IO_QUICKSAVE_SWAGGER_DIR', '/io.quicksave.bootstrap/swagger-editor')
IO_QUICKSAVE_LOG_DIR = os.environ.get('IO_QUICKSAVE_LOG_DIR', '/io.quicksave.log')
IO_QUICKSAVE_WWW_DIR = os.environ.get('IO_QUICKSAVE_WWW_DIR', '/io.quicksave.www')
IO_QUICKSAVE_BOOT_DIR = os.environ.get('IO_QUICKSAVE_BOOT_DIR', '/io.quicksave.bootstrap/boot')
IO_QUICKSAVE_CPPAPI_DIR = os.environ.get('IO_QUICKSAVE_CPPAPI_DIR', '/io.quicksave.cppapi')
IO_QUICKSAVE_LOCUST_HOST = os.environ.get('IO_QUICKSAVE_LOCUST_HOST', 'localhost')
IO_QUICKSAVE_API_HOST = os.environ.get('IO_QUICKSAVE_API_HOST', 'localhost')
IO_QUICKSAVE_CDN_HOST = os.environ.get('IO_QUICKSAVE_CDN_HOST', 'localhost')
IO_QUICKSAVE_OAUTH_HOST = os.environ.get('IO_QUICKSAVE_OAUTH_HOST', 'localhost')
IO_QUICKSAVE_SWAGGER = os.environ.get('IO_QUICKSAVE_SWAGGER', 'swagger.quicksave.io')
IO_QUICKSAVE_SWAGGER_HOST = os.environ.get('IO_QUICKSAVE_SWAGGER_HOST', 'localhost')
IO_QUICKSAVE_MQ_HOST = os.environ.get('IO_QUICKSAVE_MQ_HOST', 'localhost')
IO_QUICKSAVE_MEMCACHED_HOST = os.environ.get('IO_QUICKSAVE_MEMCACHED_HOST', '127.0.0.1')
IO_QUICKSAVE_MEMCACHED_PORT = os.environ.get('IO_QUICKSAVE_MEMCACHED_PORT', '11211')
IO_QUICKSAVE_MEMCACHED_CONNECTION_STRING = os.environ.get('IO_QUICKSAVE_MEMCACHED_CONNECTION_STRING', '--SERVER=127.0.0.1:11211')
IO_QUICKSAVE_LOG_HOST = os.environ.get('IO_QUICKSAVE_LOG_HOST', 'localhost')
IO_QUICKSAVE_PLUGIN_DIR = os.environ.get('IO_QUICKSAVE_PLUGIN_DIR', '/io.quicksave.bootstrap/plugin-engine')
IO_QUICKSAVE_LIBBEANS_DIR = os.environ.get('IO_QUICKSAVE_LIBBEANS_DIR', '/io.quicksave.bootstrap/libbeans')
IO_QUICKSAVE_QSQL_DIR = os.environ.get('IO_QUICKSAVE_QSQL_DIR', '/io.quicksave.bootstrap/qsql')
IO_QUICKSAVE_FUSE_DIR = os.environ.get('IO_QUICKSAVE_FUSE_DIR', '/io.quicksave.bootstrap/fuse')
IO_QUICKSAVE_BEANS_DIR = os.environ.get('IO_QUICKSAVE_BEANS_DIR', '/io.quicksave.bootstrap/beans')
IO_QUICKSAVE_DB_DIR = os.environ.get('IO_QUICKSAVE_DB_DIR', '/io.quicksave.db')
IO_QUICKSAVE_DB_UNITTEST = os.environ.get('IO_QUICKSAVE_DB_UNITTEST', '/io.quicksave.db/unittest.sqlite3')
IO_QUICKSAVE_UNITTEST_DATABASE_CONNECTION_STRING = os.environ.get('IO_QUICKSAVE_UNITTEST_DATABASE_CONNECTION_STRING', 'sqlite:///io.quicksave.db/unittest.sqlite3')
MASTER_HOST = os.environ.get('MASTER_HOST', 'master.quicksave.io')
SLAVE_HOST = os.environ.get('SLAVE_HOST', 'slave.quicksave.io')
IO_QUICKSAVE_MASTER_DATABASE_CONNECTION_STRING = os.environ.get('IO_QUICKSAVE_MASTER_DATABASE_CONNECTION_STRING', 'postgres://host=master.quicksave.io port=5432 user=postgres')
IO_QUICKSAVE_SLAVE_DATABASE_CONNECTION_STRING = os.environ.get('IO_QUICKSAVE_SLAVE_DATABASE_CONNECTION_STRING', 'postgres://host=slave.quicksave.io port=5433 user=postgres')
IO_QUICKSAVE_LOCUST_DATABASE = os.environ.get('IO_QUICKSAVE_LOCUST_DATABASE', '/io.quicksave.db/locust.sqlite3')
IO_QUICKSAVE_LOCUST_DATABASE_CONNECTION_STRING = os.environ.get('IO_QUICKSAVE_LOCUST_DATABASE_CONNECTION_STRING', 'sqlite:///io.quicksave.db/locust.sqlite3')
IO_QUICKSAVE_PYTHONPATH = os.environ.get('IO_QUICKSAVE_PYTHONPATH', '/io.quicksave.bootstrap/libbeans:/io.quicksave.bootstrap/libbeans/pybeans/:/io.quicksave.bootstrap/plugin-engine:/io.quicksave.bootstrap/plugin-engine/pyengine:/io.quicksave.bootstrap/plugin-engine/pyasync')
IO_QUICKSAVE_LOG_PYTHON = os.environ.get('IO_QUICKSAVE_LOG_PYTHON', '/io.quicksave.log/python.log')
IO_QUICKSAVE_LOG_SERVER = os.environ.get('IO_QUICKSAVE_LOG_SERVER', '/io.quicksave.log/server.log')
STORAGE_DEFAULT_HOST = os.environ.get('STORAGE_DEFAULT_HOST', 'localhost')
STORAGE_DEFAULT_PORT = os.environ.get('STORAGE_DEFAULT_PORT', '2222')
STORAGE_DEFAULT_KEY = os.environ.get('STORAGE_DEFAULT_KEY', 'default')
IO_QUICKSAVE_LOCUST_PORT = int(os.environ.get('IO_QUICKSAVE_LOCUST_PORT', '8089'))
IO_QUICKSAVE_LOCUST_OAUTH_PORT = int(os.environ.get('IO_QUICKSAVE_LOCUST_OAUTH_PORT', '13009'))
IO_QUICKSAVE_LOCUST_API_PORT = int(os.environ.get('IO_QUICKSAVE_LOCUST_API_PORT', '11009'))
IO_QUICKSAVE_LOCUST_CDN_PORT = int(os.environ.get('IO_QUICKSAVE_LOCUST_CDN_PORT', '12009'))
IO_QUICKSAVE_API_PORT = int(os.environ.get('IO_QUICKSAVE_API_PORT', '11000'))
api_threads = int(os.environ.get('api_threads', '0'))
api_spdy_port = int(os.environ.get('api_spdy_port', '11001'))
api_h2_port = int(os.environ.get('api_h2_port', '11002'))
IO_QUICKSAVE_CDN_PORT = int(os.environ.get('IO_QUICKSAVE_CDN_PORT', '12000'))
cdn_threads = int(os.environ.get('cdn_threads', '0'))
cdn_spdy_port = int(os.environ.get('cdn_spdy_port', '12001'))
cdn_h2_port = int(os.environ.get('cdn_h2_port', '12002'))
IO_QUICKSAVE_OAUTH_PORT = int(os.environ.get('IO_QUICKSAVE_OAUTH_PORT', '13000'))
oauth_threads = int(os.environ.get('oauth_threads', '0'))
oauth_spdy_port = int(os.environ.get('oauth_spdy_port', '11001'))
oauth_h2_port = int(os.environ.get('oauth_h2_port', '11002'))
IO_QUICKSAVE_SWAGGER_PORT = int(os.environ.get('IO_QUICKSAVE_SWAGGER_PORT', '3001'))
IO_QUICKSAVE_OAUTH_TOKEN_EXPIRE_TIME = int(os.environ.get('IO_QUICKSAVE_OAUTH_TOKEN_EXPIRE_TIME', '3600'))
IO_QUICKSAVE_MQ_PORT = int(os.environ.get('IO_QUICKSAVE_MQ_PORT', '15672'))
IO_QUICKSAVE_MQ_PORT = int(os.environ.get('IO_QUICKSAVE_MQ_PORT', '15672'))
IO_QUICKSAVE_MEMADMIN_PORT = int(os.environ.get('IO_QUICKSAVE_MEMADMIN_PORT', '18080'))
IO_QUICKSAVE_LOG_PORT = int(os.environ.get('IO_QUICKSAVE_LOG_PORT', '9009'))
MASTER_PORT = int(os.environ.get('MASTER_PORT', '5432'))
SLAVE_PORT = int(os.environ.get('SLAVE_PORT', '5433'))
IO_QUICKSAVE_LOCUST_USER_MIN = int(os.environ.get('IO_QUICKSAVE_LOCUST_USER_MIN', '1000'))
IO_QUICKSAVE_LOCUST_USER_MAX = int(os.environ.get('IO_QUICKSAVE_LOCUST_USER_MAX', '1099'))
IO_QUICKSAVE_STORAGE_PORT = int(os.environ.get('IO_QUICKSAVE_STORAGE_PORT', '2222'))
