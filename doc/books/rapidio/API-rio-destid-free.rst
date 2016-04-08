
.. _API-rio-destid-free:

===============
rio_destid_free
===============

*man rio_destid_free(9)*

*4.6.0-rc1*

free a previously allocated destID


Synopsis
========

.. c:function:: void rio_destid_free( struct rio_net * net, u16 destid )

Arguments
=========

``net``
    RIO network

``destid``
    destID to free


Description
===========

Makes the specified destID available for use.
