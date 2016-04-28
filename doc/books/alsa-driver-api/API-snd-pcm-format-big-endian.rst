.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-format-big-endian:

=========================
snd_pcm_format_big_endian
=========================

*man snd_pcm_format_big_endian(9)*

*4.6.0-rc5*

Check the PCM format is big-endian


Synopsis
========

.. c:function:: int snd_pcm_format_big_endian( snd_pcm_format_t format )

Arguments
=========

``format``
    the format to check


Return
======

1 if the given PCM format is big-endian, 0 if little-endian, or a
negative error code if endian not specified.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
