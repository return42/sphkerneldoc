
.. _API-netdev-lower-get-first-private-rcu:

==================================
netdev_lower_get_first_private_rcu
==================================

*man netdev_lower_get_first_private_rcu(9)*

*4.6.0-rc1*

Get the first ->private from the lower neighbour list, RCU variant


Synopsis
========

.. c:function:: void ⋆ netdev_lower_get_first_private_rcu( struct net_device * dev )

Arguments
=========

``dev``
    device


Description
===========

Gets the first netdev_adjacent->private from the dev's lower neighbour list. The caller must hold RCU read lock.
