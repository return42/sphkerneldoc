
.. _API-snd-pcm-format-cpu-endian:

=========================
snd_pcm_format_cpu_endian
=========================

*man snd_pcm_format_cpu_endian(9)*

*4.6.0-rc1*

Check the PCM format is CPU-endian


Synopsis
========

.. c:function:: int snd_pcm_format_cpu_endian( snd_pcm_format_t format )

Arguments
=========

``format``
    the format to check


Return
======

1 if the given PCM format is CPU-endian, 0 if opposite, or a negative error code if endian not specified.
