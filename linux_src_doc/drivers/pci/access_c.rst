.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/access.c

.. _`pci_bus_set_ops`:

pci_bus_set_ops
===============

.. c:function:: struct pci_ops *pci_bus_set_ops(struct pci_bus *bus, struct pci_ops *ops)

    Set raw operations of pci bus

    :param bus:
        pci bus struct
    :type bus: struct pci_bus \*

    :param ops:
        new raw operations
    :type ops: struct pci_ops \*

.. _`pci_bus_set_ops.description`:

Description
-----------

Return previous raw operations

.. _`pci_cfg_access_lock`:

pci_cfg_access_lock
===================

.. c:function:: void pci_cfg_access_lock(struct pci_dev *dev)

    Lock PCI config reads/writes

    :param dev:
        pci device struct
    :type dev: struct pci_dev \*

.. _`pci_cfg_access_lock.description`:

Description
-----------

When access is locked, any userspace reads or writes to config
space and concurrent lock requests will sleep until access is
allowed via \ :c:func:`pci_cfg_access_unlock`\  again.

.. _`pci_cfg_access_trylock`:

pci_cfg_access_trylock
======================

.. c:function:: bool pci_cfg_access_trylock(struct pci_dev *dev)

    try to lock PCI config reads/writes

    :param dev:
        pci device struct
    :type dev: struct pci_dev \*

.. _`pci_cfg_access_trylock.description`:

Description
-----------

Same as pci_cfg_access_lock, but will return 0 if access is
already locked, 1 otherwise. This function can be used from
atomic contexts.

.. _`pci_cfg_access_unlock`:

pci_cfg_access_unlock
=====================

.. c:function:: void pci_cfg_access_unlock(struct pci_dev *dev)

    Unlock PCI config reads/writes

    :param dev:
        pci device struct
    :type dev: struct pci_dev \*

.. _`pci_cfg_access_unlock.description`:

Description
-----------

This function allows PCI config accesses to resume.

.. This file was automatic generated / don't edit.

