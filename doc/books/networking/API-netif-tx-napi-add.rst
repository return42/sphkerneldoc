
.. _API-netif-tx-napi-add:

=================
netif_tx_napi_add
=================

*man netif_tx_napi_add(9)*

*4.6.0-rc1*

initialize a NAPI context


Synopsis
========

.. c:function:: void netif_tx_napi_add( struct net_device * dev, struct napi_struct * napi, int (*poll) struct napi_struct *, int, int weight )

Arguments
=========

``dev``
    network device

``napi``
    NAPI context

``poll``
    polling function

``weight``
    default weight


Description
===========

This variant of ``netif_napi_add`` should be used from drivers using NAPI to exclusively poll a TX queue. This will avoid we add it into napi_hash[], thus polluting this hash
table.
