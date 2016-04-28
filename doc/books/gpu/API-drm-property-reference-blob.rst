.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-property-reference-blob:

===========================
drm_property_reference_blob
===========================

*man drm_property_reference_blob(9)*

*4.6.0-rc5*

Take a reference on an existing property


Synopsis
========

.. c:function:: struct drm_property_blob * drm_property_reference_blob( struct drm_property_blob * blob )

Arguments
=========

``blob``
    Pointer to blob property


Description
===========

Take a new reference on an existing blob property.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
