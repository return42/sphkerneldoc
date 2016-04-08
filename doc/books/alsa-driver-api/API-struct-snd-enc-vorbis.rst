
.. _API-struct-snd-enc-vorbis:

=====================
struct snd_enc_vorbis
=====================

*man struct snd_enc_vorbis(9)*

*4.6.0-rc1*


Synopsis
========

.. code-block:: c

    struct snd_enc_vorbis {
      __s32 quality;
      __u32 managed;
      __u32 max_bit_rate;
      __u32 min_bit_rate;
      __u32 downmix;
    };


Members
=======

quality
    Sets encoding quality to n, between -1 (low) and 10 (high). In the default mode of operation, the quality level is 3. Normal quality range is 0 - 10.

managed
    Boolean. Set bitrate management mode. This turns off the normal VBR encoding, but allows hard or soft bitrate constraints to be enforced by the encoder. This mode can be
    slower, and may also be lower quality. It is primarily useful for streaming.

max_bit_rate
    Enabled only if managed is TRUE

min_bit_rate
    Enabled only if managed is TRUE

downmix
    Boolean. Downmix input from stereo to mono (has no effect on non-stereo streams). Useful for lower-bitrate encoding.


Description
===========

These options were extracted from the OpenMAX IL spec and Gstreamer vorbisenc properties

For best quality users should specify VBR mode and set quality levels.
