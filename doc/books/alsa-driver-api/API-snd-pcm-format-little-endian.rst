
.. _API-snd-pcm-format-little-endian:

============================
snd_pcm_format_little_endian
============================

*man snd_pcm_format_little_endian(9)*

*4.6.0-rc1*

Check the PCM format is little-endian


Synopsis
========

.. c:function:: int snd_pcm_format_little_endian( snd_pcm_format_t format )

Arguments
=========

``format``
    the format to check


Return
======

1 if the given PCM format is little-endian, 0 if big-endian, or a negative error code if endian not specified.
