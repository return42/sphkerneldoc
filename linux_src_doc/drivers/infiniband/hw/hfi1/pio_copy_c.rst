.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/hfi1/pio_copy.c

.. _`pio_copy`:

pio_copy
========

.. c:function:: void pio_copy(struct hfi1_devdata *dd, struct pio_buf *pbuf, u64 pbc, const void *from, size_t count)

    copy data block to MMIO space

    :param dd:
        *undescribed*
    :type dd: struct hfi1_devdata \*

    :param pbuf:
        a number of blocks allocated within a PIO send context
    :type pbuf: struct pio_buf \*

    :param pbc:
        PBC to send
    :type pbc: u64

    :param from:
        source, must be 8 byte aligned
    :type from: const void \*

    :param count:
        number of DWORD (32-bit) quantities to copy from source
    :type count: size_t

.. _`pio_copy.description`:

Description
-----------

Copy data from source to PIO Send Buffer memory, 8 bytes at a time.
Must always write full BLOCK_SIZE bytes blocks.  The first block must
be written to the corresponding SOP=1 address.

.. _`pio_copy.known`:

Known
-----

o pbuf->start always starts on a block boundary
o pbuf can wrap only at a block boundary

.. This file was automatic generated / don't edit.

