.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/endpoint/pci-epf-core.c

.. _`pci_epf_linkup`:

pci_epf_linkup
==============

.. c:function:: void pci_epf_linkup(struct pci_epf *epf)

    Notify the function driver that EPC device has established a connection with the Root Complex.

    :param struct pci_epf \*epf:
        the EPF device bound to the EPC device which has established
        the connection with the host

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

    :param struct pci_epf \*epf:
        the EPF device which has lost the binding with the EPC device

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

    :param struct pci_epf \*epf:
        the EPF device which has been bound to the EPC device

.. _`pci_epf_bind.description`:

Description
-----------

Invoke to notify the function driver that it has been bound to a EPC device

.. _`pci_epf_free_space`:

pci_epf_free_space
==================

.. c:function:: void pci_epf_free_space(struct pci_epf *epf, void *addr, enum pci_barno bar)

    free the allocated PCI EPF register space

    :param struct pci_epf \*epf:
        *undescribed*

    :param void \*addr:
        the virtual address of the PCI EPF register space

    :param enum pci_barno bar:
        the BAR number corresponding to the register space

.. _`pci_epf_free_space.description`:

Description
-----------

Invoke to free the allocated PCI EPF register space.

.. _`pci_epf_alloc_space`:

pci_epf_alloc_space
===================

.. c:function:: void *pci_epf_alloc_space(struct pci_epf *epf, size_t size, enum pci_barno bar)

    allocate memory for the PCI EPF register space

    :param struct pci_epf \*epf:
        *undescribed*

    :param size_t size:
        the size of the memory that has to be allocated

    :param enum pci_barno bar:
        the BAR number corresponding to the allocated register space

.. _`pci_epf_alloc_space.description`:

Description
-----------

Invoke to allocate memory for the PCI EPF register space.

.. _`pci_epf_unregister_driver`:

pci_epf_unregister_driver
=========================

.. c:function:: void pci_epf_unregister_driver(struct pci_epf_driver *driver)

    unregister the PCI EPF driver

    :param struct pci_epf_driver \*driver:
        the PCI EPF driver that has to be unregistered

.. _`pci_epf_unregister_driver.description`:

Description
-----------

Invoke to unregister the PCI EPF driver.

.. _`__pci_epf_register_driver`:

\__pci_epf_register_driver
==========================

.. c:function:: int __pci_epf_register_driver(struct pci_epf_driver *driver, struct module *owner)

    register a new PCI EPF driver

    :param struct pci_epf_driver \*driver:
        structure representing PCI EPF driver

    :param struct module \*owner:
        the owner of the module that registers the PCI EPF driver

.. _`__pci_epf_register_driver.description`:

Description
-----------

Invoke to register a new PCI EPF driver.

.. _`pci_epf_destroy`:

pci_epf_destroy
===============

.. c:function:: void pci_epf_destroy(struct pci_epf *epf)

    destroy the created PCI EPF device

    :param struct pci_epf \*epf:
        the PCI EPF device that has to be destroyed.

.. _`pci_epf_destroy.description`:

Description
-----------

Invoke to destroy the PCI EPF device created by invoking \ :c:func:`pci_epf_create`\ .

.. _`pci_epf_create`:

pci_epf_create
==============

.. c:function:: struct pci_epf *pci_epf_create(const char *name)

    create a new PCI EPF device

    :param const char \*name:
        the name of the PCI EPF device. This name will be used to bind the
        the EPF device to a EPF driver

.. _`pci_epf_create.description`:

Description
-----------

Invoke to create a new PCI EPF device by providing the name of the function
device.

.. This file was automatic generated / don't edit.

