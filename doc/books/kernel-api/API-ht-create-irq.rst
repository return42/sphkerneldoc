
.. _API-ht-create-irq:

=============
ht_create_irq
=============

*man ht_create_irq(9)*

*4.6.0-rc1*

create an irq and attach it to a device.


Synopsis
========

.. c:function:: int ht_create_irq( struct pci_dev * dev, int idx )

Arguments
=========

``dev``
    The hypertransport device to find the irq capability on.

``idx``
    Which of the possible irqs to attach to.


Description
===========

ht_create_irq needs to be called for all hypertransport devices that generate irqs.

The irq number of the new irq or a negative error value is returned.
