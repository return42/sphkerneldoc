.. -*- coding: utf-8; mode: rst -*-

.. _API-netdev-state-change:

===================
netdev_state_change
===================

*man netdev_state_change(9)*

*4.6.0-rc5*

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

Called to indicate a device has changed state. This function calls the
notifier chains for netdev_chain and sends a NEWLINK message to the
routing socket.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
