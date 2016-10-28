.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/extcon/extcon-max77693.c

.. _`max77693_muic_irq`:

struct max77693_muic_irq
========================

.. c:type:: struct max77693_muic_irq


.. _`max77693_muic_irq.definition`:

Definition
----------

.. code-block:: c

    struct max77693_muic_irq {
        unsigned int irq;
        const char *name;
        unsigned int virq;
    }

.. _`max77693_muic_irq.members`:

Members
-------

irq
    the index of irq list of MUIC device.

name
    the name of irq.

virq
    the virtual irq to use irq domain

.. This file was automatic generated / don't edit.

