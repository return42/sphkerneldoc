.. -*- coding: utf-8; mode: rst -*-

===========
htc-egpio.h
===========


.. _`htc_egpio_chip`:

struct htc_egpio_chip
=====================

.. c:type:: htc_egpio_chip

    descriptor to create gpio_chip for register range


.. _`htc_egpio_chip.definition`:

Definition
----------

.. code-block:: c

  struct htc_egpio_chip {
    int reg_start;
    int gpio_base;
    int num_gpios;
    unsigned long direction;
  };


.. _`htc_egpio_chip.members`:

Members
-------

:``reg_start``:
    index of first register

:``gpio_base``:
    gpio number of first pin in this register range

:``num_gpios``:
    number of gpios in this register range, max BITS_PER_LONG
    (number of registers = DIV_ROUND_UP(num_gpios, reg_width))

:``direction``:
    bitfield, '0' = input, '1' = output,




.. _`htc_egpio_platform_data`:

struct htc_egpio_platform_data
==============================

.. c:type:: htc_egpio_platform_data

    description provided by the arch


.. _`htc_egpio_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct htc_egpio_platform_data {
    int bus_width;
    int reg_width;
    int irq_base;
    int num_irqs;
    int invert_acks;
    int ack_register;
    struct htc_egpio_chip * chip;
    int num_chips;
  };


.. _`htc_egpio_platform_data.members`:

Members
-------

:``bus_width``:
    alignment of the registers, either 16 or 32 bit

:``reg_width``:
    number of bits per register, either 8 or 16 bit

:``irq_base``:
    beginning of available IRQs (eg, IRQ_BOARD_START)

:``num_irqs``:
    number of irqs

:``invert_acks``:
    set if chip requires writing '0' to ack an irq, instead of '1'

:``ack_register``:
    location of the irq/ack register

:``chip``:
    pointer to array of htc_egpio_chip descriptors

:``num_chips``:
    number of egpio chip descriptors


