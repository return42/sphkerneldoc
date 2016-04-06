
.. _API-ipc-addid:

=========
ipc_addid
=========

*man ipc_addid(9)*

*4.6.0-rc1*

add an ipc identifier


Synopsis
========

.. c:function:: int ipc_addid( struct ipc_ids * ids, struct kern_ipc_perm * new, int size )

Arguments
=========

``ids``
    ipc identifier set

``new``
    new ipc permission set

``size``
    limit for the number of used ids


Description
===========

Add an entry 'new' to the ipc ids idr. The permissions object is initialised and the first free entry is set up and the id assigned is returned. The 'new' entry is returned in a
locked state on success. On failure the entry is not locked and a negative err-code is returned.

Called with writer ipc_ids.rwsem held.
