.. -*- coding: utf-8; mode: rst -*-

.. _API-ipc-findkey:

===========
ipc_findkey
===========

*man ipc_findkey(9)*

*4.6.0-rc5*

find a key in an ipc identifier set


Synopsis
========

.. c:function:: struct kern_ipc_perm * ipc_findkey( struct ipc_ids * ids, key_t key )

Arguments
=========

``ids``
    ipc identifier set

``key``
    key to find


Description
===========

Returns the locked pointer to the ipc structure if found or NULL
otherwise. If key is found ipc points to the owning ipc structure

Called with ipc_ids.rwsem held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
