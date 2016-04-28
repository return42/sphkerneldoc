.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-object-attach-property:

==========================
drm_object_attach_property
==========================

*man drm_object_attach_property(9)*

*4.6.0-rc5*

attach a property to a modeset object


Synopsis
========

.. c:function:: void drm_object_attach_property( struct drm_mode_object * obj, struct drm_property * property, uint64_t init_val )

Arguments
=========

``obj``
    drm modeset object

``property``
    property to attach

``init_val``
    initial value of the property


Description
===========

This attaches the given property to the modeset object with the given
initial value. Currently this function cannot fail since the properties
are stored in a statically sized array.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
