.. -*- coding: utf-8; mode: rst -*-

=====================
asoc-s3c24xx_simtec.h
=====================


.. _`s3c24xx_audio_simtec_pdata`:

struct s3c24xx_audio_simtec_pdata
=================================

.. c:type:: s3c24xx_audio_simtec_pdata

    platform data for simtec audio


.. _`s3c24xx_audio_simtec_pdata.definition`:

Definition
----------

.. code-block:: c

  struct s3c24xx_audio_simtec_pdata {
    unsigned int use_mpllin:1;
    unsigned int output_cdclk:1;
    unsigned int have_mic:1;
    unsigned int have_lout:1;
    int amp_gpio;
    int amp_gain[2];
  };


.. _`s3c24xx_audio_simtec_pdata.members`:

Members
-------

:``use_mpllin``:
    Select codec clock from MPLLin

:``output_cdclk``:
    Need to output CDCLK to the codec

:``have_mic``:
    Set if we have a MIC socket

:``have_lout``:
    Set if we have a LineOut socket

:``amp_gpio``:
    GPIO pin to enable the AMP

:``amp_gain[2]``:
    Option GPIO to control AMP gain


