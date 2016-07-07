.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/extcon/extcon-max14577.c

.. _`max14577_muic_irq`:

struct max14577_muic_irq
========================

.. c:type:: struct max14577_muic_irq


.. _`max14577_muic_irq.definition`:

Definition
----------

.. code-block:: c

    struct max14577_muic_irq {
        unsigned int irq;
        const char *name;
        unsigned int virq;
    }

.. _`max14577_muic_irq.members`:

Members
-------

irq
    the index of irq list of MUIC device.

name
    the name of irq.

virq
    the virtual irq to use irq domain

.. This file was automatic generated / don't edit.

