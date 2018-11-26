.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/leds/leds-as3645a.c

.. _`as3645a_set_current`:

as3645a_set_current
===================

.. c:function:: int as3645a_set_current(struct as3645a *flash)

    Set flash configuration registers

    :param flash:
        The flash
    :type flash: struct as3645a \*

.. _`as3645a_set_current.description`:

Description
-----------

Configure the hardware with flash, assist and indicator currents, as well as
flash timeout.

Return 0 on success, or a negative error code if an I2C communication error
occurred.

.. _`as3645a_set_control`:

as3645a_set_control
===================

.. c:function:: int as3645a_set_control(struct as3645a *flash, enum as_mode mode, bool on)

    Set flash control register

    :param flash:
        The flash
    :type flash: struct as3645a \*

    :param mode:
        Desired output mode
    :type mode: enum as_mode

    :param on:
        Desired output state
    :type on: bool

.. _`as3645a_set_control.description`:

Description
-----------

Configure the hardware with output mode and state.

Return 0 on success, or a negative error code if an I2C communication error
occurred.

.. This file was automatic generated / don't edit.

