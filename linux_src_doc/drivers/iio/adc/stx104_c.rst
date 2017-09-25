.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iio/adc/stx104.c

.. _`stx104_iio`:

struct stx104_iio
=================

.. c:type:: struct stx104_iio

    IIO device private data structure

.. _`stx104_iio.definition`:

Definition
----------

.. code-block:: c

    struct stx104_iio {
        unsigned int chan_out_states[STX104_NUM_OUT_CHAN];
        unsigned int base;
    }

.. _`stx104_iio.members`:

Members
-------

chan_out_states
    channels' output states

base
    base port address of the IIO device

.. _`stx104_gpio`:

struct stx104_gpio
==================

.. c:type:: struct stx104_gpio

    GPIO device private data structure

.. _`stx104_gpio.definition`:

Definition
----------

.. code-block:: c

    struct stx104_gpio {
        struct gpio_chip chip;
        spinlock_t lock;
        unsigned int base;
        unsigned int out_state;
    }

.. _`stx104_gpio.members`:

Members
-------

chip
    instance of the gpio_chip

lock
    synchronization lock to prevent I/O race conditions

base
    base port address of the GPIO device

out_state
    output bits state

.. This file was automatic generated / don't edit.

