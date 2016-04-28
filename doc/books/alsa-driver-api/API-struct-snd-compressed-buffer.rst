.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-snd-compressed-buffer:

============================
struct snd_compressed_buffer
============================

*man struct snd_compressed_buffer(9)*

*4.6.0-rc5*

compressed buffer


Synopsis
========

.. code-block:: c

    struct snd_compressed_buffer {
      __u32 fragment_size;
      __u32 fragments;
    };


Members
=======

fragment_size
    size of buffer fragment in bytes

fragments
    number of such fragments


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
