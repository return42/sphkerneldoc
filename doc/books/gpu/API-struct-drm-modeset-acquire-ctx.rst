
.. _API-struct-drm-modeset-acquire-ctx:

==============================
struct drm_modeset_acquire_ctx
==============================

*man struct drm_modeset_acquire_ctx(9)*

*4.6.0-rc1*

locking context (see ww_acquire_ctx)


Synopsis
========

.. code-block:: c

    struct drm_modeset_acquire_ctx {
      struct ww_acquire_ctx ww_ctx;
      struct drm_modeset_lock * contended;
      struct list_head locked;
      bool trylock_only;
    };


Members
=======

ww_ctx
    base acquire ctx

contended
    used internally for -EDEADLK handling

locked
    list of held locks

trylock_only
    trylock mode used in atomic contexts/panic notifiers


Description
===========

Each thread competing for a set of locks must use one acquire ctx. And if any lock fxn returns -EDEADLK, it must backoff and retry.
