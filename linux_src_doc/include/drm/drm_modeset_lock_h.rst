.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_modeset_lock.h

.. _`drm_modeset_acquire_ctx`:

struct drm_modeset_acquire_ctx
==============================

.. c:type:: struct drm_modeset_acquire_ctx

    locking context (see ww_acquire_ctx)

.. _`drm_modeset_acquire_ctx.definition`:

Definition
----------

.. code-block:: c

    struct drm_modeset_acquire_ctx {
        struct ww_acquire_ctx ww_ctx;
        struct drm_modeset_lock *contended;
        struct list_head locked;
        bool trylock_only;
        bool interruptible;
    }

.. _`drm_modeset_acquire_ctx.members`:

Members
-------

ww_ctx
    base acquire ctx

contended
    used internally for -EDEADLK handling

locked
    list of held locks

trylock_only
    trylock mode used in atomic contexts/panic notifiers

interruptible
    whether interruptible locking should be used.

.. _`drm_modeset_acquire_ctx.description`:

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

.. _`drm_modeset_lock.definition`:

Definition
----------

.. code-block:: c

    struct drm_modeset_lock {
        struct ww_mutex mutex;
        struct list_head head;
    }

.. _`drm_modeset_lock.members`:

Members
-------

mutex
    resource locking

head
    used to hold it's place on \ :c:type:`drm_atomi_state.locked <drm_atomi_state>`\  list when
    part of an atomic update

.. _`drm_modeset_lock.description`:

Description
-----------

Used for locking CRTCs and other modeset resources.

.. _`drm_modeset_lock_fini`:

drm_modeset_lock_fini
=====================

.. c:function:: void drm_modeset_lock_fini(struct drm_modeset_lock *lock)

    cleanup lock

    :param lock:
        lock to cleanup
    :type lock: struct drm_modeset_lock \*

.. _`drm_modeset_is_locked`:

drm_modeset_is_locked
=====================

.. c:function:: bool drm_modeset_is_locked(struct drm_modeset_lock *lock)

    equivalent to \ :c:func:`mutex_is_locked`\ 

    :param lock:
        lock to check
    :type lock: struct drm_modeset_lock \*

.. This file was automatic generated / don't edit.

