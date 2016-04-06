
.. _API-drm-gem-object-free:

===================
drm_gem_object_free
===================

*man drm_gem_object_free(9)*

*4.6.0-rc1*

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

Called after the last reference to the object has been lost. Must be called holding struct_ mutex

Frees the object
