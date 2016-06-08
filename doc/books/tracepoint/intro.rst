.. -*- coding: utf-8; mode: rst -*-

.. _intro:

************
Introduction
************

Tracepoints are static probe points that are located in strategic points
throughout the kernel. 'Probes' register/unregister with tracepoints via
a callback mechanism. The 'probes' are strictly typed functions that are
passed a unique set of parameters defined by each tracepoint.

From this simple callback mechanism, 'probes' can be used to profile,
debug, and understand kernel behavior. There are a number of tools that
provide a framework for using 'probes'. These tools include Systemtap,
ftrace, and LTTng.

Tracepoints are defined in a number of header files via various macros.
Thus, the purpose of this document is to provide a clear accounting of
the available tracepoints. The intention is to understand not only what
tracepoints are available but also to understand where future
tracepoints might be added.

The API presented has functions of the form:
``trace_tracepointname(function parameters)``. These are the tracepoints
callbacks that are found throughout the code. Registering and
unregistering probes with these callback sites is covered in the
``Documentation/trace/*`` directory.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
