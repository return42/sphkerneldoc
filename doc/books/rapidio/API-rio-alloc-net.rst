
.. _API-rio-alloc-net:

=============
rio_alloc_net
=============

*man rio_alloc_net(9)*

*4.6.0-rc1*

Allocate and initialize a new RIO network data structure


Synopsis
========

.. c:function:: struct rio_net ⋆ rio_alloc_net( struct rio_mport * mport )

Arguments
=========

``mport``
    Master port associated with the RIO network


Description
===========

Allocates a RIO network structure, initializes per-network list heads, and adds the associated master port to the network list of associated master ports. Returns a RIO network
pointer on success or ``NULL`` on failure.
