
.. _API---audit-syscall-exit:

====================
__audit_syscall_exit
====================

*man __audit_syscall_exit(9)*

*4.6.0-rc1*

deallocate audit context after a system call


Synopsis
========

.. c:function:: void __audit_syscall_exit( int success, long return_code )

Arguments
=========

``success``
    success value of the syscall

``return_code``
    return value of the syscall


Description
===========

Tear down after system call. If the audit context has been marked as auditable (either because of the AUDIT_RECORD_CONTEXT state from filtering, or because some other part of the
kernel wrote an audit message), then write out the syscall information. In call cases, free the names stored from ``getname``.
