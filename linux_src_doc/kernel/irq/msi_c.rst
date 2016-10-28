.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/irq/msi.c

.. _`msi_domain_set_affinity`:

msi_domain_set_affinity
=======================

.. c:function:: int msi_domain_set_affinity(struct irq_data *irq_data, const struct cpumask *mask, bool force)

    Generic affinity setter function for MSI domains

    :param struct irq_data \*irq_data:
        The irq data associated to the interrupt

    :param const struct cpumask \*mask:
        The affinity mask to set

    :param bool force:
        Flag to enforce setting (disable online checks)

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

    :param struct fwnode_handle \*fwnode:
        Optional fwnode of the interrupt controller

    :param struct msi_domain_info \*info:
        MSI domain info

    :param struct irq_domain \*parent:
        Parent irq domain

.. _`msi_domain_alloc_irqs`:

msi_domain_alloc_irqs
=====================

.. c:function:: int msi_domain_alloc_irqs(struct irq_domain *domain, struct device *dev, int nvec)

    Allocate interrupts from a MSI interrupt domain

    :param struct irq_domain \*domain:
        The domain to allocate from

    :param struct device \*dev:
        Pointer to device struct of the device for which the interrupts
        are allocated

    :param int nvec:
        The number of interrupts to allocate

.. _`msi_domain_alloc_irqs.description`:

Description
-----------

Returns 0 on success or an error code.

.. _`msi_domain_free_irqs`:

msi_domain_free_irqs
====================

.. c:function:: void msi_domain_free_irqs(struct irq_domain *domain, struct device *dev)

    Free interrupts from a MSI interrupt \ ``domain``\  associated tp \ ``dev``\ 

    :param struct irq_domain \*domain:
        The domain to managing the interrupts

    :param struct device \*dev:
        Pointer to device struct of the device for which the interrupts
        are free

.. _`msi_get_domain_info`:

msi_get_domain_info
===================

.. c:function:: struct msi_domain_info *msi_get_domain_info(struct irq_domain *domain)

    Get the MSI interrupt domain info for \ ``domain``\ 

    :param struct irq_domain \*domain:
        The interrupt domain to retrieve data from

.. _`msi_get_domain_info.description`:

Description
-----------

Returns the pointer to the msi_domain_info stored in
\ ``domain``\ ->host_data.

.. This file was automatic generated / don't edit.

