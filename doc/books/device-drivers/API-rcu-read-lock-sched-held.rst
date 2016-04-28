.. -*- coding: utf-8; mode: rst -*-

.. _API-rcu-read-lock-sched-held:

========================
rcu_read_lock_sched_held
========================

*man rcu_read_lock_sched_held(9)*

*4.6.0-rc5*

might we be in RCU-sched read-side critical section?


Synopsis
========

.. c:function:: int rcu_read_lock_sched_held( void )

Arguments
=========

``void``
    no arguments


Description
===========

If CONFIG_DEBUG_LOCK_ALLOC is selected, returns nonzero iff in an
RCU-sched read-side critical section. In absence of
CONFIG_DEBUG_LOCK_ALLOC, this assumes we are in an RCU-sched
read-side critical section unless it can prove otherwise. Note that
disabling of preemption (including disabling irqs) counts as an
RCU-sched read-side critical section. This is useful for debug checks in
functions that required that they be called within an RCU-sched
read-side critical section.

Check ``debug_lockdep_rcu_enabled`` to prevent false positives during
boot and while lockdep is disabled.

Note that if the CPU is in the idle loop from an RCU point of view (ie:
that we are in the section between ``rcu_idle_enter`` and
``rcu_idle_exit``) then ``rcu_read_lock_held`` returns false even if the
CPU did an ``rcu_read_lock``. The reason for this is that RCU ignores
CPUs that are in such a section, considering these as in extended
quiescent state, so such a CPU is effectively never in an RCU read-side
critical section regardless of what RCU primitives it invokes. This
state of affairs is required --- we need to keep an RCU-free window in
idle where the CPU may possibly enter into low power mode. This way we
can notice an extended quiescent state to other CPUs that started a
grace period. Otherwise we would delay any grace period as long as we
run in the idle task.

Similarly, we avoid claiming an SRCU read lock held if the current CPU
is offline.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
