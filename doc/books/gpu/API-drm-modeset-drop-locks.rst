.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-modeset-drop-locks:

======================
drm_modeset_drop_locks
======================

*man drm_modeset_drop_locks(9)*

*4.6.0-rc5*

drop all locks


Synopsis
========

.. c:function:: void drm_modeset_drop_locks( struct drm_modeset_acquire_ctx * ctx )

Arguments
=========

``ctx``
    the acquire context


Description
===========

Drop all locks currently held against this acquire context.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
