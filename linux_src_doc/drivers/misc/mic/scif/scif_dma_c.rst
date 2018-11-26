.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/scif/scif_dma.c

.. _`scif_copy_work`:

struct scif_copy_work
=====================

.. c:type:: struct scif_copy_work

    Work for DMA copy

.. _`scif_copy_work.definition`:

Definition
----------

.. code-block:: c

    struct scif_copy_work {
        s64 src_offset;
        s64 dst_offset;
        struct scif_window *src_window;
        struct scif_window *dst_window;
        int loopback;
        size_t len;
        struct scif_dma_comp_cb *comp_cb;
        struct scif_dev *remote_dev;
        int fence_type;
        bool ordered;
    }

.. _`scif_copy_work.members`:

Members
-------

src_offset
    Starting source offset

dst_offset
    Starting destination offset

src_window
    Starting src registered window

dst_window
    Starting dst registered window

loopback
    true if this is a loopback DMA transfer

len
    Length of the transfer

comp_cb
    DMA copy completion callback

remote_dev
    The remote SCIF peer device

fence_type
    polling or interrupt based

ordered
    is this a tail byte ordered DMA transfer

.. _`scif_reserve_dma_chan`:

scif_reserve_dma_chan
=====================

.. c:function:: int scif_reserve_dma_chan(struct scif_endpt *ep)

    :param ep:
        Endpoint Descriptor.
    :type ep: struct scif_endpt \*

.. _`scif_reserve_dma_chan.description`:

Description
-----------

This routine reserves a DMA channel for a particular
endpoint. All DMA transfers for an endpoint are always
programmed on the same DMA channel.

.. _`__scif_rma_destroy_tcw`:

\__scif_rma_destroy_tcw
=======================

.. c:function:: void __scif_rma_destroy_tcw(struct scif_mmu_notif *mmn, u64 start, u64 len)

    :param mmn:
        *undescribed*
    :type mmn: struct scif_mmu_notif \*

    :param start:
        *undescribed*
    :type start: u64

    :param len:
        *undescribed*
    :type len: u64

.. _`__scif_rma_destroy_tcw.description`:

Description
-----------

This routine destroys temporary cached windows

.. _`scif_register_temp`:

scif_register_temp
==================

.. c:function:: int scif_register_temp(scif_epd_t epd, unsigned long addr, size_t len, int prot, off_t *out_offset, struct scif_window **out_window)

    :param epd:
        End Point Descriptor.
    :type epd: scif_epd_t

    :param addr:
        virtual address to/from which to copy
    :type addr: unsigned long

    :param len:
        length of range to copy
    :type len: size_t

    :param prot:
        *undescribed*
    :type prot: int

    :param out_offset:
        computed offset returned by reference.
    :type out_offset: off_t \*

    :param out_window:
        allocated registered window returned by reference.
    :type out_window: struct scif_window \*\*

.. _`scif_register_temp.description`:

Description
-----------

Create a temporary registered window. The peer will not know about this
window. This API is used for \ :c:func:`scif_vreadfrom`\ /scif_vwriteto() API's.

.. _`scif_rma_destroy_windows`:

scif_rma_destroy_windows
========================

.. c:function:: void scif_rma_destroy_windows( void)

    :param void:
        no arguments
    :type void: 

.. _`scif_rma_destroy_windows.description`:

Description
-----------

This routine destroys all windows queued for cleanup

.. _`scif_rma_destroy_tcw_invalid`:

scif_rma_destroy_tcw_invalid
============================

.. c:function:: void scif_rma_destroy_tcw_invalid( void)

    :param void:
        no arguments
    :type void: 

.. _`scif_rma_destroy_tcw_invalid.description`:

Description
-----------

This routine destroys temporary cached registered windows
which have been queued for cleanup.

.. _`scif_rma_completion_cb`:

scif_rma_completion_cb
======================

.. c:function:: void scif_rma_completion_cb(void *data)

    :param data:
        RMA cookie
    :type data: void \*

.. _`scif_rma_completion_cb.description`:

Description
-----------

RMA interrupt completion callback.

.. _`scif_rma_copy`:

scif_rma_copy
=============

.. c:function:: int scif_rma_copy(scif_epd_t epd, off_t loffset, unsigned long addr, size_t len, off_t roffset, int flags, enum scif_rma_dir dir, bool last_chunk)

    :param epd:
        end point descriptor.
    :type epd: scif_epd_t

    :param loffset:
        offset in local registered address space to/from which to copy
    :type loffset: off_t

    :param addr:
        user virtual address to/from which to copy
    :type addr: unsigned long

    :param len:
        length of range to copy
    :type len: size_t

    :param roffset:
        offset in remote registered address space to/from which to copy
    :type roffset: off_t

    :param flags:
        flags
    :type flags: int

    :param dir:
        LOCAL->REMOTE or vice versa.
    :type dir: enum scif_rma_dir

    :param last_chunk:
        true if this is the last chunk of a larger transfer
    :type last_chunk: bool

.. _`scif_rma_copy.description`:

Description
-----------

Validate parameters, check if src/dst registered ranges requested for copy
are valid and initiate either CPU or DMA copy.

.. This file was automatic generated / don't edit.

