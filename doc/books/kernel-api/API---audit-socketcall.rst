.. -*- coding: utf-8; mode: rst -*-

.. _API---audit-socketcall:

==================
__audit_socketcall
==================

*man __audit_socketcall(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
