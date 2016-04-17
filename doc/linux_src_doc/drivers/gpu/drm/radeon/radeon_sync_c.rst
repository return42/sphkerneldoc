.. -*- coding: utf-8; mode: rst -*-

=============
radeon_sync.c
=============


.. _`radeon_sync_create`:

radeon_sync_create
==================

.. c:function:: void radeon_sync_create (struct radeon_sync *sync)

    zero init sync object

    :param struct radeon_sync \*sync:
        sync object to initialize



.. _`radeon_sync_create.description`:

Description
-----------

Just clear the sync object for now.



.. _`radeon_sync_fence`:

radeon_sync_fence
=================

.. c:function:: void radeon_sync_fence (struct radeon_sync *sync, struct radeon_fence *fence)

    use the semaphore to sync to a fence

    :param struct radeon_sync \*sync:
        sync object to add fence to

    :param struct radeon_fence \*fence:
        fence to sync to



.. _`radeon_sync_fence.description`:

Description
-----------

Sync to the fence using the semaphore objects



.. _`radeon_sync_resv`:

radeon_sync_resv
================

.. c:function:: int radeon_sync_resv (struct radeon_device *rdev, struct radeon_sync *sync, struct reservation_object *resv, bool shared)

    use the semaphores to sync to a reservation object

    :param struct radeon_device \*rdev:

        *undescribed*

    :param struct radeon_sync \*sync:
        sync object to add fences from reservation object to

    :param struct reservation_object \*resv:
        reservation object with embedded fence

    :param bool shared:
        true if we should only sync to the exclusive fence



.. _`radeon_sync_resv.description`:

Description
-----------

Sync to the fence using the semaphore objects



.. _`radeon_sync_rings`:

radeon_sync_rings
=================

.. c:function:: int radeon_sync_rings (struct radeon_device *rdev, struct radeon_sync *sync, int ring)

    sync ring to all registered fences

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_sync \*sync:
        sync object to use

    :param int ring:
        ring that needs sync



.. _`radeon_sync_rings.description`:

Description
-----------

Ensure that all registered fences are signaled before letting
the ring continue. The caller must hold the ring lock.



.. _`radeon_sync_free`:

radeon_sync_free
================

.. c:function:: void radeon_sync_free (struct radeon_device *rdev, struct radeon_sync *sync, struct radeon_fence *fence)

    free the sync object

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_sync \*sync:
        sync object to use

    :param struct radeon_fence \*fence:
        fence to use for the free



.. _`radeon_sync_free.description`:

Description
-----------

Free the sync object by freeing all semaphores in it.

