.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/img-ir/img-ir-hw.c

.. _`img_ir_control`:

img_ir_control
==============

.. c:function:: u32 img_ir_control(const struct img_ir_control *control)

    Convert control struct to control register value.

    :param control:
        Control data
    :type control: const struct img_ir_control \*

.. _`img_ir_control.return`:

Return
------

The control register value equivalent of \ ``control``\ .

.. _`img_ir_timing_range_convert`:

img_ir_timing_range_convert
===========================

.. c:function:: void img_ir_timing_range_convert(struct img_ir_timing_range *out, const struct img_ir_timing_range *in, unsigned int tolerance, unsigned long clock_hz, unsigned int shift)

    Convert microsecond range.

    :param out:
        Output timing range in clock cycles with a shift.
    :type out: struct img_ir_timing_range \*

    :param in:
        Input timing range in microseconds.
    :type in: const struct img_ir_timing_range \*

    :param tolerance:
        Tolerance as a fraction of 128 (roughly percent).
    :type tolerance: unsigned int

    :param clock_hz:
        IR clock rate in Hz.
    :type clock_hz: unsigned long

    :param shift:
        Shift of output units.
    :type shift: unsigned int

.. _`img_ir_timing_range_convert.description`:

Description
-----------

Converts min and max from microseconds to IR clock cycles, applies a
tolerance, and shifts for the register, rounding in the right direction.
Note that in and out can safely be the same object.

.. _`img_ir_symbol_timing`:

img_ir_symbol_timing
====================

.. c:function:: u32 img_ir_symbol_timing(const struct img_ir_symbol_timing *timing, unsigned int tolerance, unsigned long clock_hz, unsigned int pd_shift, unsigned int w_shift)

    Convert symbol timing struct to register value.

    :param timing:
        Symbol timing data
    :type timing: const struct img_ir_symbol_timing \*

    :param tolerance:
        Timing tolerance where 0-128 represents 0-100%
    :type tolerance: unsigned int

    :param clock_hz:
        Frequency of source clock in Hz
    :type clock_hz: unsigned long

    :param pd_shift:
        Shift to apply to symbol period
    :type pd_shift: unsigned int

    :param w_shift:
        Shift to apply to symbol width
    :type w_shift: unsigned int

.. _`img_ir_symbol_timing.return`:

Return
------

Symbol timing register value based on arguments.

.. _`img_ir_free_timing`:

img_ir_free_timing
==================

.. c:function:: u32 img_ir_free_timing(const struct img_ir_free_timing *timing, unsigned long clock_hz)

    Convert free time timing struct to register value.

    :param timing:
        Free symbol timing data
    :type timing: const struct img_ir_free_timing \*

    :param clock_hz:
        Source clock frequency in Hz
    :type clock_hz: unsigned long

.. _`img_ir_free_timing.return`:

Return
------

Free symbol timing register value.

.. _`img_ir_free_timing_dynamic`:

img_ir_free_timing_dynamic
==========================

.. c:function:: u32 img_ir_free_timing_dynamic(u32 st_ft, struct img_ir_filter *filter)

    Update free time register value.

    :param st_ft:
        Static free time register value from img_ir_free_timing.
    :type st_ft: u32

    :param filter:
        Current filter which may additionally restrict min/max len.
    :type filter: struct img_ir_filter \*

.. _`img_ir_free_timing_dynamic.return`:

Return
------

Updated free time register value based on the current filter.

.. _`img_ir_timings_convert`:

img_ir_timings_convert
======================

.. c:function:: void img_ir_timings_convert(struct img_ir_timing_regvals *regs, const struct img_ir_timings *timings, unsigned int tolerance, unsigned int clock_hz)

    Convert timings to register values

    :param regs:
        Output timing register values
    :type regs: struct img_ir_timing_regvals \*

    :param timings:
        Input timing data
    :type timings: const struct img_ir_timings \*

    :param tolerance:
        Timing tolerance where 0-128 represents 0-100%
    :type tolerance: unsigned int

    :param clock_hz:
        Source clock frequency in Hz
    :type clock_hz: unsigned int

.. _`img_ir_decoder_preprocess`:

img_ir_decoder_preprocess
=========================

.. c:function:: void img_ir_decoder_preprocess(struct img_ir_decoder *decoder)

    Preprocess timings in decoder.

    :param decoder:
        Decoder to be preprocessed.
    :type decoder: struct img_ir_decoder \*

.. _`img_ir_decoder_preprocess.description`:

Description
-----------

Ensures that the symbol timing ranges are valid with respect to ordering, and
does some fixed conversion on them.

.. _`img_ir_decoder_convert`:

img_ir_decoder_convert
======================

.. c:function:: void img_ir_decoder_convert(const struct img_ir_decoder *decoder, struct img_ir_reg_timings *reg_timings, unsigned int clock_hz)

    Generate internal timings in decoder.

    :param decoder:
        Decoder to be converted to internal timings.
    :type decoder: const struct img_ir_decoder \*

    :param reg_timings:
        Timing register values.
    :type reg_timings: struct img_ir_reg_timings \*

    :param clock_hz:
        IR clock rate in Hz.
    :type clock_hz: unsigned int

.. _`img_ir_decoder_convert.description`:

Description
-----------

Fills out the repeat timings and timing register values for a specific clock
rate.

.. _`img_ir_write_timings`:

img_ir_write_timings
====================

.. c:function:: void img_ir_write_timings(struct img_ir_priv *priv, struct img_ir_timing_regvals *regs, enum rc_filter_type type)

    Write timings to the hardware now

    :param priv:
        IR private data
    :type priv: struct img_ir_priv \*

    :param regs:
        Timing register values to write
    :type regs: struct img_ir_timing_regvals \*

    :param type:
        RC filter type (RC_FILTER\_\*)
    :type type: enum rc_filter_type

.. _`img_ir_write_timings.description`:

Description
-----------

Write timing register values \ ``regs``\  to the hardware, taking into account the
current filter which may impose restrictions on the length of the expected
data.

.. _`img_ir_set_decoder`:

img_ir_set_decoder
==================

.. c:function:: void img_ir_set_decoder(struct img_ir_priv *priv, const struct img_ir_decoder *decoder, u64 proto)

    Set the current decoder.

    :param priv:
        IR private data.
    :type priv: struct img_ir_priv \*

    :param decoder:
        Decoder to use with immediate effect.
    :type decoder: const struct img_ir_decoder \*

    :param proto:
        Protocol bitmap (or 0 to use decoder->type).
    :type proto: u64

.. _`img_ir_decoder_compatible`:

img_ir_decoder_compatible
=========================

.. c:function:: bool img_ir_decoder_compatible(struct img_ir_priv *priv, const struct img_ir_decoder *dec)

    Find whether a decoder will work with a device.

    :param priv:
        IR private data.
    :type priv: struct img_ir_priv \*

    :param dec:
        Decoder to check.
    :type dec: const struct img_ir_decoder \*

.. _`img_ir_decoder_compatible.return`:

Return
------

true if \ ``dec``\  is compatible with the device \ ``priv``\  refers to.

.. _`img_ir_allowed_protos`:

img_ir_allowed_protos
=====================

.. c:function:: u64 img_ir_allowed_protos(struct img_ir_priv *priv)

    Get allowed protocols from global decoder list.

    :param priv:
        IR private data.
    :type priv: struct img_ir_priv \*

.. _`img_ir_allowed_protos.return`:

Return
------

Mask of protocols supported by the device \ ``priv``\  refers to.

.. _`img_ir_enable_wake`:

img_ir_enable_wake
==================

.. c:function:: int img_ir_enable_wake(struct img_ir_priv *priv)

    Switch to wake mode.

    :param priv:
        IR private data.
    :type priv: struct img_ir_priv \*

.. _`img_ir_enable_wake.return`:

Return
------

non-zero if the IR can wake the system.

.. _`img_ir_disable_wake`:

img_ir_disable_wake
===================

.. c:function:: int img_ir_disable_wake(struct img_ir_priv *priv)

    Switch out of wake mode.

    :param priv:
        IR private data
    :type priv: struct img_ir_priv \*

.. _`img_ir_disable_wake.return`:

Return
------

1 if the hardware should be allowed to wake from a sleep state.
0 otherwise.

.. _`img_ir_probe_hw_caps`:

img_ir_probe_hw_caps
====================

.. c:function:: void img_ir_probe_hw_caps(struct img_ir_priv *priv)

    Probe capabilities of the hardware.

    :param priv:
        IR private data.
    :type priv: struct img_ir_priv \*

.. This file was automatic generated / don't edit.

