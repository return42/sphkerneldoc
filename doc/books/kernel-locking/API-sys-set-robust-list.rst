.. -*- coding: utf-8; mode: rst -*-

.. _API-sys-set-robust-list:

===================
sys_set_robust_list
===================

*man sys_set_robust_list(9)*

*4.6.0-rc5*

Set the robust-futex list head of a task


Synopsis
========

.. c:function:: long sys_set_robust_list( struct robust_list_head __user * head, size_t len )

Arguments
=========

``head``
    pointer to the list-head

``len``
    length of the list-head, as userspace expects


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
