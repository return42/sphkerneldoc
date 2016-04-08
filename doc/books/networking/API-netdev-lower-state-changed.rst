
.. _API-netdev-lower-state-changed:

==========================
netdev_lower_state_changed
==========================

*man netdev_lower_state_changed(9)*

*4.6.0-rc1*

Dispatch event about lower device state change


Synopsis
========

.. c:function:: void netdev_lower_state_changed( struct net_device * lower_dev, void * lower_state_info )

Arguments
=========

``lower_dev``
    device

``lower_state_info``
    state to dispatch


Description
===========

Send NETDEV_CHANGELOWERSTATE to netdev notifiers with info. The caller must hold the RTNL lock.
