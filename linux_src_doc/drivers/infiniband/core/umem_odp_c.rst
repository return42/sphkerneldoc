.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/core/umem_odp.c

.. _`ib_umem_odp_map_dma_pages`:

ib_umem_odp_map_dma_pages
=========================

.. c:function:: int ib_umem_odp_map_dma_pages(struct ib_umem_odp *umem_odp, u64 user_virt, u64 bcnt, u64 access_mask, unsigned long current_seq)

    Pin and DMA map userspace memory in an ODP MR.

    :param umem_odp:
        the umem to map and pin
    :type umem_odp: struct ib_umem_odp \*

    :param user_virt:
        the address from which we need to map.
    :type user_virt: u64

    :param bcnt:
        the minimal number of bytes to pin and map. The mapping might be
        bigger due to alignment, and may also be smaller in case of an error
        pinning or mapping a page. The actual pages mapped is returned in
        the return value.
    :type bcnt: u64

    :param access_mask:
        bit mask of the requested access permissions for the given
        range.
    :type access_mask: u64

    :param current_seq:
        the MMU notifiers sequance value for synchronization with
        invalidations. the sequance number is read from
        umem_odp->notifiers_seq before calling this function
    :type current_seq: unsigned long

.. _`ib_umem_odp_map_dma_pages.description`:

Description
-----------

Pins the range of pages passed in the argument, and maps them to
DMA addresses. The DMA addresses of the mapped pages is updated in
umem_odp->dma_list.

Returns the number of pages mapped in success, negative error code
for failure.
An -EAGAIN error code is returned when a concurrent mmu notifier prevents
the function from completing its task.
An -ENOENT error code indicates that userspace process is being terminated
and mm was already destroyed.

.. This file was automatic generated / don't edit.

