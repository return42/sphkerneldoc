.. -*- coding: utf-8; mode: rst -*-

.. _API-sched-setscheduler:

==================
sched_setscheduler
==================

*man sched_setscheduler(9)*

*4.6.0-rc5*

change the scheduling policy and/or RT priority of a thread.


Synopsis
========

.. c:function:: int sched_setscheduler( struct task_struct * p, int policy, const struct sched_param * param )

Arguments
=========

``p``
    the task in question.

``policy``
    new policy.

``param``
    structure containing the new RT priority.


Return
======

0 on success. An error code otherwise.

NOTE that the task may be already dead.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
