.. -*- coding: utf-8; mode: rst -*-

.. _API-media-remove-intf-links:

=======================
media_remove_intf_links
=======================

*man media_remove_intf_links(9)*

*4.6.0-rc5*

remove all links associated with an interface


Synopsis
========

.. c:function:: void media_remove_intf_links( struct media_interface * intf )

Arguments
=========

``intf``
    pointer to ``media_interface``


Notes
=====

this is called automatically when an entity is unregistered via
``media_device_register_entity`` and by ``media_devnode_remove``.

Prefer to use this one, instead of ``__media_remove_intf_links``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
