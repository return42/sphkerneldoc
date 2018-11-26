.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_mn.c

.. _`mmu-notifier`:

MMU Notifier
============

For coherent userptr handling registers an MMU notifier to inform the driver
about updates on the page tables of a process.

When somebody tries to invalidate the page tables we block the update until
all operations on the pages in question are completed, then those pages are
marked as accessed and also dirty if it wasn't a read only access.

New command submissions using the userptrs in question are delayed until all
page table invalidation are completed and we once more see a coherent process
address space.

.. _`amdgpu_mn`:

struct amdgpu_mn
================

.. c:type:: struct amdgpu_mn


.. _`amdgpu_mn.definition`:

Definition
----------

.. code-block:: c

    struct amdgpu_mn {
        struct amdgpu_device *adev;
        struct mm_struct *mm;
        struct mmu_notifier mn;
        enum amdgpu_mn_type type;
        struct work_struct work;
        struct hlist_node node;
        struct rw_semaphore lock;
        struct rb_root_cached objects;
        struct mutex read_lock;
        atomic_t recursion;
    }

.. _`amdgpu_mn.members`:

Members
-------

adev
    amdgpu device pointer

mm
    process address space

mn
    MMU notifier structure

type
    type of MMU notifier

work
    destruction work item

node
    hash table node to find structure by adev and mn

lock
    rw semaphore protecting the notifier nodes

objects
    interval tree containing amdgpu_mn_nodes

read_lock
    mutex for recursive locking of \ ``lock``\ 

recursion
    depth of recursion

.. _`amdgpu_mn.description`:

Description
-----------

Data for each amdgpu device and process address space.

.. _`amdgpu_mn_node`:

struct amdgpu_mn_node
=====================

.. c:type:: struct amdgpu_mn_node


.. _`amdgpu_mn_node.definition`:

Definition
----------

.. code-block:: c

    struct amdgpu_mn_node {
        struct interval_tree_node it;
        struct list_head bos;
    }

.. _`amdgpu_mn_node.members`:

Members
-------

it
    interval node defining start-last of the affected address range

bos
    list of all BOs in the affected address range

.. _`amdgpu_mn_node.description`:

Description
-----------

Manages all BOs which are affected of a certain range of address space.

.. _`amdgpu_mn_destroy`:

amdgpu_mn_destroy
=================

.. c:function:: void amdgpu_mn_destroy(struct work_struct *work)

    destroy the MMU notifier

    :param work:
        previously sheduled work item
    :type work: struct work_struct \*

.. _`amdgpu_mn_destroy.description`:

Description
-----------

Lazy destroys the notifier from a work item

.. _`amdgpu_mn_release`:

amdgpu_mn_release
=================

.. c:function:: void amdgpu_mn_release(struct mmu_notifier *mn, struct mm_struct *mm)

    callback to notify about mm destruction

    :param mn:
        our notifier
    :type mn: struct mmu_notifier \*

    :param mm:
        the mm this callback is about
    :type mm: struct mm_struct \*

.. _`amdgpu_mn_release.description`:

Description
-----------

Shedule a work item to lazy destroy our notifier.

.. _`amdgpu_mn_lock`:

amdgpu_mn_lock
==============

.. c:function:: void amdgpu_mn_lock(struct amdgpu_mn *mn)

    take the write side lock for this notifier

    :param mn:
        our notifier
    :type mn: struct amdgpu_mn \*

.. _`amdgpu_mn_unlock`:

amdgpu_mn_unlock
================

.. c:function:: void amdgpu_mn_unlock(struct amdgpu_mn *mn)

    drop the write side lock for this notifier

    :param mn:
        our notifier
    :type mn: struct amdgpu_mn \*

.. _`amdgpu_mn_read_lock`:

amdgpu_mn_read_lock
===================

.. c:function:: int amdgpu_mn_read_lock(struct amdgpu_mn *amn, bool blockable)

    take the read side lock for this notifier

    :param amn:
        our notifier
    :type amn: struct amdgpu_mn \*

    :param blockable:
        *undescribed*
    :type blockable: bool

.. _`amdgpu_mn_read_unlock`:

amdgpu_mn_read_unlock
=====================

.. c:function:: void amdgpu_mn_read_unlock(struct amdgpu_mn *amn)

    drop the read side lock for this notifier

    :param amn:
        our notifier
    :type amn: struct amdgpu_mn \*

.. _`amdgpu_mn_invalidate_node`:

amdgpu_mn_invalidate_node
=========================

.. c:function:: void amdgpu_mn_invalidate_node(struct amdgpu_mn_node *node, unsigned long start, unsigned long end)

    unmap all BOs of a node

    :param node:
        the node with the BOs to unmap
    :type node: struct amdgpu_mn_node \*

    :param start:
        start of address range affected
    :type start: unsigned long

    :param end:
        end of address range affected
    :type end: unsigned long

.. _`amdgpu_mn_invalidate_node.description`:

Description
-----------

Block for operations on BOs to finish and mark pages as accessed and
potentially dirty.

.. _`amdgpu_mn_invalidate_range_start_gfx`:

amdgpu_mn_invalidate_range_start_gfx
====================================

.. c:function:: int amdgpu_mn_invalidate_range_start_gfx(struct mmu_notifier *mn, struct mm_struct *mm, unsigned long start, unsigned long end, bool blockable)

    callback to notify about mm change

    :param mn:
        our notifier
    :type mn: struct mmu_notifier \*

    :param mm:
        the mm this callback is about
    :type mm: struct mm_struct \*

    :param start:
        start of updated range
    :type start: unsigned long

    :param end:
        end of updated range
    :type end: unsigned long

    :param blockable:
        *undescribed*
    :type blockable: bool

.. _`amdgpu_mn_invalidate_range_start_gfx.description`:

Description
-----------

Block for operations on BOs to finish and mark pages as accessed and
potentially dirty.

.. _`amdgpu_mn_invalidate_range_start_hsa`:

amdgpu_mn_invalidate_range_start_hsa
====================================

.. c:function:: int amdgpu_mn_invalidate_range_start_hsa(struct mmu_notifier *mn, struct mm_struct *mm, unsigned long start, unsigned long end, bool blockable)

    callback to notify about mm change

    :param mn:
        our notifier
    :type mn: struct mmu_notifier \*

    :param mm:
        the mm this callback is about
    :type mm: struct mm_struct \*

    :param start:
        start of updated range
    :type start: unsigned long

    :param end:
        end of updated range
    :type end: unsigned long

    :param blockable:
        *undescribed*
    :type blockable: bool

.. _`amdgpu_mn_invalidate_range_start_hsa.description`:

Description
-----------

We temporarily evict all BOs between start and end. This
necessitates evicting all user-mode queues of the process. The BOs
are restorted in amdgpu_mn_invalidate_range_end_hsa.

.. _`amdgpu_mn_invalidate_range_end`:

amdgpu_mn_invalidate_range_end
==============================

.. c:function:: void amdgpu_mn_invalidate_range_end(struct mmu_notifier *mn, struct mm_struct *mm, unsigned long start, unsigned long end)

    callback to notify about mm change

    :param mn:
        our notifier
    :type mn: struct mmu_notifier \*

    :param mm:
        the mm this callback is about
    :type mm: struct mm_struct \*

    :param start:
        start of updated range
    :type start: unsigned long

    :param end:
        end of updated range
    :type end: unsigned long

.. _`amdgpu_mn_invalidate_range_end.description`:

Description
-----------

Release the lock again to allow new command submissions.

.. _`amdgpu_mn_get`:

amdgpu_mn_get
=============

.. c:function:: struct amdgpu_mn *amdgpu_mn_get(struct amdgpu_device *adev, enum amdgpu_mn_type type)

    create notifier context

    :param adev:
        amdgpu device pointer
    :type adev: struct amdgpu_device \*

    :param type:
        type of MMU notifier context
    :type type: enum amdgpu_mn_type

.. _`amdgpu_mn_get.description`:

Description
-----------

Creates a notifier context for current->mm.

.. _`amdgpu_mn_register`:

amdgpu_mn_register
==================

.. c:function:: int amdgpu_mn_register(struct amdgpu_bo *bo, unsigned long addr)

    register a BO for notifier updates

    :param bo:
        amdgpu buffer object
    :type bo: struct amdgpu_bo \*

    :param addr:
        userptr addr we should monitor
    :type addr: unsigned long

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

    :param bo:
        amdgpu buffer object
    :type bo: struct amdgpu_bo \*

.. _`amdgpu_mn_unregister.description`:

Description
-----------

Remove any registration of MMU notifier updates from the buffer object.

.. This file was automatic generated / don't edit.

