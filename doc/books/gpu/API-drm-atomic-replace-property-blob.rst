.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-replace-property-blob:

================================
drm_atomic_replace_property_blob
================================

*man drm_atomic_replace_property_blob(9)*

*4.6.0-rc5*

replace a blob property


Synopsis
========

.. c:function:: void drm_atomic_replace_property_blob( struct drm_property_blob ** blob, struct drm_property_blob * new_blob, bool * replaced )

Arguments
=========

``blob``
    a pointer to the member blob to be replaced

``new_blob``
    the new blob to replace with

``replaced``
    whether the blob has been replaced


RETURNS
=======

Zero on success, error code on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
