.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/vpd.c

.. _`pci_read_vpd`:

pci_read_vpd
============

.. c:function:: ssize_t pci_read_vpd(struct pci_dev *dev, loff_t pos, size_t count, void *buf)

    Read one entry from Vital Product Data

    :param dev:
        pci device struct
    :type dev: struct pci_dev \*

    :param pos:
        offset in vpd space
    :type pos: loff_t

    :param count:
        number of bytes to read
    :type count: size_t

    :param buf:
        pointer to where to store result
    :type buf: void \*

.. _`pci_write_vpd`:

pci_write_vpd
=============

.. c:function:: ssize_t pci_write_vpd(struct pci_dev *dev, loff_t pos, size_t count, const void *buf)

    Write entry to Vital Product Data

    :param dev:
        pci device struct
    :type dev: struct pci_dev \*

    :param pos:
        offset in vpd space
    :type pos: loff_t

    :param count:
        number of bytes to write
    :type count: size_t

    :param buf:
        buffer containing write data
    :type buf: const void \*

.. _`pci_set_vpd_size`:

pci_set_vpd_size
================

.. c:function:: int pci_set_vpd_size(struct pci_dev *dev, size_t len)

    Set size of Vital Product Data space

    :param dev:
        pci device struct
    :type dev: struct pci_dev \*

    :param len:
        size of vpd space
    :type len: size_t

.. _`pci_vpd_size`:

pci_vpd_size
============

.. c:function:: size_t pci_vpd_size(struct pci_dev *dev, size_t old_size)

    determine actual size of Vital Product Data

    :param dev:
        pci device struct
    :type dev: struct pci_dev \*

    :param old_size:
        current assumed size, also maximum allowed size
    :type old_size: size_t

.. This file was automatic generated / don't edit.

