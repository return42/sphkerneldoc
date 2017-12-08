.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_mn.c

.. _`amdgpu_mn_destroy`:

amdgpu_mn_destroy
=================

.. c:function:: void amdgpu_mn_destroy(struct work_struct *work)

    destroy the rmn

    :param struct work_struct \*work:
        previously sheduled work item

.. _`amdgpu_mn_destroy.description`:

Description
-----------

Lazy destroys the notifier from a work item

.. _`amdgpu_mn_release`:

amdgpu_mn_release
=================

.. c:function:: void amdgpu_mn_release(struct mmu_notifier *mn, struct mm_struct *mm)

    callback to notify about mm destruction

    :param struct mmu_notifier \*mn:
        the mm this callback is about

    :param struct mm_struct \*mm:
        *undescribed*

.. _`amdgpu_mn_release.description`:

Description
-----------

Shedule a work item to lazy destroy our notifier.

.. _`amdgpu_mn_lock`:

amdgpu_mn_lock
==============

.. c:function:: void amdgpu_mn_lock(struct amdgpu_mn *mn)

    take the write side lock for this mn

    :param struct amdgpu_mn \*mn:
        *undescribed*

.. _`amdgpu_mn_unlock`:

amdgpu_mn_unlock
================

.. c:function:: void amdgpu_mn_unlock(struct amdgpu_mn *mn)

    drop the write side lock for this mn

    :param struct amdgpu_mn \*mn:
        *undescribed*

.. _`amdgpu_mn_read_lock`:

amdgpu_mn_read_lock
===================

.. c:function:: void amdgpu_mn_read_lock(struct amdgpu_mn *rmn)

    take the rmn read lock

    :param struct amdgpu_mn \*rmn:
        our notifier

.. _`amdgpu_mn_read_lock.description`:

Description
-----------

Take the rmn read side lock.

.. _`amdgpu_mn_read_unlock`:

amdgpu_mn_read_unlock
=====================

.. c:function:: void amdgpu_mn_read_unlock(struct amdgpu_mn *rmn)

    drop the rmn read lock

    :param struct amdgpu_mn \*rmn:
        our notifier

.. _`amdgpu_mn_read_unlock.description`:

Description
-----------

Drop the rmn read side lock.

.. _`amdgpu_mn_invalidate_node`:

amdgpu_mn_invalidate_node
=========================

.. c:function:: void amdgpu_mn_invalidate_node(struct amdgpu_mn_node *node, unsigned long start, unsigned long end)

    unmap all BOs of a node

    :param struct amdgpu_mn_node \*node:
        the node with the BOs to unmap

    :param unsigned long start:
        *undescribed*

    :param unsigned long end:
        *undescribed*

.. _`amdgpu_mn_invalidate_node.description`:

Description
-----------

We block for all BOs and unmap them by move them
into system domain again.

.. _`amdgpu_mn_invalidate_range_start`:

amdgpu_mn_invalidate_range_start
================================

.. c:function:: void amdgpu_mn_invalidate_range_start(struct mmu_notifier *mn, struct mm_struct *mm, unsigned long start, unsigned long end)

    callback to notify about mm change

    :param struct mmu_notifier \*mn:
        the mm this callback is about

    :param struct mm_struct \*mm:
        *undescribed*

    :param unsigned long start:
        start of updated range

    :param unsigned long end:
        end of updated range

.. _`amdgpu_mn_invalidate_range_start.description`:

Description
-----------

We block for all BOs between start and end to be idle and
unmap them by move them into system domain again.

.. _`amdgpu_mn_invalidate_range_end`:

amdgpu_mn_invalidate_range_end
==============================

.. c:function:: void amdgpu_mn_invalidate_range_end(struct mmu_notifier *mn, struct mm_struct *mm, unsigned long start, unsigned long end)

    callback to notify about mm change

    :param struct mmu_notifier \*mn:
        the mm this callback is about

    :param struct mm_struct \*mm:
        *undescribed*

    :param unsigned long start:
        start of updated range

    :param unsigned long end:
        end of updated range

.. _`amdgpu_mn_invalidate_range_end.description`:

Description
-----------

Release the lock again to allow new command submissions.

.. _`amdgpu_mn_get`:

amdgpu_mn_get
=============

.. c:function:: struct amdgpu_mn *amdgpu_mn_get(struct amdgpu_device *adev)

    create notifier context

    :param struct amdgpu_device \*adev:
        amdgpu device pointer

.. _`amdgpu_mn_get.description`:

Description
-----------

Creates a notifier context for current->mm.

.. _`amdgpu_mn_register`:

amdgpu_mn_register
==================

.. c:function:: int amdgpu_mn_register(struct amdgpu_bo *bo, unsigned long addr)

    register a BO for notifier updates

    :param struct amdgpu_bo \*bo:
        amdgpu buffer object

    :param unsigned long addr:
        userptr addr we should monitor

.. _`amdgpu_mn_register.description`:

Description
-----------

Registers an MMU notifier for the given BO at the specified address.
Returns 0 on success, -ERRNO if anything goes wrong.

.. _`amdgpu_mn_unregister`:

amdgpu_mn_unregister
====================

.. c:function:: void amdgpu_mn_unregister(struct amdgpu_bo *bo)

    unregister a BO for notifier updates

    :param struct amdgpu_bo \*bo:
        amdgpu buffer object

.. _`amdgpu_mn_unregister.description`:

Description
-----------

Remove any registration of MMU notifier updates from the buffer object.

.. This file was automatic generated / don't edit.

