.. -*- coding: utf-8; mode: rst -*-

==========
umem_odp.c
==========


.. _`ib_umem_odp_map_dma_pages`:

ib_umem_odp_map_dma_pages
=========================

.. c:function:: int ib_umem_odp_map_dma_pages (struct ib_umem *umem, u64 user_virt, u64 bcnt, u64 access_mask, unsigned long current_seq)

    Pin and DMA map userspace memory in an ODP MR.

    :param struct ib_umem \*umem:
        the umem to map and pin

    :param u64 user_virt:
        the address from which we need to map.

    :param u64 bcnt:
        the minimal number of bytes to pin and map. The mapping might be
        bigger due to alignment, and may also be smaller in case of an error
        pinning or mapping a page. The actual pages mapped is returned in
        the return value.

    :param u64 access_mask:
        bit mask of the requested access permissions for the given
        range.

    :param unsigned long current_seq:
        the MMU notifiers sequance value for synchronization with
        invalidations. the sequance number is read from
        umem->odp_data->notifiers_seq before calling this function



.. _`ib_umem_odp_map_dma_pages.description`:

Description
-----------


Pins the range of pages passed in the argument, and maps them to
DMA addresses. The DMA addresses of the mapped pages is updated in
umem->odp_data->dma_list.

Returns the number of pages mapped in success, negative error code
for failure.
An -EAGAIN error code is returned when a concurrent mmu notifier prevents
the function from completing its task.

