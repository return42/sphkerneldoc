.. -*- coding: utf-8; mode: rst -*-

===========
tw68-risc.c
===========



.. _xref_tw68_risc_buffer:

tw68_risc_buffer
================

.. c:function:: int tw68_risc_buffer (struct pci_dev * pci, struct tw68_buf * buf, struct scatterlist * sglist, unsigned int top_offset, unsigned int bottom_offset, unsigned int bpl, unsigned int padding, unsigned int lines)

    

    :param struct pci_dev * pci:

        _undescribed_

    :param struct tw68_buf * buf:

        _undescribed_

    :param struct scatterlist * sglist:

        _undescribed_

    :param unsigned int top_offset:

        _undescribed_

    :param unsigned int bottom_offset:

        _undescribed_

    :param unsigned int bpl:

        _undescribed_

    :param unsigned int padding:

        _undescribed_

    :param unsigned int lines:

        _undescribed_



Description
-----------



	This routine is called by tw68-video.  It allocates
	memory for the dma controller "program" and then fills in that
	memory with the appropriate "instructions".


	**pci_dev**	structure with info about the pci
			slot which our device is in.
	**risc**		structure with info about the memory
			used for our controller program.
	**sglist**		scatter-gather list entry
	**top_offset**	offset within the risc program area for the
			first odd frame line
	**bottom_offset**	offset within the risc program area for the
			first even frame line
	**bpl**		number of data bytes per scan line
	**padding**	number of extra bytes to add at end of line
	**lines**		number of scan lines


