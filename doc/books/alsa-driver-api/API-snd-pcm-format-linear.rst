
.. _API-snd-pcm-format-linear:

=====================
snd_pcm_format_linear
=====================

*man snd_pcm_format_linear(9)*

*4.6.0-rc1*

Check the PCM format is linear


Synopsis
========

.. c:function:: int snd_pcm_format_linear( snd_pcm_format_t format )

Arguments
=========

``format``
    the format to check


Return
======

1 if the given PCM format is linear, 0 if not.
