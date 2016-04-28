.. -*- coding: utf-8; mode: rst -*-

.. _API-ipcget-new:

==========
ipcget_new
==========

*man ipcget_new(9)*

*4.6.0-rc5*

create a new ipc object


Synopsis
========

.. c:function:: int ipcget_new( struct ipc_namespace * ns, struct ipc_ids * ids, const struct ipc_ops * ops, struct ipc_params * params )

Arguments
=========

``ns``
    ipc namespace

``ids``
    ipc identifier set

``ops``
    the actual creation routine to call

``params``
    its parameters


Description
===========

This routine is called by sys_msgget, ``sys_semget`` and ``sys_shmget``
when the key is IPC_PRIVATE.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
