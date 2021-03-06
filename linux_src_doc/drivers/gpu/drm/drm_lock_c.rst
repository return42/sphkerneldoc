.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_lock.c

.. _`drm_lock_take`:

drm_lock_take
=============

.. c:function:: int drm_lock_take(struct drm_lock_data *lock_data, unsigned int context)

    :param lock_data:
        *undescribed*
    :type lock_data: struct drm_lock_data \*

    :param context:
        *undescribed*
    :type context: unsigned int

.. _`drm_lock_take.description`:

Description
-----------

\param lock lock pointer.
\param context locking context.
\return one if the lock is held, or zero otherwise.

Attempt to mark the lock as held by the given context, via the \p cmpxchg instruction.

.. _`drm_lock_transfer`:

drm_lock_transfer
=================

.. c:function:: int drm_lock_transfer(struct drm_lock_data *lock_data, unsigned int context)

    inside \*\_unlock to give lock to kernel before calling \*\_dma_schedule.

    :param lock_data:
        *undescribed*
    :type lock_data: struct drm_lock_data \*

    :param context:
        *undescribed*
    :type context: unsigned int

.. _`drm_lock_transfer.description`:

Description
-----------

\param dev DRM device.
\param lock lock pointer.
\param context locking context.
\return always one.

Resets the lock file pointer.
Marks the lock as held by the given context, via the \p cmpxchg instruction.

.. _`drm_legacy_lock`:

drm_legacy_lock
===============

.. c:function:: int drm_legacy_lock(struct drm_device *dev, void *data, struct drm_file *file_priv)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param data:
        *undescribed*
    :type data: void \*

    :param file_priv:
        *undescribed*
    :type file_priv: struct drm_file \*

.. _`drm_legacy_lock.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg user argument, pointing to a drm_lock structure.
\return zero on success or negative number on failure.

Add the current task to the lock wait queue, and attempt to take to lock.

.. _`drm_legacy_unlock`:

drm_legacy_unlock
=================

.. c:function:: int drm_legacy_unlock(struct drm_device *dev, void *data, struct drm_file *file_priv)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param data:
        *undescribed*
    :type data: void \*

    :param file_priv:
        *undescribed*
    :type file_priv: struct drm_file \*

.. _`drm_legacy_unlock.description`:

Description
-----------

\param inode device inode.
\param file_priv DRM file private.
\param cmd command.
\param arg user argument, pointing to a drm_lock structure.
\return zero on success or negative number on failure.

Transfer and free the lock.

.. _`drm_legacy_idlelock_take`:

drm_legacy_idlelock_take
========================

.. c:function:: void drm_legacy_idlelock_take(struct drm_lock_data *lock_data)

    with the kernel context if it is free, otherwise it gets the highest priority when and if it is eventually released.

    :param lock_data:
        *undescribed*
    :type lock_data: struct drm_lock_data \*

.. _`drm_legacy_idlelock_take.description`:

Description
-----------

This guarantees that the kernel will \_eventually\_ have the lock \_unless\_ it is held
by a blocked process. (In the latter case an explicit wait for the hardware lock would cause
a deadlock, which is why the "idlelock" was invented).

This should be sufficient to wait for GPU idle without
having to worry about starvation.

.. This file was automatic generated / don't edit.

