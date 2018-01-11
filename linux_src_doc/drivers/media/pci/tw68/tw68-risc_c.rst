.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/pci/tw68/tw68-risc.c

.. _`tw68_risc_field`:

tw68_risc_field
===============

.. c:function:: __le32 *tw68_risc_field(__le32 *rp, struct scatterlist *sglist, unsigned int offset, u32 sync_line, unsigned int bpl, unsigned int padding, unsigned int lines, bool jump)

    :param __le32 \*rp:
        pointer to current risc program position

    :param struct scatterlist \*sglist:
        pointer to "scatter-gather list" of buffer pointers

    :param unsigned int offset:
        offset to target memory buffer

    :param u32 sync_line:
        0 -> no sync, 1 -> odd sync, 2 -> even sync

    :param unsigned int bpl:
        number of bytes per scan line

    :param unsigned int padding:
        number of bytes of padding to add

    :param unsigned int lines:
        number of lines in field

    :param bool jump:
        insert a jump at the start

.. _`tw68_risc_buffer`:

tw68_risc_buffer
================

.. c:function:: int tw68_risc_buffer(struct pci_dev *pci, struct tw68_buf *buf, struct scatterlist *sglist, unsigned int top_offset, unsigned int bottom_offset, unsigned int bpl, unsigned int padding, unsigned int lines)

    :param struct pci_dev \*pci:
        structure with info about the pci
        slot which our device is in.

    :param struct tw68_buf \*buf:
        structure with info about the memory
        used for our controller program.

    :param struct scatterlist \*sglist:
        scatter-gather list entry

    :param unsigned int top_offset:
        offset within the risc program area for the
        first odd frame line

    :param unsigned int bottom_offset:
        offset within the risc program area for the
        first even frame line

    :param unsigned int bpl:
        number of data bytes per scan line

    :param unsigned int padding:
        number of extra bytes to add at end of line

    :param unsigned int lines:
        number of scan lines

.. _`tw68_risc_buffer.description`:

Description
-----------

This routine is called by tw68-video.  It allocates
memory for the dma controller "program" and then fills in that
memory with the appropriate "instructions".

.. This file was automatic generated / don't edit.

