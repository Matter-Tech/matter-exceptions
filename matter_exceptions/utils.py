import os
import sentry_sdk

IS_ENV_LOCAL_OR_TEST = os.environ.get("IS_ENV_LOCAL_OR_TEST", True)
SENTRY_DSN = os.environ.get("SENTRY_DSN")


def capture_error(message: str, extra: dict = None, level: str = "error"):
    if extra is None:
        extra = {}

    if not IS_ENV_LOCAL_OR_TEST and SENTRY_DSN is not None:
        with sentry_sdk.push_scope() as scope:
            for key, value in extra.items():
                scope.set_extra(key, value)

            sentry_sdk.capture_message(message, level)
