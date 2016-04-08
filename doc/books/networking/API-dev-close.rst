
.. _API-dev-close:

=========
dev_close
=========

*man dev_close(9)*

*4.6.0-rc1*

shutdown an interface.


Synopsis
========

.. c:function:: int dev_close( struct net_device * dev )

Arguments
=========

``dev``
    device to shutdown


Description
===========

This function moves an active device into down state. A ``NETDEV_GOING_DOWN`` is sent to the netdev notifier chain. The device is then deactivated and finally a ``NETDEV_DOWN`` is
sent to the notifier chain.
