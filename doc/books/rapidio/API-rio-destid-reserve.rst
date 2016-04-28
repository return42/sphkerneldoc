.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-destid-reserve:

==================
rio_destid_reserve
==================

*man rio_destid_reserve(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
