.. -*- coding: utf-8; mode: rst -*-

.. _API-is-global-init:

==============
is_global_init
==============

*man is_global_init(9)*

*4.6.0-rc5*

check if a task structure is init. Since init is free to have
sub-threads we need to check tgid.


Synopsis
========

.. c:function:: int is_global_init( struct task_struct * tsk )

Arguments
=========

``tsk``
    Task structure to be checked.


Description
===========

Check if a task structure is the first user space task the kernel
created.


Return
======

1 if the task structure is init. 0 otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
