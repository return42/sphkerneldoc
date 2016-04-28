.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-alloc-net:

=============
rio_alloc_net
=============

*man rio_alloc_net(9)*

*4.6.0-rc5*

Allocate and initialize a new RIO network data structure


Synopsis
========

.. c:function:: struct rio_net * rio_alloc_net( struct rio_mport * mport )

Arguments
=========

``mport``
    Master port associated with the RIO network


Description
===========

Allocates a RIO network structure, initializes per-network list heads,
and adds the associated master port to the network list of associated
master ports. Returns a RIO network pointer on success or ``NULL`` on
failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
