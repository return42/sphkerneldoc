.. -*- coding: utf-8; mode: rst -*-

=====
pcm.c
=====


.. _`s3c_pcm_info`:

struct s3c_pcm_info
===================

.. c:type:: s3c_pcm_info

    S3C PCM Controller information


.. _`s3c_pcm_info.definition`:

Definition
----------

.. code-block:: c

  struct s3c_pcm_info {
    struct device * dev;
    void __iomem * regs;
    struct s3c_dma_params * dma_playback;
    struct s3c_dma_params * dma_capture;
  };


.. _`s3c_pcm_info.members`:

Members
-------

:``dev``:
    The parent device passed to use from the probe.

:``regs``:
    The pointer to the device register block.

:``dma_playback``:
    DMA information for playback channel.

:``dma_capture``:
    DMA information for capture channel.


