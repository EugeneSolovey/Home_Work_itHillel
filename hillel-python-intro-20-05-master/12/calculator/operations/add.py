from logging.action_logging import log_action

# Error - calculator is not a
# from ..logging import action_logging


def add(x, y):
    log_action("addition")
    return x + y
