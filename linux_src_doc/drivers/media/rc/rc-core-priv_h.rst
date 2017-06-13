.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/rc-core-priv.h

.. _`ir_raw_timings_manchester`:

struct ir_raw_timings_manchester
================================

.. c:type:: struct ir_raw_timings_manchester

    Manchester coding timings

.. _`ir_raw_timings_manchester.definition`:

Definition
----------

.. code-block:: c

    struct ir_raw_timings_manchester {
        unsigned int leader;
        unsigned int pulse_space_start:1;
        unsigned int clock;
        unsigned int invert:1;
        unsigned int trailer_space;
    }

.. _`ir_raw_timings_manchester.members`:

Members
-------

leader
    duration of leader pulse (if any) 0 if continuing
    existing signal (see \ ``pulse_space_start``\ )

pulse_space_start
    1 for starting with pulse (0 for starting with space)

clock
    duration of each pulse/space in ns

invert
    if set clock logic is inverted
    (0 = space + pulse, 1 = pulse + space)

trailer_space
    duration of trailer space in ns

.. _`ir_raw_gen_pulse_space`:

ir_raw_gen_pulse_space
======================

.. c:function:: int ir_raw_gen_pulse_space(struct ir_raw_event **ev, unsigned int *max, unsigned int pulse_width, unsigned int space_width)

    generate pulse and space raw events.

    :param struct ir_raw_event \*\*ev:
        Pointer to pointer to next free raw event.
        Will be incremented for each raw event written.

    :param unsigned int \*max:
        Pointer to number of raw events available in buffer.
        Will be decremented for each raw event written.

    :param unsigned int pulse_width:
        Width of pulse in ns.

    :param unsigned int space_width:
        Width of space in ns.

.. _`ir_raw_gen_pulse_space.return`:

Return
------

0 on success.
-ENOBUFS if there isn't enough buffer space to write both raw
events. In this case \ ``max``\  events will have been written.

.. _`ir_raw_timings_pd`:

struct ir_raw_timings_pd
========================

.. c:type:: struct ir_raw_timings_pd

    pulse-distance modulation timings

.. _`ir_raw_timings_pd.definition`:

Definition
----------

.. code-block:: c

    struct ir_raw_timings_pd {
        unsigned int header_pulse;
        unsigned int header_space;
        unsigned int bit_pulse;
        unsigned int bit_space;
        unsigned int trailer_pulse;
        unsigned int trailer_space;
        unsigned int msb_first:1;
    }

.. _`ir_raw_timings_pd.members`:

Members
-------

header_pulse
    duration of header pulse in ns (0 for none)

header_space
    duration of header space in ns

bit_pulse
    duration of bit pulse in ns

bit_space
    duration of bit space (for logic 0 and 1) in ns

trailer_pulse
    duration of trailer pulse in ns

trailer_space
    duration of trailer space in ns

msb_first
    1 if most significant bit is sent first

.. _`ir_raw_timings_pl`:

struct ir_raw_timings_pl
========================

.. c:type:: struct ir_raw_timings_pl

    pulse-length modulation timings

.. _`ir_raw_timings_pl.definition`:

Definition
----------

.. code-block:: c

    struct ir_raw_timings_pl {
        unsigned int header_pulse;
        unsigned int bit_space;
        unsigned int bit_pulse;
        unsigned int trailer_space;
        unsigned int msb_first:1;
    }

.. _`ir_raw_timings_pl.members`:

Members
-------

header_pulse
    duration of header pulse in ns (0 for none)

bit_space
    duration of bit space in ns

bit_pulse
    duration of bit pulse (for logic 0 and 1) in ns

trailer_space
    duration of trailer space in ns

msb_first
    1 if most significant bit is sent first

.. This file was automatic generated / don't edit.

