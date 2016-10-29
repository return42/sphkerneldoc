.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/workqueue.h

.. _`work_pending`:

work_pending
============

.. c:function::  work_pending( work)

    Find out whether a work item is currently pending

    :param  work:
        The work item in question

.. _`delayed_work_pending`:

delayed_work_pending
====================

.. c:function::  delayed_work_pending( w)

    Find out whether a delayable work item is currently pending

    :param  w:
        The work item in question

.. _`alloc_workqueue`:

alloc_workqueue
===============

.. c:function::  alloc_workqueue( fmt,  flags,  max_active,  args...)

    allocate a workqueue

    :param  fmt:
        printf format for the name of the workqueue

    :param  flags:
        WQ\_\* flags

    :param  max_active:
        max in-flight work items, 0 for default

    :param  args...:
        args for \ ``fmt``\ 

.. _`alloc_workqueue.description`:

Description
-----------

Allocate a workqueue with the specified parameters.  For detailed
information on WQ\_\* flags, please refer to Documentation/workqueue.txt.

The \__lock_name macro dance is to guarantee that single lock_class_key
doesn't end up with different namesm, which isn't allowed by lockdep.

.. _`alloc_workqueue.return`:

Return
------

Pointer to the allocated workqueue on success, \ ``NULL``\  on failure.

.. _`alloc_ordered_workqueue`:

alloc_ordered_workqueue
=======================

.. c:function::  alloc_ordered_workqueue( fmt,  flags,  args...)

    allocate an ordered workqueue

    :param  fmt:
        printf format for the name of the workqueue

    :param  flags:
        WQ\_\* flags (only WQ_FREEZABLE and WQ_MEM_RECLAIM are meaningful)

    :param  args...:
        args for \ ``fmt``\ 

.. _`alloc_ordered_workqueue.description`:

Description
-----------

Allocate an ordered workqueue.  An ordered workqueue executes at
most one work item at any given time in the queued order.  They are
implemented as unbound workqueues with \ ``max_active``\  of one.

.. _`alloc_ordered_workqueue.return`:

Return
------

Pointer to the allocated workqueue on success, \ ``NULL``\  on failure.

.. _`queue_work`:

queue_work
==========

.. c:function:: bool queue_work(struct workqueue_struct *wq, struct work_struct *work)

    queue work on a workqueue

    :param struct workqueue_struct \*wq:
        workqueue to use

    :param struct work_struct \*work:
        work to queue

.. _`queue_work.description`:

Description
-----------

Returns \ ``false``\  if \ ``work``\  was already on a queue, \ ``true``\  otherwise.

We queue the work to the CPU on which it was submitted, but if the CPU dies
it can be processed by another CPU.

.. _`queue_delayed_work`:

queue_delayed_work
==================

.. c:function:: bool queue_delayed_work(struct workqueue_struct *wq, struct delayed_work *dwork, unsigned long delay)

    queue work on a workqueue after delay

    :param struct workqueue_struct \*wq:
        workqueue to use

    :param struct delayed_work \*dwork:
        delayable work to queue

    :param unsigned long delay:
        number of jiffies to wait before queueing

.. _`queue_delayed_work.description`:

Description
-----------

Equivalent to \ :c:func:`queue_delayed_work_on`\  but tries to use the local CPU.

.. _`mod_delayed_work`:

mod_delayed_work
================

.. c:function:: bool mod_delayed_work(struct workqueue_struct *wq, struct delayed_work *dwork, unsigned long delay)

    modify delay of or queue a delayed work

    :param struct workqueue_struct \*wq:
        workqueue to use

    :param struct delayed_work \*dwork:
        work to queue

    :param unsigned long delay:
        number of jiffies to wait before queueing

.. _`mod_delayed_work.description`:

Description
-----------

\ :c:func:`mod_delayed_work_on`\  on local CPU.

.. _`schedule_work_on`:

schedule_work_on
================

.. c:function:: bool schedule_work_on(int cpu, struct work_struct *work)

    put work task on a specific cpu

    :param int cpu:
        cpu to put the work task on

    :param struct work_struct \*work:
        job to be done

.. _`schedule_work_on.description`:

Description
-----------

This puts a job on a specific cpu

.. _`schedule_work`:

schedule_work
=============

.. c:function:: bool schedule_work(struct work_struct *work)

    put work task in global workqueue

    :param struct work_struct \*work:
        job to be done

.. _`schedule_work.description`:

Description
-----------

Returns \ ``false``\  if \ ``work``\  was already on the kernel-global workqueue and
\ ``true``\  otherwise.

This puts a job in the kernel-global workqueue if it was not already
queued and leaves it in the same position on the kernel-global
workqueue otherwise.

.. _`flush_scheduled_work`:

flush_scheduled_work
====================

.. c:function:: void flush_scheduled_work( void)

    ensure that any scheduled work has run to completion.

    :param  void:
        no arguments

.. _`flush_scheduled_work.description`:

Description
-----------

Forces execution of the kernel-global workqueue and blocks until its
completion.

Think twice before calling this function!  It's very easy to get into
trouble if you don't take great care.  Either of the following situations

.. _`flush_scheduled_work.will-lead-to-deadlock`:

will lead to deadlock
---------------------


One of the work items currently on the workqueue needs to acquire
a lock held by your code or its caller.

Your code is running in the context of a work routine.

They will be detected by lockdep when they occur, but the first might not
occur very often.  It depends on what work items are on the workqueue and
what locks they need, which you have no control over.

In most situations flushing the entire workqueue is overkill; you merely
need to know that a particular work item isn't queued and isn't running.
In such cases you should use \ :c:func:`cancel_delayed_work_sync`\  or
\ :c:func:`cancel_work_sync`\  instead.

.. _`schedule_delayed_work_on`:

schedule_delayed_work_on
========================

.. c:function:: bool schedule_delayed_work_on(int cpu, struct delayed_work *dwork, unsigned long delay)

    queue work in global workqueue on CPU after delay

    :param int cpu:
        cpu to use

    :param struct delayed_work \*dwork:
        job to be done

    :param unsigned long delay:
        number of jiffies to wait

.. _`schedule_delayed_work_on.description`:

Description
-----------

After waiting for a given time this puts a job in the kernel-global
workqueue on the specified CPU.

.. _`schedule_delayed_work`:

schedule_delayed_work
=====================

.. c:function:: bool schedule_delayed_work(struct delayed_work *dwork, unsigned long delay)

    put work task in global workqueue after delay

    :param struct delayed_work \*dwork:
        job to be done

    :param unsigned long delay:
        number of jiffies to wait or 0 for immediate execution

.. _`schedule_delayed_work.description`:

Description
-----------

After waiting for a given time this puts a job in the kernel-global
workqueue.

.. _`keventd_up`:

keventd_up
==========

.. c:function:: bool keventd_up( void)

    is workqueue initialized yet?

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.
