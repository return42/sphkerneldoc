
.. _API-netdev-lower-get-next-private:

=============================
netdev_lower_get_next_private
=============================

*man netdev_lower_get_next_private(9)*

*4.6.0-rc1*

Get the next ->private from the lower neighbour list


Synopsis
========

.. c:function:: void ⋆ netdev_lower_get_next_private( struct net_device * dev, struct list_head ** iter )

Arguments
=========

``dev``
    device

``iter``
    list_head ⋆⋆ of the current position


Description
===========

Gets the next netdev_adjacent->private from the dev's lower neighbour list, starting from iter position. The caller must hold either hold the RTNL lock or its own locking that
guarantees that the neighbour lower list will remain unchanged.
