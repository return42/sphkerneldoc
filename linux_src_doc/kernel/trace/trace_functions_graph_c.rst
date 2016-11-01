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

ftrace_graph_stop() is called when a severe error is detected in
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

.. _`ftrace_graph_ret_addr`:

ftrace_graph_ret_addr
=====================

.. c:function:: unsigned long ftrace_graph_ret_addr(struct task_struct *task, int *idx, unsigned long ret, unsigned long *retp)

    convert a potentially modified stack return address to its original value

    :param struct task_struct \*task:
        *undescribed*

    :param int \*idx:
        *undescribed*

    :param unsigned long ret:
        *undescribed*

    :param unsigned long \*retp:
        *undescribed*

.. _`ftrace_graph_ret_addr.description`:

Description
-----------

This function can be called by stack unwinding code to convert a found stack
return address ('ret') to its original value, in case the function graph
tracer has modified it to be 'return_to_handler'.  If the address hasn't
been modified, the unchanged value of 'ret' is returned.

'idx' is a state variable which should be initialized by the caller to zero
before the first call.

'retp' is a pointer to the return address on the stack.  It's ignored if
the arch doesn't have HAVE_FUNCTION_GRAPH_RET_ADDR_PTR defined.

.. This file was automatic generated / don't edit.

