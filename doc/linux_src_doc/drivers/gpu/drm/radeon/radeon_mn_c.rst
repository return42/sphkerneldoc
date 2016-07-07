.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_mn.c

.. _`radeon_mn_destroy`:

radeon_mn_destroy
=================

.. c:function:: void radeon_mn_destroy(struct work_struct *work)

    destroy the rmn

    :param struct work_struct \*work:
        previously sheduled work item

.. _`radeon_mn_destroy.description`:

Description
-----------

Lazy destroys the notifier from a work item

.. _`radeon_mn_release`:

radeon_mn_release
=================

.. c:function:: void radeon_mn_release(struct mmu_notifier *mn, struct mm_struct *mm)

    callback to notify about mm destruction

    :param struct mmu_notifier \*mn:
        the mm this callback is about

    :param struct mm_struct \*mm:
        *undescribed*

.. _`radeon_mn_release.description`:

Description
-----------

Shedule a work item to lazy destroy our notifier.

.. _`radeon_mn_invalidate_range_start`:

radeon_mn_invalidate_range_start
================================

.. c:function:: void radeon_mn_invalidate_range_start(struct mmu_notifier *mn, struct mm_struct *mm, unsigned long start, unsigned long end)

    callback to notify about mm change

    :param struct mmu_notifier \*mn:
        the mm this callback is about

    :param struct mm_struct \*mm:
        *undescribed*

    :param unsigned long start:
        start of updated range

    :param unsigned long end:
        end of updated range

.. _`radeon_mn_invalidate_range_start.description`:

Description
-----------

We block for all BOs between start and end to be idle and
unmap them by move them into system domain again.

.. _`radeon_mn_get`:

radeon_mn_get
=============

.. c:function:: struct radeon_mn *radeon_mn_get(struct radeon_device *rdev)

    create notifier context

    :param struct radeon_device \*rdev:
        radeon device pointer

.. _`radeon_mn_get.description`:

Description
-----------

Creates a notifier context for current->mm.

.. _`radeon_mn_register`:

radeon_mn_register
==================

.. c:function:: int radeon_mn_register(struct radeon_bo *bo, unsigned long addr)

    register a BO for notifier updates

    :param struct radeon_bo \*bo:
        radeon buffer object

    :param unsigned long addr:
        userptr addr we should monitor

.. _`radeon_mn_register.description`:

Description
-----------

Registers an MMU notifier for the given BO at the specified address.
Returns 0 on success, -ERRNO if anything goes wrong.

.. _`radeon_mn_unregister`:

radeon_mn_unregister
====================

.. c:function:: void radeon_mn_unregister(struct radeon_bo *bo)

    unregister a BO for notifier updates

    :param struct radeon_bo \*bo:
        radeon buffer object

.. _`radeon_mn_unregister.description`:

Description
-----------

Remove any registration of MMU notifier updates from the buffer object.

.. This file was automatic generated / don't edit.

