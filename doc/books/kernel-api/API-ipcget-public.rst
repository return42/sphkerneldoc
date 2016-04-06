
.. _API-ipcget-public:

=============
ipcget_public
=============

*man ipcget_public(9)*

*4.6.0-rc1*

get an ipc object or create a new one


Synopsis
========

.. c:function:: int ipcget_public( struct ipc_namespace * ns, struct ipc_ids * ids, const struct ipc_ops * ops, struct ipc_params * params )

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

This routine is called by sys_msgget, ``sys_semget`` and ``sys_shmget`` when the key is not IPC_PRIVATE. It adds a new entry if the key is not found and does some permission /
security checkings if the key is found.

On success, the ipc id is returned.
