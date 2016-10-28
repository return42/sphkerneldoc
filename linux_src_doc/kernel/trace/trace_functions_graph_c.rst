.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/trace_functions_graph.c

.. _`ftrace_graph_is_dead`:

ftrace_graph_is_dead
====================

.. c:function:: bool ftrace_graph_is_dead( void)

    returns true if \ :c:func:`ftrace_graph_stop`\  was called

    :param  void:
        no arguments

.. _`ftrace_graph_is_dead.description`:

Description
-----------

\ :c:func:`ftrace_graph_stop`\  is called when a severe error is detected in
the function graph tracing. This function is called by the critical
paths of function graph to keep those paths from doing any more harm.

.. _`ftrace_graph_stop`:

ftrace_graph_stop
=================

.. c:function:: void ftrace_graph_stop( void)

    set to permanently disable function graph tracincg

    :param  void:
        no arguments

.. _`ftrace_graph_stop.description`:

Description
-----------

In case of an error int function graph tracing, this is called
to try to keep function graph tracing from causing any more harm.
Usually this is pretty severe and this is called to try to at least
get a warning out to the user.

.. This file was automatic generated / don't edit.

