.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/workqueue.c

.. _`for_each_pool`:

for_each_pool
=============

.. c:function::  for_each_pool( pool,  pi)

    iterate through all worker_pools in the system

    :param  pool:
        iteration cursor

    :param  pi:
        integer used for iteration

.. _`for_each_pool.description`:

Description
-----------

This must be called either with wq_pool_mutex held or sched RCU read
locked.  If the pool needs to be used beyond the locking in effect, the
caller is responsible for guaranteeing that the pool stays online.

The if/else clause exists only for the lockdep assertion and can be
ignored.

.. _`for_each_pool_worker`:

for_each_pool_worker
====================

.. c:function::  for_each_pool_worker( worker,  pool)

    iterate through all workers of a worker_pool

    :param  worker:
        iteration cursor

    :param  pool:
        worker_pool to iterate workers of

.. _`for_each_pool_worker.description`:

Description
-----------

This must be called with \ ``pool``\ ->attach_mutex.

The if/else clause exists only for the lockdep assertion and can be
ignored.

.. _`for_each_pwq`:

for_each_pwq
============

.. c:function::  for_each_pwq( pwq,  wq)

    iterate through all pool_workqueues of the specified workqueue

    :param  pwq:
        iteration cursor

    :param  wq:
        the target workqueue

.. _`for_each_pwq.description`:

Description
-----------

This must be called either with wq->mutex held or sched RCU read locked.
If the pwq needs to be used beyond the locking in effect, the caller is
responsible for guaranteeing that the pwq stays online.

The if/else clause exists only for the lockdep assertion and can be
ignored.

.. _`worker_pool_assign_id`:

worker_pool_assign_id
=====================

.. c:function:: int worker_pool_assign_id(struct worker_pool *pool)

    allocate ID and assing it to \ ``pool``\ 

    :param struct worker_pool \*pool:
        the pool pointer of interest

.. _`worker_pool_assign_id.description`:

Description
-----------

Returns 0 if ID in [0, WORK_OFFQ_POOL_NONE) is allocated and assigned
successfully, -errno on failure.

.. _`unbound_pwq_by_node`:

unbound_pwq_by_node
===================

.. c:function:: struct pool_workqueue *unbound_pwq_by_node(struct workqueue_struct *wq, int node)

    return the unbound pool_workqueue for the given node

    :param struct workqueue_struct \*wq:
        the target workqueue

    :param int node:
        the node ID

.. _`unbound_pwq_by_node.description`:

Description
-----------

This must be called with any of wq_pool_mutex, wq->mutex or sched RCU
read locked.
If the pwq needs to be used beyond the locking in effect, the caller is
responsible for guaranteeing that the pwq stays online.

.. _`unbound_pwq_by_node.return`:

Return
------

The unbound pool_workqueue for \ ``node``\ .

.. _`get_work_pool`:

get_work_pool
=============

.. c:function:: struct worker_pool *get_work_pool(struct work_struct *work)

    return the worker_pool a given work was associated with

    :param struct work_struct \*work:
        the work item of interest

.. _`get_work_pool.description`:

Description
-----------

Pools are created and destroyed under wq_pool_mutex, and allows read
access under sched-RCU read lock.  As such, this function should be
called under wq_pool_mutex or with preemption disabled.

All fields of the returned pool are accessible as long as the above
mentioned locking is in effect.  If the returned pool needs to be used
beyond the critical section, the caller is responsible for ensuring the
returned pool is and stays online.

.. _`get_work_pool.return`:

Return
------

The worker_pool \ ``work``\  was last associated with.  \ ``NULL``\  if none.

.. _`get_work_pool_id`:

get_work_pool_id
================

.. c:function:: int get_work_pool_id(struct work_struct *work)

    return the worker pool ID a given work is associated with

    :param struct work_struct \*work:
        the work item of interest

.. _`get_work_pool_id.return`:

Return
------

The worker_pool ID \ ``work``\  was last associated with.
\ ``WORK_OFFQ_POOL_NONE``\  if none.

.. _`wake_up_worker`:

wake_up_worker
==============

.. c:function:: void wake_up_worker(struct worker_pool *pool)

    wake up an idle worker

    :param struct worker_pool \*pool:
        worker pool to wake worker from

.. _`wake_up_worker.description`:

Description
-----------

Wake up the first idle worker of \ ``pool``\ .

.. _`wake_up_worker.context`:

Context
-------

spin_lock_irq(pool->lock).

.. _`wq_worker_waking_up`:

wq_worker_waking_up
===================

.. c:function:: void wq_worker_waking_up(struct task_struct *task, int cpu)

    a worker is waking up

    :param struct task_struct \*task:
        task waking up

    :param int cpu:
        CPU \ ``task``\  is waking up to

.. _`wq_worker_waking_up.description`:

Description
-----------

This function is called during \ :c:func:`try_to_wake_up`\  when a worker is
being awoken.

.. _`wq_worker_waking_up.context`:

Context
-------

spin_lock_irq(rq->lock)

.. _`wq_worker_sleeping`:

wq_worker_sleeping
==================

.. c:function:: struct task_struct *wq_worker_sleeping(struct task_struct *task)

    a worker is going to sleep

    :param struct task_struct \*task:
        task going to sleep

.. _`wq_worker_sleeping.description`:

Description
-----------

This function is called during \ :c:func:`schedule`\  when a busy worker is
going to sleep.  Worker on the same cpu can be woken up by
returning pointer to its task.

.. _`wq_worker_sleeping.context`:

Context
-------

spin_lock_irq(rq->lock)

.. _`wq_worker_sleeping.return`:

Return
------

Worker task on \ ``cpu``\  to wake up, \ ``NULL``\  if none.

.. _`worker_set_flags`:

worker_set_flags
================

.. c:function:: void worker_set_flags(struct worker *worker, unsigned int flags)

    set worker flags and adjust nr_running accordingly

    :param struct worker \*worker:
        self

    :param unsigned int flags:
        flags to set

.. _`worker_set_flags.description`:

Description
-----------

Set \ ``flags``\  in \ ``worker``\ ->flags and adjust nr_running accordingly.

.. _`worker_set_flags.context`:

Context
-------

spin_lock_irq(pool->lock)

.. _`worker_clr_flags`:

worker_clr_flags
================

.. c:function:: void worker_clr_flags(struct worker *worker, unsigned int flags)

    clear worker flags and adjust nr_running accordingly

    :param struct worker \*worker:
        self

    :param unsigned int flags:
        flags to clear

.. _`worker_clr_flags.description`:

Description
-----------

Clear \ ``flags``\  in \ ``worker``\ ->flags and adjust nr_running accordingly.

.. _`worker_clr_flags.context`:

Context
-------

spin_lock_irq(pool->lock)

.. _`find_worker_executing_work`:

find_worker_executing_work
==========================

.. c:function:: struct worker *find_worker_executing_work(struct worker_pool *pool, struct work_struct *work)

    find worker which is executing a work

    :param struct worker_pool \*pool:
        pool of interest

    :param struct work_struct \*work:
        work to find worker for

.. _`find_worker_executing_work.description`:

Description
-----------

Find a worker which is executing \ ``work``\  on \ ``pool``\  by searching
\ ``pool``\ ->busy_hash which is keyed by the address of \ ``work``\ .  For a worker
to match, its current execution should match the address of \ ``work``\  and
its work function.  This is to avoid unwanted dependency between
unrelated work executions through a work item being recycled while still
being executed.

This is a bit tricky.  A work item may be freed once its execution
starts and nothing prevents the freed area from being recycled for
another work item.  If the same work item address ends up being reused
before the original execution finishes, workqueue will identify the
recycled work item as currently executing and make it wait until the
current execution finishes, introducing an unwanted dependency.

This function checks the work item address and work function to avoid
false positives.  Note that this isn't complete as one may construct a
work function which can introduce dependency onto itself through a
recycled work item.  Well, if somebody wants to shoot oneself in the
foot that badly, there's only so much we can do, and if such deadlock
actually occurs, it should be easy to locate the culprit work function.

.. _`find_worker_executing_work.context`:

Context
-------

spin_lock_irq(pool->lock).

.. _`find_worker_executing_work.return`:

Return
------

Pointer to worker which is executing \ ``work``\  if found, \ ``NULL``\ 
otherwise.

.. _`move_linked_works`:

move_linked_works
=================

.. c:function:: void move_linked_works(struct work_struct *work, struct list_head *head, struct work_struct **nextp)

    move linked works to a list

    :param struct work_struct \*work:
        start of series of works to be scheduled

    :param struct list_head \*head:
        target list to append \ ``work``\  to

    :param struct work_struct \*\*nextp:
        out parameter for nested worklist walking

.. _`move_linked_works.description`:

Description
-----------

Schedule linked works starting from \ ``work``\  to \ ``head``\ .  Work series to
be scheduled starts at \ ``work``\  and includes any consecutive work with
WORK_STRUCT_LINKED set in its predecessor.

If \ ``nextp``\  is not NULL, it's updated to point to the next work of
the last scheduled work.  This allows \ :c:func:`move_linked_works`\  to be
nested inside outer \ :c:func:`list_for_each_entry_safe`\ .

.. _`move_linked_works.context`:

Context
-------

spin_lock_irq(pool->lock).

.. _`get_pwq`:

get_pwq
=======

.. c:function:: void get_pwq(struct pool_workqueue *pwq)

    get an extra reference on the specified pool_workqueue

    :param struct pool_workqueue \*pwq:
        pool_workqueue to get

.. _`get_pwq.description`:

Description
-----------

Obtain an extra reference on \ ``pwq``\ .  The caller should guarantee that
\ ``pwq``\  has positive refcnt and be holding the matching pool->lock.

.. _`put_pwq`:

put_pwq
=======

.. c:function:: void put_pwq(struct pool_workqueue *pwq)

    put a pool_workqueue reference

    :param struct pool_workqueue \*pwq:
        pool_workqueue to put

.. _`put_pwq.description`:

Description
-----------

Drop a reference of \ ``pwq``\ .  If its refcnt reaches zero, schedule its
destruction.  The caller should be holding the matching pool->lock.

.. _`put_pwq_unlocked`:

put_pwq_unlocked
================

.. c:function:: void put_pwq_unlocked(struct pool_workqueue *pwq)

    put_pwq() with surrounding pool lock/unlock

    :param struct pool_workqueue \*pwq:
        pool_workqueue to put (can be \ ``NULL``\ )

.. _`put_pwq_unlocked.description`:

Description
-----------

put_pwq() with locking.  This function also allows \ ``NULL``\  \ ``pwq``\ .

.. _`pwq_dec_nr_in_flight`:

pwq_dec_nr_in_flight
====================

.. c:function:: void pwq_dec_nr_in_flight(struct pool_workqueue *pwq, int color)

    decrement pwq's nr_in_flight

    :param struct pool_workqueue \*pwq:
        pwq of interest

    :param int color:
        color of work which left the queue

.. _`pwq_dec_nr_in_flight.description`:

Description
-----------

A work either has completed or is removed from pending queue,
decrement nr_in_flight of its pwq and handle workqueue flushing.

.. _`pwq_dec_nr_in_flight.context`:

Context
-------

spin_lock_irq(pool->lock).

.. _`try_to_grab_pending`:

try_to_grab_pending
===================

.. c:function:: int try_to_grab_pending(struct work_struct *work, bool is_dwork, unsigned long *flags)

    steal work item from worklist and disable irq

    :param struct work_struct \*work:
        work item to steal

    :param bool is_dwork:
        @work is a delayed_work

    :param unsigned long \*flags:
        place to store irq state

.. _`try_to_grab_pending.description`:

Description
-----------

Try to grab PENDING bit of \ ``work``\ .  This function can handle \ ``work``\  in any
stable state - idle, on timer or on worklist.

.. _`try_to_grab_pending.return`:

Return
------

 1           if \ ``work``\  was pending and we successfully stole PENDING
 0           if \ ``work``\  was idle and we claimed PENDING
 -EAGAIN     if PENDING couldn't be grabbed at the moment, safe to busy-retry
 -ENOENT     if someone else is canceling \ ``work``\ , this state may persist
             for arbitrarily long

.. _`try_to_grab_pending.note`:

Note
----

On >= 0 return, the caller owns \ ``work``\ 's PENDING bit.  To avoid getting
interrupted while holding PENDING and \ ``work``\  off queue, irq must be
disabled on entry.  This, combined with delayed_work->timer being
irqsafe, ensures that we return -EAGAIN for finite short period of time.

On successful return, >= 0, irq is disabled and the caller is
responsible for releasing it using local_irq_restore(*@flags).

This function is safe to call from any context including IRQ handler.

.. _`insert_work`:

insert_work
===========

.. c:function:: void insert_work(struct pool_workqueue *pwq, struct work_struct *work, struct list_head *head, unsigned int extra_flags)

    insert a work into a pool

    :param struct pool_workqueue \*pwq:
        pwq \ ``work``\  belongs to

    :param struct work_struct \*work:
        work to insert

    :param struct list_head \*head:
        insertion point

    :param unsigned int extra_flags:
        extra WORK_STRUCT_* flags to set

.. _`insert_work.description`:

Description
-----------

Insert \ ``work``\  which belongs to \ ``pwq``\  after \ ``head``\ .  \ ``extra_flags``\  is or'd to
work_struct flags.

.. _`insert_work.context`:

Context
-------

spin_lock_irq(pool->lock).

.. _`queue_work_on`:

queue_work_on
=============

.. c:function:: bool queue_work_on(int cpu, struct workqueue_struct *wq, struct work_struct *work)

    queue work on specific cpu

    :param int cpu:
        CPU number to execute work on

    :param struct workqueue_struct \*wq:
        workqueue to use

    :param struct work_struct \*work:
        work to queue

.. _`queue_work_on.description`:

Description
-----------

We queue the work to a specific CPU, the caller must ensure it
can't go away.

.. _`queue_work_on.return`:

Return
------

%false if \ ``work``\  was already on a queue, \ ``true``\  otherwise.

.. _`queue_delayed_work_on`:

queue_delayed_work_on
=====================

.. c:function:: bool queue_delayed_work_on(int cpu, struct workqueue_struct *wq, struct delayed_work *dwork, unsigned long delay)

    queue work on specific CPU after delay

    :param int cpu:
        CPU number to execute work on

    :param struct workqueue_struct \*wq:
        workqueue to use

    :param struct delayed_work \*dwork:
        work to queue

    :param unsigned long delay:
        number of jiffies to wait before queueing

.. _`queue_delayed_work_on.return`:

Return
------

%false if \ ``work``\  was already on a queue, \ ``true``\  otherwise.  If
\ ``delay``\  is zero and \ ``dwork``\  is idle, it will be scheduled for immediate
execution.

.. _`mod_delayed_work_on`:

mod_delayed_work_on
===================

.. c:function:: bool mod_delayed_work_on(int cpu, struct workqueue_struct *wq, struct delayed_work *dwork, unsigned long delay)

    modify delay of or queue a delayed work on specific CPU

    :param int cpu:
        CPU number to execute work on

    :param struct workqueue_struct \*wq:
        workqueue to use

    :param struct delayed_work \*dwork:
        work to queue

    :param unsigned long delay:
        number of jiffies to wait before queueing

.. _`mod_delayed_work_on.description`:

Description
-----------

If \ ``dwork``\  is idle, equivalent to \ :c:func:`queue_delayed_work_on`\ ; otherwise,
modify \ ``dwork``\ 's timer so that it expires after \ ``delay``\ .  If \ ``delay``\  is
zero, \ ``work``\  is guaranteed to be scheduled immediately regardless of its
current state.

.. _`mod_delayed_work_on.return`:

Return
------

%false if \ ``dwork``\  was idle and queued, \ ``true``\  if \ ``dwork``\  was
pending and its timer was modified.

This function is safe to call from any context including IRQ handler.
See \ :c:func:`try_to_grab_pending`\  for details.

.. _`worker_enter_idle`:

worker_enter_idle
=================

.. c:function:: void worker_enter_idle(struct worker *worker)

    enter idle state

    :param struct worker \*worker:
        worker which is entering idle state

.. _`worker_enter_idle.description`:

Description
-----------

@worker is entering idle state.  Update stats and idle timer if
necessary.

.. _`worker_enter_idle.locking`:

LOCKING
-------

spin_lock_irq(pool->lock).

.. _`worker_leave_idle`:

worker_leave_idle
=================

.. c:function:: void worker_leave_idle(struct worker *worker)

    leave idle state

    :param struct worker \*worker:
        worker which is leaving idle state

.. _`worker_leave_idle.description`:

Description
-----------

@worker is leaving idle state.  Update stats.

.. _`worker_leave_idle.locking`:

LOCKING
-------

spin_lock_irq(pool->lock).

.. _`worker_attach_to_pool`:

worker_attach_to_pool
=====================

.. c:function:: void worker_attach_to_pool(struct worker *worker, struct worker_pool *pool)

    attach a worker to a pool

    :param struct worker \*worker:
        worker to be attached

    :param struct worker_pool \*pool:
        the target pool

.. _`worker_attach_to_pool.description`:

Description
-----------

Attach \ ``worker``\  to \ ``pool``\ .  Once attached, the \ ``WORKER_UNBOUND``\  flag and
cpu-binding of \ ``worker``\  are kept coordinated with the pool across
cpu-[un]hotplugs.

.. _`worker_detach_from_pool`:

worker_detach_from_pool
=======================

.. c:function:: void worker_detach_from_pool(struct worker *worker, struct worker_pool *pool)

    detach a worker from its pool

    :param struct worker \*worker:
        worker which is attached to its pool

    :param struct worker_pool \*pool:
        the pool \ ``worker``\  is attached to

.. _`worker_detach_from_pool.description`:

Description
-----------

Undo the attaching which had been done in \ :c:func:`worker_attach_to_pool`\ .  The
caller worker shouldn't access to the pool after detached except it has
other reference to the pool.

.. _`create_worker`:

create_worker
=============

.. c:function:: struct worker *create_worker(struct worker_pool *pool)

    create a new workqueue worker

    :param struct worker_pool \*pool:
        pool the new worker will belong to

.. _`create_worker.description`:

Description
-----------

Create and start a new worker which is attached to \ ``pool``\ .

.. _`create_worker.context`:

Context
-------

Might sleep.  Does GFP_KERNEL allocations.

.. _`create_worker.return`:

Return
------

Pointer to the newly created worker.

.. _`destroy_worker`:

destroy_worker
==============

.. c:function:: void destroy_worker(struct worker *worker)

    destroy a workqueue worker

    :param struct worker \*worker:
        worker to be destroyed

.. _`destroy_worker.description`:

Description
-----------

Destroy \ ``worker``\  and adjust \ ``pool``\  stats accordingly.  The worker should
be idle.

.. _`destroy_worker.context`:

Context
-------

spin_lock_irq(pool->lock).

.. _`maybe_create_worker`:

maybe_create_worker
===================

.. c:function:: void maybe_create_worker(struct worker_pool *pool)

    create a new worker if necessary

    :param struct worker_pool \*pool:
        pool to create a new worker for

.. _`maybe_create_worker.description`:

Description
-----------

Create a new worker for \ ``pool``\  if necessary.  \ ``pool``\  is guaranteed to
have at least one idle worker on return from this function.  If
creating a new worker takes longer than MAYDAY_INTERVAL, mayday is
sent to all rescuers with works scheduled on \ ``pool``\  to resolve
possible allocation deadlock.

On return, \ :c:func:`need_to_create_worker`\  is guaranteed to be \ ``false``\  and
\ :c:func:`may_start_working`\  \ ``true``\ .

.. _`maybe_create_worker.locking`:

LOCKING
-------

spin_lock_irq(pool->lock) which may be released and regrabbed
multiple times.  Does GFP_KERNEL allocations.  Called only from
manager.

.. _`manage_workers`:

manage_workers
==============

.. c:function:: bool manage_workers(struct worker *worker)

    manage worker pool

    :param struct worker \*worker:
        self

.. _`manage_workers.description`:

Description
-----------

Assume the manager role and manage the worker pool \ ``worker``\  belongs
to.  At any given time, there can be only zero or one manager per
pool.  The exclusion is handled automatically by this function.

The caller can safely start processing works on false return.  On
true return, it's guaranteed that \ :c:func:`need_to_create_worker`\  is false
and \ :c:func:`may_start_working`\  is true.

.. _`manage_workers.context`:

Context
-------

spin_lock_irq(pool->lock) which may be released and regrabbed
multiple times.  Does GFP_KERNEL allocations.

.. _`manage_workers.return`:

Return
------

%false if the pool doesn't need management and the caller can safely
start processing works, \ ``true``\  if management function was performed and
the conditions that the caller verified before calling the function may
no longer be true.

.. _`process_one_work`:

process_one_work
================

.. c:function:: void process_one_work(struct worker *worker, struct work_struct *work)

    process single work

    :param struct worker \*worker:
        self

    :param struct work_struct \*work:
        work to process

.. _`process_one_work.description`:

Description
-----------

Process \ ``work``\ .  This function contains all the logics necessary to
process a single work including synchronization against and
interaction with other workers on the same cpu, queueing and
flushing.  As long as context requirement is met, any worker can
call this function to process a work.

.. _`process_one_work.context`:

Context
-------

spin_lock_irq(pool->lock) which is released and regrabbed.

.. _`process_scheduled_works`:

process_scheduled_works
=======================

.. c:function:: void process_scheduled_works(struct worker *worker)

    process scheduled works

    :param struct worker \*worker:
        self

.. _`process_scheduled_works.description`:

Description
-----------

Process all scheduled works.  Please note that the scheduled list
may change while processing a work, so this function repeatedly
fetches a work from the top and executes it.

.. _`process_scheduled_works.context`:

Context
-------

spin_lock_irq(pool->lock) which may be released and regrabbed
multiple times.

.. _`worker_thread`:

worker_thread
=============

.. c:function:: int worker_thread(void *__worker)

    the worker thread function

    :param void \*__worker:
        self

.. _`worker_thread.description`:

Description
-----------

The worker thread function.  All workers belong to a worker_pool -
either a per-cpu one or dynamic unbound one.  These workers process all
work items regardless of their specific target workqueue.  The only
exception is work items which belong to workqueues with a rescuer which
will be explained in \ :c:func:`rescuer_thread`\ .

.. _`worker_thread.return`:

Return
------

0

.. _`rescuer_thread`:

rescuer_thread
==============

.. c:function:: int rescuer_thread(void *__rescuer)

    the rescuer thread function

    :param void \*__rescuer:
        self

.. _`rescuer_thread.description`:

Description
-----------

Workqueue rescuer thread function.  There's one rescuer for each
workqueue which has WQ_MEM_RECLAIM set.

Regular work processing on a pool may block trying to create a new
worker which uses GFP_KERNEL allocation which has slight chance of
developing into deadlock if some works currently on the same queue
need to be processed to satisfy the GFP_KERNEL allocation.  This is
the problem rescuer solves.

When such condition is possible, the pool summons rescuers of all
workqueues which have works queued on the pool and let them process
those works so that forward progress can be guaranteed.

This should happen rarely.

.. _`rescuer_thread.return`:

Return
------

0

.. _`check_flush_dependency`:

check_flush_dependency
======================

.. c:function:: void check_flush_dependency(struct workqueue_struct *target_wq, struct work_struct *target_work)

    check for flush dependency sanity

    :param struct workqueue_struct \*target_wq:
        workqueue being flushed

    :param struct work_struct \*target_work:
        work item being flushed (NULL for workqueue flushes)

.. _`check_flush_dependency.description`:

Description
-----------

%current is trying to flush the whole \ ``target_wq``\  or \ ``target_work``\  on it.
If \ ``target_wq``\  doesn't have \ ``WQ_MEM_RECLAIM``\ , verify that \ ``current``\  is not
reclaiming memory or running on a workqueue which doesn't have
\ ``WQ_MEM_RECLAIM``\  as that can break forward-progress guarantee leading to
a deadlock.

.. _`insert_wq_barrier`:

insert_wq_barrier
=================

.. c:function:: void insert_wq_barrier(struct pool_workqueue *pwq, struct wq_barrier *barr, struct work_struct *target, struct worker *worker)

    insert a barrier work

    :param struct pool_workqueue \*pwq:
        pwq to insert barrier into

    :param struct wq_barrier \*barr:
        wq_barrier to insert

    :param struct work_struct \*target:
        target work to attach \ ``barr``\  to

    :param struct worker \*worker:
        worker currently executing \ ``target``\ , NULL if \ ``target``\  is not executing

.. _`insert_wq_barrier.description`:

Description
-----------

@barr is linked to \ ``target``\  such that \ ``barr``\  is completed only after
\ ``target``\  finishes execution.  Please note that the ordering
guarantee is observed only with respect to \ ``target``\  and on the local
cpu.

Currently, a queued barrier can't be canceled.  This is because
\ :c:func:`try_to_grab_pending`\  can't determine whether the work to be
grabbed is at the head of the queue and thus can't clear LINKED
flag of the previous work while there must be a valid next work
after a work with LINKED flag set.

Note that when \ ``worker``\  is non-NULL, \ ``target``\  may be modified
underneath us, so we can't reliably determine pwq from \ ``target``\ .

.. _`insert_wq_barrier.context`:

Context
-------

spin_lock_irq(pool->lock).

.. _`flush_workqueue_prep_pwqs`:

flush_workqueue_prep_pwqs
=========================

.. c:function:: bool flush_workqueue_prep_pwqs(struct workqueue_struct *wq, int flush_color, int work_color)

    prepare pwqs for workqueue flushing

    :param struct workqueue_struct \*wq:
        workqueue being flushed

    :param int flush_color:
        new flush color, < 0 for no-op

    :param int work_color:
        new work color, < 0 for no-op

.. _`flush_workqueue_prep_pwqs.description`:

Description
-----------

Prepare pwqs for workqueue flushing.

If \ ``flush_color``\  is non-negative, flush_color on all pwqs should be
-1.  If no pwq has in-flight commands at the specified color, all
pwq->flush_color's stay at -1 and \ ``false``\  is returned.  If any pwq
has in flight commands, its pwq->flush_color is set to
\ ``flush_color``\ , \ ``wq``\ ->nr_pwqs_to_flush is updated accordingly, pwq
wakeup logic is armed and \ ``true``\  is returned.

The caller should have initialized \ ``wq``\ ->first_flusher prior to
calling this function with non-negative \ ``flush_color``\ .  If
\ ``flush_color``\  is negative, no flush color update is done and \ ``false``\ 
is returned.

If \ ``work_color``\  is non-negative, all pwqs should have the same
work_color which is previous to \ ``work_color``\  and all will be
advanced to \ ``work_color``\ .

.. _`flush_workqueue_prep_pwqs.context`:

Context
-------

mutex_lock(wq->mutex).

.. _`flush_workqueue_prep_pwqs.return`:

Return
------

%true if \ ``flush_color``\  >= 0 and there's something to flush.  \ ``false``\ 
otherwise.

.. _`flush_workqueue`:

flush_workqueue
===============

.. c:function:: void flush_workqueue(struct workqueue_struct *wq)

    ensure that any scheduled work has run to completion.

    :param struct workqueue_struct \*wq:
        workqueue to flush

.. _`flush_workqueue.description`:

Description
-----------

This function sleeps until all work items which were queued on entry
have finished execution, but it is not livelocked by new incoming ones.

.. _`drain_workqueue`:

drain_workqueue
===============

.. c:function:: void drain_workqueue(struct workqueue_struct *wq)

    drain a workqueue

    :param struct workqueue_struct \*wq:
        workqueue to drain

.. _`drain_workqueue.description`:

Description
-----------

Wait until the workqueue becomes empty.  While draining is in progress,
only chain queueing is allowed.  IOW, only currently pending or running
work items on \ ``wq``\  can queue further work items on it.  \ ``wq``\  is flushed
repeatedly until it becomes empty.  The number of flushing is determined
by the depth of chaining and should be relatively short.  Whine if it
takes too long.

.. _`flush_work`:

flush_work
==========

.. c:function:: bool flush_work(struct work_struct *work)

    wait for a work to finish executing the last queueing instance

    :param struct work_struct \*work:
        the work to flush

.. _`flush_work.description`:

Description
-----------

Wait until \ ``work``\  has finished execution.  \ ``work``\  is guaranteed to be idle
on return if it hasn't been requeued since flush started.

.. _`flush_work.return`:

Return
------

%true if \ :c:func:`flush_work`\  waited for the work to finish execution,
\ ``false``\  if it was already idle.

.. _`cancel_work_sync`:

cancel_work_sync
================

.. c:function:: bool cancel_work_sync(struct work_struct *work)

    cancel a work and wait for it to finish

    :param struct work_struct \*work:
        the work to cancel

.. _`cancel_work_sync.description`:

Description
-----------

Cancel \ ``work``\  and wait for its execution to finish.  This function
can be used even if the work re-queues itself or migrates to
another workqueue.  On return from this function, \ ``work``\  is
guaranteed to be not pending or executing on any CPU.

cancel_work_sync(&delayed_work->work) must not be used for
delayed_work's.  Use \ :c:func:`cancel_delayed_work_sync`\  instead.

The caller must ensure that the workqueue on which \ ``work``\  was last
queued can't be destroyed before this function returns.

.. _`cancel_work_sync.return`:

Return
------

%true if \ ``work``\  was pending, \ ``false``\  otherwise.

.. _`flush_delayed_work`:

flush_delayed_work
==================

.. c:function:: bool flush_delayed_work(struct delayed_work *dwork)

    wait for a dwork to finish executing the last queueing

    :param struct delayed_work \*dwork:
        the delayed work to flush

.. _`flush_delayed_work.description`:

Description
-----------

Delayed timer is cancelled and the pending work is queued for
immediate execution.  Like \ :c:func:`flush_work`\ , this function only
considers the last queueing instance of \ ``dwork``\ .

.. _`flush_delayed_work.return`:

Return
------

%true if \ :c:func:`flush_work`\  waited for the work to finish execution,
\ ``false``\  if it was already idle.

.. _`cancel_delayed_work`:

cancel_delayed_work
===================

.. c:function:: bool cancel_delayed_work(struct delayed_work *dwork)

    cancel a delayed work

    :param struct delayed_work \*dwork:
        delayed_work to cancel

.. _`cancel_delayed_work.description`:

Description
-----------

Kill off a pending delayed_work.

.. _`cancel_delayed_work.return`:

Return
------

%true if \ ``dwork``\  was pending and canceled; \ ``false``\  if it wasn't
pending.

.. _`cancel_delayed_work.note`:

Note
----

The work callback function may still be running on return, unless
it returns \ ``true``\  and the work doesn't re-arm itself.  Explicitly flush or
use \ :c:func:`cancel_delayed_work_sync`\  to wait on it.

This function is safe to call from any context including IRQ handler.

.. _`cancel_delayed_work_sync`:

cancel_delayed_work_sync
========================

.. c:function:: bool cancel_delayed_work_sync(struct delayed_work *dwork)

    cancel a delayed work and wait for it to finish

    :param struct delayed_work \*dwork:
        the delayed work cancel

.. _`cancel_delayed_work_sync.description`:

Description
-----------

This is \ :c:func:`cancel_work_sync`\  for delayed works.

.. _`cancel_delayed_work_sync.return`:

Return
------

%true if \ ``dwork``\  was pending, \ ``false``\  otherwise.

.. _`schedule_on_each_cpu`:

schedule_on_each_cpu
====================

.. c:function:: int schedule_on_each_cpu(work_func_t func)

    execute a function synchronously on each online CPU

    :param work_func_t func:
        the function to call

.. _`schedule_on_each_cpu.description`:

Description
-----------

schedule_on_each_cpu() executes \ ``func``\  on each online CPU using the
system workqueue and blocks until all CPUs have completed.
\ :c:func:`schedule_on_each_cpu`\  is very slow.

.. _`schedule_on_each_cpu.return`:

Return
------

0 on success, -errno on failure.

.. _`execute_in_process_context`:

execute_in_process_context
==========================

.. c:function:: int execute_in_process_context(work_func_t fn, struct execute_work *ew)

    reliably execute the routine with user context

    :param work_func_t fn:
        the function to execute

    :param struct execute_work \*ew:
        guaranteed storage for the execute work structure (must
        be available when the work executes)

.. _`execute_in_process_context.description`:

Description
-----------

Executes the function immediately if process context is available,
otherwise schedules the function for delayed execution.

.. _`execute_in_process_context.return`:

Return
------

0 - function was executed
             1 - function was scheduled for execution

.. _`free_workqueue_attrs`:

free_workqueue_attrs
====================

.. c:function:: void free_workqueue_attrs(struct workqueue_attrs *attrs)

    free a workqueue_attrs

    :param struct workqueue_attrs \*attrs:
        workqueue_attrs to free

.. _`free_workqueue_attrs.description`:

Description
-----------

Undo \ :c:func:`alloc_workqueue_attrs`\ .

.. _`alloc_workqueue_attrs`:

alloc_workqueue_attrs
=====================

.. c:function:: struct workqueue_attrs *alloc_workqueue_attrs(gfp_t gfp_mask)

    allocate a workqueue_attrs

    :param gfp_t gfp_mask:
        allocation mask to use

.. _`alloc_workqueue_attrs.description`:

Description
-----------

Allocate a new workqueue_attrs, initialize with default settings and
return it.

.. _`alloc_workqueue_attrs.return`:

Return
------

The allocated new workqueue_attr on success. \ ``NULL``\  on failure.

.. _`init_worker_pool`:

init_worker_pool
================

.. c:function:: int init_worker_pool(struct worker_pool *pool)

    initialize a newly zalloc'd worker_pool

    :param struct worker_pool \*pool:
        worker_pool to initialize

.. _`init_worker_pool.description`:

Description
-----------

Initialize a newly zalloc'd \ ``pool``\ .  It also allocates \ ``pool``\ ->attrs.

.. _`init_worker_pool.return`:

Return
------

0 on success, -errno on failure.  Even on failure, all fields
inside \ ``pool``\  proper are initialized and \ :c:func:`put_unbound_pool`\  can be called
on \ ``pool``\  safely to release it.

.. _`put_unbound_pool`:

put_unbound_pool
================

.. c:function:: void put_unbound_pool(struct worker_pool *pool)

    put a worker_pool

    :param struct worker_pool \*pool:
        worker_pool to put

.. _`put_unbound_pool.description`:

Description
-----------

Put \ ``pool``\ .  If its refcnt reaches zero, it gets destroyed in sched-RCU
safe manner.  \ :c:func:`get_unbound_pool`\  calls this function on its failure path
and this function should be able to release pools which went through,
successfully or not, \ :c:func:`init_worker_pool`\ .

Should be called with wq_pool_mutex held.

.. _`get_unbound_pool`:

get_unbound_pool
================

.. c:function:: struct worker_pool *get_unbound_pool(const struct workqueue_attrs *attrs)

    get a worker_pool with the specified attributes

    :param const struct workqueue_attrs \*attrs:
        the attributes of the worker_pool to get

.. _`get_unbound_pool.description`:

Description
-----------

Obtain a worker_pool which has the same attributes as \ ``attrs``\ , bump the
reference count and return it.  If there already is a matching
worker_pool, it will be used; otherwise, this function attempts to
create a new one.

Should be called with wq_pool_mutex held.

.. _`get_unbound_pool.return`:

Return
------

On success, a worker_pool with the same attributes as \ ``attrs``\ .
On failure, \ ``NULL``\ .

.. _`pwq_adjust_max_active`:

pwq_adjust_max_active
=====================

.. c:function:: void pwq_adjust_max_active(struct pool_workqueue *pwq)

    update a pwq's max_active to the current setting

    :param struct pool_workqueue \*pwq:
        target pool_workqueue

.. _`pwq_adjust_max_active.description`:

Description
-----------

If \ ``pwq``\  isn't freezing, set \ ``pwq``\ ->max_active to the associated
workqueue's saved_max_active and activate delayed work items
accordingly.  If \ ``pwq``\  is freezing, clear \ ``pwq``\ ->max_active to zero.

.. _`wq_calc_node_cpumask`:

wq_calc_node_cpumask
====================

.. c:function:: bool wq_calc_node_cpumask(const struct workqueue_attrs *attrs, int node, int cpu_going_down, cpumask_t *cpumask)

    calculate a wq_attrs' cpumask for the specified node

    :param const struct workqueue_attrs \*attrs:
        the wq_attrs of the default pwq of the target workqueue

    :param int node:
        the target NUMA node

    :param int cpu_going_down:
        if >= 0, the CPU to consider as offline

    :param cpumask_t \*cpumask:
        outarg, the resulting cpumask

.. _`wq_calc_node_cpumask.description`:

Description
-----------

Calculate the cpumask a workqueue with \ ``attrs``\  should use on \ ``node``\ .  If
\ ``cpu_going_down``\  is >= 0, that cpu is considered offline during
calculation.  The result is stored in \ ``cpumask``\ .

If NUMA affinity is not enabled, \ ``attrs``\ ->cpumask is always used.  If
enabled and \ ``node``\  has online CPUs requested by \ ``attrs``\ , the returned
cpumask is the intersection of the possible CPUs of \ ``node``\  and
\ ``attrs``\ ->cpumask.

The caller is responsible for ensuring that the cpumask of \ ``node``\  stays
stable.

.. _`wq_calc_node_cpumask.return`:

Return
------

%true if the resulting \ ``cpumask``\  is different from \ ``attrs``\ ->cpumask,
\ ``false``\  if equal.

.. _`apply_workqueue_attrs`:

apply_workqueue_attrs
=====================

.. c:function:: int apply_workqueue_attrs(struct workqueue_struct *wq, const struct workqueue_attrs *attrs)

    apply new workqueue_attrs to an unbound workqueue

    :param struct workqueue_struct \*wq:
        the target workqueue

    :param const struct workqueue_attrs \*attrs:
        the workqueue_attrs to apply, allocated with \ :c:func:`alloc_workqueue_attrs`\ 

.. _`apply_workqueue_attrs.description`:

Description
-----------

Apply \ ``attrs``\  to an unbound workqueue \ ``wq``\ .  Unless disabled, on NUMA
machines, this function maps a separate pwq to each NUMA node with
possibles CPUs in \ ``attrs``\ ->cpumask so that work items are affine to the
NUMA node it was issued on.  Older pwqs are released as in-flight work
items finish.  Note that a work item which repeatedly requeues itself
back-to-back will stay on its current pwq.

Performs GFP_KERNEL allocations.

.. _`apply_workqueue_attrs.return`:

Return
------

0 on success and -errno on failure.

.. _`wq_update_unbound_numa`:

wq_update_unbound_numa
======================

.. c:function:: void wq_update_unbound_numa(struct workqueue_struct *wq, int cpu, bool online)

    update NUMA affinity of a wq for CPU hot[un]plug

    :param struct workqueue_struct \*wq:
        the target workqueue

    :param int cpu:
        the CPU coming up or going down

    :param bool online:
        whether \ ``cpu``\  is coming up or going down

.. _`wq_update_unbound_numa.description`:

Description
-----------

This function is to be called from \ ``CPU_DOWN_PREPARE``\ , \ ``CPU_ONLINE``\  and
\ ``CPU_DOWN_FAILED``\ .  \ ``cpu``\  is being hot[un]plugged, update NUMA affinity of
\ ``wq``\  accordingly.

If NUMA affinity can't be adjusted due to memory allocation failure, it
falls back to \ ``wq``\ ->dfl_pwq which may not be optimal but is always
correct.

Note that when the last allowed CPU of a NUMA node goes offline for a
workqueue with a cpumask spanning multiple nodes, the workers which were
already executing the work items for the workqueue will lose their CPU
affinity and may execute on any CPU.  This is similar to how per-cpu
workqueues behave on CPU_DOWN.  If a workqueue user wants strict
affinity, it's the user's responsibility to flush the work item from
CPU_DOWN_PREPARE.

.. _`destroy_workqueue`:

destroy_workqueue
=================

.. c:function:: void destroy_workqueue(struct workqueue_struct *wq)

    safely terminate a workqueue

    :param struct workqueue_struct \*wq:
        target workqueue

.. _`destroy_workqueue.description`:

Description
-----------

Safely destroy a workqueue. All work currently pending will be done first.

.. _`workqueue_set_max_active`:

workqueue_set_max_active
========================

.. c:function:: void workqueue_set_max_active(struct workqueue_struct *wq, int max_active)

    adjust max_active of a workqueue

    :param struct workqueue_struct \*wq:
        target workqueue

    :param int max_active:
        new max_active value.

.. _`workqueue_set_max_active.description`:

Description
-----------

Set max_active of \ ``wq``\  to \ ``max_active``\ .

.. _`workqueue_set_max_active.context`:

Context
-------

Don't call from IRQ context.

.. _`current_is_workqueue_rescuer`:

current_is_workqueue_rescuer
============================

.. c:function:: bool current_is_workqueue_rescuer( void)

    is \ ``current``\  workqueue rescuer?

    :param  void:
        no arguments

.. _`current_is_workqueue_rescuer.description`:

Description
-----------

Determine whether \ ``current``\  is a workqueue rescuer.  Can be used from
work functions to determine whether it's being run off the rescuer task.

.. _`current_is_workqueue_rescuer.return`:

Return
------

%true if \ ``current``\  is a workqueue rescuer. \ ``false``\  otherwise.

.. _`workqueue_congested`:

workqueue_congested
===================

.. c:function:: bool workqueue_congested(int cpu, struct workqueue_struct *wq)

    test whether a workqueue is congested

    :param int cpu:
        CPU in question

    :param struct workqueue_struct \*wq:
        target workqueue

.. _`workqueue_congested.description`:

Description
-----------

Test whether \ ``wq``\ 's cpu workqueue for \ ``cpu``\  is congested.  There is
no synchronization around this function and the test result is
unreliable and only useful as advisory hints or for debugging.

If \ ``cpu``\  is WORK_CPU_UNBOUND, the test is performed on the local CPU.
Note that both per-cpu and unbound workqueues may be associated with
multiple pool_workqueues which have separate congested states.  A
workqueue being congested on one CPU doesn't mean the workqueue is also
contested on other CPUs / NUMA nodes.

.. _`workqueue_congested.return`:

Return
------

%true if congested, \ ``false``\  otherwise.

.. _`work_busy`:

work_busy
=========

.. c:function:: unsigned int work_busy(struct work_struct *work)

    test whether a work is currently pending or running

    :param struct work_struct \*work:
        the work to be tested

.. _`work_busy.description`:

Description
-----------

Test whether \ ``work``\  is currently pending or running.  There is no
synchronization around this function and the test result is
unreliable and only useful as advisory hints or for debugging.

.. _`work_busy.return`:

Return
------

OR'd bitmask of WORK_BUSY_* bits.

.. _`set_worker_desc`:

set_worker_desc
===============

.. c:function:: void set_worker_desc(const char *fmt,  ...)

    set description for the current work item

    :param const char \*fmt:
        printf-style format string

    :param ... :
        arguments for the format string

.. _`set_worker_desc.description`:

Description
-----------

This function can be called by a running work function to describe what
the work item is about.  If the worker task gets dumped, this
information will be printed out together to help debugging.  The
description can be at most WORKER_DESC_LEN including the trailing '\0'.

.. _`print_worker_info`:

print_worker_info
=================

.. c:function:: void print_worker_info(const char *log_lvl, struct task_struct *task)

    print out worker information and description

    :param const char \*log_lvl:
        the log level to use when printing

    :param struct task_struct \*task:
        target task

.. _`print_worker_info.description`:

Description
-----------

If \ ``task``\  is a worker and currently executing a work item, print out the
name of the workqueue being serviced and worker description set with
\ :c:func:`set_worker_desc`\  by the currently executing work item.

This function can be safely called on any task as long as the
task_struct itself is accessible.  While safe, this function isn't
synchronized and may print out mixups or garbages of limited length.

.. _`show_workqueue_state`:

show_workqueue_state
====================

.. c:function:: void show_workqueue_state( void)

    dump workqueue state

    :param  void:
        no arguments

.. _`show_workqueue_state.description`:

Description
-----------

Called from a sysrq handler or \ :c:func:`try_to_freeze_tasks`\  and prints out
all busy workqueues and pools.

.. _`rebind_workers`:

rebind_workers
==============

.. c:function:: void rebind_workers(struct worker_pool *pool)

    rebind all workers of a pool to the associated CPU

    :param struct worker_pool \*pool:
        pool of interest

.. _`rebind_workers.description`:

Description
-----------

@pool->cpu is coming online.  Rebind all workers to the CPU.

.. _`restore_unbound_workers_cpumask`:

restore_unbound_workers_cpumask
===============================

.. c:function:: void restore_unbound_workers_cpumask(struct worker_pool *pool, int cpu)

    restore cpumask of unbound workers

    :param struct worker_pool \*pool:
        unbound pool of interest

    :param int cpu:
        the CPU which is coming up

.. _`restore_unbound_workers_cpumask.description`:

Description
-----------

An unbound pool may end up with a cpumask which doesn't have any online
CPUs.  When a worker of such pool get scheduled, the scheduler resets
its cpus_allowed.  If \ ``cpu``\  is in \ ``pool``\ 's cpumask which didn't have any
online CPU before, cpus_allowed of all its workers should be restored.

.. _`work_on_cpu`:

work_on_cpu
===========

.. c:function:: long work_on_cpu(int cpu, long (*fn)(void *), void *arg)

    run a function in thread context on a particular cpu

    :param int cpu:
        the cpu to run on

    :param long (\*fn)(void \*):
        the function to run

    :param void \*arg:
        the function arg

.. _`work_on_cpu.description`:

Description
-----------

It is up to the caller to ensure that the cpu doesn't go offline.
The caller must not hold any locks which would prevent \ ``fn``\  from completing.

.. _`work_on_cpu.return`:

Return
------

The value \ ``fn``\  returns.

.. _`freeze_workqueues_begin`:

freeze_workqueues_begin
=======================

.. c:function:: void freeze_workqueues_begin( void)

    begin freezing workqueues

    :param  void:
        no arguments

.. _`freeze_workqueues_begin.description`:

Description
-----------

Start freezing workqueues.  After this function returns, all freezable
workqueues will queue new works to their delayed_works list instead of
pool->worklist.

.. _`freeze_workqueues_begin.context`:

Context
-------

Grabs and releases wq_pool_mutex, wq->mutex and pool->lock's.

.. _`freeze_workqueues_busy`:

freeze_workqueues_busy
======================

.. c:function:: bool freeze_workqueues_busy( void)

    are freezable workqueues still busy?

    :param  void:
        no arguments

.. _`freeze_workqueues_busy.description`:

Description
-----------

Check whether freezing is complete.  This function must be called
between \ :c:func:`freeze_workqueues_begin`\  and \ :c:func:`thaw_workqueues`\ .

.. _`freeze_workqueues_busy.context`:

Context
-------

Grabs and releases wq_pool_mutex.

.. _`freeze_workqueues_busy.return`:

Return
------

%true if some freezable workqueues are still busy.  \ ``false``\  if freezing
is complete.

.. _`thaw_workqueues`:

thaw_workqueues
===============

.. c:function:: void thaw_workqueues( void)

    thaw workqueues

    :param  void:
        no arguments

.. _`thaw_workqueues.description`:

Description
-----------

Thaw workqueues.  Normal queueing is restored and all collected
frozen works are transferred to their respective pool worklists.

.. _`thaw_workqueues.context`:

Context
-------

Grabs and releases wq_pool_mutex, wq->mutex and pool->lock's.

.. _`workqueue_set_unbound_cpumask`:

workqueue_set_unbound_cpumask
=============================

.. c:function:: int workqueue_set_unbound_cpumask(cpumask_var_t cpumask)

    Set the low-level unbound cpumask

    :param cpumask_var_t cpumask:
        the cpumask to set

.. _`workqueue_set_unbound_cpumask.description`:

Description
-----------

 The low-level workqueues cpumask is a global cpumask that limits
 the affinity of all unbound workqueues.  This function check the \ ``cpumask``\ 
 and apply it to all unbound workqueues and updates all pwqs of them.

 Retun:      0       - Success
             -EINVAL - Invalid \ ``cpumask``\ 
             -ENOMEM - Failed to allocate memory for attrs or pwqs.

.. _`workqueue_sysfs_register`:

workqueue_sysfs_register
========================

.. c:function:: int workqueue_sysfs_register(struct workqueue_struct *wq)

    make a workqueue visible in sysfs

    :param struct workqueue_struct \*wq:
        the workqueue to register

.. _`workqueue_sysfs_register.description`:

Description
-----------

Expose \ ``wq``\  in sysfs under /sys/bus/workqueue/devices.
alloc_workqueue*() automatically calls this function if WQ_SYSFS is set
which is the preferred method.

Workqueue user should use this function directly iff it wants to apply
workqueue_attrs before making the workqueue visible in sysfs; otherwise,
\ :c:func:`apply_workqueue_attrs`\  may race against userland updating the
attributes.

.. _`workqueue_sysfs_register.return`:

Return
------

0 on success, -errno on failure.

.. _`workqueue_sysfs_unregister`:

workqueue_sysfs_unregister
==========================

.. c:function:: void workqueue_sysfs_unregister(struct workqueue_struct *wq)

    undo \ :c:func:`workqueue_sysfs_register`\ 

    :param struct workqueue_struct \*wq:
        the workqueue to unregister

.. _`workqueue_sysfs_unregister.description`:

Description
-----------

If \ ``wq``\  is registered to sysfs by \ :c:func:`workqueue_sysfs_register`\ , unregister.

.. _`workqueue_init_early`:

workqueue_init_early
====================

.. c:function:: int workqueue_init_early( void)

    early init for workqueue subsystem

    :param  void:
        no arguments

.. _`workqueue_init_early.description`:

Description
-----------

This is the first half of two-staged workqueue subsystem initialization
and invoked as soon as the bare basics - memory allocation, cpumasks and
idr are up.  It sets up all the data structures and system workqueues
and allows early boot code to create workqueues and queue/cancel work
items.  Actual work item execution starts only after kthreads can be
created and scheduled right before early initcalls.

.. _`workqueue_init`:

workqueue_init
==============

.. c:function:: int workqueue_init( void)

    bring workqueue subsystem fully online

    :param  void:
        no arguments

.. _`workqueue_init.description`:

Description
-----------

This is the latter half of two-staged workqueue subsystem initialization
and invoked as soon as kthreads can be created and scheduled.
Workqueues have been created and work items queued on them, but there
are no kworkers executing the work items yet.  Populate the worker pools
with the initial workers and enable future kworker creations.

.. This file was automatic generated / don't edit.

