
.. _API---audit-sockaddr:

================
__audit_sockaddr
================

*man __audit_sockaddr(9)*

*4.6.0-rc1*

record audit data for sys_bind, sys_connect, sys_sendto


Synopsis
========

.. c:function:: int __audit_sockaddr( int len, void * a )

Arguments
=========

``len``
    data length in user space

``a``
    data address in kernel space


Description
===========

Returns 0 for success or NULL context or < 0 on error.
