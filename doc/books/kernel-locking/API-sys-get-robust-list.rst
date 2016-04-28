.. -*- coding: utf-8; mode: rst -*-

.. _API-sys-get-robust-list:

===================
sys_get_robust_list
===================

*man sys_get_robust_list(9)*

*4.6.0-rc5*

Get the robust-futex list head of a task


Synopsis
========

.. c:function:: long sys_get_robust_list( int pid, struct robust_list_head __user *__user * head_ptr, size_t __user * len_ptr )

Arguments
=========

``pid``
    pid of the process [zero for current task]

``head_ptr``
    pointer to a list-head pointer, the kernel fills it in

``len_ptr``
    pointer to a length field, the kernel fills in the header size


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
