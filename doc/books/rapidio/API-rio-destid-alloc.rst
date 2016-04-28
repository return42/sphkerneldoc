.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-destid-alloc:

================
rio_destid_alloc
================

*man rio_destid_alloc(9)*

*4.6.0-rc5*

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

Returns next available device destination ID for the specified RIO
network. Marks allocated ID as one in use. Returns RIO_INVALID_DESTID
if new destID is not available.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
