
.. _API-media-devnode-unregister:

========================
media_devnode_unregister
========================

*man media_devnode_unregister(9)*

*4.6.0-rc1*

unregister a media device node


Synopsis
========

.. c:function:: void media_devnode_unregister( struct media_devnode * mdev )

Arguments
=========

``mdev``
    the device node to unregister


Description
===========

This unregisters the passed device. Future open calls will be met with errors.

This function can safely be called if the device node has never been registered or has already been unregistered.
