.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-format-silence-64:

=========================
snd_pcm_format_silence_64
=========================

*man snd_pcm_format_silence_64(9)*

*4.6.0-rc5*

return the silent data in 8 bytes array


Synopsis
========

.. c:function:: const unsigned char * snd_pcm_format_silence_64( snd_pcm_format_t format )

Arguments
=========

``format``
    the format to check


Return
======

The format pattern to fill or ``NULL`` if error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
