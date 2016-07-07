.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/ucb1x00-core.c

.. _`ucb1x00_io_set_dir`:

ucb1x00_io_set_dir
==================

.. c:function:: void ucb1x00_io_set_dir(struct ucb1x00 *ucb, unsigned int in, unsigned int out)

    set IO direction

    :param struct ucb1x00 \*ucb:
        UCB1x00 structure describing chip

    :param unsigned int in:
        bitfield of IO pins to be set as inputs

    :param unsigned int out:
        bitfield of IO pins to be set as outputs

.. _`ucb1x00_io_set_dir.description`:

Description
-----------

Set the IO direction of the ten general purpose IO pins on
the UCB1x00 chip.  The \ ``in``\  bitfield has priority over the
\ ``out``\  bitfield, in that if you specify a pin as both input
and output, it will end up as an input.

ucb1x00_enable must have been called to enable the comms
before using this function.

This function takes a spinlock, disabling interrupts.

.. _`ucb1x00_io_write`:

ucb1x00_io_write
================

.. c:function:: void ucb1x00_io_write(struct ucb1x00 *ucb, unsigned int set, unsigned int clear)

    set or clear IO outputs

    :param struct ucb1x00 \*ucb:
        UCB1x00 structure describing chip

    :param unsigned int set:
        bitfield of IO pins to set to logic '1'

    :param unsigned int clear:
        bitfield of IO pins to set to logic '0'

.. _`ucb1x00_io_write.description`:

Description
-----------

Set the IO output state of the specified IO pins.  The value
is retained if the pins are subsequently configured as inputs.
The \ ``clear``\  bitfield has priority over the \ ``set``\  bitfield -
outputs will be cleared.

ucb1x00_enable must have been called to enable the comms
before using this function.

This function takes a spinlock, disabling interrupts.

.. _`ucb1x00_io_read`:

ucb1x00_io_read
===============

.. c:function:: unsigned int ucb1x00_io_read(struct ucb1x00 *ucb)

    read the current state of the IO pins

    :param struct ucb1x00 \*ucb:
        UCB1x00 structure describing chip

.. _`ucb1x00_io_read.description`:

Description
-----------

Return a bitfield describing the logic state of the ten
general purpose IO pins.

ucb1x00_enable must have been called to enable the comms
before using this function.

This function does not take any mutexes or spinlocks.

.. _`ucb1x00_adc_enable`:

ucb1x00_adc_enable
==================

.. c:function:: void ucb1x00_adc_enable(struct ucb1x00 *ucb)

    enable the ADC converter

    :param struct ucb1x00 \*ucb:
        UCB1x00 structure describing chip

.. _`ucb1x00_adc_enable.description`:

Description
-----------

Enable the ucb1x00 and ADC converter on the UCB1x00 for use.
Any code wishing to use the ADC converter must call this
function prior to using it.

This function takes the ADC mutex to prevent two or more
concurrent uses, and therefore may sleep.  As a result, it
can only be called from process context, not interrupt
context.

You should release the ADC as soon as possible using
ucb1x00_adc_disable.

.. _`ucb1x00_adc_read`:

ucb1x00_adc_read
================

.. c:function:: unsigned int ucb1x00_adc_read(struct ucb1x00 *ucb, int adc_channel, int sync)

    read the specified ADC channel

    :param struct ucb1x00 \*ucb:
        UCB1x00 structure describing chip

    :param int adc_channel:
        ADC channel mask

    :param int sync:
        wait for syncronisation pulse.

.. _`ucb1x00_adc_read.description`:

Description
-----------

Start an ADC conversion and wait for the result.  Note that
synchronised ADC conversions (via the ADCSYNC pin) must wait
until the trigger is asserted and the conversion is finished.

This function currently spins waiting for the conversion to
complete (2 frames max without sync).

If called for a synchronised ADC conversion, it may sleep
with the ADC mutex held.

.. _`ucb1x00_adc_disable`:

ucb1x00_adc_disable
===================

.. c:function:: void ucb1x00_adc_disable(struct ucb1x00 *ucb)

    disable the ADC converter

    :param struct ucb1x00 \*ucb:
        UCB1x00 structure describing chip

.. _`ucb1x00_adc_disable.description`:

Description
-----------

Disable the ADC converter and release the ADC mutex.

.. This file was automatic generated / don't edit.

