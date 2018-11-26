.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/tracepoint.h

.. _`tracepoint_string`:

tracepoint_string
=================

.. c:function::  tracepoint_string( str)

    register constant persistent string to trace system \ ``str``\  - a constant persistent string that will be referenced in tracepoints

    :param str:
        *undescribed*
    :type str: 

.. _`tracepoint_string.description`:

Description
-----------

If constant strings are being used in tracepoints, it is faster and
more efficient to just save the pointer to the string and reference
that with a printf "%s" instead of saving the string in the ring buffer
and wasting space and time.

The problem with the above approach is that userspace tools that read
the binary output of the trace buffers do not have access to the string.
Instead they just show the address of the string which is not very
useful to users.

With \ :c:func:`tracepoint_string`\ , the string will be registered to the tracing
system and exported to userspace via the debugfs/tracing/printk_formats
file that maps the string address to the string text. This way userspace
tools that read the binary buffers have a way to map the pointers to
the ASCII strings they represent.

The \ ``str``\  used must be a constant string and persistent as it would not
make sense to show a string that no longer exists. But it is still fine
to be used with modules, because when modules are unloaded, if they
had tracepoints, the ring buffers are cleared too. As long as the string
does not change during the life of the module, it is fine to use
\ :c:func:`tracepoint_string`\  within a module.

.. This file was automatic generated / don't edit.

