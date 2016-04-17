.. -*- coding: utf-8; mode: rst -*-

==========
scif_dma.c
==========


.. _`scif_copy_work`:

struct scif_copy_work
=====================

.. c:type:: scif_copy_work

    Work for DMA copy


.. _`scif_copy_work.definition`:

Definition
----------

.. code-block:: c

  struct scif_copy_work {
    s64 src_offset;
    s64 dst_offset;
    struct scif_window * src_window;
    struct scif_window * dst_window;
    int loopback;
    size_t len;
    struct scif_dma_comp_cb * comp_cb;
    struct scif_dev * remote_dev;
    int fence_type;
    bool ordered;
  };


.. _`scif_copy_work.members`:

Members
-------

:``src_offset``:
    Starting source offset

:``dst_offset``:
    Starting destination offset

:``src_window``:
    Starting src registered window

:``dst_window``:
    Starting dst registered window

:``loopback``:
    true if this is a loopback DMA transfer

:``len``:
    Length of the transfer

:``comp_cb``:
    DMA copy completion callback

:``remote_dev``:
    The remote SCIF peer device

:``fence_type``:
    polling or interrupt based

:``ordered``:
    is this a tail byte ordered DMA transfer




.. _`scif_reserve_dma_chan`:

scif_reserve_dma_chan
=====================

.. c:function:: int scif_reserve_dma_chan (struct scif_endpt *ep)

    :param struct scif_endpt \*ep:
        Endpoint Descriptor.



.. _`scif_reserve_dma_chan.description`:

Description
-----------

This routine reserves a DMA channel for a particular
endpoint. All DMA transfers for an endpoint are always
programmed on the same DMA channel.



.. _`__scif_rma_destroy_tcw`:

__scif_rma_destroy_tcw
======================

.. c:function:: void __scif_rma_destroy_tcw (struct scif_mmu_notif *mmn, struct scif_endpt *ep, u64 start, u64 len)

    :param struct scif_mmu_notif \*mmn:

        *undescribed*

    :param struct scif_endpt \*ep:

        *undescribed*

    :param u64 start:

        *undescribed*

    :param u64 len:

        *undescribed*



.. _`__scif_rma_destroy_tcw.description`:

Description
-----------


This routine destroys temporary cached windows



.. _`scif_register_temp`:

scif_register_temp
==================

.. c:function:: int scif_register_temp (scif_epd_t epd, unsigned long addr, size_t len, int prot, off_t *out_offset, struct scif_window **out_window)

    :param scif_epd_t epd:
        End Point Descriptor.

    :param unsigned long addr:
        virtual address to/from which to copy

    :param size_t len:
        length of range to copy

    :param int prot:

        *undescribed*

    :param off_t \*out_offset:
        computed offset returned by reference.

    :param struct scif_window \*\*out_window:
        allocated registered window returned by reference.



.. _`scif_register_temp.description`:

Description
-----------

Create a temporary registered window. The peer will not know about this
window. This API is used for :c:func:`scif_vreadfrom`/:c:func:`scif_vwriteto` API's.



.. _`scif_rma_destroy_windows`:

scif_rma_destroy_windows
========================

.. c:function:: void scif_rma_destroy_windows ( void)

    :param void:
        no arguments



.. _`scif_rma_destroy_windows.description`:

Description
-----------


This routine destroys all windows queued for cleanup



.. _`scif_rma_destroy_tcw_invalid`:

scif_rma_destroy_tcw_invalid
============================

.. c:function:: void scif_rma_destroy_tcw_invalid ( void)

    :param void:
        no arguments



.. _`scif_rma_destroy_tcw_invalid.description`:

Description
-----------


This routine destroys temporary cached registered windows
which have been queued for cleanup.



.. _`scif_rma_completion_cb`:

scif_rma_completion_cb
======================

.. c:function:: void scif_rma_completion_cb (void *data)

    :param void \*data:
        RMA cookie



.. _`scif_rma_completion_cb.description`:

Description
-----------

RMA interrupt completion callback.



.. _`scif_rma_copy`:

scif_rma_copy
=============

.. c:function:: int scif_rma_copy (scif_epd_t epd, off_t loffset, unsigned long addr, size_t len, off_t roffset, int flags, enum scif_rma_dir dir, bool last_chunk)

    :param scif_epd_t epd:
        end point descriptor.

    :param off_t loffset:
        offset in local registered address space to/from which to copy

    :param unsigned long addr:
        user virtual address to/from which to copy

    :param size_t len:
        length of range to copy

    :param off_t roffset:
        offset in remote registered address space to/from which to copy

    :param int flags:
        flags

    :param enum scif_rma_dir dir:
        LOCAL->REMOTE or vice versa.

    :param bool last_chunk:
        true if this is the last chunk of a larger transfer



.. _`scif_rma_copy.description`:

Description
-----------

Validate parameters, check if src/dst registered ranges requested for copy
are valid and initiate either CPU or DMA copy.

