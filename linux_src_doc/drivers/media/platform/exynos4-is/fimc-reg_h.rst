.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/exynos4-is/fimc-reg.h

.. _`fimc_hw_set_dma_seq`:

fimc_hw_set_dma_seq
===================

.. c:function:: void fimc_hw_set_dma_seq(struct fimc_dev *dev, u32 mask)

    configure output DMA buffer sequence

    :param dev:
        *undescribed*
    :type dev: struct fimc_dev \*

    :param mask:
        bitmask for the DMA output buffer registers, set to 0 to skip buffer
        This function masks output DMA ring buffers, it allows to select which of
        the 32 available output buffer address registers will be used by the DMA
        engine.
    :type mask: u32

.. This file was automatic generated / don't edit.

