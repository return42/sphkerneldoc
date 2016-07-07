.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-altera.c

.. _`altera_gpio_chip`:

struct altera_gpio_chip
=======================

.. c:type:: struct altera_gpio_chip


.. _`altera_gpio_chip.definition`:

Definition
----------

.. code-block:: c

    struct altera_gpio_chip {
        struct of_mm_gpio_chip mmchip;
        spinlock_t gpio_lock;
        int interrupt_trigger;
        int mapped_irq;
    }

.. _`altera_gpio_chip.members`:

Members
-------

mmchip
    memory mapped chip structure.

gpio_lock
    synchronization lock so that new irq/set/get requests

interrupt_trigger
    specifies the hardware configured IRQ trigger type

mapped_irq
    kernel mapped irq number.

.. _`altera_gpio_irq_set_type`:

altera_gpio_irq_set_type
========================

.. c:function:: int altera_gpio_irq_set_type(struct irq_data *d, unsigned int type)

    just checks if the requested set_type matches the synthesized IRQ type

    :param struct irq_data \*d:
        *undescribed*

    :param unsigned int type:
        *undescribed*

.. This file was automatic generated / don't edit.

