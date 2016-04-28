.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-property-lookup-blob:

========================
drm_property_lookup_blob
========================

*man drm_property_lookup_blob(9)*

*4.6.0-rc5*

look up a blob property and take a reference


Synopsis
========

.. c:function:: struct drm_property_blob * drm_property_lookup_blob( struct drm_device * dev, uint32_t id )

Arguments
=========

``dev``
    drm device

``id``
    id of the blob property


Description
===========

If successful, this takes an additional reference to the blob property.
callers need to make sure to eventually unreference the returned
property again, using ``drm_property_unreference_blob``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
