.. -*- coding: utf-8; mode: rst -*-

=================
compress_params.h
=================


.. _`snd_enc_vorbis`:

struct snd_enc_vorbis
=====================

.. c:type:: snd_enc_vorbis

    


.. _`snd_enc_vorbis.definition`:

Definition
----------

.. code-block:: c

  struct snd_enc_vorbis {
    __s32 quality;
    __u32 managed;
    __u32 max_bit_rate;
    __u32 min_bit_rate;
    __u32 downmix;
  };


.. _`snd_enc_vorbis.members`:

Members
-------

:``quality``:
    Sets encoding quality to n, between -1 (low) and 10 (high).
    In the default mode of operation, the quality level is 3.
    Normal quality range is 0 - 10.

:``managed``:
    Boolean. Set  bitrate  management  mode. This turns off the
    normal VBR encoding, but allows hard or soft bitrate constraints to be
    enforced by the encoder. This mode can be slower, and may also be
    lower quality. It is primarily useful for streaming.

:``max_bit_rate``:
    Enabled only if managed is TRUE

:``min_bit_rate``:
    Enabled only if managed is TRUE

:``downmix``:
    Boolean. Downmix input from stereo to mono (has no effect on
    non-stereo streams). Useful for lower-bitrate encoding.




.. _`snd_enc_vorbis.description`:

Description
-----------

These options were extracted from the OpenMAX IL spec and Gstreamer vorbisenc
properties

For best quality users should specify VBR mode and set quality levels.



.. _`snd_enc_real`:

struct snd_enc_real
===================

.. c:type:: snd_enc_real

    


.. _`snd_enc_real.definition`:

Definition
----------

.. code-block:: c

  struct snd_enc_real {
    __u32 quant_bits;
    __u32 start_region;
    __u32 num_regions;
  };


.. _`snd_enc_real.members`:

Members
-------

:``quant_bits``:
    number of coupling quantization bits in the stream

:``start_region``:
    coupling start region in the stream

:``num_regions``:
    number of regions value




.. _`snd_enc_real.description`:

Description
-----------

These options were extracted from the OpenMAX IL spec



.. _`snd_enc_flac`:

struct snd_enc_flac
===================

.. c:type:: snd_enc_flac

    


.. _`snd_enc_flac.definition`:

Definition
----------

.. code-block:: c

  struct snd_enc_flac {
    __u32 num;
    __u32 gain;
  };


.. _`snd_enc_flac.members`:

Members
-------

:``num``:
    serial number, valid only for OGG formats
    needs to be set by application

:``gain``:
    Add replay gain tags




.. _`snd_enc_flac.description`:

Description
-----------

These options were extracted from the FLAC online documentation



.. _`snd_enc_flac.at-http`:

at http
-------

//flac.sourceforge.net/documentation_tools_flac.html

To make the API simpler, it is assumed that the user will select quality
profiles. Additional options that affect encoding quality and speed can
be added at a later stage if needed.

By default the Subset format is used by encoders.

TAGS such as pictures, etc, cannot be handled by an offloaded encoder and are
not supported in this API.

