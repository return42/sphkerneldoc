.. -*- coding: utf-8; mode: rst -*-

.. _API-ipc-obtain-object-idr:

=====================
ipc_obtain_object_idr
=====================

*man ipc_obtain_object_idr(9)*

*4.6.0-rc5*


Synopsis
========

.. c:function:: struct kern_ipc_perm * ipc_obtain_object_idr( struct ipc_ids * ids, int id )

Arguments
=========

``ids``
    ipc identifier set

``id``
    ipc id to look for


Description
===========

Look for an id in the ipc ids idr and return associated ipc object.

Call inside the RCU critical section. The ipc object is *not* locked on
exit.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
