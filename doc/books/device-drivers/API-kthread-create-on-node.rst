
.. _API-kthread-create-on-node:

======================
kthread_create_on_node
======================

*man kthread_create_on_node(9)*

*4.6.0-rc1*

create a kthread.


Synopsis
========

.. c:function:: struct task_struct ⋆ kthread_create_on_node( int (*threadfn) void *data, void * data, int node, const char namefmt[], ... )

Arguments
=========

``threadfn``
    the function to run until signal_pending(current).

``data``
    data ptr for ``threadfn``.

``node``
    task and thread structures for the thread are allocated on this node

``namefmt[]``
    printf-style name for the thread.

``...``
    variable arguments


Description
===========

This helper function creates and names a kernel thread. The thread will be stopped: use ``wake_up_process`` to start it. See also ``kthread_run``. The new thread has SCHED_NORMAL
policy and is affine to all CPUs.

If thread is going to be bound on a particular cpu, give its node in ``node``, to get NUMA affinity for kthread stack, or else give NUMA_NO_NODE. When woken, the thread will run
``threadfn``\ () with ``data`` as its argument. ``threadfn``\ () can either call ``do_exit`` directly if it is a standalone thread for which no one will call ``kthread_stop``, or
return when '``kthread_should_stop``' is true (which means ``kthread_stop`` has been called). The return value should be zero or a negative error number; it will be passed to
``kthread_stop``.

Returns a task_struct or ERR_PTR(-ENOMEM) or ERR_PTR(-EINTR).
