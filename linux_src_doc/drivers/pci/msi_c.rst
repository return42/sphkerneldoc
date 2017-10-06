.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/pci/msi.c

.. _`pci_msi_mask_irq`:

pci_msi_mask_irq
================

.. c:function:: void pci_msi_mask_irq(struct irq_data *data)

    Generic irq chip callback to mask PCI/MSI interrupts

    :param struct irq_data \*data:
        pointer to irqdata associated to that interrupt

.. _`pci_msi_unmask_irq`:

pci_msi_unmask_irq
==================

.. c:function:: void pci_msi_unmask_irq(struct irq_data *data)

    Generic irq chip callback to unmask PCI/MSI interrupts

    :param struct irq_data \*data:
        pointer to irqdata associated to that interrupt

.. _`msi_capability_init`:

msi_capability_init
===================

.. c:function:: int msi_capability_init(struct pci_dev *dev, int nvec, const struct irq_affinity *affd)

    configure device's MSI capability structure

    :param struct pci_dev \*dev:
        pointer to the pci_dev data structure of MSI device function

    :param int nvec:
        number of interrupts to allocate

    :param const struct irq_affinity \*affd:
        description of automatic irq affinity assignments (may be \ ``NULL``\ )

.. _`msi_capability_init.description`:

Description
-----------

Setup the MSI capability structure of the device with the requested
number of interrupts.  A return value of zero indicates the successful
setup of an entry with the new MSI irq.  A negative return value indicates
an error, and a positive return value indicates the number of interrupts
which could have been allocated.

.. _`msix_capability_init`:

msix_capability_init
====================

.. c:function:: int msix_capability_init(struct pci_dev *dev, struct msix_entry *entries, int nvec, const struct irq_affinity *affd)

    configure device's MSI-X capability

    :param struct pci_dev \*dev:
        pointer to the pci_dev data structure of MSI-X device function

    :param struct msix_entry \*entries:
        pointer to an array of struct msix_entry entries

    :param int nvec:
        number of \ ``entries``\ 

    :param const struct irq_affinity \*affd:
        Optional pointer to enable automatic affinity assignement

.. _`msix_capability_init.description`:

Description
-----------

Setup the MSI-X capability structure of device function with a
single MSI-X irq. A return of zero indicates the successful setup of
requested MSI-X entries with allocated irqs or non-zero for otherwise.

.. _`pci_msi_supported`:

pci_msi_supported
=================

.. c:function:: int pci_msi_supported(struct pci_dev *dev, int nvec)

    check whether MSI may be enabled on a device

    :param struct pci_dev \*dev:
        pointer to the pci_dev data structure of MSI device function

    :param int nvec:
        how many MSIs have been requested ?

.. _`pci_msi_supported.description`:

Description
-----------

Look at global flags, the device itself, and its parent buses
to determine if MSI/-X are supported for the device. If MSI/-X is
supported return 1, else return 0.

.. _`pci_msi_vec_count`:

pci_msi_vec_count
=================

.. c:function:: int pci_msi_vec_count(struct pci_dev *dev)

    Return the number of MSI vectors a device can send

    :param struct pci_dev \*dev:
        device to report about

.. _`pci_msi_vec_count.description`:

Description
-----------

This function returns the number of MSI vectors a device requested via
Multiple Message Capable register. It returns a negative errno if the
device is not capable sending MSI interrupts. Otherwise, the call succeeds
and returns a power of two, up to a maximum of 2^5 (32), according to the
MSI specification.

.. _`pci_msix_vec_count`:

pci_msix_vec_count
==================

.. c:function:: int pci_msix_vec_count(struct pci_dev *dev)

    return the number of device's MSI-X table entries

    :param struct pci_dev \*dev:
        pointer to the pci_dev data structure of MSI-X device function
        This function returns the number of device's MSI-X table entries and
        therefore the number of MSI-X vectors device is capable of sending.
        It returns a negative errno if the device is not capable of sending MSI-X
        interrupts.

.. _`pci_msi_enabled`:

pci_msi_enabled
===============

.. c:function:: int pci_msi_enabled( void)

    is MSI enabled?

    :param  void:
        no arguments

.. _`pci_msi_enabled.description`:

Description
-----------

Returns true if MSI has not been disabled by the command-line option
pci=nomsi.

.. _`pci_enable_msix_range`:

pci_enable_msix_range
=====================

.. c:function:: int pci_enable_msix_range(struct pci_dev *dev, struct msix_entry *entries, int minvec, int maxvec)

    configure device's MSI-X capability structure

    :param struct pci_dev \*dev:
        pointer to the pci_dev data structure of MSI-X device function

    :param struct msix_entry \*entries:
        pointer to an array of MSI-X entries

    :param int minvec:
        minimum number of MSI-X irqs requested

    :param int maxvec:
        maximum number of MSI-X irqs requested

.. _`pci_enable_msix_range.description`:

Description
-----------

Setup the MSI-X capability structure of device function with a maximum
possible number of interrupts in the range between \ ``minvec``\  and \ ``maxvec``\ 
upon its software driver call to request for MSI-X mode enabled on its
hardware device function. It returns a negative errno if an error occurs.
If it succeeds, it returns the actual number of interrupts allocated and
indicates the successful configuration of MSI-X capability structure
with new allocated MSI-X interrupts.

.. _`pci_alloc_irq_vectors_affinity`:

pci_alloc_irq_vectors_affinity
==============================

.. c:function:: int pci_alloc_irq_vectors_affinity(struct pci_dev *dev, unsigned int min_vecs, unsigned int max_vecs, unsigned int flags, const struct irq_affinity *affd)

    allocate multiple IRQs for a device

    :param struct pci_dev \*dev:
        PCI device to operate on

    :param unsigned int min_vecs:
        minimum number of vectors required (must be >= 1)

    :param unsigned int max_vecs:
        maximum (desired) number of vectors

    :param unsigned int flags:
        flags or quirks for the allocation

    :param const struct irq_affinity \*affd:
        optional description of the affinity requirements

.. _`pci_alloc_irq_vectors_affinity.description`:

Description
-----------

Allocate up to \ ``max_vecs``\  interrupt vectors for \ ``dev``\ , using MSI-X or MSI
vectors if available, and fall back to a single legacy vector
if neither is available.  Return the number of vectors allocated,
(which might be smaller than \ ``max_vecs``\ ) if successful, or a negative
error code on error. If less than \ ``min_vecs``\  interrupt vectors are
available for \ ``dev``\  the function will fail with -ENOSPC.

To get the Linux IRQ number used for a vector that can be passed to
\ :c:func:`request_irq`\  use the \ :c:func:`pci_irq_vector`\  helper.

.. _`pci_free_irq_vectors`:

pci_free_irq_vectors
====================

.. c:function:: void pci_free_irq_vectors(struct pci_dev *dev)

    free previously allocated IRQs for a device

    :param struct pci_dev \*dev:
        PCI device to operate on

.. _`pci_free_irq_vectors.description`:

Description
-----------

Undoes the allocations and enabling in \ :c:func:`pci_alloc_irq_vectors`\ .

.. _`pci_irq_vector`:

pci_irq_vector
==============

.. c:function:: int pci_irq_vector(struct pci_dev *dev, unsigned int nr)

    return Linux IRQ number of a device vector

    :param struct pci_dev \*dev:
        PCI device to operate on

    :param unsigned int nr:
        device-relative interrupt vector index (0-based).

.. _`pci_irq_get_affinity`:

pci_irq_get_affinity
====================

.. c:function:: const struct cpumask *pci_irq_get_affinity(struct pci_dev *dev, int nr)

    return the affinity of a particular msi vector

    :param struct pci_dev \*dev:
        PCI device to operate on

    :param int nr:
        device-relative interrupt vector index (0-based).

.. _`pci_irq_get_node`:

pci_irq_get_node
================

.. c:function:: int pci_irq_get_node(struct pci_dev *pdev, int vec)

    return the numa node of a particular msi vector

    :param struct pci_dev \*pdev:
        PCI device to operate on

    :param int vec:
        device-relative interrupt vector index (0-based).

.. _`pci_msi_domain_write_msg`:

pci_msi_domain_write_msg
========================

.. c:function:: void pci_msi_domain_write_msg(struct irq_data *irq_data, struct msi_msg *msg)

    Helper to write MSI message to PCI config space

    :param struct irq_data \*irq_data:
        Pointer to interrupt data of the MSI interrupt

    :param struct msi_msg \*msg:
        Pointer to the message

.. _`pci_msi_domain_calc_hwirq`:

pci_msi_domain_calc_hwirq
=========================

.. c:function:: irq_hw_number_t pci_msi_domain_calc_hwirq(struct pci_dev *dev, struct msi_desc *desc)

    Generate a unique ID for an MSI source

    :param struct pci_dev \*dev:
        Pointer to the PCI device

    :param struct msi_desc \*desc:
        Pointer to the msi descriptor

.. _`pci_msi_domain_calc_hwirq.description`:

Description
-----------

The ID number is only used within the irqdomain.

.. _`pci_msi_domain_check_cap`:

pci_msi_domain_check_cap
========================

.. c:function:: int pci_msi_domain_check_cap(struct irq_domain *domain, struct msi_domain_info *info, struct device *dev)

    Verify that \ ``domain``\  supports the capabilities for \ ``dev``\ 

    :param struct irq_domain \*domain:
        The interrupt domain to check

    :param struct msi_domain_info \*info:
        The domain info for verification

    :param struct device \*dev:
        The device to check

.. _`pci_msi_domain_check_cap.return`:

Return
------

 0 if the functionality is supported
 1 if Multi MSI is requested, but the domain does not support it
 -ENOTSUPP otherwise

.. _`pci_msi_create_irq_domain`:

pci_msi_create_irq_domain
=========================

.. c:function:: struct irq_domain *pci_msi_create_irq_domain(struct fwnode_handle *fwnode, struct msi_domain_info *info, struct irq_domain *parent)

    Create a MSI interrupt domain

    :param struct fwnode_handle \*fwnode:
        Optional fwnode of the interrupt controller

    :param struct msi_domain_info \*info:
        MSI domain info

    :param struct irq_domain \*parent:
        Parent irq domain

.. _`pci_msi_create_irq_domain.description`:

Description
-----------

Updates the domain and chip ops and creates a MSI interrupt domain.

.. _`pci_msi_create_irq_domain.return`:

Return
------

A domain pointer or NULL in case of failure.

.. _`pci_msi_domain_get_msi_rid`:

pci_msi_domain_get_msi_rid
==========================

.. c:function:: u32 pci_msi_domain_get_msi_rid(struct irq_domain *domain, struct pci_dev *pdev)

    Get the MSI requester id (RID)

    :param struct irq_domain \*domain:
        The interrupt domain

    :param struct pci_dev \*pdev:
        The PCI device.

.. _`pci_msi_domain_get_msi_rid.description`:

Description
-----------

The RID for a device is formed from the alias, with a firmware
supplied mapping applied

.. _`pci_msi_domain_get_msi_rid.return`:

Return
------

The RID.

.. _`pci_msi_get_device_domain`:

pci_msi_get_device_domain
=========================

.. c:function:: struct irq_domain *pci_msi_get_device_domain(struct pci_dev *pdev)

    Get the MSI domain for a given PCI device

    :param struct pci_dev \*pdev:
        The PCI device

.. _`pci_msi_get_device_domain.description`:

Description
-----------

Use the firmware data to find a device-specific MSI domain
(i.e. not one that is set as a default).

.. _`pci_msi_get_device_domain.return`:

Return
------

The corresponding MSI domain or NULL if none has been found.

.. This file was automatic generated / don't edit.

