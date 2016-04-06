
.. _API-kthread-worker-fn:

=================
kthread_worker_fn
=================

*man kthread_worker_fn(9)*

*4.6.0-rc1*

kthread function to process kthread_worker


Synopsis
========

.. c:function:: int kthread_worker_fn( void * worker_ptr )

Arguments
=========

``worker_ptr``
    pointer to initialized kthread_worker


Description
===========

This function can be used as ``threadfn`` to ``kthread_create`` or ``kthread_run`` with ``worker_ptr`` argument pointing to an initialized kthread_worker. The started kthread will
process work_list until the it is stopped with ``kthread_stop``. A kthread can also call this function directly after extra initialization.

Different kthreads can be used for the same kthread_worker as long as there's only one kthread attached to it at any given time. A kthread_worker without an attached kthread
simply collects queued kthread_works.
