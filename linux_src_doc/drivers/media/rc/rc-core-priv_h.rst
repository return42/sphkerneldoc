.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/rc/rc-core-priv.h

.. _`rc_open`:

rc_open
=======

.. c:function:: int rc_open(struct rc_dev *rdev)

    Opens a RC device

    :param rdev:
        pointer to struct rc_dev.
    :type rdev: struct rc_dev \*

.. _`rc_close`:

rc_close
========

.. c:function:: void rc_close(struct rc_dev *rdev)

    Closes a RC device

    :param rdev:
        pointer to struct rc_dev.
    :type rdev: struct rc_dev \*

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
        unsigned int leader_pulse;
        unsigned int leader_space;
        unsigned int clock;
        unsigned int invert:1;
        unsigned int trailer_space;
    }

.. _`ir_raw_timings_manchester.members`:

Members
-------

leader_pulse
    duration of leader pulse (if any) 0 if continuing
    existing signal

leader_space
    duration of leader space (if any)

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

    :param ev:
        Pointer to pointer to next free raw event.
        Will be incremented for each raw event written.
    :type ev: struct ir_raw_event \*\*

    :param max:
        Pointer to number of raw events available in buffer.
        Will be decremented for each raw event written.
    :type max: unsigned int \*

    :param pulse_width:
        Width of pulse in ns.
    :type pulse_width: unsigned int

    :param space_width:
        Width of space in ns.
    :type space_width: unsigned int

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
        unsigned int bit_space[2];
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
        unsigned int bit_pulse[2];
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

