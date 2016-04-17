.. -*- coding: utf-8; mode: rst -*-

===========
timb_gpio.h
===========


.. _`timbgpio_platform_data`:

struct timbgpio_platform_data
=============================

.. c:type:: timbgpio_platform_data

    Platform data of the Timberdale GPIO driver @gpio_base The number of the first GPIO pin, set to -1 for dynamic number allocation. @nr_pins Number of pins that is supported by the hardware (1-32) @irq_base If IRQ is supported by the hardware, this is the base


.. _`timbgpio_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct timbgpio_platform_data {
  };


.. _`timbgpio_platform_data.members`:

Members
-------




.. _`timbgpio_platform_data.number-of-irq`:

number of IRQ
-------------

s. One IRQ per pin will be used. Set to

                        -1 if IRQ:s is not supported.

