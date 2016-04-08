
.. _API-netdev-all-upper-get-next-dev-rcu:

=================================
netdev_all_upper_get_next_dev_rcu
=================================

*man netdev_all_upper_get_next_dev_rcu(9)*

*4.6.0-rc1*

Get the next dev from upper list


Synopsis
========

.. c:function:: struct net_device ⋆ netdev_all_upper_get_next_dev_rcu( struct net_device * dev, struct list_head ** iter )

Arguments
=========

``dev``
    device

``iter``
    list_head ⋆⋆ of the current position


Description
===========

Gets the next device from the dev's upper list, starting from iter position. The caller must hold RCU read lock.
