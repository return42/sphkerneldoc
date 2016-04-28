.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-object-free:

===================
drm_gem_object_free
===================

*man drm_gem_object_free(9)*

*4.6.0-rc5*

free a GEM object


Synopsis
========

.. c:function:: void drm_gem_object_free( struct kref * kref )

Arguments
=========

``kref``
    kref of the object to free


Description
===========

Called after the last reference to the object has been lost. Must be
called holding struct_ mutex

Frees the object


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
