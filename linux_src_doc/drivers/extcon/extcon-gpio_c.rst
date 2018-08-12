.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/extcon/extcon-gpio.c

.. _`gpio_extcon_data`:

struct gpio_extcon_data
=======================

.. c:type:: struct gpio_extcon_data

    A simple GPIO-controlled extcon device state container.

.. _`gpio_extcon_data.definition`:

Definition
----------

.. code-block:: c

    struct gpio_extcon_data {
        struct extcon_dev *edev;
        int irq;
        struct delayed_work work;
        unsigned long debounce_jiffies;
        struct gpio_desc *gpiod;
        unsigned int extcon_id;
        unsigned long debounce;
        unsigned long irq_flags;
        bool check_on_resume;
    }

.. _`gpio_extcon_data.members`:

Members
-------

edev
    Extcon device.

irq
    Interrupt line for the external connector.

work
    Work fired by the interrupt.

debounce_jiffies
    Number of jiffies to wait for the GPIO to stabilize, from the debounce
    value.

gpiod
    GPIO descriptor for this external connector.

extcon_id
    The unique id of specific external connector.

debounce
    Debounce time for GPIO IRQ in ms.

irq_flags
    IRQ Flags (e.g., IRQF_TRIGGER_LOW).

check_on_resume
    Boolean describing whether to check the state of gpio
    while resuming from sleep.

.. This file was automatic generated / don't edit.

