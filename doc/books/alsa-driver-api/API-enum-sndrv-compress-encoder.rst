.. -*- coding: utf-8; mode: rst -*-

.. _API-enum-sndrv-compress-encoder:

===========================
enum sndrv_compress_encoder
===========================

*man enum sndrv_compress_encoder(9)*

*4.6.0-rc5*


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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
