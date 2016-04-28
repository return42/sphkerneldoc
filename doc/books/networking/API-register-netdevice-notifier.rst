.. -*- coding: utf-8; mode: rst -*-

.. _API-register-netdevice-notifier:

===========================
register_netdevice_notifier
===========================

*man register_netdevice_notifier(9)*

*4.6.0-rc5*

register a network notifier block


Synopsis
========

.. c:function:: int register_netdevice_notifier( struct notifier_block * nb )

Arguments
=========

``nb``
    notifier


Description
===========

Register a notifier to be called when network device events occur. The
notifier passed is linked into the kernel structures and must not be
reused until it has been unregistered. A negative errno code is returned
on a failure.

When registered all registration and up events are replayed to the new
notifier to allow device to have a race free view of the network device
list.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
