.. -*- coding: utf-8; mode: rst -*-

.. _API-ipc-check-perms:

===============
ipc_check_perms
===============

*man ipc_check_perms(9)*

*4.6.0-rc5*

check security and permissions for an ipc object


Synopsis
========

.. c:function:: int ipc_check_perms( struct ipc_namespace * ns, struct kern_ipc_perm * ipcp, const struct ipc_ops * ops, struct ipc_params * params )

Arguments
=========

``ns``
    ipc namespace

``ipcp``
    ipc permission set

``ops``
    the actual security routine to call

``params``
    its parameters


Description
===========

This routine is called by ``sys_msgget``, ``sys_semget`` and
``sys_shmget`` when the key is not IPC_PRIVATE and that key already
exists in the ds IDR.

On success, the ipc id is returned.

It is called with ipc_ids.rwsem and ipcp->lock held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
