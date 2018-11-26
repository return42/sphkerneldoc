.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/rcu/tree_exp.h

.. _`synchronize_rcu_expedited`:

synchronize_rcu_expedited
=========================

.. c:function:: void synchronize_rcu_expedited( void)

    Brute-force RCU grace period

    :param void:
        no arguments
    :type void: 

.. _`synchronize_rcu_expedited.description`:

Description
-----------

Wait for an RCU-preempt grace period, but expedite it.  The basic
idea is to IPI all non-idle non-nohz online CPUs.  The IPI handler
checks whether the CPU is in an RCU-preempt critical section, and
if so, it sets a flag that causes the outermost \ :c:func:`rcu_read_unlock`\ 
to report the quiescent state.  On the other hand, if the CPU is
not in an RCU read-side critical section, the IPI handler reports
the quiescent state immediately.

Although this is a greate improvement over previous expedited
implementations, it is still unfriendly to real-time workloads, so is
thus not recommended for any sort of common-case code.  In fact, if
you are using \ :c:func:`synchronize_rcu_expedited`\  in a loop, please restructure
your code to batch your updates, and then Use a single \ :c:func:`synchronize_rcu`\ 
instead.

This has the same semantics as (but is more brutal than) \ :c:func:`synchronize_rcu`\ .

.. This file was automatic generated / don't edit.

