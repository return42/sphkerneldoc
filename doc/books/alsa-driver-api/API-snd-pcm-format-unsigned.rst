
.. _API-snd-pcm-format-unsigned:

=======================
snd_pcm_format_unsigned
=======================

*man snd_pcm_format_unsigned(9)*

*4.6.0-rc1*

Check the PCM format is unsigned linear


Synopsis
========

.. c:function:: int snd_pcm_format_unsigned( snd_pcm_format_t format )

Arguments
=========

``format``
    the format to check


Return
======

1 if the given PCM format is unsigned linear, 0 if signed linear, and a negative error code for non-linear formats.
