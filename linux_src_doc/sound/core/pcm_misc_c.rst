.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/core/pcm_misc.c

.. _`snd_pcm_format_signed`:

snd_pcm_format_signed
=====================

.. c:function:: int snd_pcm_format_signed(snd_pcm_format_t format)

    Check the PCM format is signed linear

    :param format:
        the format to check
    :type format: snd_pcm_format_t

.. _`snd_pcm_format_signed.return`:

Return
------

1 if the given PCM format is signed linear, 0 if unsigned
linear, and a negative error code for non-linear formats.

.. _`snd_pcm_format_unsigned`:

snd_pcm_format_unsigned
=======================

.. c:function:: int snd_pcm_format_unsigned(snd_pcm_format_t format)

    Check the PCM format is unsigned linear

    :param format:
        the format to check
    :type format: snd_pcm_format_t

.. _`snd_pcm_format_unsigned.return`:

Return
------

1 if the given PCM format is unsigned linear, 0 if signed
linear, and a negative error code for non-linear formats.

.. _`snd_pcm_format_linear`:

snd_pcm_format_linear
=====================

.. c:function:: int snd_pcm_format_linear(snd_pcm_format_t format)

    Check the PCM format is linear

    :param format:
        the format to check
    :type format: snd_pcm_format_t

.. _`snd_pcm_format_linear.return`:

Return
------

1 if the given PCM format is linear, 0 if not.

.. _`snd_pcm_format_little_endian`:

snd_pcm_format_little_endian
============================

.. c:function:: int snd_pcm_format_little_endian(snd_pcm_format_t format)

    Check the PCM format is little-endian

    :param format:
        the format to check
    :type format: snd_pcm_format_t

.. _`snd_pcm_format_little_endian.return`:

Return
------

1 if the given PCM format is little-endian, 0 if
big-endian, or a negative error code if endian not specified.

.. _`snd_pcm_format_big_endian`:

snd_pcm_format_big_endian
=========================

.. c:function:: int snd_pcm_format_big_endian(snd_pcm_format_t format)

    Check the PCM format is big-endian

    :param format:
        the format to check
    :type format: snd_pcm_format_t

.. _`snd_pcm_format_big_endian.return`:

Return
------

1 if the given PCM format is big-endian, 0 if
little-endian, or a negative error code if endian not specified.

.. _`snd_pcm_format_width`:

snd_pcm_format_width
====================

.. c:function:: int snd_pcm_format_width(snd_pcm_format_t format)

    return the bit-width of the format

    :param format:
        the format to check
    :type format: snd_pcm_format_t

.. _`snd_pcm_format_width.return`:

Return
------

The bit-width of the format, or a negative error code
if unknown format.

.. _`snd_pcm_format_physical_width`:

snd_pcm_format_physical_width
=============================

.. c:function:: int snd_pcm_format_physical_width(snd_pcm_format_t format)

    return the physical bit-width of the format

    :param format:
        the format to check
    :type format: snd_pcm_format_t

.. _`snd_pcm_format_physical_width.return`:

Return
------

The physical bit-width of the format, or a negative error code
if unknown format.

.. _`snd_pcm_format_size`:

snd_pcm_format_size
===================

.. c:function:: ssize_t snd_pcm_format_size(snd_pcm_format_t format, size_t samples)

    return the byte size of samples on the given format

    :param format:
        the format to check
    :type format: snd_pcm_format_t

    :param samples:
        sampling rate
    :type samples: size_t

.. _`snd_pcm_format_size.return`:

Return
------

The byte size of the given samples for the format, or a
negative error code if unknown format.

.. _`snd_pcm_format_silence_64`:

snd_pcm_format_silence_64
=========================

.. c:function:: const unsigned char *snd_pcm_format_silence_64(snd_pcm_format_t format)

    return the silent data in 8 bytes array

    :param format:
        the format to check
    :type format: snd_pcm_format_t

.. _`snd_pcm_format_silence_64.return`:

Return
------

The format pattern to fill or \ ``NULL``\  if error.

.. _`snd_pcm_format_set_silence`:

snd_pcm_format_set_silence
==========================

.. c:function:: int snd_pcm_format_set_silence(snd_pcm_format_t format, void *data, unsigned int samples)

    set the silence data on the buffer

    :param format:
        the PCM format
    :type format: snd_pcm_format_t

    :param data:
        the buffer pointer
    :type data: void \*

    :param samples:
        the number of samples to set silence
    :type samples: unsigned int

.. _`snd_pcm_format_set_silence.description`:

Description
-----------

Sets the silence data on the buffer for the given samples.

.. _`snd_pcm_format_set_silence.return`:

Return
------

Zero if successful, or a negative error code on failure.

.. _`snd_pcm_limit_hw_rates`:

snd_pcm_limit_hw_rates
======================

.. c:function:: int snd_pcm_limit_hw_rates(struct snd_pcm_runtime *runtime)

    determine rate_min/rate_max fields

    :param runtime:
        the runtime instance
    :type runtime: struct snd_pcm_runtime \*

.. _`snd_pcm_limit_hw_rates.description`:

Description
-----------

Determines the rate_min and rate_max fields from the rates bits of
the given runtime->hw.

.. _`snd_pcm_limit_hw_rates.return`:

Return
------

Zero if successful.

.. _`snd_pcm_rate_to_rate_bit`:

snd_pcm_rate_to_rate_bit
========================

.. c:function:: unsigned int snd_pcm_rate_to_rate_bit(unsigned int rate)

    converts sample rate to SNDRV_PCM_RATE_xxx bit

    :param rate:
        the sample rate to convert
    :type rate: unsigned int

.. _`snd_pcm_rate_to_rate_bit.return`:

Return
------

The SNDRV_PCM_RATE_xxx flag that corresponds to the given rate, or
SNDRV_PCM_RATE_KNOT for an unknown rate.

.. _`snd_pcm_rate_bit_to_rate`:

snd_pcm_rate_bit_to_rate
========================

.. c:function:: unsigned int snd_pcm_rate_bit_to_rate(unsigned int rate_bit)

    converts SNDRV_PCM_RATE_xxx bit to sample rate

    :param rate_bit:
        the rate bit to convert
    :type rate_bit: unsigned int

.. _`snd_pcm_rate_bit_to_rate.return`:

Return
------

The sample rate that corresponds to the given SNDRV_PCM_RATE_xxx flag
or 0 for an unknown rate bit.

.. _`snd_pcm_rate_mask_intersect`:

snd_pcm_rate_mask_intersect
===========================

.. c:function:: unsigned int snd_pcm_rate_mask_intersect(unsigned int rates_a, unsigned int rates_b)

    computes the intersection between two rate masks

    :param rates_a:
        The first rate mask
    :type rates_a: unsigned int

    :param rates_b:
        The second rate mask
    :type rates_b: unsigned int

.. _`snd_pcm_rate_mask_intersect.description`:

Description
-----------

This function computes the rates that are supported by both rate masks passed
to the function. It will take care of the special handling of
SNDRV_PCM_RATE_CONTINUOUS and SNDRV_PCM_RATE_KNOT.

.. _`snd_pcm_rate_mask_intersect.return`:

Return
------

A rate mask containing the rates that are supported by both rates_a
and rates_b.

.. _`snd_pcm_rate_range_to_bits`:

snd_pcm_rate_range_to_bits
==========================

.. c:function:: unsigned int snd_pcm_rate_range_to_bits(unsigned int rate_min, unsigned int rate_max)

    converts rate range to SNDRV_PCM_RATE_xxx bit

    :param rate_min:
        the minimum sample rate
    :type rate_min: unsigned int

    :param rate_max:
        the maximum sample rate
    :type rate_max: unsigned int

.. _`snd_pcm_rate_range_to_bits.description`:

Description
-----------

This function has an implicit assumption: the rates in the given range have
only the pre-defined rates like 44100 or 16000.

.. _`snd_pcm_rate_range_to_bits.return`:

Return
------

The SNDRV_PCM_RATE_xxx flag that corresponds to the given rate range,
or SNDRV_PCM_RATE_KNOT for an unknown range.

.. This file was automatic generated / don't edit.

