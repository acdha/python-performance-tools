========================
Python Performance Tools
========================

Simple utilities to make it easier to track performance of Python programs under normal operations

Context Managers
----------------

DisplayElapsed
~~~~~~~~~~~~~~

This context manager makes it easy to display console-oriented start/end messages with end-user tolerable
formatting.

Usage::

    with DisplayElapsed("{now} uploading {filename} (original: {original})\n",
                        "{now} uploaded {filename} in {elapsed:.1f} seconds",
                        filename=remote_path, original=local_path):
        upload_filename(…)

Notes:

* DisplayElapsed takes one positional argument: ``message``. The message is formatted using
  `str.format <http://docs.python.org/2/library/string.html#format-string-syntax>`_ with the values ``{now}``
  and ``{elapsed}`` provided automatically. All other keyword arguments provided to ``DisplayElapsed`` will be
  available during formatting.
* If ``message`` contains ``{{now}}`` it will be replaced with the current timestamp
* If ``message`` does not contain ``{{now}}`` it will be prepended unless ``include_timestamp=False``
* If ``postamble`` is not specified, it will default to ``" ({elapsed:.1f} seconds)"``
* If ``output`` is not specified, it will default to ``sys.stdout``
* If ``output_on_error`` is not True, the normal postamble display will be suppressed when an exception occurs
* By default, a newline will not be emitted after the opening message so the message and postamble will be
  displayed on a single line. ``output`` will be flushed, if supported, to provide immediate feedback.
  Provide a message which ends in ``\n`` if you want multi-line output.