.. -*- coding: utf-8; mode: rst -*-

===========
img-ir-hw.h
===========



.. _xref_struct_img_ir_control:

struct img_ir_control
=====================

.. c:type:: struct img_ir_control

    Decoder control settings



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
  };



Members
-------

:``unsigned:1 decoden``:
    Primary decoder enable

:``unsigned:2 code_type``:
    Decode type (see IMG_IR_CODETYPE_*)

:``unsigned:1 hdrtog``:
    Detect header toggle symbol after leader symbol

:``unsigned:1 ldrdec``:
    Don't discard leader if maximum width reached

:``unsigned:1 decodinpol``:
    Decoder input polarity (1=active high)

:``unsigned:1 bitorien``:
    Bit orientation (1=MSB first)

:``unsigned:1 d1validsel``:
    Decoder 2 takes over if it detects valid data

:``unsigned:1 bitinv``:
    Bit inversion switch (1=don't invert)

:``unsigned:1 decodend2``:
    Secondary decoder enable (no leader symbol)

:``unsigned:1 bitoriend2``:
    Bit orientation (1=MSB first)

:``unsigned:1 bitinvd2``:
    Secondary decoder bit inversion switch (1=don't invert)





.. _xref_struct_img_ir_timing_range:

struct img_ir_timing_range
==========================

.. c:type:: struct img_ir_timing_range

    range of timing values



Definition
----------

.. code-block:: c

  struct img_ir_timing_range {
    u16 min;
    u16 max;
  };



Members
-------

:``u16 min``:
    Minimum timing value

:``u16 max``:
    Maximum timing value (if < **min**, this will be set to **min** during
    		preprocessing step, so it is normally not explicitly initialised
    		and is taken care of by the tolerance)





.. _xref_struct_img_ir_symbol_timing:

struct img_ir_symbol_timing
===========================

.. c:type:: struct img_ir_symbol_timing

    timing data for a symbol



Definition
----------

.. code-block:: c

  struct img_ir_symbol_timing {
    struct img_ir_timing_range pulse;
    struct img_ir_timing_range space;
  };



Members
-------

:``struct img_ir_timing_range pulse``:
    Timing range for the length of the pulse in this symbol

:``struct img_ir_timing_range space``:
    Timing range for the length of the space in this symbol





.. _xref_struct_img_ir_free_timing:

struct img_ir_free_timing
=========================

.. c:type:: struct img_ir_free_timing

    timing data for free time symbol



Definition
----------

.. code-block:: c

  struct img_ir_free_timing {
    u8 minlen;
    u8 maxlen;
    u16 ft_min;
  };



Members
-------

:``u8 minlen``:
    Minimum number of bits of data

:``u8 maxlen``:
    Maximum number of bits of data

:``u16 ft_min``:
    Minimum free time after message





.. _xref_struct_img_ir_timings:

struct img_ir_timings
=====================

.. c:type:: struct img_ir_timings

    Timing values.



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
  };



Members
-------

:``struct img_ir_symbol_timing ldr``:
    Leader symbol timing data

:``struct img_ir_symbol_timing s00``:
    Zero symbol timing data for primary decoder

:``struct img_ir_symbol_timing s01``:
    One symbol timing data for primary decoder

:``struct img_ir_symbol_timing s10``:
    Zero symbol timing data for secondary (no leader symbol) decoder

:``struct img_ir_symbol_timing s11``:
    One symbol timing data for secondary (no leader symbol) decoder

:``struct img_ir_free_timing ft``:
    Free time symbol timing data





.. _xref_struct_img_ir_filter:

struct img_ir_filter
====================

.. c:type:: struct img_ir_filter

    Filter IR events.



Definition
----------

.. code-block:: c

  struct img_ir_filter {
    u64 data;
    u64 mask;
    u8 minlen;
    u8 maxlen;
  };



Members
-------

:``u64 data``:
    Data to match.

:``u64 mask``:
    Mask of bits to compare.

:``u8 minlen``:
    Additional minimum number of bits.

:``u8 maxlen``:
    Additional maximum number of bits.





.. _xref_struct_img_ir_timing_regvals:

struct img_ir_timing_regvals
============================

.. c:type:: struct img_ir_timing_regvals

    Calculated timing register values.



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
  };



Members
-------

:``u32 ldr``:
    Leader symbol timing register value

:``u32 s00``:
    Zero symbol timing register value for primary decoder

:``u32 s01``:
    One symbol timing register value for primary decoder

:``u32 s10``:
    Zero symbol timing register value for secondary decoder

:``u32 s11``:
    One symbol timing register value for secondary decoder

:``u32 ft``:
    Free time symbol timing register value





.. _xref_struct_img_ir_scancode_req:

struct img_ir_scancode_req
==========================

.. c:type:: struct img_ir_scancode_req

    Scancode request data.



Definition
----------

.. code-block:: c

  struct img_ir_scancode_req {
    enum rc_type protocol;
    u32 scancode;
    u8 toggle;
  };



Members
-------

:``enum rc_type protocol``:
    Protocol code of received message (defaults to
    		RC_TYPE_UNKNOWN).

:``u32 scancode``:
    Scan code of received message (must be written by
    		handler if IMG_IR_SCANCODE is returned).

:``u8 toggle``:
    Toggle bit (defaults to 0).





.. _xref_struct_img_ir_decoder:

struct img_ir_decoder
=====================

.. c:type:: struct img_ir_decoder

    Decoder settings for an IR protocol.



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
    int (* scancode) (int len, u64 raw, u64 enabled_protocols,struct img_ir_scancode_req *request);
    int (* filter) (const struct rc_scancode_filter *in,struct img_ir_filter *out, u64 protocols);
  };



Members
-------

:``u64 type``:
    Protocol types bitmap.

:``unsigned int tolerance``:
    Timing tolerance as a percentage (default 10%).

:``unsigned int unit``:
    Unit of timings in nanoseconds (default 1 us).

:``struct img_ir_timings timings``:
    Primary timings

:``struct img_ir_timings rtimings``:
    Additional override timings while waiting for repeats.

:``unsigned int repeat``:
    Maximum repeat interval (always in milliseconds).

:``struct img_ir_control control``:
    Control flags.

:``int (*)(int len, u64 raw, u64 enabled_protocols,struct img_ir_scancode_req *request) scancode``:
    Pointer to function to convert the IR data into a scancode (it
    		must be safe to execute in interrupt context).
    		Returns IMG_IR_SCANCODE to emit new scancode.
    		Returns IMG_IR_REPEATCODE to repeat previous code.
    		Returns -errno (e.g. -EINVAL) on error.

:``int (*)(const struct rc_scancode_filter *in,struct img_ir_filter *out, u64 protocols) filter``:
    Pointer to function to convert scancode filter to raw hardware
    		filter. The minlen and maxlen fields will have been initialised
    		to the maximum range.





.. _xref_struct_img_ir_reg_timings:

struct img_ir_reg_timings
=========================

.. c:type:: struct img_ir_reg_timings

    Reg values for decoder timings at clock rate.



Definition
----------

.. code-block:: c

  struct img_ir_reg_timings {
    u32 ctrl;
    struct img_ir_timing_regvals timings;
    struct img_ir_timing_regvals rtimings;
  };



Members
-------

:``u32 ctrl``:
    Processed control register value.

:``struct img_ir_timing_regvals timings``:
    Processed primary timings.

:``struct img_ir_timing_regvals rtimings``:
    Processed repeat timings.





.. _xref_struct_img_ir_priv_hw:

struct img_ir_priv_hw
=====================

.. c:type:: struct img_ir_priv_hw

    Private driver data for hardware decoder.



Definition
----------

.. code-block:: c

  struct img_ir_priv_hw {
    unsigned int ct_quirks[4];
    struct rc_dev * rdev;
    struct notifier_block clk_nb;
    struct timer_list end_timer;
    struct timer_list suspend_timer;
    const struct img_ir_decoder * decoder;
    u64 enabled_protocols;
    unsigned long clk_hz;
    struct img_ir_reg_timings reg_timings;
    unsigned int flags;
    struct img_ir_filter filters[RC_FILTER_MAX];
    enum img_ir_mode mode;
    bool stopping;
    u32 suspend_irqen;
    u32 quirk_suspend_irq;
  };



Members
-------

:``unsigned int ct_quirks[4]``:
    Quirk bits for each code type.

:``struct rc_dev * rdev``:
    Remote control device

:``struct notifier_block clk_nb``:
    Notifier block for clock notify events.

:``struct timer_list end_timer``:
    Timer until repeat timeout.

:``struct timer_list suspend_timer``:
    Timer to re-enable protocol.

:``const struct img_ir_decoder * decoder``:
    Current decoder settings.

:``u64 enabled_protocols``:
    Currently enabled protocols.

:``unsigned long clk_hz``:
    Current core clock rate in Hz.

:``struct img_ir_reg_timings reg_timings``:
    Timing reg values for decoder at clock rate.

:``unsigned int flags``:
    IMG_IR_F_*.

:``struct img_ir_filter filters[RC_FILTER_MAX]``:
    HW filters (derived from scancode filters).

:``enum img_ir_mode mode``:
    Current decode mode.

:``bool stopping``:
    Indicates that decoder is being taken down and timers
    			should not be restarted.

:``u32 suspend_irqen``:
    Saved IRQ enable mask over suspend.

:``u32 quirk_suspend_irq``:
    Saved IRQ enable mask over quirk suspend timer.



