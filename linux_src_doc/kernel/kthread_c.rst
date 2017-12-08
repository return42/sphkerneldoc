.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/kthread.c

.. _`kthread_should_stop`:

kthread_should_stop
===================

.. c:function:: bool kthread_should_stop( void)

    should this kthread return now?

    :param  void:
        no arguments

.. _`kthread_should_stop.description`:

Description
-----------

When someone calls \ :c:func:`kthread_stop`\  on your kthread, it will be woken
and this will return true.  You should then return, and your return
value will be passed through to \ :c:func:`kthread_stop`\ .

.. _`kthread_should_park`:

kthread_should_park
===================

.. c:function:: bool kthread_should_park( void)

    should this kthread park now?

    :param  void:
        no arguments

.. _`kthread_should_park.description`:

Description
-----------

When someone calls \ :c:func:`kthread_park`\  on your kthread, it will be woken
and this will return true.  You should then do the necessary
cleanup and call \ :c:func:`kthread_parkme`\ 

Similar to \ :c:func:`kthread_should_stop`\ , but this keeps the thread alive
and in a park position. \ :c:func:`kthread_unpark`\  "restarts" the thread and
calls the thread function again.

.. _`kthread_freezable_should_stop`:

kthread_freezable_should_stop
=============================

.. c:function:: bool kthread_freezable_should_stop(bool *was_frozen)

    should this freezable kthread return now?

    :param bool \*was_frozen:
        optional out parameter, indicates whether \ ``current``\  was frozen

.. _`kthread_freezable_should_stop.description`:

Description
-----------

kthread_should_stop() for freezable kthreads, which will enter
refrigerator if necessary.  This function is safe from \ :c:func:`kthread_stop`\  /
freezer deadlock and freezable kthreads should use this function instead
of calling \ :c:func:`try_to_freeze`\  directly.

.. _`kthread_data`:

kthread_data
============

.. c:function:: void *kthread_data(struct task_struct *task)

    return data value specified on kthread creation

    :param struct task_struct \*task:
        kthread task in question

.. _`kthread_data.description`:

Description
-----------

Return the data value specified when kthread \ ``task``\  was created.
The caller is responsible for ensuring the validity of \ ``task``\  when
calling this function.

.. _`kthread_probe_data`:

kthread_probe_data
==================

.. c:function:: void *kthread_probe_data(struct task_struct *task)

    speculative version of \ :c:func:`kthread_data`\ 

    :param struct task_struct \*task:
        possible kthread task in question

.. _`kthread_probe_data.description`:

Description
-----------

@task could be a kthread task.  Return the data value specified when it
was created if accessible.  If \ ``task``\  isn't a kthread task or its data is
inaccessible for any reason, \ ``NULL``\  is returned.  This function requires
that \ ``task``\  itself is safe to dereference.

.. _`kthread_create_on_node`:

kthread_create_on_node
======================

.. c:function:: struct task_struct *kthread_create_on_node(int (*threadfn)(void *data), void *data, int node, const char namefmt,  ...)

    create a kthread.

    :param int (\*threadfn)(void \*data):
        the function to run until signal_pending(current).

    :param void \*data:
        data ptr for \ ``threadfn``\ .

    :param int node:
        task and thread structures for the thread are allocated on this node

    :param const char namefmt:
        printf-style name for the thread.

    :param ellipsis ellipsis:
        variable arguments

.. _`kthread_create_on_node.description`:

Description
-----------

This helper function creates and names a kernel
thread.  The thread will be stopped: use \ :c:func:`wake_up_process`\  to start
it.  See also \ :c:func:`kthread_run`\ .  The new thread has SCHED_NORMAL policy and
is affine to all CPUs.

If thread is going to be bound on a particular cpu, give its node
in \ ``node``\ , to get NUMA affinity for kthread stack, or else give NUMA_NO_NODE.
When woken, the thread will run \ ``threadfn``\ () with \ ``data``\  as its
argument. \ ``threadfn``\ () can either call \ :c:func:`do_exit`\  directly if it is a
standalone thread for which no one will call \ :c:func:`kthread_stop`\ , or
return when 'kthread_should_stop()' is true (which means
\ :c:func:`kthread_stop`\  has been called).  The return value should be zero
or a negative error number; it will be passed to \ :c:func:`kthread_stop`\ .

Returns a task_struct or ERR_PTR(-ENOMEM) or ERR_PTR(-EINTR).

.. _`kthread_bind`:

kthread_bind
============

.. c:function:: void kthread_bind(struct task_struct *p, unsigned int cpu)

    bind a just-created kthread to a cpu.

    :param struct task_struct \*p:
        thread created by \ :c:func:`kthread_create`\ .

    :param unsigned int cpu:
        cpu (might not be online, must be possible) for \ ``k``\  to run on.

.. _`kthread_bind.description`:

Description
-----------

This function is equivalent to \ :c:func:`set_cpus_allowed`\ ,
except that \ ``cpu``\  doesn't need to be online, and the thread must be
stopped (i.e., just returned from \ :c:func:`kthread_create`\ ).

.. _`kthread_create_on_cpu`:

kthread_create_on_cpu
=====================

.. c:function:: struct task_struct *kthread_create_on_cpu(int (*threadfn)(void *data), void *data, unsigned int cpu, const char *namefmt)

    Create a cpu bound kthread

    :param int (\*threadfn)(void \*data):
        the function to run until signal_pending(current).

    :param void \*data:
        data ptr for \ ``threadfn``\ .

    :param unsigned int cpu:
        The cpu on which the thread should be bound,

    :param const char \*namefmt:
        printf-style name for the thread. Format is restricted
        to "name.*%u". Code fills in cpu number.

.. _`kthread_create_on_cpu.description`:

Description
-----------

This helper function creates and names a kernel thread
The thread will be woken and put into park mode.

.. _`kthread_unpark`:

kthread_unpark
==============

.. c:function:: void kthread_unpark(struct task_struct *k)

    unpark a thread created by \ :c:func:`kthread_create`\ .

    :param struct task_struct \*k:
        thread created by \ :c:func:`kthread_create`\ .

.. _`kthread_unpark.description`:

Description
-----------

Sets \ :c:func:`kthread_should_park`\  for \ ``k``\  to return false, wakes it, and
waits for it to return. If the thread is marked percpu then its
bound to the cpu again.

.. _`kthread_park`:

kthread_park
============

.. c:function:: int kthread_park(struct task_struct *k)

    park a thread created by \ :c:func:`kthread_create`\ .

    :param struct task_struct \*k:
        thread created by \ :c:func:`kthread_create`\ .

.. _`kthread_park.description`:

Description
-----------

Sets \ :c:func:`kthread_should_park`\  for \ ``k``\  to return true, wakes it, and
waits for it to return. This can also be called after \ :c:func:`kthread_create`\ 
instead of calling \ :c:func:`wake_up_process`\ : the thread will park without
calling \ :c:func:`threadfn`\ .

Returns 0 if the thread is parked, -ENOSYS if the thread exited.
If called by the kthread itself just the park bit is set.

.. _`kthread_stop`:

kthread_stop
============

.. c:function:: int kthread_stop(struct task_struct *k)

    stop a thread created by \ :c:func:`kthread_create`\ .

    :param struct task_struct \*k:
        thread created by \ :c:func:`kthread_create`\ .

.. _`kthread_stop.description`:

Description
-----------

Sets \ :c:func:`kthread_should_stop`\  for \ ``k``\  to return true, wakes it, and
waits for it to exit. This can also be called after \ :c:func:`kthread_create`\ 
instead of calling \ :c:func:`wake_up_process`\ : the thread will exit without
calling \ :c:func:`threadfn`\ .

If \ :c:func:`threadfn`\  may call \ :c:func:`do_exit`\  itself, the caller must ensure
task_struct can't go away.

Returns the result of \ :c:func:`threadfn`\ , or \ ``-EINTR``\  if \ :c:func:`wake_up_process`\ 
was never called.

.. _`kthread_worker_fn`:

kthread_worker_fn
=================

.. c:function:: int kthread_worker_fn(void *worker_ptr)

    kthread function to process kthread_worker

    :param void \*worker_ptr:
        pointer to initialized kthread_worker

.. _`kthread_worker_fn.description`:

Description
-----------

This function implements the main cycle of kthread worker. It processes
work_list until it is stopped with \ :c:func:`kthread_stop`\ . It sleeps when the queue
is empty.

The works are not allowed to keep any locks, disable preemption or interrupts
when they finish. There is defined a safe point for freezing when one work
finishes and before a new one is started.

Also the works must not be handled by more than one worker at the same time,
see also \ :c:func:`kthread_queue_work`\ .

.. _`kthread_create_worker`:

kthread_create_worker
=====================

.. c:function:: struct kthread_worker *kthread_create_worker(unsigned int flags, const char namefmt,  ...)

    create a kthread worker

    :param unsigned int flags:
        flags modifying the default behavior of the worker

    :param const char namefmt:
        printf-style name for the kthread worker (task).

    :param ellipsis ellipsis:
        variable arguments

.. _`kthread_create_worker.description`:

Description
-----------

Returns a pointer to the allocated worker on success, ERR_PTR(-ENOMEM)
when the needed structures could not get allocated, and ERR_PTR(-EINTR)
when the worker was SIGKILLed.

.. _`kthread_create_worker_on_cpu`:

kthread_create_worker_on_cpu
============================

.. c:function:: struct kthread_worker *kthread_create_worker_on_cpu(int cpu, unsigned int flags, const char namefmt,  ...)

    create a kthread worker and bind it it to a given CPU and the associated NUMA node.

    :param int cpu:
        CPU number

    :param unsigned int flags:
        flags modifying the default behavior of the worker

    :param const char namefmt:
        printf-style name for the kthread worker (task).

    :param ellipsis ellipsis:
        variable arguments

.. _`kthread_create_worker_on_cpu.description`:

Description
-----------

Use a valid CPU number if you want to bind the kthread worker
to the given CPU and the associated NUMA node.

A good practice is to add the cpu number also into the worker name.
For example, use kthread_create_worker_on_cpu(cpu, "helper/%d", cpu).

Returns a pointer to the allocated worker on success, ERR_PTR(-ENOMEM)
when the needed structures could not get allocated, and ERR_PTR(-EINTR)
when the worker was SIGKILLed.

.. _`kthread_queue_work`:

kthread_queue_work
==================

.. c:function:: bool kthread_queue_work(struct kthread_worker *worker, struct kthread_work *work)

    queue a kthread_work

    :param struct kthread_worker \*worker:
        target kthread_worker

    :param struct kthread_work \*work:
        kthread_work to queue

.. _`kthread_queue_work.description`:

Description
-----------

Queue \ ``work``\  to work processor \ ``task``\  for async execution.  \ ``task``\ 
must have been created with \ :c:func:`kthread_worker_create`\ .  Returns \ ``true``\ 
if \ ``work``\  was successfully queued, \ ``false``\  if it was already pending.

Reinitialize the work if it needs to be used by another worker.
For example, when the worker was stopped and started again.

.. _`kthread_delayed_work_timer_fn`:

kthread_delayed_work_timer_fn
=============================

.. c:function:: void kthread_delayed_work_timer_fn(struct timer_list *t)

    callback that queues the associated kthread delayed work when the timer expires.

    :param struct timer_list \*t:
        pointer to the expired timer

.. _`kthread_delayed_work_timer_fn.description`:

Description
-----------

The format of the function is defined by struct timer_list.
It should have been called from irqsafe timer with irq already off.

.. _`kthread_queue_delayed_work`:

kthread_queue_delayed_work
==========================

.. c:function:: bool kthread_queue_delayed_work(struct kthread_worker *worker, struct kthread_delayed_work *dwork, unsigned long delay)

    queue the associated kthread work after a delay.

    :param struct kthread_worker \*worker:
        target kthread_worker

    :param struct kthread_delayed_work \*dwork:
        kthread_delayed_work to queue

    :param unsigned long delay:
        number of jiffies to wait before queuing

.. _`kthread_queue_delayed_work.description`:

Description
-----------

If the work has not been pending it starts a timer that will queue
the work after the given \ ``delay``\ . If \ ``delay``\  is zero, it queues the
work immediately.

.. _`kthread_queue_delayed_work.return`:

Return
------

%false if the \ ``work``\  has already been pending. It means that
either the timer was running or the work was queued. It returns \ ``true``\ 
otherwise.

.. _`kthread_flush_work`:

kthread_flush_work
==================

.. c:function:: void kthread_flush_work(struct kthread_work *work)

    flush a kthread_work

    :param struct kthread_work \*work:
        work to flush

.. _`kthread_flush_work.description`:

Description
-----------

If \ ``work``\  is queued or executing, wait for it to finish execution.

.. _`kthread_mod_delayed_work`:

kthread_mod_delayed_work
========================

.. c:function:: bool kthread_mod_delayed_work(struct kthread_worker *worker, struct kthread_delayed_work *dwork, unsigned long delay)

    modify delay of or queue a kthread delayed work

    :param struct kthread_worker \*worker:
        kthread worker to use

    :param struct kthread_delayed_work \*dwork:
        kthread delayed work to queue

    :param unsigned long delay:
        number of jiffies to wait before queuing

.. _`kthread_mod_delayed_work.description`:

Description
-----------

If \ ``dwork``\  is idle, equivalent to \ :c:func:`kthread_queue_delayed_work`\ . Otherwise,
modify \ ``dwork``\ 's timer so that it expires after \ ``delay``\ . If \ ``delay``\  is zero,
\ ``work``\  is guaranteed to be queued immediately.

.. _`kthread_mod_delayed_work.return`:

Return
------

%true if \ ``dwork``\  was pending and its timer was modified,
\ ``false``\  otherwise.

A special case is when the work is being canceled in parallel.
It might be caused either by the real \ :c:func:`kthread_cancel_delayed_work_sync`\ 
or yet another \ :c:func:`kthread_mod_delayed_work`\  call. We let the other command
win and return \ ``false``\  here. The caller is supposed to synchronize these
operations a reasonable way.

This function is safe to call from any context including IRQ handler.
See \ :c:func:`__kthread_cancel_work`\  and \ :c:func:`kthread_delayed_work_timer_fn`\ 
for details.

.. _`kthread_cancel_work_sync`:

kthread_cancel_work_sync
========================

.. c:function:: bool kthread_cancel_work_sync(struct kthread_work *work)

    cancel a kthread work and wait for it to finish

    :param struct kthread_work \*work:
        the kthread work to cancel

.. _`kthread_cancel_work_sync.description`:

Description
-----------

Cancel \ ``work``\  and wait for its execution to finish.  This function
can be used even if the work re-queues itself. On return from this
function, \ ``work``\  is guaranteed to be not pending or executing on any CPU.

kthread_cancel_work_sync(&delayed_work->work) must not be used for
delayed_work's. Use \ :c:func:`kthread_cancel_delayed_work_sync`\  instead.

The caller must ensure that the worker on which \ ``work``\  was last
queued can't be destroyed before this function returns.

.. _`kthread_cancel_work_sync.return`:

Return
------

%true if \ ``work``\  was pending, \ ``false``\  otherwise.

.. _`kthread_cancel_delayed_work_sync`:

kthread_cancel_delayed_work_sync
================================

.. c:function:: bool kthread_cancel_delayed_work_sync(struct kthread_delayed_work *dwork)

    cancel a kthread delayed work and wait for it to finish.

    :param struct kthread_delayed_work \*dwork:
        the kthread delayed work to cancel

.. _`kthread_cancel_delayed_work_sync.description`:

Description
-----------

This is \ :c:func:`kthread_cancel_work_sync`\  for delayed works.

.. _`kthread_cancel_delayed_work_sync.return`:

Return
------

%true if \ ``dwork``\  was pending, \ ``false``\  otherwise.

.. _`kthread_flush_worker`:

kthread_flush_worker
====================

.. c:function:: void kthread_flush_worker(struct kthread_worker *worker)

    flush all current works on a kthread_worker

    :param struct kthread_worker \*worker:
        worker to flush

.. _`kthread_flush_worker.description`:

Description
-----------

Wait until all currently executing or pending works on \ ``worker``\  are
finished.

.. _`kthread_destroy_worker`:

kthread_destroy_worker
======================

.. c:function:: void kthread_destroy_worker(struct kthread_worker *worker)

    destroy a kthread worker

    :param struct kthread_worker \*worker:
        worker to be destroyed

.. _`kthread_destroy_worker.description`:

Description
-----------

Flush and destroy \ ``worker``\ .  The simple flush is enough because the kthread
worker API is used only in trivial scenarios.  There are no multi-step state
machines needed.

.. _`kthread_associate_blkcg`:

kthread_associate_blkcg
=======================

.. c:function:: void kthread_associate_blkcg(struct cgroup_subsys_state *css)

    associate blkcg to current kthread

    :param struct cgroup_subsys_state \*css:
        the cgroup info

.. _`kthread_associate_blkcg.description`:

Description
-----------

Current thread must be a kthread. The thread is running jobs on behalf of
other threads. In some cases, we expect the jobs attach cgroup info of
original threads instead of that of current thread. This function stores
original thread's cgroup info in current kthread context for later
retrieval.

.. _`kthread_blkcg`:

kthread_blkcg
=============

.. c:function:: struct cgroup_subsys_state *kthread_blkcg( void)

    get associated blkcg css of current kthread

    :param  void:
        no arguments

.. _`kthread_blkcg.description`:

Description
-----------

Current thread must be a kthread.

.. This file was automatic generated / don't edit.

