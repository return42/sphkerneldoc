
.. _API-struct-drm-modeset-lock:

=======================
struct drm_modeset_lock
=======================

*man struct drm_modeset_lock(9)*

*4.6.0-rc1*

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
    used to hold it's place on state->locked list when part of an atomic update


Description
===========

Used for locking CRTCs and other modeset resources.
