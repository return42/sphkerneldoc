.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/endpoint/pci-epf-core.c

.. _`define_mutex`:

DEFINE_MUTEX
============

.. c:function::  DEFINE_MUTEX( pci_epf_mutex)

    :param pci_epf_mutex:
        *undescribed*
    :type pci_epf_mutex: 

.. _`define_mutex.description`:

Description
-----------

Copyright (C) 2017 Texas Instruments

.. _`define_mutex.author`:

Author
------

Kishon Vijay Abraham I <kishon@ti.com>

.. _`pci_epf_linkup`:

pci_epf_linkup
==============

.. c:function:: void pci_epf_linkup(struct pci_epf *epf)

    Notify the function driver that EPC device has established a connection with the Root Complex.

    :param epf:
        the EPF device bound to the EPC device which has established
        the connection with the host
    :type epf: struct pci_epf \*

.. _`pci_epf_linkup.description`:

Description
-----------

Invoke to notify the function driver that EPC device has established
a connection with the Root Complex.

.. _`pci_epf_unbind`:

pci_epf_unbind
==============

.. c:function:: void pci_epf_unbind(struct pci_epf *epf)

    Notify the function driver that the binding between the EPF device and EPC device has been lost

    :param epf:
        the EPF device which has lost the binding with the EPC device
    :type epf: struct pci_epf \*

.. _`pci_epf_unbind.description`:

Description
-----------

Invoke to notify the function driver that the binding between the EPF device
and EPC device has been lost.

.. _`pci_epf_bind`:

pci_epf_bind
============

.. c:function:: int pci_epf_bind(struct pci_epf *epf)

    Notify the function driver that the EPF device has been bound to a EPC device

    :param epf:
        the EPF device which has been bound to the EPC device
    :type epf: struct pci_epf \*

.. _`pci_epf_bind.description`:

Description
-----------

Invoke to notify the function driver that it has been bound to a EPC device

.. _`pci_epf_free_space`:

pci_epf_free_space
==================

.. c:function:: void pci_epf_free_space(struct pci_epf *epf, void *addr, enum pci_barno bar)

    free the allocated PCI EPF register space

    :param epf:
        *undescribed*
    :type epf: struct pci_epf \*

    :param addr:
        the virtual address of the PCI EPF register space
    :type addr: void \*

    :param bar:
        the BAR number corresponding to the register space
    :type bar: enum pci_barno

.. _`pci_epf_free_space.description`:

Description
-----------

Invoke to free the allocated PCI EPF register space.

.. _`pci_epf_alloc_space`:

pci_epf_alloc_space
===================

.. c:function:: void *pci_epf_alloc_space(struct pci_epf *epf, size_t size, enum pci_barno bar)

    allocate memory for the PCI EPF register space

    :param epf:
        *undescribed*
    :type epf: struct pci_epf \*

    :param size:
        the size of the memory that has to be allocated
    :type size: size_t

    :param bar:
        the BAR number corresponding to the allocated register space
    :type bar: enum pci_barno

.. _`pci_epf_alloc_space.description`:

Description
-----------

Invoke to allocate memory for the PCI EPF register space.

.. _`pci_epf_unregister_driver`:

pci_epf_unregister_driver
=========================

.. c:function:: void pci_epf_unregister_driver(struct pci_epf_driver *driver)

    unregister the PCI EPF driver

    :param driver:
        the PCI EPF driver that has to be unregistered
    :type driver: struct pci_epf_driver \*

.. _`pci_epf_unregister_driver.description`:

Description
-----------

Invoke to unregister the PCI EPF driver.

.. _`__pci_epf_register_driver`:

\__pci_epf_register_driver
==========================

.. c:function:: int __pci_epf_register_driver(struct pci_epf_driver *driver, struct module *owner)

    register a new PCI EPF driver

    :param driver:
        structure representing PCI EPF driver
    :type driver: struct pci_epf_driver \*

    :param owner:
        the owner of the module that registers the PCI EPF driver
    :type owner: struct module \*

.. _`__pci_epf_register_driver.description`:

Description
-----------

Invoke to register a new PCI EPF driver.

.. _`pci_epf_destroy`:

pci_epf_destroy
===============

.. c:function:: void pci_epf_destroy(struct pci_epf *epf)

    destroy the created PCI EPF device

    :param epf:
        the PCI EPF device that has to be destroyed.
    :type epf: struct pci_epf \*

.. _`pci_epf_destroy.description`:

Description
-----------

Invoke to destroy the PCI EPF device created by invoking \ :c:func:`pci_epf_create`\ .

.. _`pci_epf_create`:

pci_epf_create
==============

.. c:function:: struct pci_epf *pci_epf_create(const char *name)

    create a new PCI EPF device

    :param name:
        the name of the PCI EPF device. This name will be used to bind the
        the EPF device to a EPF driver
    :type name: const char \*

.. _`pci_epf_create.description`:

Description
-----------

Invoke to create a new PCI EPF device by providing the name of the function
device.

.. This file was automatic generated / don't edit.

