.. -*- coding: utf-8; mode: rst -*-

=============
tree_plugin.h
=============

.. _`synchronize_rcu`:

synchronize_rcu
===============

.. c:function:: void synchronize_rcu ( void)

    wait until a grace period has elapsed.

    :param void:
        no arguments


.. _`synchronize_rcu.description`:

Description
-----------


Control will return to the caller some time after a full grace
period has elapsed, in other words after all currently executing RCU
read-side critical sections have completed.  Note, however, that
upon return from :c:func:`synchronize_rcu`, the caller might well be executing
concurrently with new RCU read-side critical sections that began while
:c:func:`synchronize_rcu` was waiting.  RCU read-side critical sections are
delimited by :c:func:`rcu_read_lock` and :c:func:`rcu_read_unlock`, and may be nested.

See the description of :c:func:`synchronize_sched` for more detailed information
on memory ordering guarantees.


.. _`synchronize_rcu_expedited`:

synchronize_rcu_expedited
=========================

.. c:function:: void synchronize_rcu_expedited ( void)

    Brute-force RCU grace period

    :param void:
        no arguments


.. _`synchronize_rcu_expedited.description`:

Description
-----------


Wait for an RCU-preempt grace period, but expedite it.  The basic
idea is to invoke :c:func:`synchronize_sched_expedited` to push all the tasks to
the ->blkd_tasks lists and wait for this list to drain.  This consumes
significant time on all CPUs and is unfriendly to real-time workloads,
so is thus not recommended for any sort of common-case code.
In fact, if you are using :c:func:`synchronize_rcu_expedited` in a loop,
please restructure your code to batch your updates, and then Use a
single :c:func:`synchronize_rcu` instead.


.. _`rcu_barrier`:

rcu_barrier
===========

.. c:function:: void rcu_barrier ( void)

    Wait until all in-flight call_rcu() callbacks complete.

    :param void:
        no arguments


.. _`rcu_barrier.description`:

Description
-----------


Note that this primitive does not necessarily wait for an RCU grace period
to complete.  For example, if there are no RCU callbacks queued anywhere
in the system, then :c:func:`rcu_barrier` is within its rights to return
immediately, without waiting for anything, much less an RCU grace period.

