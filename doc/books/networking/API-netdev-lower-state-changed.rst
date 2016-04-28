.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-lower-state-changed:

==========================
netdev_lower_state_changed
==========================

*man netdev_lower_state_changed(9)*

*4.6.0-rc5*

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

Send NETDEV_CHANGELOWERSTATE to netdev notifiers with info. The caller
must hold the RTNL lock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
