.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-snd-compr-codec-caps:

===========================
struct snd_compr_codec_caps
===========================

*man struct snd_compr_codec_caps(9)*

*4.6.0-rc5*

query capability of codec


Synopsis
========

.. code-block:: c

    struct snd_compr_codec_caps {
      __u32 codec;
      __u32 num_descriptors;
      struct snd_codec_desc descriptor[MAX_NUM_CODEC_DESCRIPTORS];
    };


Members
=======

codec
    codec for which capability is queried

num_descriptors
    number of codec descriptors

descriptor[MAX_NUM_CODEC_DESCRIPTORS]
    array of codec capability descriptor


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
