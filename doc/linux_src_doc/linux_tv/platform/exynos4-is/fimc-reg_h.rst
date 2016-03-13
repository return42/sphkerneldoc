.. -*- coding: utf-8; mode: rst -*-

==========
fimc-reg.h
==========



.. _xref_fimc_hw_set_dma_seq:

fimc_hw_set_dma_seq
===================

.. c:function:: void fimc_hw_set_dma_seq (struct fimc_dev * dev, u32 mask)

    configure output DMA buffer sequence

    :param struct fimc_dev * dev:

        _undescribed_

    :param u32 mask:
        bitmask for the DMA output buffer registers, set to 0 to skip buffer
        This function masks output DMA ring buffers, it allows to select which of
        the 32 available output buffer address registers will be used by the DMA
        engine.


