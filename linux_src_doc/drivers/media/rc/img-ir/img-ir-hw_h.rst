.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/img-ir/img-ir-hw.h

.. _`img_ir_control`:

struct img_ir_control
=====================

.. c:type:: struct img_ir_control

    Decoder control settings

.. _`img_ir_control.definition`:

Definition
----------

.. code-block:: c

    struct img_ir_control {
        unsigned decoden:1;
        unsigned code_type:2;
        unsigned hdrtog:1;
        unsigned ldrdec:1;
        unsigned decodinpol:1;
        unsigned bitorien:1;
        unsigned d1validsel:1;
        unsigned bitinv:1;
        unsigned decodend2:1;
        unsigned bitoriend2:1;
        unsigned bitinvd2:1;
    }

.. _`img_ir_control.members`:

Members
-------

decoden
    Primary decoder enable

code_type
    Decode type (see IMG_IR_CODETYPE\_\*)

hdrtog
    Detect header toggle symbol after leader symbol

ldrdec
    Don't discard leader if maximum width reached

decodinpol
    Decoder input polarity (1=active high)

bitorien
    Bit orientation (1=MSB first)

d1validsel
    Decoder 2 takes over if it detects valid data

bitinv
    Bit inversion switch (1=don't invert)

decodend2
    Secondary decoder enable (no leader symbol)

bitoriend2
    Bit orientation (1=MSB first)

bitinvd2
    Secondary decoder bit inversion switch (1=don't invert)

.. _`img_ir_timing_range`:

struct img_ir_timing_range
==========================

.. c:type:: struct img_ir_timing_range

    range of timing values

.. _`img_ir_timing_range.definition`:

Definition
----------

.. code-block:: c

    struct img_ir_timing_range {
        u16 min;
        u16 max;
    }

.. _`img_ir_timing_range.members`:

Members
-------

min
    Minimum timing value

max
    Maximum timing value (if < \ ``min``\ , this will be set to \ ``min``\  during
    preprocessing step, so it is normally not explicitly initialised
    and is taken care of by the tolerance)

.. _`img_ir_symbol_timing`:

struct img_ir_symbol_timing
===========================

.. c:type:: struct img_ir_symbol_timing

    timing data for a symbol

.. _`img_ir_symbol_timing.definition`:

Definition
----------

.. code-block:: c

    struct img_ir_symbol_timing {
        struct img_ir_timing_range pulse;
        struct img_ir_timing_range space;
    }

.. _`img_ir_symbol_timing.members`:

Members
-------

pulse
    Timing range for the length of the pulse in this symbol

space
    Timing range for the length of the space in this symbol

.. _`img_ir_free_timing`:

struct img_ir_free_timing
=========================

.. c:type:: struct img_ir_free_timing

    timing data for free time symbol

.. _`img_ir_free_timing.definition`:

Definition
----------

.. code-block:: c

    struct img_ir_free_timing {
        u8 minlen;
        u8 maxlen;
        u16 ft_min;
    }

.. _`img_ir_free_timing.members`:

Members
-------

minlen
    Minimum number of bits of data

maxlen
    Maximum number of bits of data

ft_min
    Minimum free time after message

.. _`img_ir_timings`:

struct img_ir_timings
=====================

.. c:type:: struct img_ir_timings

    Timing values.

.. _`img_ir_timings.definition`:

Definition
----------

.. code-block:: c

    struct img_ir_timings {
        struct img_ir_symbol_timing ldr;
        struct img_ir_symbol_timing s00;
        struct img_ir_symbol_timing s01;
        struct img_ir_symbol_timing s10;
        struct img_ir_symbol_timing s11;
        struct img_ir_free_timing ft;
    }

.. _`img_ir_timings.members`:

Members
-------

ldr
    Leader symbol timing data

s00
    Zero symbol timing data for primary decoder

s01
    One symbol timing data for primary decoder

s10
    Zero symbol timing data for secondary (no leader symbol) decoder

s11
    One symbol timing data for secondary (no leader symbol) decoder

ft
    Free time symbol timing data

.. _`img_ir_filter`:

struct img_ir_filter
====================

.. c:type:: struct img_ir_filter

    Filter IR events.

.. _`img_ir_filter.definition`:

Definition
----------

.. code-block:: c

    struct img_ir_filter {
        u64 data;
        u64 mask;
        u8 minlen;
        u8 maxlen;
    }

.. _`img_ir_filter.members`:

Members
-------

data
    Data to match.

mask
    Mask of bits to compare.

minlen
    Additional minimum number of bits.

maxlen
    Additional maximum number of bits.

.. _`img_ir_timing_regvals`:

struct img_ir_timing_regvals
============================

.. c:type:: struct img_ir_timing_regvals

    Calculated timing register values.

.. _`img_ir_timing_regvals.definition`:

Definition
----------

.. code-block:: c

    struct img_ir_timing_regvals {
        u32 ldr;
        u32 s00;
        u32 s01;
        u32 s10;
        u32 s11;
        u32 ft;
    }

.. _`img_ir_timing_regvals.members`:

Members
-------

ldr
    Leader symbol timing register value

s00
    Zero symbol timing register value for primary decoder

s01
    One symbol timing register value for primary decoder

s10
    Zero symbol timing register value for secondary decoder

s11
    One symbol timing register value for secondary decoder

ft
    Free time symbol timing register value

.. _`img_ir_scancode_req`:

struct img_ir_scancode_req
==========================

.. c:type:: struct img_ir_scancode_req

    Scancode request data.

.. _`img_ir_scancode_req.definition`:

Definition
----------

.. code-block:: c

    struct img_ir_scancode_req {
        enum rc_type protocol;
        u32 scancode;
        u8 toggle;
    }

.. _`img_ir_scancode_req.members`:

Members
-------

protocol
    Protocol code of received message (defaults to
    RC_TYPE_UNKNOWN).

scancode
    Scan code of received message (must be written by
    handler if IMG_IR_SCANCODE is returned).

toggle
    Toggle bit (defaults to 0).

.. _`img_ir_decoder`:

struct img_ir_decoder
=====================

.. c:type:: struct img_ir_decoder

    Decoder settings for an IR protocol.

.. _`img_ir_decoder.definition`:

Definition
----------

.. code-block:: c

    struct img_ir_decoder {
        u64 type;
        unsigned int tolerance;
        unsigned int unit;
        struct img_ir_timings timings;
        struct img_ir_timings rtimings;
        unsigned int repeat;
        struct img_ir_control control;
        int (*scancode)(int len, u64 raw, u64 enabled_protocols,struct img_ir_scancode_req *request);
        int (*filter)(const struct rc_scancode_filter *in,struct img_ir_filter *out, u64 protocols);
    }

.. _`img_ir_decoder.members`:

Members
-------

type
    Protocol types bitmap.

tolerance
    Timing tolerance as a percentage (default 10%).

unit
    Unit of timings in nanoseconds (default 1 us).

timings
    Primary timings

rtimings
    Additional override timings while waiting for repeats.

repeat
    Maximum repeat interval (always in milliseconds).

control
    Control flags.

scancode
    Pointer to function to convert the IR data into a scancode (it
    must be safe to execute in interrupt context).
    Returns IMG_IR_SCANCODE to emit new scancode.
    Returns IMG_IR_REPEATCODE to repeat previous code.
    Returns -errno (e.g. -EINVAL) on error.

filter
    Pointer to function to convert scancode filter to raw hardware
    filter. The minlen and maxlen fields will have been initialised
    to the maximum range.

.. _`img_ir_reg_timings`:

struct img_ir_reg_timings
=========================

.. c:type:: struct img_ir_reg_timings

    Reg values for decoder timings at clock rate.

.. _`img_ir_reg_timings.definition`:

Definition
----------

.. code-block:: c

    struct img_ir_reg_timings {
        u32 ctrl;
        struct img_ir_timing_regvals timings;
        struct img_ir_timing_regvals rtimings;
    }

.. _`img_ir_reg_timings.members`:

Members
-------

ctrl
    Processed control register value.

timings
    Processed primary timings.

rtimings
    Processed repeat timings.

.. _`img_ir_priv_hw`:

struct img_ir_priv_hw
=====================

.. c:type:: struct img_ir_priv_hw

    Private driver data for hardware decoder.

.. _`img_ir_priv_hw.definition`:

Definition
----------

.. code-block:: c

    struct img_ir_priv_hw {
        unsigned int ct_quirks;
        struct rc_dev *rdev;
        struct notifier_block clk_nb;
        struct timer_list end_timer;
        struct timer_list suspend_timer;
        const struct img_ir_decoder *decoder;
        u64 enabled_protocols;
        unsigned long clk_hz;
        struct img_ir_reg_timings reg_timings;
        unsigned int flags;
        struct img_ir_filter filters;
        enum img_ir_mode mode;
        bool stopping;
        u32 suspend_irqen;
        u32 quirk_suspend_irq;
    }

.. _`img_ir_priv_hw.members`:

Members
-------

ct_quirks
    Quirk bits for each code type.

rdev
    Remote control device

clk_nb
    Notifier block for clock notify events.

end_timer
    Timer until repeat timeout.

suspend_timer
    Timer to re-enable protocol.

decoder
    Current decoder settings.

enabled_protocols
    Currently enabled protocols.

clk_hz
    Current core clock rate in Hz.

reg_timings
    Timing reg values for decoder at clock rate.

flags
    IMG_IR_F\_\*.

filters
    HW filters (derived from scancode filters).

mode
    Current decode mode.

stopping
    Indicates that decoder is being taken down and timers
    should not be restarted.

suspend_irqen
    Saved IRQ enable mask over suspend.

quirk_suspend_irq
    Saved IRQ enable mask over quirk suspend timer.

.. This file was automatic generated / don't edit.

