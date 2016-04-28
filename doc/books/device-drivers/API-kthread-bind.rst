.. -*- coding: utf-8; mode: rst -*-

.. _API-kthread-bind:

============
kthread_bind
============

*man kthread_bind(9)*

*4.6.0-rc5*

bind a just-created kthread to a cpu.


Synopsis
========

.. c:function:: void kthread_bind( struct task_struct * p, unsigned int cpu )

Arguments
=========

``p``
    thread created by ``kthread_create``.

``cpu``
    cpu (might not be online, must be possible) for ``k`` to run on.


Description
===========

This function is equivalent to ``set_cpus_allowed``, except that ``cpu``
doesn't need to be online, and the thread must be stopped (i.e., just
returned from ``kthread_create``).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
