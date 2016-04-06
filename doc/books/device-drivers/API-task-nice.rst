
.. _API-task-nice:

=========
task_nice
=========

*man task_nice(9)*

*4.6.0-rc1*

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
