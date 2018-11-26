.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/handle.c

.. _`handle_bad_irq`:

handle_bad_irq
==============

.. c:function:: void handle_bad_irq(struct irq_desc *desc)

    handle spurious and unhandled irqs

    :param desc:
        description of the interrupt
    :type desc: struct irq_desc \*

.. _`handle_bad_irq.description`:

Description
-----------

Handles spurious and unhandled IRQ's. It also prints a debugmessage.

.. This file was automatic generated / don't edit.

