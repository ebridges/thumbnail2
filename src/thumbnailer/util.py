from os import environ
from logging import getLogger, basicConfig, DEBUG, INFO, debug, info, warning

from sentry_sdk import init
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration

from thumbnailer import version


DEFAULT_WIDTH = 222
DEFAULT_HEIGHT = 222
MONITORING_DSN = 'SENTRY_DSN'
OPERATING_ENV = 'OPERATING_ENV'


def configure_logging(verbose):
    if verbose:
        level = DEBUG
    else:
        level = INFO

    if getLogger().hasHandlers():
        # The Lambda environment pre-configures a handler logging to stderr.
        # If a handler is already configured, `.basicConfig` does not execute.
        # Thus we set the level directly.
        getLogger().setLevel(level)
    else:
        basicConfig(
            format='[%(asctime)s][%(levelname)s] %(message)s',
            datefmt='%Y/%m/%d %H:%M:%S',
            level=level,
        )


def init_monitoring():
    dsn = environ.get(MONITORING_DSN)
    env = environ.get(OPERATING_ENV)
    
    if not dsn:
        warning(f'DSN not found in envronment under key {MONITORING_DSN}')
        return
    
    info(f'Configuring monitoring via DSN: {dsn}')
    init(
        dsn=dsn,
        integrations=[AwsLambdaIntegration()],
        release=f'v{version}',
        send_default_pii=False,
        traces_sample_rate=0.50,
        environment=env,
        _experiments={'auto_enabling_integrations': True},
    )

