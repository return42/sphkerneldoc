
.. _API-ipc64-perm-to-ipc-perm:

======================
ipc64_perm_to_ipc_perm
======================

*man ipc64_perm_to_ipc_perm(9)*

*4.6.0-rc1*

convert new ipc permissions to old


Synopsis
========

.. c:function:: void ipc64_perm_to_ipc_perm( struct ipc64_perm * in, struct ipc_perm * out )

Arguments
=========

``in``
    new style ipc permissions

``out``
    old style ipc permissions


Description
===========

Turn the new style permissions object ``in`` into a compatibility object and store it into the ``out`` pointer.
