.. -*- coding: utf-8; mode: rst -*-

=========
kthread.h
=========

.. _`kthread_run`:

kthread_run
===========

.. c:function:: kthread_run ( threadfn,  data,  namefmt,  ...)

    create and wake a thread.

    :param threadfn:
        the function to run until signal_pending(current).

    :param data:
        data ptr for ``threadfn``\ .

    :param namefmt:
        printf-style name for the thread.

    :param ...:
        variable arguments


.. _`kthread_run.description`:

Description
-----------

Description: Convenient wrapper for :c:func:`kthread_create` followed by
:c:func:`wake_up_process`.  Returns the kthread or ERR_PTR(-ENOMEM).

