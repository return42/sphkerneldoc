.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mfd/ti-lmu.h

.. _`ti_lmu`:

struct ti_lmu
=============

.. c:type:: struct ti_lmu


.. _`ti_lmu.definition`:

Definition
----------

.. code-block:: c

    struct ti_lmu {
        struct device *dev;
        struct regmap *regmap;
        struct gpio_desc *en_gpio;
        struct blocking_notifier_head notifier;
    }

.. _`ti_lmu.members`:

Members
-------

dev
    Parent device pointer

regmap
    Used for i2c communcation on accessing registers

en_gpio
    GPIO for HWEN pin [Optional]

notifier
    Notifier for reporting hwmon event

.. This file was automatic generated / don't edit.

