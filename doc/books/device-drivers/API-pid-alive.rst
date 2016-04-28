.. -*- coding: utf-8; mode: rst -*-

.. _API-pid-alive:

=========
pid_alive
=========

*man pid_alive(9)*

*4.6.0-rc5*

check that a task structure is not stale


Synopsis
========

.. c:function:: int pid_alive( const struct task_struct * p )

Arguments
=========

``p``
    Task structure to be checked.


Description
===========

Test if a process is not yet dead (at most zombie state) If pid_alive
fails, then pointers within the task structure can be stale and must not
be dereferenced.


Return
======

1 if the process is alive. 0 otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
