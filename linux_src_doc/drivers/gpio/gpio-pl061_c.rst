.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpio/gpio-pl061.c

.. _`pl061_irq_ack`:

pl061_irq_ack
=============

.. c:function:: void pl061_irq_ack(struct irq_data *d)

    ACK an edge IRQ

    :param d:
        IRQ data for this IRQ
    :type d: struct irq_data \*

.. _`pl061_irq_ack.description`:

Description
-----------

This gets called from the edge IRQ handler to ACK the edge IRQ
in the GPIOIC (interrupt-clear) register. For level IRQs this is

.. _`pl061_irq_ack.not-needed`:

not needed
----------

these go away when the level signal goes away.

.. This file was automatic generated / don't edit.

