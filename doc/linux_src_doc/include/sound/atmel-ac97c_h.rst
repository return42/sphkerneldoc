.. -*- coding: utf-8; mode: rst -*-

=============
atmel-ac97c.h
=============


.. _`ac97c_platform_data`:

struct ac97c_platform_data
==========================

.. c:type:: ac97c_platform_data

    board specific AC97C configuration


.. _`ac97c_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct ac97c_platform_data {
    struct dw_dma_slave rx_dws;
    struct dw_dma_slave tx_dws;
    int reset_pin;
  };


.. _`ac97c_platform_data.members`:

Members
-------

:``rx_dws``:
    DMA slave interface to use for sound capture.

:``tx_dws``:
    DMA slave interface to use for sound playback.

:``reset_pin``:
    GPIO pin wired to the reset input on the external AC97 codec,
    optional to use, set to -ENODEV if not in use. AC97 layer will
    try to do a software reset of the external codec anyway.




.. _`ac97c_platform_data.description`:

Description
-----------

If the user do not want to use a DMA channel for playback or capture, i.e.
only one feature is required on the board. The slave for playback or capture
can be set to NULL. The AC97C driver will take use of this when setting up
the sound streams.

