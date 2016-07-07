.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_sync.c

.. _`amdgpu_sync_create`:

amdgpu_sync_create
==================

.. c:function:: void amdgpu_sync_create(struct amdgpu_sync *sync)

    zero init sync object

    :param struct amdgpu_sync \*sync:
        sync object to initialize

.. _`amdgpu_sync_create.description`:

Description
-----------

Just clear the sync object for now.

.. _`amdgpu_sync_same_dev`:

amdgpu_sync_same_dev
====================

.. c:function:: bool amdgpu_sync_same_dev(struct amdgpu_device *adev, struct fence *f)

    test if fence belong to us

    :param struct amdgpu_device \*adev:
        amdgpu device to use for the test

    :param struct fence \*f:
        fence to test

.. _`amdgpu_sync_same_dev.description`:

Description
-----------

Test if the fence was issued by us.

.. _`amdgpu_sync_get_owner`:

amdgpu_sync_get_owner
=====================

.. c:function:: void *amdgpu_sync_get_owner(struct fence *f)

    extract the owner of a fence

    :param struct fence \*f:
        *undescribed*

.. _`amdgpu_sync_get_owner.description`:

Description
-----------

Extract who originally created the fence.

.. _`amdgpu_sync_keep_later`:

amdgpu_sync_keep_later
======================

.. c:function:: void amdgpu_sync_keep_later(struct fence **keep, struct fence *fence)

    Keep the later fence

    :param struct fence \*\*keep:
        existing fence to test

    :param struct fence \*fence:
        new fence

.. _`amdgpu_sync_keep_later.description`:

Description
-----------

Either keep the existing fence or the new one, depending which one is later.

.. _`amdgpu_sync_add_later`:

amdgpu_sync_add_later
=====================

.. c:function:: bool amdgpu_sync_add_later(struct amdgpu_sync *sync, struct fence *f)

    add the fence to the hash

    :param struct amdgpu_sync \*sync:
        sync object to add the fence to

    :param struct fence \*f:
        fence to add

.. _`amdgpu_sync_add_later.description`:

Description
-----------

Tries to add the fence to an existing hash entry. Returns true when an entry
was found, false otherwise.

.. _`amdgpu_sync_fence`:

amdgpu_sync_fence
=================

.. c:function:: int amdgpu_sync_fence(struct amdgpu_device *adev, struct amdgpu_sync *sync, struct fence *f)

    remember to sync to this fence

    :param struct amdgpu_device \*adev:
        *undescribed*

    :param struct amdgpu_sync \*sync:
        sync object to add fence to

    :param struct fence \*f:
        *undescribed*

.. _`amdgpu_sync_resv`:

amdgpu_sync_resv
================

.. c:function:: int amdgpu_sync_resv(struct amdgpu_device *adev, struct amdgpu_sync *sync, struct reservation_object *resv, void *owner)

    sync to a reservation object

    :param struct amdgpu_device \*adev:
        *undescribed*

    :param struct amdgpu_sync \*sync:
        sync object to add fences from reservation object to

    :param struct reservation_object \*resv:
        reservation object with embedded fence

    :param void \*owner:
        *undescribed*

.. _`amdgpu_sync_resv.description`:

Description
-----------

Sync to the fence

.. _`amdgpu_sync_is_idle`:

amdgpu_sync_is_idle
===================

.. c:function:: bool amdgpu_sync_is_idle(struct amdgpu_sync *sync)

    test if all fences are signaled

    :param struct amdgpu_sync \*sync:
        the sync object

.. _`amdgpu_sync_is_idle.description`:

Description
-----------

Returns true if all fences in the sync object are signaled.

.. _`amdgpu_sync_cycle_fences`:

amdgpu_sync_cycle_fences
========================

.. c:function:: int amdgpu_sync_cycle_fences(struct amdgpu_sync *dst, struct amdgpu_sync *src, struct fence *fence)

    move fences from one sync object into another

    :param struct amdgpu_sync \*dst:
        the destination sync object

    :param struct amdgpu_sync \*src:
        the source sync object

    :param struct fence \*fence:
        fence to add to source

.. _`amdgpu_sync_cycle_fences.description`:

Description
-----------

Remove all fences from source and put them into destination and add
fence as new one into source.

.. _`amdgpu_sync_free`:

amdgpu_sync_free
================

.. c:function:: void amdgpu_sync_free(struct amdgpu_sync *sync)

    free the sync object

    :param struct amdgpu_sync \*sync:
        sync object to use

.. _`amdgpu_sync_free.description`:

Description
-----------

Free the sync object.

.. _`amdgpu_sync_init`:

amdgpu_sync_init
================

.. c:function:: int amdgpu_sync_init( void)

    init sync object subsystem

    :param  void:
        no arguments

.. _`amdgpu_sync_init.description`:

Description
-----------

Allocate the slab allocator.

.. _`amdgpu_sync_fini`:

amdgpu_sync_fini
================

.. c:function:: void amdgpu_sync_fini( void)

    fini sync object subsystem

    :param  void:
        no arguments

.. _`amdgpu_sync_fini.description`:

Description
-----------

Free the slab allocator.

.. This file was automatic generated / don't edit.

