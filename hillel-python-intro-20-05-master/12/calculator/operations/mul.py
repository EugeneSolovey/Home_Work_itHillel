from logging import action_logging


def mul(x, y):
    action_logging.log_action("multiplication")
    return x * y
