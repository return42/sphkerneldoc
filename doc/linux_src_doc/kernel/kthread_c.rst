.. -*- coding: utf-8; mode: rst -*-

=========
kthread.c
=========

.. _`kthread_should_stop`:

kthread_should_stop
===================

.. c:function:: bool kthread_should_stop ( void)

    should this kthread return now?

    :param void:
        no arguments


.. _`kthread_should_stop.description`:

Description
-----------


When someone calls :c:func:`kthread_stop` on your kthread, it will be woken
and this will return true.  You should then return, and your return
value will be passed through to :c:func:`kthread_stop`.


.. _`kthread_should_park`:

kthread_should_park
===================

.. c:function:: bool kthread_should_park ( void)

    should this kthread park now?

    :param void:
        no arguments


.. _`kthread_should_park.description`:

Description
-----------


When someone calls :c:func:`kthread_park` on your kthread, it will be woken
and this will return true.  You should then do the necessary
cleanup and call :c:func:`kthread_parkme`

Similar to :c:func:`kthread_should_stop`, but this keeps the thread alive
and in a park position. :c:func:`kthread_unpark` "restarts" the thread and
calls the thread function again.


.. _`kthread_freezable_should_stop`:

kthread_freezable_should_stop
=============================

.. c:function:: bool kthread_freezable_should_stop (bool *was_frozen)

    should this freezable kthread return now?

    :param bool \*was_frozen:
        optional out parameter, indicates whether ``current`` was frozen


.. _`kthread_freezable_should_stop.description`:

Description
-----------

:c:func:`kthread_should_stop` for freezable kthreads, which will enter
refrigerator if necessary.  This function is safe from :c:func:`kthread_stop` /
freezer deadlock and freezable kthreads should use this function instead
of calling :c:func:`try_to_freeze` directly.


.. _`kthread_data`:

kthread_data
============

.. c:function:: void *kthread_data (struct task_struct *task)

    return data value specified on kthread creation

    :param struct task_struct \*task:
        kthread task in question


.. _`kthread_data.description`:

Description
-----------

Return the data value specified when kthread ``task`` was created.
The caller is responsible for ensuring the validity of ``task`` when
calling this function.


.. _`probe_kthread_data`:

probe_kthread_data
==================

.. c:function:: void *probe_kthread_data (struct task_struct *task)

    speculative version of kthread_data()

    :param struct task_struct \*task:
        possible kthread task in question


.. _`probe_kthread_data.description`:

Description
-----------

``task`` could be a kthread task.  Return the data value specified when it
was created if accessible.  If ``task`` isn't a kthread task or its data is
inaccessible for any reason, ``NULL`` is returned.  This function requires
that ``task`` itself is safe to dereference.


.. _`kthread_create_on_node`:

kthread_create_on_node
======================

.. c:function:: struct task_struct *kthread_create_on_node (int (*threadfn) (void *data, void *data, int node, const char namefmt[],  ...)

    create a kthread.

    :param int (\*threadfn) (void \*data):
        the function to run until signal_pending(current).

    :param void \*data:
        data ptr for ``threadfn``\ .

    :param int node:
        task and thread structures for the thread are allocated on this node

    :param const char namefmt:
        printf-style name for the thread.

    :param ...:
        variable arguments


.. _`kthread_create_on_node.description`:

Description
-----------

Description: This helper function creates and names a kernel
thread.  The thread will be stopped: use :c:func:`wake_up_process` to start
it.  See also :c:func:`kthread_run`.  The new thread has SCHED_NORMAL policy and
is affine to all CPUs.

If thread is going to be bound on a particular cpu, give its node
in ``node``\ , to get NUMA affinity for kthread stack, or else give NUMA_NO_NODE.
When woken, the thread will run @:c:func:`threadfn` with ``data`` as its
argument. @:c:func:`threadfn` can either call :c:func:`do_exit` directly if it is a
standalone thread for which no one will call :c:func:`kthread_stop`, or
return when ':c:func:`kthread_should_stop`' is true (which means
:c:func:`kthread_stop` has been called).  The return value should be zero
or a negative error number; it will be passed to :c:func:`kthread_stop`.

Returns a task_struct or ERR_PTR(-ENOMEM) or ERR_PTR(-EINTR).


.. _`kthread_bind`:

kthread_bind
============

.. c:function:: void kthread_bind (struct task_struct *p, unsigned int cpu)

    bind a just-created kthread to a cpu.

    :param struct task_struct \*p:
        thread created by :c:func:`kthread_create`.

    :param unsigned int cpu:
        cpu (might not be online, must be possible) for ``k`` to run on.


.. _`kthread_bind.description`:

Description
-----------

Description: This function is equivalent to :c:func:`set_cpus_allowed`,
except that ``cpu`` doesn't need to be online, and the thread must be
stopped (i.e., just returned from :c:func:`kthread_create`).


.. _`kthread_create_on_cpu`:

kthread_create_on_cpu
=====================

.. c:function:: struct task_struct *kthread_create_on_cpu (int (*threadfn) (void *data, void *data, unsigned int cpu, const char *namefmt)

    Create a cpu bound kthread

    :param int (\*threadfn) (void \*data):
        the function to run until signal_pending(current).

    :param void \*data:
        data ptr for ``threadfn``\ .

    :param unsigned int cpu:
        The cpu on which the thread should be bound,

    :param const char \*namefmt:
        printf-style name for the thread. Format is restricted
        to "name.\*\ ``u``\ ". Code fills in cpu number.


.. _`kthread_create_on_cpu.description`:

Description
-----------

Description: This helper function creates and names a kernel thread
The thread will be woken and put into park mode.


.. _`kthread_unpark`:

kthread_unpark
==============

.. c:function:: void kthread_unpark (struct task_struct *k)

    unpark a thread created by kthread_create().

    :param struct task_struct \*k:
        thread created by :c:func:`kthread_create`.


.. _`kthread_unpark.description`:

Description
-----------

Sets :c:func:`kthread_should_park` for ``k`` to return false, wakes it, and
waits for it to return. If the thread is marked percpu then its
bound to the cpu again.


.. _`kthread_park`:

kthread_park
============

.. c:function:: int kthread_park (struct task_struct *k)

    park a thread created by kthread_create().

    :param struct task_struct \*k:
        thread created by :c:func:`kthread_create`.


.. _`kthread_park.description`:

Description
-----------

Sets :c:func:`kthread_should_park` for ``k`` to return true, wakes it, and
waits for it to return. This can also be called after :c:func:`kthread_create`
instead of calling :c:func:`wake_up_process`: the thread will park without
calling :c:func:`threadfn`.

Returns 0 if the thread is parked, -ENOSYS if the thread exited.
If called by the kthread itself just the park bit is set.


.. _`kthread_stop`:

kthread_stop
============

.. c:function:: int kthread_stop (struct task_struct *k)

    stop a thread created by kthread_create().

    :param struct task_struct \*k:
        thread created by :c:func:`kthread_create`.


.. _`kthread_stop.description`:

Description
-----------

Sets :c:func:`kthread_should_stop` for ``k`` to return true, wakes it, and
waits for it to exit. This can also be called after :c:func:`kthread_create`
instead of calling :c:func:`wake_up_process`: the thread will exit without
calling :c:func:`threadfn`.

If :c:func:`threadfn` may call :c:func:`do_exit` itself, the caller must ensure
task_struct can't go away.

Returns the result of :c:func:`threadfn`, or ``-EINTR`` if :c:func:`wake_up_process`
was never called.


.. _`kthread_worker_fn`:

kthread_worker_fn
=================

.. c:function:: int kthread_worker_fn (void *worker_ptr)

    kthread function to process kthread_worker

    :param void \*worker_ptr:
        pointer to initialized kthread_worker


.. _`kthread_worker_fn.description`:

Description
-----------

This function can be used as ``threadfn`` to :c:func:`kthread_create` or
:c:func:`kthread_run` with ``worker_ptr`` argument pointing to an initialized
kthread_worker.  The started kthread will process work_list until
the it is stopped with :c:func:`kthread_stop`.  A kthread can also call
this function directly after extra initialization.

Different kthreads can be used for the same kthread_worker as long
as there's only one kthread attached to it at any given time.  A
kthread_worker without an attached kthread simply collects queued
kthread_works.


.. _`queue_kthread_work`:

queue_kthread_work
==================

.. c:function:: bool queue_kthread_work (struct kthread_worker *worker, struct kthread_work *work)

    queue a kthread_work

    :param struct kthread_worker \*worker:
        target kthread_worker

    :param struct kthread_work \*work:
        kthread_work to queue


.. _`queue_kthread_work.description`:

Description
-----------

Queue ``work`` to work processor ``task`` for async execution.  ``task``
must have been created with :c:func:`kthread_worker_create`.  Returns ``true``
if ``work`` was successfully queued, ``false`` if it was already pending.


.. _`flush_kthread_work`:

flush_kthread_work
==================

.. c:function:: void flush_kthread_work (struct kthread_work *work)

    flush a kthread_work

    :param struct kthread_work \*work:
        work to flush


.. _`flush_kthread_work.description`:

Description
-----------

If ``work`` is queued or executing, wait for it to finish execution.


.. _`flush_kthread_worker`:

flush_kthread_worker
====================

.. c:function:: void flush_kthread_worker (struct kthread_worker *worker)

    flush all current works on a kthread_worker

    :param struct kthread_worker \*worker:
        worker to flush


.. _`flush_kthread_worker.description`:

Description
-----------

Wait until all currently executing or pending works on ``worker`` are
finished.

