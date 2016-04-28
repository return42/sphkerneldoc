.. -*- coding: utf-8; mode: rst -*-

.. _API-ipcget:

======
ipcget
======

*man ipcget(9)*

*4.6.0-rc5*

Common sys_* ``get`` code


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
    operations to be called on ipc object creation, permission checks
    and further checks

``params``
    the parameters needed by the previous operations.


Description
===========

Common routine called by ``sys_msgget``, ``sys_semget`` and
``sys_shmget``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
