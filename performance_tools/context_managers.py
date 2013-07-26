from __future__ import absolute_import, print_function

from datetime import datetime
from timeit import default_timer as timer
import sys


class DisplayElapsed(object):
    def __init__(self, message, postamble=None, output=sys.stdout,
                 include_timestamp=True, **context):

        self.context = context
        self.output = output

        if include_timestamp and '{now' not in message:
            message = "{now} %s" % message
        self.message = message

        if postamble is None:
            postamble = " ({elapsed:,.1f} seconds)"
        self.postamble = postamble

    def __enter__(self):
        self.output_message(self.message, end='')
        self.start = timer()

    def __exit__(self, *args):
        end = timer()

        elapsed = end - self.start

        self.output_message(self.postamble, elapsed=elapsed)

    def output_message(self, message, end='\n', **kwargs):
        ctx = {}
        ctx.update(self.context)
        ctx.update(kwargs)

        if '{now' in message:
            ctx["now"] = datetime.now().strftime('%Y-%m-%d %H:%M')

        if callable(self.output):
            self.output(message, ctx)
        else:
            print(message.format(**ctx), file=self.output, end=end)
            if hasattr(self.output, "flush"):
                self.output.flush()
