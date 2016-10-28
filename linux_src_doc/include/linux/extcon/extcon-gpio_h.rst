.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/extcon/extcon-gpio.h

.. _`gpio_extcon_pdata`:

struct gpio_extcon_pdata
========================

.. c:type:: struct gpio_extcon_pdata

    A simple GPIO-controlled extcon device.

.. _`gpio_extcon_pdata.definition`:

Definition
----------

.. code-block:: c

    struct gpio_extcon_pdata {
        unsigned int extcon_id;
        unsigned gpio;
        bool gpio_active_low;
        unsigned long debounce;
        unsigned long irq_flags;
        bool check_on_resume;
    }

.. _`gpio_extcon_pdata.members`:

Members
-------

extcon_id
    The unique id of specific external connector.

gpio
    Corresponding GPIO.

gpio_active_low
    Boolean describing whether gpio active state is 1 or 0
    If true, low state of gpio means active.
    If false, high state of gpio means active.

debounce
    Debounce time for GPIO IRQ in ms.

irq_flags
    IRQ Flags (e.g., IRQF_TRIGGER_LOW).

check_on_resume
    Boolean describing whether to check the state of gpio
    while resuming from sleep.

.. This file was automatic generated / don't edit.

