.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-it87.c

.. _`it87_gpio`:

struct it87_gpio
================

.. c:type:: struct it87_gpio

    it87-specific GPIO chip \ ``chip``\  the underlying gpio_chip structure \ ``lock``\  a lock to avoid races between operations \ ``io_base``\  base address for gpio ports \ ``io_size``\  size of the port rage starting from io_base. \ ``output_base``\  Super I/O register address for Output Enable register \ ``simple_base``\  Super I/O 'Simple I/O' Enable register \ ``simple_size``\  Super IO 'Simple I/O' Enable register size; this is required because IT87xx chips might only provide Simple I/O switches on a subset of lines, whereas the others keep the same status all time.

.. _`it87_gpio.definition`:

Definition
----------

.. code-block:: c

    struct it87_gpio {
        struct gpio_chip chip;
        spinlock_t lock;
        u16 io_base;
        u16 io_size;
        u8 output_base;
        u8 simple_base;
        u8 simple_size;
    }

.. _`it87_gpio.members`:

Members
-------

chip
    *undescribed*

lock
    *undescribed*

io_base
    *undescribed*

io_size
    *undescribed*

output_base
    *undescribed*

simple_base
    *undescribed*

simple_size
    *undescribed*

.. This file was automatic generated / don't edit.

