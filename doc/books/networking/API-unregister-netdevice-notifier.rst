.. -*- coding: utf-8; mode: rst -*-

.. _API-unregister-netdevice-notifier:

=============================
unregister_netdevice_notifier
=============================

*man unregister_netdevice_notifier(9)*

*4.6.0-rc5*

unregister a network notifier block


Synopsis
========

.. c:function:: int unregister_netdevice_notifier( struct notifier_block * nb )

Arguments
=========

``nb``
    notifier


Description
===========

Unregister a notifier previously registered by
``register_netdevice_notifier``. The notifier is unlinked into the
kernel structures and may then be reused. A negative errno code is
returned on a failure.

After unregistering unregister and down device events are synthesized
for all devices on the device list to the removed notifier to remove the
need for special case cleanup code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
