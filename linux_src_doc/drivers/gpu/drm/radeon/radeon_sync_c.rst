.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_sync.c

.. _`radeon_sync_create`:

radeon_sync_create
==================

.. c:function:: void radeon_sync_create(struct radeon_sync *sync)

    zero init sync object

    :param sync:
        sync object to initialize
    :type sync: struct radeon_sync \*

.. _`radeon_sync_create.description`:

Description
-----------

Just clear the sync object for now.

.. _`radeon_sync_fence`:

radeon_sync_fence
=================

.. c:function:: void radeon_sync_fence(struct radeon_sync *sync, struct radeon_fence *fence)

    use the semaphore to sync to a fence

    :param sync:
        sync object to add fence to
    :type sync: struct radeon_sync \*

    :param fence:
        fence to sync to
    :type fence: struct radeon_fence \*

.. _`radeon_sync_fence.description`:

Description
-----------

Sync to the fence using the semaphore objects

.. _`radeon_sync_resv`:

radeon_sync_resv
================

.. c:function:: int radeon_sync_resv(struct radeon_device *rdev, struct radeon_sync *sync, struct reservation_object *resv, bool shared)

    use the semaphores to sync to a reservation object

    :param rdev:
        *undescribed*
    :type rdev: struct radeon_device \*

    :param sync:
        sync object to add fences from reservation object to
    :type sync: struct radeon_sync \*

    :param resv:
        reservation object with embedded fence
    :type resv: struct reservation_object \*

    :param shared:
        true if we should only sync to the exclusive fence
    :type shared: bool

.. _`radeon_sync_resv.description`:

Description
-----------

Sync to the fence using the semaphore objects

.. _`radeon_sync_rings`:

radeon_sync_rings
=================

.. c:function:: int radeon_sync_rings(struct radeon_device *rdev, struct radeon_sync *sync, int ring)

    sync ring to all registered fences

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param sync:
        sync object to use
    :type sync: struct radeon_sync \*

    :param ring:
        ring that needs sync
    :type ring: int

.. _`radeon_sync_rings.description`:

Description
-----------

Ensure that all registered fences are signaled before letting
the ring continue. The caller must hold the ring lock.

.. _`radeon_sync_free`:

radeon_sync_free
================

.. c:function:: void radeon_sync_free(struct radeon_device *rdev, struct radeon_sync *sync, struct radeon_fence *fence)

    free the sync object

    :param rdev:
        radeon_device pointer
    :type rdev: struct radeon_device \*

    :param sync:
        sync object to use
    :type sync: struct radeon_sync \*

    :param fence:
        fence to use for the free
    :type fence: struct radeon_fence \*

.. _`radeon_sync_free.description`:

Description
-----------

Free the sync object by freeing all semaphores in it.

.. This file was automatic generated / don't edit.

