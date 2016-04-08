
.. _API-rio-destid-alloc:

================
rio_destid_alloc
================

*man rio_destid_alloc(9)*

*4.6.0-rc1*

Allocate next available destID for given network


Synopsis
========

.. c:function:: u16 rio_destid_alloc( struct rio_net * net )

Arguments
=========

``net``
    RIO network


Description
===========

Returns next available device destination ID for the specified RIO network. Marks allocated ID as one in use. Returns RIO_INVALID_DESTID if new destID is not available.
