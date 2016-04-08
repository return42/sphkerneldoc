
.. _API-enum-sndrv-compress-encoder:

===========================
enum sndrv_compress_encoder
===========================

*man enum sndrv_compress_encoder(9)*

*4.6.0-rc1*


Synopsis
========

.. code-block:: c

    enum sndrv_compress_encoder {
      SNDRV_COMPRESS_ENCODER_PADDING,
      SNDRV_COMPRESS_ENCODER_DELAY
    };


Constants
=========

SNDRV_COMPRESS_ENCODER_PADDING
    no of samples appended by the encoder at the end of the track

SNDRV_COMPRESS_ENCODER_DELAY
    no of samples inserted by the encoder at the beginning of the track
