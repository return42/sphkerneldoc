.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-snd-compr-caps:

=====================
struct snd_compr_caps
=====================

*man struct snd_compr_caps(9)*

*4.6.0-rc5*

caps descriptor


Synopsis
========

.. code-block:: c

    struct snd_compr_caps {
      __u32 num_codecs;
      __u32 direction;
      __u32 min_fragment_size;
      __u32 max_fragment_size;
      __u32 min_fragments;
      __u32 max_fragments;
      __u32 codecs[MAX_NUM_CODECS];
      __u32 reserved[11];
    };


Members
=======

num_codecs
    number of codecs supported

direction
    direction supported. Of type snd_compr_direction

min_fragment_size
    minimum fragment supported by DSP

max_fragment_size
    maximum fragment supported by DSP

min_fragments
    min fragments supported by DSP

max_fragments
    max fragments supported by DSP

codecs[MAX_NUM_CODECS]
    pointer to array of codecs

reserved[11]
    reserved field


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
