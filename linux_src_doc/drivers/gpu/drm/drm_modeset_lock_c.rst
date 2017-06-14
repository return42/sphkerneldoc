.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_modeset_lock.c

.. _`kms-locking`:

kms locking
===========

As KMS moves toward more fine grained locking, and atomic ioctl where
userspace can indirectly control locking order, it becomes necessary
to use \ :c:type:`struct ww_mutex <ww_mutex>`\  and acquire-contexts to avoid deadlocks.  But because
the locking is more distributed around the driver code, we want a bit
of extra utility/tracking out of our acquire-ctx.  This is provided
by \ :c:type:`struct drm_modeset_lock <drm_modeset_lock>`\  and \ :c:type:`struct drm_modeset_acquire_ctx <drm_modeset_acquire_ctx>`\ .

For basic principles of \ :c:type:`struct ww_mutex <ww_mutex>`\ , see: Documentation/locking/ww-mutex-design.txt

The basic usage pattern is to::

    drm_modeset_acquire_init(&ctx)
    retry:
    foreach (lock in random_ordered_set_of_locks) {
        ret = drm_modeset_lock(lock, \ :c:type:`struct ctx <ctx>`\ )
        if (ret == -EDEADLK) {
            drm_modeset_backoff(&ctx);
            goto retry;
        }
    }
    ... do stuff ...
    drm_modeset_drop_locks(&ctx);
    drm_modeset_acquire_fini(&ctx);

On top of of these per-object locks using \ :c:type:`struct ww_mutex <ww_mutex>`\  there's also an overall
\ :c:type:`drm_mode_config.mutex <drm_mode_config>`\ , for protecting everything else. Mostly this means
probe state of connectors, and preventing hotplug add/removal of connectors.

Finally there's a bunch of dedicated locks to protect drm core internal
lists and lookup data structures.

.. _`drm_modeset_lock_all`:

drm_modeset_lock_all
====================

.. c:function:: void drm_modeset_lock_all(struct drm_device *dev)

    take all modeset locks

    :param struct drm_device \*dev:
        DRM device

.. _`drm_modeset_lock_all.description`:

Description
-----------

This function takes all modeset locks, suitable where a more fine-grained
scheme isn't (yet) implemented. Locks must be dropped by calling the
\ :c:func:`drm_modeset_unlock_all`\  function.

This function is deprecated. It allocates a lock acquisition context and
stores it in \ :c:type:`drm_device.mode_config <drm_device>`\ . This facilitate conversion of
existing code because it removes the need to manually deal with the
acquisition context, but it is also brittle because the context is global
and care must be taken not to nest calls. New code should use the
\ :c:func:`drm_modeset_lock_all_ctx`\  function and pass in the context explicitly.

.. _`drm_modeset_unlock_all`:

drm_modeset_unlock_all
======================

.. c:function:: void drm_modeset_unlock_all(struct drm_device *dev)

    drop all modeset locks

    :param struct drm_device \*dev:
        DRM device

.. _`drm_modeset_unlock_all.description`:

Description
-----------

This function drops all modeset locks taken by a previous call to the
\ :c:func:`drm_modeset_lock_all`\  function.

This function is deprecated. It uses the lock acquisition context stored
in \ :c:type:`drm_device.mode_config <drm_device>`\ . This facilitates conversion of existing
code because it removes the need to manually deal with the acquisition
context, but it is also brittle because the context is global and care must
be taken not to nest calls. New code should pass the acquisition context
directly to the \ :c:func:`drm_modeset_drop_locks`\  function.

.. _`drm_warn_on_modeset_not_all_locked`:

drm_warn_on_modeset_not_all_locked
==================================

.. c:function:: void drm_warn_on_modeset_not_all_locked(struct drm_device *dev)

    check that all modeset locks are locked

    :param struct drm_device \*dev:
        device

.. _`drm_warn_on_modeset_not_all_locked.description`:

Description
-----------

Useful as a debug assert.

.. _`drm_modeset_acquire_init`:

drm_modeset_acquire_init
========================

.. c:function:: void drm_modeset_acquire_init(struct drm_modeset_acquire_ctx *ctx, uint32_t flags)

    initialize acquire context

    :param struct drm_modeset_acquire_ctx \*ctx:
        the acquire context

    :param uint32_t flags:
        for future

.. _`drm_modeset_acquire_fini`:

drm_modeset_acquire_fini
========================

.. c:function:: void drm_modeset_acquire_fini(struct drm_modeset_acquire_ctx *ctx)

    cleanup acquire context

    :param struct drm_modeset_acquire_ctx \*ctx:
        the acquire context

.. _`drm_modeset_drop_locks`:

drm_modeset_drop_locks
======================

.. c:function:: void drm_modeset_drop_locks(struct drm_modeset_acquire_ctx *ctx)

    drop all locks

    :param struct drm_modeset_acquire_ctx \*ctx:
        the acquire context

.. _`drm_modeset_drop_locks.description`:

Description
-----------

Drop all locks currently held against this acquire context.

.. _`drm_modeset_backoff`:

drm_modeset_backoff
===================

.. c:function:: void drm_modeset_backoff(struct drm_modeset_acquire_ctx *ctx)

    deadlock avoidance backoff

    :param struct drm_modeset_acquire_ctx \*ctx:
        the acquire context

.. _`drm_modeset_backoff.description`:

Description
-----------

If deadlock is detected (ie. \ :c:func:`drm_modeset_lock`\  returns -EDEADLK),
you must call this function to drop all currently held locks and
block until the contended lock becomes available.

.. _`drm_modeset_backoff_interruptible`:

drm_modeset_backoff_interruptible
=================================

.. c:function:: int drm_modeset_backoff_interruptible(struct drm_modeset_acquire_ctx *ctx)

    deadlock avoidance backoff

    :param struct drm_modeset_acquire_ctx \*ctx:
        the acquire context

.. _`drm_modeset_backoff_interruptible.description`:

Description
-----------

Interruptible version of \ :c:func:`drm_modeset_backoff`\ 

.. _`drm_modeset_lock_init`:

drm_modeset_lock_init
=====================

.. c:function:: void drm_modeset_lock_init(struct drm_modeset_lock *lock)

    initialize lock

    :param struct drm_modeset_lock \*lock:
        lock to init

.. _`drm_modeset_lock`:

drm_modeset_lock
================

.. c:function:: int drm_modeset_lock(struct drm_modeset_lock *lock, struct drm_modeset_acquire_ctx *ctx)

    take modeset lock

    :param struct drm_modeset_lock \*lock:
        lock to take

    :param struct drm_modeset_acquire_ctx \*ctx:
        acquire ctx

.. _`drm_modeset_lock.description`:

Description
-----------

If ctx is not NULL, then its ww acquire context is used and the
lock will be tracked by the context and can be released by calling
\ :c:func:`drm_modeset_drop_locks`\ .  If -EDEADLK is returned, this means a
deadlock scenario has been detected and it is an error to attempt
to take any more locks without first calling \ :c:func:`drm_modeset_backoff`\ .

.. _`drm_modeset_lock_interruptible`:

drm_modeset_lock_interruptible
==============================

.. c:function:: int drm_modeset_lock_interruptible(struct drm_modeset_lock *lock, struct drm_modeset_acquire_ctx *ctx)

    take modeset lock

    :param struct drm_modeset_lock \*lock:
        lock to take

    :param struct drm_modeset_acquire_ctx \*ctx:
        acquire ctx

.. _`drm_modeset_lock_interruptible.description`:

Description
-----------

Interruptible version of \ :c:func:`drm_modeset_lock`\ 

.. _`drm_modeset_unlock`:

drm_modeset_unlock
==================

.. c:function:: void drm_modeset_unlock(struct drm_modeset_lock *lock)

    drop modeset lock

    :param struct drm_modeset_lock \*lock:
        lock to release

.. _`drm_modeset_lock_all_ctx`:

drm_modeset_lock_all_ctx
========================

.. c:function:: int drm_modeset_lock_all_ctx(struct drm_device *dev, struct drm_modeset_acquire_ctx *ctx)

    take all modeset locks

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_modeset_acquire_ctx \*ctx:
        lock acquisition context

.. _`drm_modeset_lock_all_ctx.description`:

Description
-----------

This function takes all modeset locks, suitable where a more fine-grained
scheme isn't (yet) implemented.

Unlike \ :c:func:`drm_modeset_lock_all`\ , it doesn't take the \ :c:type:`drm_mode_config.mutex <drm_mode_config>`\ 
since that lock isn't required for modeset state changes. Callers which
need to grab that lock too need to do so outside of the acquire context
\ ``ctx``\ .

Locks acquired with this function should be released by calling the
\ :c:func:`drm_modeset_drop_locks`\  function on \ ``ctx``\ .

.. _`drm_modeset_lock_all_ctx.return`:

Return
------

0 on success or a negative error-code on failure.

.. This file was automatic generated / don't edit.

