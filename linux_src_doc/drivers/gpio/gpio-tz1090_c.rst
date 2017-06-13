.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-tz1090.c

.. _`tz1090_gpio_bank`:

struct tz1090_gpio_bank
=======================

.. c:type:: struct tz1090_gpio_bank

    GPIO bank private data

.. _`tz1090_gpio_bank.definition`:

Definition
----------

.. code-block:: c

    struct tz1090_gpio_bank {
        struct gpio_chip chip;
        struct irq_domain *domain;
        void __iomem *reg;
        int irq;
        char label;
    }

.. _`tz1090_gpio_bank.members`:

Members
-------

chip
    Generic GPIO chip for GPIO bank

domain
    IRQ domain for GPIO bank (may be NULL)

reg
    Base of registers, offset for this GPIO bank

irq
    IRQ number for GPIO bank

label
    Debug GPIO bank label, used for storage of chip->label

.. _`tz1090_gpio_bank.description`:

Description
-----------

This is the main private data for a GPIO bank. It encapsulates a gpio_chip,
and the callbacks for the gpio_chip can access the private data with the
\ :c:func:`to_bank`\  macro below.

.. _`tz1090_gpio`:

struct tz1090_gpio
==================

.. c:type:: struct tz1090_gpio

    Overall GPIO device private data

.. _`tz1090_gpio.definition`:

Definition
----------

.. code-block:: c

    struct tz1090_gpio {
        struct device *dev;
        void __iomem *reg;
    }

.. _`tz1090_gpio.members`:

Members
-------

dev
    Device (from platform device)

reg
    Base of GPIO registers

.. _`tz1090_gpio.description`:

Description
-----------

Represents the overall GPIO device. This structure is actually only
temporary, and used during init.

.. _`tz1090_gpio_bank_info`:

struct tz1090_gpio_bank_info
============================

.. c:type:: struct tz1090_gpio_bank_info

    Temporary registration info for GPIO bank

.. _`tz1090_gpio_bank_info.definition`:

Definition
----------

.. code-block:: c

    struct tz1090_gpio_bank_info {
        struct tz1090_gpio *priv;
        struct device_node *node;
        unsigned int index;
    }

.. _`tz1090_gpio_bank_info.members`:

Members
-------

priv
    Overall GPIO device private data

node
    Device tree node specific to this GPIO bank

index
    Index of bank in range 0-2

.. This file was automatic generated / don't edit.

