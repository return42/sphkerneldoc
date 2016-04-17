.. -*- coding: utf-8; mode: rst -*-

==============
platform-msi.c
==============


.. _`platform_msi_create_irq_domain`:

platform_msi_create_irq_domain
==============================

.. c:function:: struct irq_domain *platform_msi_create_irq_domain (struct fwnode_handle *fwnode, struct msi_domain_info *info, struct irq_domain *parent)

    Create a platform MSI interrupt domain

    :param struct fwnode_handle \*fwnode:
        Optional fwnode of the interrupt controller

    :param struct msi_domain_info \*info:
        MSI domain info

    :param struct irq_domain \*parent:
        Parent irq domain



.. _`platform_msi_create_irq_domain.description`:

Description
-----------

Updates the domain and chip ops and creates a platform MSI
interrupt domain.



.. _`platform_msi_create_irq_domain.returns`:

Returns
-------

A domain pointer or NULL in case of failure.



.. _`platform_msi_domain_alloc_irqs`:

platform_msi_domain_alloc_irqs
==============================

.. c:function:: int platform_msi_domain_alloc_irqs (struct device *dev, unsigned int nvec, irq_write_msi_msg_t write_msi_msg)

    Allocate MSI interrupts for @dev

    :param struct device \*dev:
        The device for which to allocate interrupts

    :param unsigned int nvec:
        The number of interrupts to allocate

    :param irq_write_msi_msg_t write_msi_msg:
        Callback to write an interrupt message for ``dev``



.. _`platform_msi_domain_alloc_irqs.returns`:

Returns
-------

Zero for success, or an error code in case of failure



.. _`platform_msi_domain_free_irqs`:

platform_msi_domain_free_irqs
=============================

.. c:function:: void platform_msi_domain_free_irqs (struct device *dev)

    Free MSI interrupts for @dev

    :param struct device \*dev:
        The device for which to free interrupts



.. _`platform_msi_get_host_data`:

platform_msi_get_host_data
==========================

.. c:function:: void *platform_msi_get_host_data (struct irq_domain *domain)

    Query the private data associated with a platform-msi domain

    :param struct irq_domain \*domain:
        The platform-msi domain



.. _`platform_msi_get_host_data.description`:

Description
-----------

Returns the private data provided when calling
platform_msi_create_device_domain.



.. _`platform_msi_create_device_domain`:

platform_msi_create_device_domain
=================================

.. c:function:: struct irq_domain *platform_msi_create_device_domain (struct device *dev, unsigned int nvec, irq_write_msi_msg_t write_msi_msg, const struct irq_domain_ops *ops, void *host_data)

    Create a platform-msi domain

    :param struct device \*dev:
        The device generating the MSIs

    :param unsigned int nvec:
        The number of MSIs that need to be allocated

    :param irq_write_msi_msg_t write_msi_msg:
        Callback to write an interrupt message for ``dev``

    :param const struct irq_domain_ops \*ops:
        The hierarchy domain operations to use

    :param void \*host_data:
        Private data associated to this domain



.. _`platform_msi_create_device_domain.description`:

Description
-----------

Returns an irqdomain for ``nvec`` interrupts



.. _`platform_msi_domain_free`:

platform_msi_domain_free
========================

.. c:function:: void platform_msi_domain_free (struct irq_domain *domain, unsigned int virq, unsigned int nvec)

    Free interrupts associated with a platform-msi domain

    :param struct irq_domain \*domain:
        The platform-msi domain

    :param unsigned int virq:
        The base irq from which to perform the free operation

    :param unsigned int nvec:
        How many interrupts to free from ``virq``



.. _`platform_msi_domain_alloc`:

platform_msi_domain_alloc
=========================

.. c:function:: int platform_msi_domain_alloc (struct irq_domain *domain, unsigned int virq, unsigned int nr_irqs)

    Allocate interrupts associated with a platform-msi domain

    :param struct irq_domain \*domain:
        The platform-msi domain

    :param unsigned int virq:
        The base irq from which to perform the allocate operation

    :param unsigned int nr_irqs:

        *undescribed*



.. _`platform_msi_domain_alloc.description`:

Description
-----------

Return 0 on success, or an error code on failure. Must be called
with irq_domain_mutex held (which can only be done as part of a
top-level interrupt allocation).

