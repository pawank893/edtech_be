import logging


def get(log_root=None, formatter=None, handler=None):
    if not formatter:
        formatter = 'logstash_fmtr'

    if not handler:
        handler = 'logging.handlers.WatchedFileHandler'

    if not log_root.endswith('/'):
        log_root += '/'

    return {
        'version': 1,
        'disable_existing_loggers': False,

        'filters': {
            'request_filter': {
                '()': 'log_request_id.filters.RequestIDFilter'
            },
            'error_filter': {
                '()': 'edtech.settings.utils.filters.LogLevelFilter',
                'level': logging.ERROR
            },
            'warn_filter': {
                '()': 'edtech.settings.utils.filters.LogLevelFilter',
                'level': logging.WARN
            },
            'debug_filter': {
                '()': 'edtech.settings.utils.filters.LogLevelFilter',
                'level': logging.DEBUG
            },
            'info_filter': {
                '()': 'edtech.settings.utils.filters.LogLevelFilter',
                'level': logging.INFO
            },
            'critical_filter': {
                '()': 'edtech.settings.utils.filters.LogLevelFilter',
                'level': logging.CRITICAL
            }
        },
        'formatters': {
            'verbose': {
                'format': "[%(request_id)s] [%(asctime)s] %(levelname)s  [%(name)s:%(lineno)s] %(message)s",
                'datefmt': "%d/%b/%Y %H:%M:%S"},
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
            'logstash_fmtr': {
                '()': 'logstash_formatter.LogstashFormatterV1'
                # TODO: Commented out to find any possibilities of logstash formatter erring in keys.
                # Once there are any type errors we can uncomment the below code
                # 'json_cls': ObjectEncoder
            },
        },
        'handlers': {
            'null': {
                'level': 'INFO',
                'class': 'logging.NullHandler',
            },
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
                'filters': ['request_filter']
            },
            'django': {
                'level': 'DEBUG',
                'class': handler,
                'filters': ['request_filter'],
                'formatter': formatter,
                'filename': log_root + 'django.log',
            },
            'default': {
                'level': 'DEBUG',
                'class': handler,
                'filters': ['request_filter'],
                'formatter': formatter,
                'filename': log_root + 'default.log',
            },
            'error_handler': {
                'level': 'ERROR',
                'class': handler,
                'filters': ['error_filter', 'request_filter'],
                'formatter': formatter,
                'filename': log_root + 'app_error.log',
            },
            'warn_handler': {
                'level': 'WARN',
                'class': handler,
                'filters': ['warn_filter', 'request_filter'],
                'formatter': formatter,
                'filename': log_root + 'app_warn.log',
            },
            'info_handler': {
                'level': 'INFO',
                'class': handler,
                'filters': ['info_filter', 'request_filter'],
                'formatter': formatter,
                'filename': log_root + 'app_info.log',
            },
            'debug_handler': {
                'level': 'DEBUG',
                'class': handler,
                'filters': ['debug_filter', 'request_filter'],
                'formatter': formatter,
                'filename': log_root + 'app_debug.log',
            },
            'critical_handler': {
                'level': 'CRITICAL',
                'class': handler,
                'filters': ['critical_filter', 'request_filter'],
                'formatter': formatter,
                'filename': log_root + 'app_critical.log',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['django'],
                'level': 'DEBUG',
                'propagate': True,
            },
            'athena': {
                'handlers': ['console', 'error_handler', 'warn_handler', 'info_handler', 'debug_handler', 'critical_handler'],
                'level': 'DEBUG',
            },
            'b2b': {
                'handlers': ['console', 'error_handler', 'warn_handler', 'info_handler', 'debug_handler', 'critical_handler'],
                'level': 'DEBUG',
            },
            'data_sync': {
                'handlers': ['console', 'error_handler', 'warn_handler', 'info_handler', 'debug_handler', 'critical_handler'],
                'level': 'DEBUG',
            },
            'third_party_intg': {
                'handlers': ['console', 'error_handler', 'warn_handler', 'info_handler', 'debug_handler', 'critical_handler'],
                'level': 'DEBUG',
            },
            '': {
                'handlers': ['default','console', 'critical_handler'],
                'level': 'DEBUG',
            },
        },
    }
