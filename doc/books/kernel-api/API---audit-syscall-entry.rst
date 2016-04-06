
.. _API---audit-syscall-entry:

=====================
__audit_syscall_entry
=====================

*man __audit_syscall_entry(9)*

*4.6.0-rc1*

fill in an audit record at syscall entry


Synopsis
========

.. c:function:: void __audit_syscall_entry( int major, unsigned long a1, unsigned long a2, unsigned long a3, unsigned long a4 )

Arguments
=========

``major``
    major syscall type (function)

``a1``
    additional syscall register 1

``a2``
    additional syscall register 2

``a3``
    additional syscall register 3

``a4``
    additional syscall register 4


Description
===========

Fill in audit context at syscall entry. This only happens if the audit context was created when the task was created and the state or filters demand the audit context be built. If
the state from the per-task filter or from the per-syscall filter is AUDIT_RECORD_CONTEXT, then the record will be written at syscall exit time (otherwise, it will only be
written if another part of the kernel requests that it be written).
