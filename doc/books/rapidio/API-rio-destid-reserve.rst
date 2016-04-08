
.. _API-rio-destid-reserve:

==================
rio_destid_reserve
==================

*man rio_destid_reserve(9)*

*4.6.0-rc1*

Reserve the specivied destID


Synopsis
========

.. c:function:: int rio_destid_reserve( struct rio_net * net, u16 destid )

Arguments
=========

``net``
    RIO network

``destid``
    destID to reserve


Description
===========

Tries to reserve the specified destID. Returns 0 if successful.
