.. -*- coding: utf-8; mode: rst -*-

.. _API---audit-sockaddr:

================
__audit_sockaddr
================

*man __audit_sockaddr(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
