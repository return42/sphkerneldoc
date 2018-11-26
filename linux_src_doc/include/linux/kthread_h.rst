.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/kthread.h

.. _`kthread_create`:

kthread_create
==============

.. c:function::  kthread_create( threadfn,  data,  namefmt,  arg...)

    create a kthread on the current node

    :param threadfn:
        the function to run in the thread
    :type threadfn: 

    :param data:
        data pointer for \ ``threadfn``\ ()
    :type data: 

    :param namefmt:
        printf-style format string for the thread name
    :type namefmt: 

.. _`kthread_create.description`:

Description
-----------

This macro will create a kthread on the current node, leaving it in
the stopped state.  This is just a helper for \ :c:func:`kthread_create_on_node`\ ;
see the documentation there for more details.

.. _`kthread_run`:

kthread_run
===========

.. c:function::  kthread_run( threadfn,  data,  namefmt,  ...)

    create and wake a thread.

    :param threadfn:
        the function to run until signal_pending(current).
    :type threadfn: 

    :param data:
        data ptr for \ ``threadfn``\ .
    :type data: 

    :param namefmt:
        printf-style name for the thread.
    :type namefmt: 

    :param ellipsis ellipsis:
        variable arguments

.. _`kthread_run.description`:

Description
-----------

Convenient wrapper for \ :c:func:`kthread_create`\  followed by
\ :c:func:`wake_up_process`\ .  Returns the kthread or ERR_PTR(-ENOMEM).

.. This file was automatic generated / don't edit.

