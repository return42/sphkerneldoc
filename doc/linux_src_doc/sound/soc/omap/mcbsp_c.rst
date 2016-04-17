.. -*- coding: utf-8; mode: rst -*-

=======
mcbsp.c
=======


.. _`omap_mcbsp_dma_reg_params`:

omap_mcbsp_dma_reg_params
=========================

.. c:function:: int omap_mcbsp_dma_reg_params (struct omap_mcbsp *mcbsp, unsigned int stream)

    returns the address of mcbsp data register @id - mcbsp id @stream - indicates the direction of data flow (rx or tx)

    :param struct omap_mcbsp \*mcbsp:

        *undescribed*

    :param unsigned int stream:

        *undescribed*



.. _`omap_mcbsp_dma_reg_params.description`:

Description
-----------


Returns the address of mcbsp data transmit register or data receive register
to be used by DMA for transferring/receiving data based on the value of
``stream`` for the requested mcbsp given by ``id``

