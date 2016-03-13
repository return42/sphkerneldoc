.. -*- coding: utf-8; mode: rst -*-

===========
img-ir-hw.c
===========



.. _xref_img_ir_control:

img_ir_control
==============

.. c:function:: u32 img_ir_control (const struct img_ir_control * control)

    Convert control struct to control register value.

    :param const struct img_ir_control * control:
        Control data



Returns
-------

The control register value equivalent of **control**.




.. _xref_img_ir_timing_range_convert:

img_ir_timing_range_convert
===========================

.. c:function:: void img_ir_timing_range_convert (struct img_ir_timing_range * out, const struct img_ir_timing_range * in, unsigned int tolerance, unsigned long clock_hz, unsigned int shift)

    Convert microsecond range.

    :param struct img_ir_timing_range * out:
        Output timing range in clock cycles with a shift.

    :param const struct img_ir_timing_range * in:
        Input timing range in microseconds.

    :param unsigned int tolerance:
        Tolerance as a fraction of 128 (roughly percent).

    :param unsigned long clock_hz:
        IR clock rate in Hz.

    :param unsigned int shift:
        Shift of output units.



Description
-----------

Converts min and max from microseconds to IR clock cycles, applies a
tolerance, and shifts for the register, rounding in the right direction.
Note that in and out can safely be the same object.




.. _xref_img_ir_symbol_timing:

img_ir_symbol_timing
====================

.. c:function:: u32 img_ir_symbol_timing (const struct img_ir_symbol_timing * timing, unsigned int tolerance, unsigned long clock_hz, unsigned int pd_shift, unsigned int w_shift)

    Convert symbol timing struct to register value.

    :param const struct img_ir_symbol_timing * timing:
        Symbol timing data

    :param unsigned int tolerance:
        Timing tolerance where 0-128 represents 0-100%

    :param unsigned long clock_hz:
        Frequency of source clock in Hz

    :param unsigned int pd_shift:
        Shift to apply to symbol period

    :param unsigned int w_shift:
        Shift to apply to symbol width



Returns
-------

Symbol timing register value based on arguments.




.. _xref_img_ir_free_timing:

img_ir_free_timing
==================

.. c:function:: u32 img_ir_free_timing (const struct img_ir_free_timing * timing, unsigned long clock_hz)

    Convert free time timing struct to register value.

    :param const struct img_ir_free_timing * timing:
        Free symbol timing data

    :param unsigned long clock_hz:
        Source clock frequency in Hz



Returns
-------

Free symbol timing register value.




.. _xref_img_ir_free_timing_dynamic:

img_ir_free_timing_dynamic
==========================

.. c:function:: u32 img_ir_free_timing_dynamic (u32 st_ft, struct img_ir_filter * filter)

    Update free time register value.

    :param u32 st_ft:
        Static free time register value from img_ir_free_timing.

    :param struct img_ir_filter * filter:
        Current filter which may additionally restrict min/max len.



Returns
-------

Updated free time register value based on the current filter.




.. _xref_img_ir_timings_convert:

img_ir_timings_convert
======================

.. c:function:: void img_ir_timings_convert (struct img_ir_timing_regvals * regs, const struct img_ir_timings * timings, unsigned int tolerance, unsigned int clock_hz)

    Convert timings to register values

    :param struct img_ir_timing_regvals * regs:
        Output timing register values

    :param const struct img_ir_timings * timings:
        Input timing data

    :param unsigned int tolerance:
        Timing tolerance where 0-128 represents 0-100%

    :param unsigned int clock_hz:
        Source clock frequency in Hz




.. _xref_img_ir_decoder_preprocess:

img_ir_decoder_preprocess
=========================

.. c:function:: void img_ir_decoder_preprocess (struct img_ir_decoder * decoder)

    Preprocess timings in decoder.

    :param struct img_ir_decoder * decoder:
        Decoder to be preprocessed.



Description
-----------

Ensures that the symbol timing ranges are valid with respect to ordering, and
does some fixed conversion on them.




.. _xref_img_ir_decoder_convert:

img_ir_decoder_convert
======================

.. c:function:: void img_ir_decoder_convert (const struct img_ir_decoder * decoder, struct img_ir_reg_timings * reg_timings, unsigned int clock_hz)

    Generate internal timings in decoder.

    :param const struct img_ir_decoder * decoder:
        Decoder to be converted to internal timings.

    :param struct img_ir_reg_timings * reg_timings:

        _undescribed_

    :param unsigned int clock_hz:
        IR clock rate in Hz.



Description
-----------

Fills out the repeat timings and timing register values for a specific clock
rate.




.. _xref_img_ir_write_timings:

img_ir_write_timings
====================

.. c:function:: void img_ir_write_timings (struct img_ir_priv * priv, struct img_ir_timing_regvals * regs, enum rc_filter_type type)

    Write timings to the hardware now

    :param struct img_ir_priv * priv:
        IR private data

    :param struct img_ir_timing_regvals * regs:
        Timing register values to write

    :param enum rc_filter_type type:
        RC filter type (RC_FILTER_*)



Description
-----------

Write timing register values **regs** to the hardware, taking into account the
current filter which may impose restrictions on the length of the expected
data.




.. _xref_img_ir_set_decoder:

img_ir_set_decoder
==================

.. c:function:: void img_ir_set_decoder (struct img_ir_priv * priv, const struct img_ir_decoder * decoder, u64 proto)

    Set the current decoder.

    :param struct img_ir_priv * priv:
        IR private data.

    :param const struct img_ir_decoder * decoder:
        Decoder to use with immediate effect.

    :param u64 proto:
        Protocol bitmap (or 0 to use decoder->type).




.. _xref_img_ir_decoder_compatible:

img_ir_decoder_compatible
=========================

.. c:function:: bool img_ir_decoder_compatible (struct img_ir_priv * priv, const struct img_ir_decoder * dec)

    Find whether a decoder will work with a device.

    :param struct img_ir_priv * priv:
        IR private data.

    :param const struct img_ir_decoder * dec:
        Decoder to check.



Returns
-------

true if **dec** is compatible with the device **priv** refers to.




.. _xref_img_ir_allowed_protos:

img_ir_allowed_protos
=====================

.. c:function:: u64 img_ir_allowed_protos (struct img_ir_priv * priv)

    Get allowed protocols from global decoder list.

    :param struct img_ir_priv * priv:
        IR private data.



Returns
-------

Mask of protocols supported by the device **priv** refers to.




.. _xref_img_ir_enable_wake:

img_ir_enable_wake
==================

.. c:function:: int img_ir_enable_wake (struct img_ir_priv * priv)

    Switch to wake mode.

    :param struct img_ir_priv * priv:
        IR private data.



Returns
-------

non-zero if the IR can wake the system.




.. _xref_img_ir_disable_wake:

img_ir_disable_wake
===================

.. c:function:: int img_ir_disable_wake (struct img_ir_priv * priv)

    Switch out of wake mode.

    :param struct img_ir_priv * priv:
        IR private data



Returns
-------

1 if the hardware should be allowed to wake from a sleep state.
		0 otherwise.




.. _xref_img_ir_probe_hw_caps:

img_ir_probe_hw_caps
====================

.. c:function:: void img_ir_probe_hw_caps (struct img_ir_priv * priv)

    Probe capabilities of the hardware.

    :param struct img_ir_priv * priv:
        IR private data.


