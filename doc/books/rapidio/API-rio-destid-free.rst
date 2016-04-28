.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-destid-free:

===============
rio_destid_free
===============

*man rio_destid_free(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
