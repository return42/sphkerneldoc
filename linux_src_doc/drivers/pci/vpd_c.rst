.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/vpd.c

.. _`pci_read_vpd`:

pci_read_vpd
============

.. c:function:: ssize_t pci_read_vpd(struct pci_dev *dev, loff_t pos, size_t count, void *buf)

    Read one entry from Vital Product Data

    :param struct pci_dev \*dev:
        pci device struct

    :param loff_t pos:
        offset in vpd space

    :param size_t count:
        number of bytes to read

    :param void \*buf:
        pointer to where to store result

.. _`pci_write_vpd`:

pci_write_vpd
=============

.. c:function:: ssize_t pci_write_vpd(struct pci_dev *dev, loff_t pos, size_t count, const void *buf)

    Write entry to Vital Product Data

    :param struct pci_dev \*dev:
        pci device struct

    :param loff_t pos:
        offset in vpd space

    :param size_t count:
        number of bytes to write

    :param const void \*buf:
        buffer containing write data

.. _`pci_set_vpd_size`:

pci_set_vpd_size
================

.. c:function:: int pci_set_vpd_size(struct pci_dev *dev, size_t len)

    Set size of Vital Product Data space

    :param struct pci_dev \*dev:
        pci device struct

    :param size_t len:
        size of vpd space

.. _`pci_vpd_size`:

pci_vpd_size
============

.. c:function:: size_t pci_vpd_size(struct pci_dev *dev, size_t old_size)

    determine actual size of Vital Product Data

    :param struct pci_dev \*dev:
        pci device struct

    :param size_t old_size:
        current assumed size, also maximum allowed size

.. This file was automatic generated / don't edit.

