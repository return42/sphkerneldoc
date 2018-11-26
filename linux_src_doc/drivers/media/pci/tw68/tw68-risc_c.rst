.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/pci/tw68/tw68-risc.c

.. _`tw68_risc_field`:

tw68_risc_field
===============

.. c:function:: __le32 *tw68_risc_field(__le32 *rp, struct scatterlist *sglist, unsigned int offset, u32 sync_line, unsigned int bpl, unsigned int padding, unsigned int lines, bool jump)

    :param rp:
        pointer to current risc program position
    :type rp: __le32 \*

    :param sglist:
        pointer to "scatter-gather list" of buffer pointers
    :type sglist: struct scatterlist \*

    :param offset:
        offset to target memory buffer
    :type offset: unsigned int

    :param sync_line:
        0 -> no sync, 1 -> odd sync, 2 -> even sync
    :type sync_line: u32

    :param bpl:
        number of bytes per scan line
    :type bpl: unsigned int

    :param padding:
        number of bytes of padding to add
    :type padding: unsigned int

    :param lines:
        number of lines in field
    :type lines: unsigned int

    :param jump:
        insert a jump at the start
    :type jump: bool

.. _`tw68_risc_buffer`:

tw68_risc_buffer
================

.. c:function:: int tw68_risc_buffer(struct pci_dev *pci, struct tw68_buf *buf, struct scatterlist *sglist, unsigned int top_offset, unsigned int bottom_offset, unsigned int bpl, unsigned int padding, unsigned int lines)

    :param pci:
        structure with info about the pci
        slot which our device is in.
    :type pci: struct pci_dev \*

    :param buf:
        structure with info about the memory
        used for our controller program.
    :type buf: struct tw68_buf \*

    :param sglist:
        scatter-gather list entry
    :type sglist: struct scatterlist \*

    :param top_offset:
        offset within the risc program area for the
        first odd frame line
    :type top_offset: unsigned int

    :param bottom_offset:
        offset within the risc program area for the
        first even frame line
    :type bottom_offset: unsigned int

    :param bpl:
        number of data bytes per scan line
    :type bpl: unsigned int

    :param padding:
        number of extra bytes to add at end of line
    :type padding: unsigned int

    :param lines:
        number of scan lines
    :type lines: unsigned int

.. _`tw68_risc_buffer.description`:

Description
-----------

This routine is called by tw68-video.  It allocates
memory for the dma controller "program" and then fills in that
memory with the appropriate "instructions".

.. This file was automatic generated / don't edit.

