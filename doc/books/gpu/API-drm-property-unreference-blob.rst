.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-property-unreference-blob:

=============================
drm_property_unreference_blob
=============================

*man drm_property_unreference_blob(9)*

*4.6.0-rc5*

Unreference a blob property


Synopsis
========

.. c:function:: void drm_property_unreference_blob( struct drm_property_blob * blob )

Arguments
=========

``blob``
    Pointer to blob property


Description
===========

Drop a reference on a blob property. May free the object.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
