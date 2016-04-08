
.. _API-wimax-dev-add:

=============
wimax_dev_add
=============

*man wimax_dev_add(9)*

*4.6.0-rc1*

Register a new WiMAX device


Synopsis
========

.. c:function:: int wimax_dev_add( struct wimax_dev * wimax_dev, struct net_device * net_dev )

Arguments
=========

``wimax_dev``
    WiMAX device descriptor (as embedded in your ``net_dev``'s priv data). You must have called ``wimax_dev_init`` on it before.

``net_dev``
    net device the ``wimax_dev`` is associated with. The function expects ``SET_NETDEV_DEV`` and ``register_netdev`` were already called on it.


Description
===========

Registers the new WiMAX device, sets up the user-kernel control interface (generic netlink) and common WiMAX infrastructure.

Note that the parts that will allow interaction with user space are setup at the very end, when the rest is in place, as once that happens, the driver might get user space control
requests via netlink or from debugfs that might translate into calls into wimax_dev->op_⋆().
