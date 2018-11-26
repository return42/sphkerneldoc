.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/eventpoll.c

.. _`ep_events_available`:

ep_events_available
===================

.. c:function:: int ep_events_available(struct eventpoll *ep)

    Checks if ready events might be available.

    :param ep:
        Pointer to the eventpoll context.
    :type ep: struct eventpoll \*

.. _`ep_events_available.return`:

Return
------

Returns a value different than zero if ready events are available,
or zero otherwise.

.. _`ep_call_nested`:

ep_call_nested
==============

.. c:function:: int ep_call_nested(struct nested_calls *ncalls, int max_nests, int (*nproc)(void *, void *, int), void *priv, void *cookie, void *ctx)

    Perform a bound (possibly) nested call, by checking that the recursion limit is not exceeded, and that the same nested call (by the meaning of same cookie) is no re-entered.

    :param ncalls:
        Pointer to the nested_calls structure to be used for this call.
    :type ncalls: struct nested_calls \*

    :param max_nests:
        Maximum number of allowed nesting calls.
    :type max_nests: int

    :param int (\*nproc)(void \*, void \*, int):
        Nested call core function pointer.

    :param priv:
        Opaque data to be passed to the \ ``nproc``\  callback.
    :type priv: void \*

    :param cookie:
        Cookie to be used to identify this nested call.
    :type cookie: void \*

    :param ctx:
        This instance context.
    :type ctx: void \*

.. _`ep_call_nested.return`:

Return
------

Returns the code returned by the \ ``nproc``\  callback, or -1 if
the maximum recursion limit has been exceeded.

.. _`ep_scan_ready_list`:

ep_scan_ready_list
==================

.. c:function:: __poll_t ep_scan_ready_list(struct eventpoll *ep, __poll_t (*sproc)(struct eventpoll *, struct list_head *, void *), void *priv, int depth, bool ep_locked)

    Scans the ready list in a way that makes possible for the scan code, to call f_op->poll(). Also allows for O(NumReady) performance.

    :param ep:
        Pointer to the epoll private data structure.
    :type ep: struct eventpoll \*

    :param __poll_t (\*sproc)(struct eventpoll \*, struct list_head \*, void \*):
        Pointer to the scan callback.

    :param priv:
        Private opaque data passed to the \ ``sproc``\  callback.
    :type priv: void \*

    :param depth:
        The current depth of recursive f_op->poll calls.
    :type depth: int

    :param ep_locked:
        caller already holds ep->mtx
    :type ep_locked: bool

.. _`ep_scan_ready_list.return`:

Return
------

The same integer error code returned by the \ ``sproc``\  callback.

.. _`reverse_path_check`:

reverse_path_check
==================

.. c:function:: int reverse_path_check( void)

    The tfile_check_list is list of file \*, which have links that are proposed to be newly added. We need to make sure that those added links don't add too many paths such that we will spend all our time waking up eventpoll objects.

    :param void:
        no arguments
    :type void: 

.. _`reverse_path_check.return`:

Return
------

Returns zero if the proposed links don't create too many paths,
-1 otherwise.

.. _`ep_poll`:

ep_poll
=======

.. c:function:: int ep_poll(struct eventpoll *ep, struct epoll_event __user *events, int maxevents, long timeout)

    Retrieves ready events, and delivers them to the caller supplied event buffer.

    :param ep:
        Pointer to the eventpoll context.
    :type ep: struct eventpoll \*

    :param events:
        Pointer to the userspace buffer where the ready events should be
        stored.
    :type events: struct epoll_event __user \*

    :param maxevents:
        Size (in terms of number of events) of the caller event buffer.
    :type maxevents: int

    :param timeout:
        Maximum timeout for the ready events fetch operation, in
        milliseconds. If the \ ``timeout``\  is zero, the function will not block,
        while if the \ ``timeout``\  is less than zero, the function will block
        until at least one event has been retrieved (or an error
        occurred).
    :type timeout: long

.. _`ep_poll.return`:

Return
------

Returns the number of ready events which have been fetched, or an
error code, in case of error.

.. _`ep_loop_check_proc`:

ep_loop_check_proc
==================

.. c:function:: int ep_loop_check_proc(void *priv, void *cookie, int call_nests)

    Callback function to be passed to the \ ``ep_call_nested``\ () API, to verify that adding an epoll file inside another epoll structure, does not violate the constraints, in terms of closed loops, or too deep chains (which can result in excessive stack usage).

    :param priv:
        Pointer to the epoll file to be currently checked.
    :type priv: void \*

    :param cookie:
        Original cookie for this call. This is the top-of-the-chain epoll
        data structure pointer.
    :type cookie: void \*

    :param call_nests:
        Current dept of the \ ``ep_call_nested``\ () call stack.
    :type call_nests: int

.. _`ep_loop_check_proc.return`:

Return
------

Returns zero if adding the epoll \ ``file``\  inside current epoll
structure \ ``ep``\  does not violate the constraints, or -1 otherwise.

.. _`ep_loop_check`:

ep_loop_check
=============

.. c:function:: int ep_loop_check(struct eventpoll *ep, struct file *file)

    Performs a check to verify that adding an epoll file (@file) another epoll file (represented by \ ``ep``\ ) does not create closed loops or too deep chains.

    :param ep:
        Pointer to the epoll private data structure.
    :type ep: struct eventpoll \*

    :param file:
        Pointer to the epoll file to be checked.
    :type file: struct file \*

.. _`ep_loop_check.return`:

Return
------

Returns zero if adding the epoll \ ``file``\  inside current epoll
structure \ ``ep``\  does not violate the constraints, or -1 otherwise.

.. This file was automatic generated / don't edit.

