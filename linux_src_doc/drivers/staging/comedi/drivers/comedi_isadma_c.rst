.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/drivers/comedi_isadma.c

.. _`comedi_isadma_program`:

comedi_isadma_program
=====================

.. c:function:: void comedi_isadma_program(struct comedi_isadma_desc *desc)

    program and enable an ISA DMA transfer

    :param desc:
        the ISA DMA cookie to program and enable
    :type desc: struct comedi_isadma_desc \*

.. _`comedi_isadma_disable`:

comedi_isadma_disable
=====================

.. c:function:: unsigned int comedi_isadma_disable(unsigned int dma_chan)

    disable the ISA DMA channel

    :param dma_chan:
        the DMA channel to disable
    :type dma_chan: unsigned int

.. _`comedi_isadma_disable.description`:

Description
-----------

Returns the residue (remaining bytes) left in the DMA transfer.

.. _`comedi_isadma_disable_on_sample`:

comedi_isadma_disable_on_sample
===============================

.. c:function:: unsigned int comedi_isadma_disable_on_sample(unsigned int dma_chan, unsigned int size)

    disable the ISA DMA channel

    :param dma_chan:
        the DMA channel to disable
    :type dma_chan: unsigned int

    :param size:
        the sample size (in bytes)
    :type size: unsigned int

.. _`comedi_isadma_disable_on_sample.description`:

Description
-----------

Returns the residue (remaining bytes) left in the DMA transfer.

.. _`comedi_isadma_poll`:

comedi_isadma_poll
==================

.. c:function:: unsigned int comedi_isadma_poll(struct comedi_isadma *dma)

    poll the current DMA transfer

    :param dma:
        the ISA DMA to poll
    :type dma: struct comedi_isadma \*

.. _`comedi_isadma_poll.description`:

Description
-----------

Returns the position (in bytes) of the current DMA transfer.

.. _`comedi_isadma_set_mode`:

comedi_isadma_set_mode
======================

.. c:function:: void comedi_isadma_set_mode(struct comedi_isadma_desc *desc, char dma_dir)

    set the ISA DMA transfer direction

    :param desc:
        the ISA DMA cookie to set
    :type desc: struct comedi_isadma_desc \*

    :param dma_dir:
        the DMA direction
    :type dma_dir: char

.. _`comedi_isadma_alloc`:

comedi_isadma_alloc
===================

.. c:function:: struct comedi_isadma *comedi_isadma_alloc(struct comedi_device *dev, int n_desc, unsigned int dma_chan1, unsigned int dma_chan2, unsigned int maxsize, char dma_dir)

    allocate and initialize the ISA DMA

    :param dev:
        comedi_device struct
    :type dev: struct comedi_device \*

    :param n_desc:
        the number of cookies to allocate
    :type n_desc: int

    :param dma_chan1:
        *undescribed*
    :type dma_chan1: unsigned int

    :param dma_chan2:
        DMA channel for the second cookie
    :type dma_chan2: unsigned int

    :param maxsize:
        the size of the buffer to allocate for each cookie
    :type maxsize: unsigned int

    :param dma_dir:
        the DMA direction
    :type dma_dir: char

.. _`comedi_isadma_alloc.description`:

Description
-----------

Returns the allocated and initialized ISA DMA or NULL if anything fails.

.. _`comedi_isadma_free`:

comedi_isadma_free
==================

.. c:function:: void comedi_isadma_free(struct comedi_isadma *dma)

    free the ISA DMA

    :param dma:
        the ISA DMA to free
    :type dma: struct comedi_isadma \*

.. This file was automatic generated / don't edit.

