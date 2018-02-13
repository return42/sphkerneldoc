.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/clocksource/timer-stm32.c

.. _`stm32_timer_of_bits_set`:

stm32_timer_of_bits_set
=======================

.. c:function:: void stm32_timer_of_bits_set(struct timer_of *to, int bits)

    set accessor helper

    :param struct timer_of \*to:
        a timer_of structure pointer

    :param int bits:
        the number of bits (16 or 32)

.. _`stm32_timer_of_bits_set.description`:

Description
-----------

Accessor helper to set the number of bits in the timer-of private
structure.

.. _`stm32_timer_of_bits_get`:

stm32_timer_of_bits_get
=======================

.. c:function:: int stm32_timer_of_bits_get(struct timer_of *to)

    get accessor helper

    :param struct timer_of \*to:
        a timer_of structure pointer

.. _`stm32_timer_of_bits_get.description`:

Description
-----------

Accessor helper to get the number of bits in the timer-of private
structure.

Returns an integer corresponding to the number of bits.

.. _`stm32_timer_start`:

stm32_timer_start
=================

.. c:function:: void stm32_timer_start(struct timer_of *to)

    Start the counter without event

    :param struct timer_of \*to:
        a timer_of structure pointer

.. _`stm32_timer_start.description`:

Description
-----------

Start the timer in order to have the counter reset and start
incrementing but disable interrupt event when there is a counter
overflow. By default, the counter direction is used as upcounter.

.. _`stm32_timer_set_width`:

stm32_timer_set_width
=====================

.. c:function:: void stm32_timer_set_width(struct timer_of *to)

    Sort out the timer width (32/16)

    :param struct timer_of \*to:
        a pointer to a timer-of structure

.. _`stm32_timer_set_width.description`:

Description
-----------

Write the 32-bit max value and read/return the result. If the timer
is 32 bits wide, the result will be UINT_MAX, otherwise it will
be truncated by the 16-bit register to USHRT_MAX.

.. _`stm32_timer_set_prescaler`:

stm32_timer_set_prescaler
=========================

.. c:function:: void stm32_timer_set_prescaler(struct timer_of *to)

    Compute and set the prescaler register

    :param struct timer_of \*to:
        a pointer to a timer-of structure

.. _`stm32_timer_set_prescaler.description`:

Description
-----------

Depending on the timer width, compute the prescaler to always
target a 10MHz timer rate for 16 bits. 32-bit timers are
considered precise and long enough to not use the prescaler.

.. This file was automatic generated / don't edit.

