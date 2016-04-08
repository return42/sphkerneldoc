
.. _API-eth-header-cache:

================
eth_header_cache
================

*man eth_header_cache(9)*

*4.6.0-rc1*

fill cache entry from neighbour


Synopsis
========

.. c:function:: int eth_header_cache( const struct neighbour * neigh, struct hh_cache * hh, __be16 type )

Arguments
=========

``neigh``
    source neighbour

``hh``
    destination cache entry

``type``
    Ethernet type field


Description
===========

Create an Ethernet header template from the neighbour.
