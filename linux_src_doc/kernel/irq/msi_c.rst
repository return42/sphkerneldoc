.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/msi.c

.. _`alloc_msi_entry`:

alloc_msi_entry
===============

.. c:function:: struct msi_desc *alloc_msi_entry(struct device *dev, int nvec, const struct cpumask *affinity)

    Allocate an initialize msi_entry

    :param dev:
        Pointer to the device for which this is allocated
    :type dev: struct device \*

    :param nvec:
        The number of vectors used in this entry
    :type nvec: int

    :param affinity:
        Optional pointer to an affinity mask array size of \ ``nvec``\ 
    :type affinity: const struct cpumask \*

.. _`alloc_msi_entry.description`:

Description
-----------

If \ ``affinity``\  is not NULL then a an affinity array[@nvec] is allocated
and the affinity masks from \ ``affinity``\  are copied.

.. _`msi_domain_set_affinity`:

msi_domain_set_affinity
=======================

.. c:function:: int msi_domain_set_affinity(struct irq_data *irq_data, const struct cpumask *mask, bool force)

    Generic affinity setter function for MSI domains

    :param irq_data:
        The irq data associated to the interrupt
    :type irq_data: struct irq_data \*

    :param mask:
        The affinity mask to set
    :type mask: const struct cpumask \*

    :param force:
        Flag to enforce setting (disable online checks)
    :type force: bool

.. _`msi_domain_set_affinity.description`:

Description
-----------

Intended to be used by MSI interrupt controllers which are
implemented with hierarchical domains.

.. _`msi_create_irq_domain`:

msi_create_irq_domain
=====================

.. c:function:: struct irq_domain *msi_create_irq_domain(struct fwnode_handle *fwnode, struct msi_domain_info *info, struct irq_domain *parent)

    Create a MSI interrupt domain

    :param fwnode:
        Optional fwnode of the interrupt controller
    :type fwnode: struct fwnode_handle \*

    :param info:
        MSI domain info
    :type info: struct msi_domain_info \*

    :param parent:
        Parent irq domain
    :type parent: struct irq_domain \*

.. _`msi_domain_alloc_irqs`:

msi_domain_alloc_irqs
=====================

.. c:function:: int msi_domain_alloc_irqs(struct irq_domain *domain, struct device *dev, int nvec)

    Allocate interrupts from a MSI interrupt domain

    :param domain:
        The domain to allocate from
    :type domain: struct irq_domain \*

    :param dev:
        Pointer to device struct of the device for which the interrupts
        are allocated
    :type dev: struct device \*

    :param nvec:
        The number of interrupts to allocate
    :type nvec: int

.. _`msi_domain_alloc_irqs.description`:

Description
-----------

Returns 0 on success or an error code.

.. _`msi_domain_free_irqs`:

msi_domain_free_irqs
====================

.. c:function:: void msi_domain_free_irqs(struct irq_domain *domain, struct device *dev)

    Free interrupts from a MSI interrupt \ ``domain``\  associated tp \ ``dev``\ 

    :param domain:
        The domain to managing the interrupts
    :type domain: struct irq_domain \*

    :param dev:
        Pointer to device struct of the device for which the interrupts
        are free
    :type dev: struct device \*

.. _`msi_get_domain_info`:

msi_get_domain_info
===================

.. c:function:: struct msi_domain_info *msi_get_domain_info(struct irq_domain *domain)

    Get the MSI interrupt domain info for \ ``domain``\ 

    :param domain:
        The interrupt domain to retrieve data from
    :type domain: struct irq_domain \*

.. _`msi_get_domain_info.description`:

Description
-----------

Returns the pointer to the msi_domain_info stored in
\ ``domain->host_data``\ .

.. This file was automatic generated / don't edit.

