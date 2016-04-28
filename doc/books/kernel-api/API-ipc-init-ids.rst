.. -*- coding: utf-8; mode: rst -*-

.. _API-ipc-init-ids:

============
ipc_init_ids
============

*man ipc_init_ids(9)*

*4.6.0-rc5*

initialise ipc identifiers


Synopsis
========

.. c:function:: void ipc_init_ids( struct ipc_ids * ids )

Arguments
=========

``ids``
    ipc identifier set


Description
===========

Set up the sequence range to use for the ipc identifier range (limited
below IPCMNI) then initialise the ids idr.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
