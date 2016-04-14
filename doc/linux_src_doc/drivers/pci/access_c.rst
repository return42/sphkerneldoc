.. -*- coding: utf-8; mode: rst -*-

========
access.c
========

.. _`pci_bus_set_ops`:

pci_bus_set_ops
===============

.. c:function:: struct pci_ops *pci_bus_set_ops (struct pci_bus *bus, struct pci_ops *ops)

    Set raw operations of pci bus

    :param struct pci_bus \*bus:
        pci bus struct

    :param struct pci_ops \*ops:
        new raw operations


.. _`pci_bus_set_ops.description`:

Description
-----------

Return previous raw operations


.. _`pci_read_vpd`:

pci_read_vpd
============

.. c:function:: ssize_t pci_read_vpd (struct pci_dev *dev, loff_t pos, size_t count, void *buf)

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

.. c:function:: ssize_t pci_write_vpd (struct pci_dev *dev, loff_t pos, size_t count, const void *buf)

    Write entry to Vital Product Data

    :param struct pci_dev \*dev:
        pci device struct

    :param loff_t pos:
        offset in vpd space

    :param size_t count:
        number of bytes to write

    :param const void \*buf:
        buffer containing write data


.. _`pci_vpd_size`:

pci_vpd_size
============

.. c:function:: size_t pci_vpd_size (struct pci_dev *dev, size_t old_size)

    determine actual size of Vital Product Data

    :param struct pci_dev \*dev:
        pci device struct

    :param size_t old_size:
        current assumed size, also maximum allowed size


.. _`pci_cfg_access_lock`:

pci_cfg_access_lock
===================

.. c:function:: void pci_cfg_access_lock (struct pci_dev *dev)

    Lock PCI config reads/writes

    :param struct pci_dev \*dev:
        pci device struct


.. _`pci_cfg_access_lock.description`:

Description
-----------

When access is locked, any userspace reads or writes to config
space and concurrent lock requests will sleep until access is
allowed via pci_cfg_access_unlocked again.


.. _`pci_cfg_access_trylock`:

pci_cfg_access_trylock
======================

.. c:function:: bool pci_cfg_access_trylock (struct pci_dev *dev)

    try to lock PCI config reads/writes

    :param struct pci_dev \*dev:
        pci device struct


.. _`pci_cfg_access_trylock.description`:

Description
-----------

Same as pci_cfg_access_lock, but will return 0 if access is
already locked, 1 otherwise. This function can be used from
atomic contexts.


.. _`pci_cfg_access_unlock`:

pci_cfg_access_unlock
=====================

.. c:function:: void pci_cfg_access_unlock (struct pci_dev *dev)

    Unlock PCI config reads/writes

    :param struct pci_dev \*dev:
        pci device struct


.. _`pci_cfg_access_unlock.description`:

Description
-----------

This function allows PCI config accesses to resume.

