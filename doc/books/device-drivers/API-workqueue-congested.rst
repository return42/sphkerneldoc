
.. _API-workqueue-congested:

===================
workqueue_congested
===================

*man workqueue_congested(9)*

*4.6.0-rc1*

test whether a workqueue is congested


Synopsis
========

.. c:function:: bool workqueue_congested( int cpu, struct workqueue_struct * wq )

Arguments
=========

``cpu``
    CPU in question

``wq``
    target workqueue


Description
===========

Test whether ``wq``'s cpu workqueue for ``cpu`` is congested. There is no synchronization around this function and the test result is unreliable and only useful as advisory hints
or for debugging.

If ``cpu`` is WORK_CPU_UNBOUND, the test is performed on the local CPU. Note that both per-cpu and unbound workqueues may be associated with multiple pool_workqueues which have
separate congested states. A workqueue being congested on one CPU doesn't mean the workqueue is also contested on other CPUs / NUMA nodes.


Return
======

``true`` if congested, ``false`` otherwise.
