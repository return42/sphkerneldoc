
.. _API-netif-dormant-on:

================
netif_dormant_on
================

*man netif_dormant_on(9)*

*4.6.0-rc1*

mark device as dormant.


Synopsis
========

.. c:function:: void netif_dormant_on( struct net_device * dev )

Arguments
=========

``dev``
    network device


Description
===========

Mark device as dormant (as per RFC2863).

The dormant state indicates that the relevant interface is not actually in a condition to pass packets (i.e., it is not 'up') but is in a “pending” state, waiting for some external
event. For “on- demand” interfaces, this new state identifies the situation where the interface is waiting for events to place it in the up state.
