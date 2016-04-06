
.. _API---audit-socketcall:

==================
__audit_socketcall
==================

*man __audit_socketcall(9)*

*4.6.0-rc1*

record audit data for sys_socketcall


Synopsis
========

.. c:function:: int __audit_socketcall( int nargs, unsigned long * args )

Arguments
=========

``nargs``
    number of args, which should not be more than AUDITSC_ARGS.

``args``
    args array
