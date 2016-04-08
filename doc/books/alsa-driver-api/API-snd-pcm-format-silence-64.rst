
.. _API-snd-pcm-format-silence-64:

=========================
snd_pcm_format_silence_64
=========================

*man snd_pcm_format_silence_64(9)*

*4.6.0-rc1*

return the silent data in 8 bytes array


Synopsis
========

.. c:function:: const unsigned char ⋆ snd_pcm_format_silence_64( snd_pcm_format_t format )

Arguments
=========

``format``
    the format to check


Return
======

The format pattern to fill or ``NULL`` if error.
