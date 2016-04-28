.. -*- coding: utf-8; mode: rst -*-

.. _API-is-idle-task:

============
is_idle_task
============

*man is_idle_task(9)*

*4.6.0-rc5*

is the specified task an idle task?


Synopsis
========

.. c:function:: bool is_idle_task( const struct task_struct * p )

Arguments
=========

``p``
    the task in question.


Return
======

1 if ``p`` is an idle task. 0 otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
