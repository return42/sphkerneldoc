
.. _API-snd-pcm-format-big-endian:

=========================
snd_pcm_format_big_endian
=========================

*man snd_pcm_format_big_endian(9)*

*4.6.0-rc1*

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

1 if the given PCM format is big-endian, 0 if little-endian, or a negative error code if endian not specified.
