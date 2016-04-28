.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-snd-enc-real:

===================
struct snd_enc_real
===================

*man struct snd_enc_real(9)*

*4.6.0-rc5*


Synopsis
========

.. code-block:: c

    struct snd_enc_real {
      __u32 quant_bits;
      __u32 start_region;
      __u32 num_regions;
    };


Members
=======

quant_bits
    number of coupling quantization bits in the stream

start_region
    coupling start region in the stream

num_regions
    number of regions value


Description
===========

These options were extracted from the OpenMAX IL spec


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
