.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/comedi/drivers/comedi_isadma.c

.. _`comedi_isadma_program`:

comedi_isadma_program
=====================

.. c:function:: void comedi_isadma_program(struct comedi_isadma_desc *desc)

    program and enable an ISA DMA transfer

    :param struct comedi_isadma_desc \*desc:
        the ISA DMA cookie to program and enable

.. _`comedi_isadma_disable`:

comedi_isadma_disable
=====================

.. c:function:: unsigned int comedi_isadma_disable(unsigned int dma_chan)

    disable the ISA DMA channel

    :param unsigned int dma_chan:
        the DMA channel to disable

.. _`comedi_isadma_disable.description`:

Description
-----------

Returns the residue (remaining bytes) left in the DMA transfer.

.. _`comedi_isadma_disable_on_sample`:

comedi_isadma_disable_on_sample
===============================

.. c:function:: unsigned int comedi_isadma_disable_on_sample(unsigned int dma_chan, unsigned int size)

    disable the ISA DMA channel

    :param unsigned int dma_chan:
        the DMA channel to disable

    :param unsigned int size:
        the sample size (in bytes)

.. _`comedi_isadma_disable_on_sample.description`:

Description
-----------

Returns the residue (remaining bytes) left in the DMA transfer.

.. _`comedi_isadma_poll`:

comedi_isadma_poll
==================

.. c:function:: unsigned int comedi_isadma_poll(struct comedi_isadma *dma)

    poll the current DMA transfer

    :param struct comedi_isadma \*dma:
        the ISA DMA to poll

.. _`comedi_isadma_poll.description`:

Description
-----------

Returns the position (in bytes) of the current DMA transfer.

.. _`comedi_isadma_set_mode`:

comedi_isadma_set_mode
======================

.. c:function:: void comedi_isadma_set_mode(struct comedi_isadma_desc *desc, char dma_dir)

    set the ISA DMA transfer direction

    :param struct comedi_isadma_desc \*desc:
        the ISA DMA cookie to set

    :param char dma_dir:
        the DMA direction

.. _`comedi_isadma_alloc`:

comedi_isadma_alloc
===================

.. c:function:: struct comedi_isadma *comedi_isadma_alloc(struct comedi_device *dev, int n_desc, unsigned int dma_chan1, unsigned int dma_chan2, unsigned int maxsize, char dma_dir)

    allocate and initialize the ISA DMA

    :param struct comedi_device \*dev:
        comedi_device struct

    :param int n_desc:
        the number of cookies to allocate

    :param unsigned int dma_chan1:
        *undescribed*

    :param unsigned int dma_chan2:
        DMA channel for the second cookie

    :param unsigned int maxsize:
        the size of the buffer to allocate for each cookie

    :param char dma_dir:
        the DMA direction

.. _`comedi_isadma_alloc.description`:

Description
-----------

Returns the allocated and initialized ISA DMA or NULL if anything fails.

.. _`comedi_isadma_free`:

comedi_isadma_free
==================

.. c:function:: void comedi_isadma_free(struct comedi_isadma *dma)

    free the ISA DMA

    :param struct comedi_isadma \*dma:
        the ISA DMA to free

.. This file was automatic generated / don't edit.

