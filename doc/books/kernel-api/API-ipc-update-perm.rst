
.. _API-ipc-update-perm:

===============
ipc_update_perm
===============

*man ipc_update_perm(9)*

*4.6.0-rc1*

update the permissions of an ipc object


Synopsis
========

.. c:function:: int ipc_update_perm( struct ipc64_perm * in, struct kern_ipc_perm * out )

Arguments
=========

``in``
    the permission given as input.

``out``
    the permission of the ipc to set.
