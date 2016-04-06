
.. _API-ipc-lock:

========
ipc_lock
========

*man ipc_lock(9)*

*4.6.0-rc1*

lock an ipc structure without rwsem held


Synopsis
========

.. c:function:: struct kern_ipc_perm ⋆ ipc_lock( struct ipc_ids * ids, int id )

Arguments
=========

``ids``
    ipc identifier set

``id``
    ipc id to look for


Description
===========

Look for an id in the ipc ids idr and lock the associated ipc object.

The ipc object is locked on successful exit.
