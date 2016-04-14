.. -*- coding: utf-8; mode: rst -*-

==================
drm_modeset_lock.h
==================

.. _`drm_modeset_acquire_ctx`:

struct drm_modeset_acquire_ctx
==============================

.. c:type:: struct drm_modeset_acquire_ctx

    locking context (see ww_acquire_ctx)



Definition
----------

.. code-block:: c

  struct drm_modeset_acquire_ctx {
    struct ww_acquire_ctx ww_ctx;
    struct drm_modeset_lock * contended;
    struct list_head locked;
    bool trylock_only;
  };



Members
-------

:``ww_ctx``:
    base acquire ctx

:``contended``:
    used internally for -EDEADLK handling

:``locked``:
    list of held locks

:``trylock_only``:
    trylock mode used in atomic contexts/panic notifiers



Description
-----------

Each thread competing for a set of locks must use one acquire
ctx.  And if any lock fxn returns -EDEADLK, it must backoff and
retry.


.. _`drm_modeset_lock`:

struct drm_modeset_lock
=======================

.. c:type:: struct drm_modeset_lock

    used for locking modeset resources.



Definition
----------

.. code-block:: c

  struct drm_modeset_lock {
    struct ww_mutex mutex;
    struct list_head head;
  };



Members
-------

:``mutex``:
    resource locking

:``head``:
    used to hold it's place on state->locked list when
    part of an atomic update



Description
-----------

Used for locking CRTCs and other modeset resources.


.. _`drm_modeset_lock_init`:

drm_modeset_lock_init
=====================

.. c:function:: void drm_modeset_lock_init (struct drm_modeset_lock *lock)

    initialize lock

    :param struct drm_modeset_lock \*lock:
        lock to init


.. _`drm_modeset_lock_fini`:

drm_modeset_lock_fini
=====================

.. c:function:: void drm_modeset_lock_fini (struct drm_modeset_lock *lock)

    cleanup lock

    :param struct drm_modeset_lock \*lock:
        lock to cleanup


.. _`drm_modeset_is_locked`:

drm_modeset_is_locked
=====================

.. c:function:: bool drm_modeset_is_locked (struct drm_modeset_lock *lock)

    equivalent to mutex_is_locked()

    :param struct drm_modeset_lock \*lock:
        lock to check

