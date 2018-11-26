.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/wireless/ath/ath5k/gpio.c

.. _`gpio-led-functions`:

GPIO/LED functions
==================

Here we control the 6 bidirectional GPIO pins provided by the hw.
We can set a GPIO pin to be an input or an output pin on GPIO control
register and then read or set its status from GPIO data input/output
registers.

We also control the two LED pins provided by the hw, LED_0 is our
"power" LED and LED_1 is our "network activity" LED but many scenarios
are available from hw. Vendors might also provide LEDs connected to the
GPIO pins, we handle them through the LED subsystem on led.c

.. _`ath5k_hw_set_ledstate`:

ath5k_hw_set_ledstate
=====================

.. c:function:: void ath5k_hw_set_ledstate(struct ath5k_hw *ah, unsigned int state)

    Set led state

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param state:
        One of AR5K_LED\_\*
    :type state: unsigned int

.. _`ath5k_hw_set_ledstate.description`:

Description
-----------

Used to set the LED blinking state. This only
works for the LED connected to the LED_0, LED_1 pins,
not the GPIO based.

.. _`ath5k_hw_set_gpio_input`:

ath5k_hw_set_gpio_input
=======================

.. c:function:: int ath5k_hw_set_gpio_input(struct ath5k_hw *ah, u32 gpio)

    Set GPIO inputs

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param gpio:
        GPIO pin to set as input
    :type gpio: u32

.. _`ath5k_hw_set_gpio_output`:

ath5k_hw_set_gpio_output
========================

.. c:function:: int ath5k_hw_set_gpio_output(struct ath5k_hw *ah, u32 gpio)

    Set GPIO outputs

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param gpio:
        The GPIO pin to set as output
    :type gpio: u32

.. _`ath5k_hw_get_gpio`:

ath5k_hw_get_gpio
=================

.. c:function:: u32 ath5k_hw_get_gpio(struct ath5k_hw *ah, u32 gpio)

    Get GPIO state

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param gpio:
        The GPIO pin to read
    :type gpio: u32

.. _`ath5k_hw_set_gpio`:

ath5k_hw_set_gpio
=================

.. c:function:: int ath5k_hw_set_gpio(struct ath5k_hw *ah, u32 gpio, u32 val)

    Set GPIO state

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param gpio:
        The GPIO pin to set
    :type gpio: u32

    :param val:
        Value to set (boolean)
    :type val: u32

.. _`ath5k_hw_set_gpio_intr`:

ath5k_hw_set_gpio_intr
======================

.. c:function:: void ath5k_hw_set_gpio_intr(struct ath5k_hw *ah, unsigned int gpio, u32 interrupt_level)

    Initialize the GPIO interrupt (RFKill switch)

    :param ah:
        The \ :c:type:`struct ath5k_hw <ath5k_hw>`\ 
    :type ah: struct ath5k_hw \*

    :param gpio:
        The GPIO pin to use
    :type gpio: unsigned int

    :param interrupt_level:
        True to generate interrupt on active pin (high)
    :type interrupt_level: u32

.. _`ath5k_hw_set_gpio_intr.description`:

Description
-----------

This function is used to set up the GPIO interrupt for the hw RFKill switch.
That switch is connected to a GPIO pin and it's number is stored on EEPROM.
It can either open or close the circuit to indicate that we should disable
RF/Wireless to save power (we also get that from EEPROM).

.. This file was automatic generated / don't edit.

