.. -*- coding: utf-8; mode: rst -*-

.. _API-task-participate-group-stop:

===========================
task_participate_group_stop
===========================

*man task_participate_group_stop(9)*

*4.6.0-rc5*

participate in a group stop


Synopsis
========

.. c:function:: bool task_participate_group_stop( struct task_struct * task )

Arguments
=========

``task``
    task participating in a group stop


Description
===========

``task`` has ``JOBCTL_STOP_PENDING`` set and is participating in a group
stop. Group stop states are cleared and the group stop count is consumed
if ``JOBCTL_STOP_CONSUME`` was set. If the consumption completes the
group stop, the appropriate ``SIGNAL_``\ * flags are set.


CONTEXT
=======

Must be called with ``task``->sighand->siglock held.


RETURNS
=======

``true`` if group stop completion should be notified to the parent,
``false`` otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
