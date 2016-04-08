
.. _API-netdev-state-change:

===================
netdev_state_change
===================

*man netdev_state_change(9)*

*4.6.0-rc1*

device changes state


Synopsis
========

.. c:function:: void netdev_state_change( struct net_device * dev )

Arguments
=========

``dev``
    device to cause notification


Description
===========

Called to indicate a device has changed state. This function calls the notifier chains for netdev_chain and sends a NEWLINK message to the routing socket.
