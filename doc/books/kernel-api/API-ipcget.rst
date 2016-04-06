
.. _API-ipcget:

======
ipcget
======

*man ipcget(9)*

*4.6.0-rc1*

Common sys_⋆ ``get`` code


Synopsis
========

.. c:function:: int ipcget( struct ipc_namespace * ns, struct ipc_ids * ids, const struct ipc_ops * ops, struct ipc_params * params )

Arguments
=========

``ns``
    namespace

``ids``
    ipc identifier set

``ops``
    operations to be called on ipc object creation, permission checks and further checks

``params``
    the parameters needed by the previous operations.


Description
===========

Common routine called by ``sys_msgget``, ``sys_semget`` and ``sys_shmget``.
