.. -*- coding: utf-8; mode: rst -*-

.. _API-media-devnode-unregister:

========================
media_devnode_unregister
========================

*man media_devnode_unregister(9)*

*4.6.0-rc5*

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

This unregisters the passed device. Future open calls will be met with
errors.

This function can safely be called if the device node has never been
registered or has already been unregistered.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
