
.. _API-eth-header-cache-update:

=======================
eth_header_cache_update
=======================

*man eth_header_cache_update(9)*

*4.6.0-rc1*

update cache entry


Synopsis
========

.. c:function:: void eth_header_cache_update( struct hh_cache * hh, const struct net_device * dev, const unsigned char * haddr )

Arguments
=========

``hh``
    destination cache entry

``dev``
    network device

``haddr``
    new hardware address


Description
===========

Called by Address Resolution module to notify changes in address.
