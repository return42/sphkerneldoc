.. -*- coding: utf-8; mode: rst -*-

.. _API-ipc-update-perm:

===============
ipc_update_perm
===============

*man ipc_update_perm(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
