.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/endpoint/pci-epc-core.c

.. _`pci_epc_put`:

pci_epc_put
===========

.. c:function:: void pci_epc_put(struct pci_epc *epc)

    release the PCI endpoint controller

    :param struct pci_epc \*epc:
        epc returned by \ :c:func:`pci_epc_get`\ 

.. _`pci_epc_put.description`:

Description
-----------

release the refcount the caller obtained by invoking \ :c:func:`pci_epc_get`\ 

.. _`pci_epc_get`:

pci_epc_get
===========

.. c:function:: struct pci_epc *pci_epc_get(const char *epc_name)

    get the PCI endpoint controller

    :param const char \*epc_name:
        device name of the endpoint controller

.. _`pci_epc_get.description`:

Description
-----------

Invoke to get struct pci_epc \* corresponding to the device name of the
endpoint controller

.. _`pci_epc_stop`:

pci_epc_stop
============

.. c:function:: void pci_epc_stop(struct pci_epc *epc)

    stop the PCI link

    :param struct pci_epc \*epc:
        the link of the EPC device that has to be stopped

.. _`pci_epc_stop.description`:

Description
-----------

Invoke to stop the PCI link

.. _`pci_epc_start`:

pci_epc_start
=============

.. c:function:: int pci_epc_start(struct pci_epc *epc)

    start the PCI link

    :param struct pci_epc \*epc:
        the link of \*this\* EPC device has to be started

.. _`pci_epc_start.description`:

Description
-----------

Invoke to start the PCI link

.. _`pci_epc_raise_irq`:

pci_epc_raise_irq
=================

.. c:function:: int pci_epc_raise_irq(struct pci_epc *epc, enum pci_epc_irq_type type, u8 interrupt_num)

    interrupt the host system

    :param struct pci_epc \*epc:
        the EPC device which has to interrupt the host

    :param enum pci_epc_irq_type type:
        specify the type of interrupt; legacy or MSI

    :param u8 interrupt_num:
        the MSI interrupt number

.. _`pci_epc_raise_irq.description`:

Description
-----------

Invoke to raise an MSI or legacy interrupt

.. _`pci_epc_get_msi`:

pci_epc_get_msi
===============

.. c:function:: int pci_epc_get_msi(struct pci_epc *epc)

    get the number of MSI interrupt numbers allocated

    :param struct pci_epc \*epc:
        the EPC device to which MSI interrupts was requested

.. _`pci_epc_get_msi.description`:

Description
-----------

Invoke to get the number of MSI interrupts allocated by the RC

.. _`pci_epc_set_msi`:

pci_epc_set_msi
===============

.. c:function:: int pci_epc_set_msi(struct pci_epc *epc, u8 interrupts)

    set the number of MSI interrupt numbers required

    :param struct pci_epc \*epc:
        the EPC device on which MSI has to be configured

    :param u8 interrupts:
        number of MSI interrupts required by the EPF

.. _`pci_epc_set_msi.description`:

Description
-----------

Invoke to set the required number of MSI interrupts.

.. _`pci_epc_unmap_addr`:

pci_epc_unmap_addr
==================

.. c:function:: void pci_epc_unmap_addr(struct pci_epc *epc, phys_addr_t phys_addr)

    unmap CPU address from PCI address

    :param struct pci_epc \*epc:
        the EPC device on which address is allocated

    :param phys_addr_t phys_addr:
        physical address of the local system

.. _`pci_epc_unmap_addr.description`:

Description
-----------

Invoke to unmap the CPU address from PCI address.

.. _`pci_epc_map_addr`:

pci_epc_map_addr
================

.. c:function:: int pci_epc_map_addr(struct pci_epc *epc, phys_addr_t phys_addr, u64 pci_addr, size_t size)

    map CPU address to PCI address

    :param struct pci_epc \*epc:
        the EPC device on which address is allocated

    :param phys_addr_t phys_addr:
        physical address of the local system

    :param u64 pci_addr:
        PCI address to which the physical address should be mapped

    :param size_t size:
        the size of the allocation

.. _`pci_epc_map_addr.description`:

Description
-----------

Invoke to map CPU address with PCI address.

.. _`pci_epc_clear_bar`:

pci_epc_clear_bar
=================

.. c:function:: void pci_epc_clear_bar(struct pci_epc *epc, int bar)

    reset the BAR

    :param struct pci_epc \*epc:
        the EPC device for which the BAR has to be cleared

    :param int bar:
        the BAR number that has to be reset

.. _`pci_epc_clear_bar.description`:

Description
-----------

Invoke to reset the BAR of the endpoint device.

.. _`pci_epc_set_bar`:

pci_epc_set_bar
===============

.. c:function:: int pci_epc_set_bar(struct pci_epc *epc, enum pci_barno bar, dma_addr_t bar_phys, size_t size, int flags)

    configure BAR in order for host to assign PCI addr space

    :param struct pci_epc \*epc:
        the EPC device on which BAR has to be configured

    :param enum pci_barno bar:
        the BAR number that has to be configured

    :param dma_addr_t bar_phys:
        *undescribed*

    :param size_t size:
        the size of the addr space

    :param int flags:
        specify memory allocation/io allocation/32bit address/64 bit address

.. _`pci_epc_set_bar.description`:

Description
-----------

Invoke to configure the BAR of the endpoint device.

.. _`pci_epc_write_header`:

pci_epc_write_header
====================

.. c:function:: int pci_epc_write_header(struct pci_epc *epc, struct pci_epf_header *header)

    write standard configuration header

    :param struct pci_epc \*epc:
        the EPC device to which the configuration header should be written

    :param struct pci_epf_header \*header:
        standard configuration header fields

.. _`pci_epc_write_header.description`:

Description
-----------

Invoke to write the configuration header to the endpoint controller. Every
endpoint controller will have a dedicated location to which the standard
configuration header would be written. The callback function should write
the header fields to this dedicated location.

.. _`pci_epc_add_epf`:

pci_epc_add_epf
===============

.. c:function:: int pci_epc_add_epf(struct pci_epc *epc, struct pci_epf *epf)

    bind PCI endpoint function to an endpoint controller

    :param struct pci_epc \*epc:
        the EPC device to which the endpoint function should be added

    :param struct pci_epf \*epf:
        the endpoint function to be added

.. _`pci_epc_add_epf.description`:

Description
-----------

A PCI endpoint device can have one or more functions. In the case of PCIe,
the specification allows up to 8 PCIe endpoint functions. Invoke
\ :c:func:`pci_epc_add_epf`\  to add a PCI endpoint function to an endpoint controller.

.. _`pci_epc_remove_epf`:

pci_epc_remove_epf
==================

.. c:function:: void pci_epc_remove_epf(struct pci_epc *epc, struct pci_epf *epf)

    remove PCI endpoint function from endpoint controller

    :param struct pci_epc \*epc:
        the EPC device from which the endpoint function should be removed

    :param struct pci_epf \*epf:
        the endpoint function to be removed

.. _`pci_epc_remove_epf.description`:

Description
-----------

Invoke to remove PCI endpoint function from the endpoint controller.

.. _`pci_epc_linkup`:

pci_epc_linkup
==============

.. c:function:: void pci_epc_linkup(struct pci_epc *epc)

    Notify the EPF device that EPC device has established a connection with the Root Complex.

    :param struct pci_epc \*epc:
        the EPC device which has established link with the host

.. _`pci_epc_linkup.description`:

Description
-----------

Invoke to Notify the EPF device that the EPC device has established a
connection with the Root Complex.

.. _`pci_epc_destroy`:

pci_epc_destroy
===============

.. c:function:: void pci_epc_destroy(struct pci_epc *epc)

    destroy the EPC device

    :param struct pci_epc \*epc:
        the EPC device that has to be destroyed

.. _`pci_epc_destroy.description`:

Description
-----------

Invoke to destroy the PCI EPC device

.. _`devm_pci_epc_destroy`:

devm_pci_epc_destroy
====================

.. c:function:: void devm_pci_epc_destroy(struct device *dev, struct pci_epc *epc)

    destroy the EPC device

    :param struct device \*dev:
        device that wants to destroy the EPC

    :param struct pci_epc \*epc:
        the EPC device that has to be destroyed

.. _`devm_pci_epc_destroy.description`:

Description
-----------

Invoke to destroy the devres associated with this
pci_epc and destroy the EPC device.

.. _`__pci_epc_create`:

__pci_epc_create
================

.. c:function:: struct pci_epc *__pci_epc_create(struct device *dev, const struct pci_epc_ops *ops, struct module *owner)

    create a new endpoint controller (EPC) device

    :param struct device \*dev:
        device that is creating the new EPC

    :param const struct pci_epc_ops \*ops:
        function pointers for performing EPC operations

    :param struct module \*owner:
        the owner of the module that creates the EPC device

.. _`__pci_epc_create.description`:

Description
-----------

Invoke to create a new EPC device and add it to pci_epc class.

.. _`__devm_pci_epc_create`:

__devm_pci_epc_create
=====================

.. c:function:: struct pci_epc *__devm_pci_epc_create(struct device *dev, const struct pci_epc_ops *ops, struct module *owner)

    create a new endpoint controller (EPC) device

    :param struct device \*dev:
        device that is creating the new EPC

    :param const struct pci_epc_ops \*ops:
        function pointers for performing EPC operations

    :param struct module \*owner:
        the owner of the module that creates the EPC device

.. _`__devm_pci_epc_create.description`:

Description
-----------

Invoke to create a new EPC device and add it to pci_epc class.
While at that, it also associates the device with the pci_epc using devres.
On driver detach, release function is invoked on the devres data,
then, devres data is freed.

.. This file was automatic generated / don't edit.

