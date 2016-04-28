.. -*- coding: utf-8; mode: rst -*-

.. _API-synchronize-srcu:

================
synchronize_srcu
================

*man synchronize_srcu(9)*

*4.6.0-rc5*

wait for prior SRCU read-side critical-section completion


Synopsis
========

.. c:function:: void synchronize_srcu( struct srcu_struct * sp )

Arguments
=========

``sp``
    srcu_struct with which to synchronize.


Description
===========

Wait for the count to drain to zero of both indexes. To avoid the
possible starvation of ``synchronize_srcu``, it waits for the count of
the index=((->completed & 1) ^ 1) to drain to zero at first, and then
flip the completed and wait for the count of the other index.

Can block; must be called from process context.

Note that it is illegal to call ``synchronize_srcu`` from the
corresponding SRCU read-side critical section; doing so will result in
deadlock. However, it is perfectly legal to call ``synchronize_srcu`` on
one srcu_struct from some other srcu_struct's read-side critical
section, as long as the resulting graph of srcu_structs is acyclic.

There are memory-ordering constraints implied by ``synchronize_srcu``.
On systems with more than one CPU, when ``synchronize_srcu`` returns,
each CPU is guaranteed to have executed a full memory barrier since the
end of its last corresponding SRCU-sched read-side critical section
whose beginning preceded the call to ``synchronize_srcu``. In addition,
each CPU having an SRCU read-side critical section that extends beyond
the return from ``synchronize_srcu`` is guaranteed to have executed a
full memory barrier after the beginning of ``synchronize_srcu`` and
before the beginning of that SRCU read-side critical section. Note that
these guarantees include CPUs that are offline, idle, or executing in
user mode, as well as CPUs that are executing in the kernel.

Furthermore, if CPU A invoked ``synchronize_srcu``, which returned to
its caller on CPU B, then both CPU A and CPU B are guaranteed to have
executed a full memory barrier during the execution of
``synchronize_srcu``. This guarantee applies even if CPU A and CPU B are
the same CPU, but again only if the system has more than one CPU.

Of course, these memory-ordering guarantees apply only when
``synchronize_srcu``, ``srcu_read_lock``, and ``srcu_read_unlock`` are
passed the same srcu_struct structure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
