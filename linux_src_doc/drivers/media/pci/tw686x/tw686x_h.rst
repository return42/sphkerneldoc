.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/pci/tw686x/tw686x.h

.. _`tw686x_dev`:

struct tw686x_dev
=================

.. c:type:: struct tw686x_dev

    global device status

.. _`tw686x_dev.definition`:

Definition
----------

.. code-block:: c

    struct tw686x_dev {
        spinlock_t lock;
        struct v4l2_device v4l2_dev;
        struct snd_card *snd_card;
        char name;
        unsigned int type;
        unsigned int dma_mode;
        struct pci_dev *pci_dev;
        __u32 __iomem *mmio;
        const struct tw686x_dma_ops *dma_ops;
        struct tw686x_video_channel *video_channels;
        struct tw686x_audio_channel *audio_channels;
        int audio_rate;
        int period_size;
        int audio_enabled;
        struct timer_list dma_delay_timer;
        u32 pending_dma_en;
        u32 pending_dma_cmd;
    }

.. _`tw686x_dev.members`:

Members
-------

lock
    spinlock controlling access to the
    shared device registers (DMA enable/disable).

v4l2_dev
    *undescribed*

snd_card
    *undescribed*

name
    *undescribed*

type
    *undescribed*

dma_mode
    *undescribed*

pci_dev
    *undescribed*

mmio
    *undescribed*

dma_ops
    *undescribed*

video_channels
    *undescribed*

audio_channels
    *undescribed*

audio_rate
    *undescribed*

period_size
    *undescribed*

audio_enabled
    *undescribed*

dma_delay_timer
    *undescribed*

pending_dma_en
    *undescribed*

pending_dma_cmd
    *undescribed*

.. This file was automatic generated / don't edit.

