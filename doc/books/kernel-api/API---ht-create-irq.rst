
.. _API---ht-create-irq:

===============
__ht_create_irq
===============

*man __ht_create_irq(9)*

*4.6.0-rc1*

create an irq and attach it to a device.


Synopsis
========

.. c:function:: int __ht_create_irq( struct pci_dev * dev, int idx, ht_irq_update_t * update )

Arguments
=========

``dev``
    The hypertransport device to find the irq capability on.

``idx``
    Which of the possible irqs to attach to.

``update``
    Function to be called when changing the htirq message


Description
===========

The irq number of the new irq or a negative error value is returned.
