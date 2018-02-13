.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/gpio_keys.h

.. _`gpio_keys_button`:

struct gpio_keys_button
=======================

.. c:type:: struct gpio_keys_button

    configuration parameters

.. _`gpio_keys_button.definition`:

Definition
----------

.. code-block:: c

    struct gpio_keys_button {
        unsigned int code;
        int gpio;
        int active_low;
        const char *desc;
        unsigned int type;
        int wakeup;
        int debounce_interval;
        bool can_disable;
        int value;
        unsigned int irq;
    }

.. _`gpio_keys_button.members`:

Members
-------

code
    input event code (KEY\_\*, SW\_\*)

gpio
    \ ``-1``\  if this key does not support gpio

active_low
    \ ``true``\  indicates that button is considered
    depressed when gpio is low

desc
    label that will be attached to button's gpio

type
    input event type (%EV_KEY, \ ``EV_SW``\ , \ ``EV_ABS``\ )

wakeup
    configure the button as a wake-up source

debounce_interval
    debounce ticks interval in msecs

can_disable
    \ ``true``\  indicates that userspace is allowed to
    disable button via sysfs

value
    axis value for \ ``EV_ABS``\ 

irq
    Irq number in case of interrupt keys

.. _`gpio_keys_platform_data`:

struct gpio_keys_platform_data
==============================

.. c:type:: struct gpio_keys_platform_data

    platform data for gpio_keys driver

.. _`gpio_keys_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct gpio_keys_platform_data {
        const struct gpio_keys_button *buttons;
        int nbuttons;
        unsigned int poll_interval;
        unsigned int rep:1;
        int (*enable)(struct device *dev);
        void (*disable)(struct device *dev);
        const char *name;
    }

.. _`gpio_keys_platform_data.members`:

Members
-------

buttons
    pointer to array of \ :c:type:`struct gpio_keys_button <gpio_keys_button>`\  structures
    describing buttons attached to the device

nbuttons
    number of elements in \ ``buttons``\  array

poll_interval
    polling interval in msecs - for polling driver only

rep
    enable input subsystem auto repeat

enable
    platform hook for enabling the device

disable
    platform hook for disabling the device

name
    input device name

.. This file was automatic generated / don't edit.

