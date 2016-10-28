.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/cirrus/ep93xx-ac97.c

.. _`ep93xx_ac97_info`:

struct ep93xx_ac97_info
=======================

.. c:type:: struct ep93xx_ac97_info

    EP93xx AC97 controller info structure

.. _`ep93xx_ac97_info.definition`:

Definition
----------

.. code-block:: c

    struct ep93xx_ac97_info {
        struct mutex lock;
        struct device *dev;
        void __iomem *regs;
        struct completion done;
        struct snd_dmaengine_dai_dma_data dma_params_rx;
        struct snd_dmaengine_dai_dma_data dma_params_tx;
    }

.. _`ep93xx_ac97_info.members`:

Members
-------

lock
    mutex serializing access to the bus (slot 1 & 2 ops)

dev
    pointer to the platform device dev structure

regs
    mapped AC97 controller registers

done
    bus ops wait here for an interrupt

dma_params_rx
    *undescribed*

dma_params_tx
    *undescribed*

.. This file was automatic generated / don't edit.

