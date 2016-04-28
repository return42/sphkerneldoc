.. -*- coding: utf-8; mode: rst -*-

.. _API---audit-ipc-set-perm:

====================
__audit_ipc_set_perm
====================

*man __audit_ipc_set_perm(9)*

*4.6.0-rc5*

record audit data for new ipc permissions


Synopsis
========

.. c:function:: void __audit_ipc_set_perm( unsigned long qbytes, uid_t uid, gid_t gid, umode_t mode )

Arguments
=========

``qbytes``
    msgq bytes

``uid``
    msgq user id

``gid``
    msgq group id

``mode``
    msgq mode (permissions)


Description
===========

Called only after ``audit_ipc_obj``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
