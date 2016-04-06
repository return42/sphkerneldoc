
.. _API-ipc-get-maxid:

=============
ipc_get_maxid
=============

*man ipc_get_maxid(9)*

*4.6.0-rc1*

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
