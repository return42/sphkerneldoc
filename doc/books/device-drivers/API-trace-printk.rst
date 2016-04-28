.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-printk:

============
trace_printk
============

*man trace_printk(9)*

*4.6.0-rc5*

printf formatting in the ftrace buffer


Synopsis
========

.. c:function:: trace_printk( fmt, ... )

Arguments
=========

``fmt``
    the printf format for printing

``...``
    variable arguments


Note
====

__trace_printk is an internal function for trace_printk and the
``ip`` is passed in via the trace_printk macro.

This function allows a kernel developer to debug fast path sections that
printk is not appropriate for. By scattering in various printk like
tracing in the code, a developer can quickly see where problems are
occurring.

This is intended as a debugging tool for the developer only. Please
refrain from leaving trace_printks scattered around in your code.
(Extra memory is used for special buffers that are allocated when
``trace_printk`` is used)

A little optization trick is done here. If there's only one argument,
there's no need to scan the string for printf formats. The
``trace_puts`` will suffice. But how can we take advantage of using
``trace_puts`` when ``trace_printk`` has only one argument? By
stringifying the args and checking the size we can tell whether or not
there are args. __stringify((__VA_ARGS__)) will turn into “()0”
with a size of 3 when there are no args, anything else will be bigger.
All we need to do is define a string to this, and then take its size and
compare to 3. If it's bigger, use ``do_trace_printk`` otherwise,
optimize it to ``trace_puts``. Then just let gcc optimize the rest.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
