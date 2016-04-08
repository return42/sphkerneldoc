
.. _API-snd-pcm-format-signed:

=====================
snd_pcm_format_signed
=====================

*man snd_pcm_format_signed(9)*

*4.6.0-rc1*

Check the PCM format is signed linear


Synopsis
========

.. c:function:: int snd_pcm_format_signed( snd_pcm_format_t format )

Arguments
=========

``format``
    the format to check


Return
======

1 if the given PCM format is signed linear, 0 if unsigned linear, and a negative error code for non-linear formats.
