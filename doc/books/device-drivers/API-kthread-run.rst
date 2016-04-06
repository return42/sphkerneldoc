
.. _API-kthread-run:

===========
kthread_run
===========

*man kthread_run(9)*

*4.6.0-rc1*

create and wake a thread.


Synopsis
========

.. c:function:: kthread_run( threadfn, data, namefmt, ... )

Arguments
=========

``threadfn``
    the function to run until signal_pending(current).

``data``
    data ptr for ``threadfn``.

``namefmt``
    printf-style name for the thread.

``...``
    variable arguments


Description
===========

Convenient wrapper for ``kthread_create`` followed by ``wake_up_process``. Returns the kthread or ERR_PTR(-ENOMEM).
