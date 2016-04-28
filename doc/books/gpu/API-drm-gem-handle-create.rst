.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-handle-create:

=====================
drm_gem_handle_create
=====================

*man drm_gem_handle_create(9)*

*4.6.0-rc5*

create a gem handle for an object


Synopsis
========

.. c:function:: int drm_gem_handle_create( struct drm_file * file_priv, struct drm_gem_object * obj, u32 * handlep )

Arguments
=========

``file_priv``
    drm file-private structure to register the handle for

``obj``
    object to register

``handlep``
    pionter to return the created handle to the caller


Description
===========

Create a handle for this object. This adds a handle reference to the
object, which includes a regular reference count. Callers will likely
want to dereference the object afterwards.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
