.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/asoc-s3c.h

.. _`s3c_audio_pdata`:

struct s3c_audio_pdata
======================

.. c:type:: struct s3c_audio_pdata

    common platform data for audio device drivers

.. _`s3c_audio_pdata.definition`:

Definition
----------

.. code-block:: c

    struct s3c_audio_pdata {
        int (*cfg_gpio)(struct platform_device *);
        dma_filter_fn dma_filter;
        void *dma_playback;
        void *dma_capture;
        void *dma_play_sec;
        void *dma_capture_mic;
        struct samsung_i2s_type type;
    }

.. _`s3c_audio_pdata.members`:

Members
-------

cfg_gpio
    Callback function to setup mux'ed pins in I2S/PCM/AC97 mode

dma_filter
    *undescribed*

dma_playback
    *undescribed*

dma_capture
    *undescribed*

dma_play_sec
    *undescribed*

dma_capture_mic
    *undescribed*

type
    *undescribed*

.. This file was automatic generated / don't edit.

