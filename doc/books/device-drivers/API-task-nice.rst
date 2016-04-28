.. -*- coding: utf-8; mode: rst -*-

.. _API-task-nice:

=========
task_nice
=========

*man task_nice(9)*

*4.6.0-rc5*

return the nice value of a given task.


Synopsis
========

.. c:function:: int task_nice( const struct task_struct * p )

Arguments
=========

``p``
    the task in question.


Return
======

The nice value [ -20 ... 0 ... 19 ].


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
