.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/ttm/ttm_bo_util.c

.. _`ttm_kmap_atomic_prot`:

ttm_kmap_atomic_prot
====================

.. c:function:: void *ttm_kmap_atomic_prot(struct page *page, pgprot_t prot)

    Efficient kernel map of a single page with specified page protection.

    :param struct page \*page:
        The page to map.

    :param pgprot_t prot:
        The page protection.

.. _`ttm_kmap_atomic_prot.description`:

Description
-----------

This function maps a TTM page using the kmap_atomic api if available,
otherwise falls back to vmap. The user must make sure that the
specified page does not have an aliased mapping with a different caching
policy unless the architecture explicitly allows it. Also mapping and
unmapping using this api must be correctly nested. Unmapping should
occur in the reverse order of mapping.

.. _`ttm_kunmap_atomic_prot`:

ttm_kunmap_atomic_prot
======================

.. c:function:: void ttm_kunmap_atomic_prot(void *addr, pgprot_t prot)

    Unmap a page that was mapped using ttm_kmap_atomic_prot.

    :param void \*addr:
        The virtual address from the map.

    :param pgprot_t prot:
        The page protection.

.. _`ttm_buffer_object_transfer`:

ttm_buffer_object_transfer
==========================

.. c:function:: int ttm_buffer_object_transfer(struct ttm_buffer_object *bo, struct ttm_buffer_object **new_obj)

    :param struct ttm_buffer_object \*bo:
        A pointer to a struct ttm_buffer_object.

    :param struct ttm_buffer_object \*\*new_obj:
        A pointer to a pointer to a newly created ttm_buffer_object,
        holding the data of \ ``bo``\  with the old placement.

.. _`ttm_buffer_object_transfer.description`:

Description
-----------

This is a utility function that may be called after an accelerated move
has been scheduled. A new buffer object is created as a placeholder for
the old data while it's being copied. When that buffer object is idle,
it can be destroyed, releasing the space of the old placement.

.. _`ttm_buffer_object_transfer.return`:

Return
------

!0: Failure.

.. This file was automatic generated / don't edit.

