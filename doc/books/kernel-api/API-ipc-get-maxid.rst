.. -*- coding: utf-8; mode: rst -*-

.. _API-ipc-get-maxid:

=============
ipc_get_maxid
=============

*man ipc_get_maxid(9)*

*4.6.0-rc5*

get the last assigned id


Synopsis
========

.. c:function:: int ipc_get_maxid( struct ipc_ids * ids )

Arguments
=========

``ids``
    ipc identifier set


Description
===========

Called with ipc_ids.rwsem held.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
