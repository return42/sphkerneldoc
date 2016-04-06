
.. _API-sys-set-robust-list:

===================
sys_set_robust_list
===================

*man sys_set_robust_list(9)*

*4.6.0-rc1*

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
