.. -*- coding: utf-8; mode: rst -*-

.. _API-of-drm-find-bridge:

==================
of_drm_find_bridge
==================

*man of_drm_find_bridge(9)*

*4.6.0-rc5*

find the bridge corresponding to the device node in the global bridge
list


Synopsis
========

.. c:function:: struct drm_bridge * of_drm_find_bridge( struct device_node * np )

Arguments
=========

``np``
    device node


RETURNS
=======

drm_bridge control struct on success, NULL on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
