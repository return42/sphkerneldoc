.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-drm-modeset-lock:

=======================
struct drm_modeset_lock
=======================

*man struct drm_modeset_lock(9)*

*4.6.0-rc5*

used for locking modeset resources.


Synopsis
========

.. code-block:: c

    struct drm_modeset_lock {
      struct ww_mutex mutex;
      struct list_head head;
    };


Members
=======

mutex
    resource locking

head
    used to hold it's place on state->locked list when part of an atomic
    update


Description
===========

Used for locking CRTCs and other modeset resources.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
