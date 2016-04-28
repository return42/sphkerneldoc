.. -*- coding: utf-8; mode: rst -*-

.. _API-ipc-lock:

========
ipc_lock
========

*man ipc_lock(9)*

*4.6.0-rc5*

lock an ipc structure without rwsem held


Synopsis
========

.. c:function:: struct kern_ipc_perm * ipc_lock( struct ipc_ids * ids, int id )

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
