
.. _API-ipcget-new:

==========
ipcget_new
==========

*man ipcget_new(9)*

*4.6.0-rc1*

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

This routine is called by sys_msgget, ``sys_semget`` and ``sys_shmget`` when the key is IPC_PRIVATE.
