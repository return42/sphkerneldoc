.. -*- coding: utf-8; mode: rst -*-

=======
htirq.c
=======

.. _`__ht_create_irq`:

__ht_create_irq
===============

.. c:function:: int __ht_create_irq (struct pci_dev *dev, int idx, ht_irq_update_t *update)

    create an irq and attach it to a device.

    :param struct pci_dev \*dev:
        The hypertransport device to find the irq capability on.

    :param int idx:
        Which of the possible irqs to attach to.

    :param ht_irq_update_t \*update:
        Function to be called when changing the htirq message


.. _`__ht_create_irq.description`:

Description
-----------

The irq number of the new irq or a negative error value is returned.


.. _`ht_create_irq`:

ht_create_irq
=============

.. c:function:: int ht_create_irq (struct pci_dev *dev, int idx)

    create an irq and attach it to a device.

    :param struct pci_dev \*dev:
        The hypertransport device to find the irq capability on.

    :param int idx:
        Which of the possible irqs to attach to.


.. _`ht_create_irq.description`:

Description
-----------

ht_create_irq needs to be called for all hypertransport devices
that generate irqs.

The irq number of the new irq or a negative error value is returned.


.. _`ht_destroy_irq`:

ht_destroy_irq
==============

.. c:function:: void ht_destroy_irq (unsigned int irq)

    destroy an irq created with ht_create_irq

    :param unsigned int irq:
        irq to be destroyed


.. _`ht_destroy_irq.description`:

Description
-----------

This reverses ht_create_irq removing the specified irq from
existence.  The irq should be free before this happens.

