.. -*- coding: utf-8; mode: rst -*-

.. _API-trace-puts:

==========
trace_puts
==========

*man trace_puts(9)*

*4.6.0-rc5*

write a string into the ftrace buffer


Synopsis
========

.. c:function:: trace_puts( str )

Arguments
=========

``str``
    the string to record


Note
====

__trace_bputs is an internal function for trace_puts and the ``ip``
is passed in via the trace_puts macro.

This is similar to ``trace_printk`` but is made for those really fast
paths that a developer wants the least amount of “Heisenbug” affects,
where the processing of the print format is still too much.

This function allows a kernel developer to debug fast path sections that
printk is not appropriate for. By scattering in various printk like
tracing in the code, a developer can quickly see where problems are
occurring.

This is intended as a debugging tool for the developer only. Please
refrain from leaving trace_puts scattered around in your code. (Extra
memory is used for special buffers that are allocated when
``trace_puts`` is used)


Returns
=======

0 if nothing was written, positive # if string was. (1 when
__trace_bputs is used, strlen(str) when __trace_puts is used)


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
