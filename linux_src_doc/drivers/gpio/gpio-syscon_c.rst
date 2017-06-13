.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-syscon.c

.. _`syscon_gpio_data`:

struct syscon_gpio_data
=======================

.. c:type:: struct syscon_gpio_data

    Configuration for the device.

.. _`syscon_gpio_data.definition`:

Definition
----------

.. code-block:: c

    struct syscon_gpio_data {
        const char *compatible;
        unsigned int flags;
        unsigned int bit_count;
        unsigned int dat_bit_offset;
        unsigned int dir_bit_offset;
        void (*set)(struct gpio_chip *chip, unsigned offset, int value);
    }

.. _`syscon_gpio_data.members`:

Members
-------

compatible
    *undescribed*

flags
    *undescribed*

bit_count
    *undescribed*

dat_bit_offset
    *undescribed*

dir_bit_offset
    *undescribed*

set
    *undescribed*

.. _`syscon_gpio_data.compatible`:

compatible
----------

SYSCON driver compatible string.

.. _`syscon_gpio_data.flags`:

flags
-----

Set of GPIO_SYSCON_FEAT\_ flags:
GPIO_SYSCON_FEAT_IN:    GPIOs supports input,
GPIO_SYSCON_FEAT_OUT:   GPIOs supports output,
GPIO_SYSCON_FEAT_DIR:   GPIOs supports switch direction.

.. _`syscon_gpio_data.bit_count`:

bit_count
---------

Number of bits used as GPIOs.

.. _`syscon_gpio_data.dat_bit_offset`:

dat_bit_offset
--------------

Offset (in bits) to the first GPIO bit.

.. _`syscon_gpio_data.dir_bit_offset`:

dir_bit_offset
--------------

Optional offset (in bits) to the first bit to switch
GPIO direction (Used with GPIO_SYSCON_FEAT_DIR flag).

.. _`syscon_gpio_data.set`:

set
---

HW specific callback to assigns output value
for signal "offset"

.. This file was automatic generated / don't edit.

