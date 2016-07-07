.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-tpic2810.c

.. _`tpic2810`:

struct tpic2810
===============

.. c:type:: struct tpic2810

    GPIO driver data

.. _`tpic2810.definition`:

Definition
----------

.. code-block:: c

    struct tpic2810 {
        struct gpio_chip chip;
        struct i2c_client *client;
        u8 buffer;
        struct mutex lock;
    }

.. _`tpic2810.members`:

Members
-------

chip
    GPIO controller chip

client
    I2C device pointer

buffer
    Buffer for device register

lock
    Protects write sequences

.. This file was automatic generated / don't edit.

