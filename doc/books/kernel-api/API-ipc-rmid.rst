.. -*- coding: utf-8; mode: rst -*-

.. _API-ipc-rmid:

========
ipc_rmid
========

*man ipc_rmid(9)*

*4.6.0-rc5*

remove an ipc identifier


Synopsis
========

.. c:function:: void ipc_rmid( struct ipc_ids * ids, struct kern_ipc_perm * ipcp )

Arguments
=========

``ids``
    ipc identifier set

``ipcp``
    ipc perm structure containing the identifier to remove


Description
===========

ipc_ids.rwsem (as a writer) and the spinlock for this ID are held
before this function is called, and remain locked on the exit.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
