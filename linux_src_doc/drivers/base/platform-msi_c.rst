.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/base/platform-msi.c

.. _`platform_msi_create_irq_domain`:

platform_msi_create_irq_domain
==============================

.. c:function:: struct irq_domain *platform_msi_create_irq_domain(struct fwnode_handle *fwnode, struct msi_domain_info *info, struct irq_domain *parent)

    Create a platform MSI interrupt domain

    :param fwnode:
        Optional fwnode of the interrupt controller
    :type fwnode: struct fwnode_handle \*

    :param info:
        MSI domain info
    :type info: struct msi_domain_info \*

    :param parent:
        Parent irq domain
    :type parent: struct irq_domain \*

.. _`platform_msi_create_irq_domain.description`:

Description
-----------

Updates the domain and chip ops and creates a platform MSI
interrupt domain.

.. _`platform_msi_create_irq_domain.return`:

Return
------

A domain pointer or NULL in case of failure.

.. _`platform_msi_domain_alloc_irqs`:

platform_msi_domain_alloc_irqs
==============================

.. c:function:: int platform_msi_domain_alloc_irqs(struct device *dev, unsigned int nvec, irq_write_msi_msg_t write_msi_msg)

    Allocate MSI interrupts for \ ``dev``\ 

    :param dev:
        The device for which to allocate interrupts
    :type dev: struct device \*

    :param nvec:
        The number of interrupts to allocate
    :type nvec: unsigned int

    :param write_msi_msg:
        Callback to write an interrupt message for \ ``dev``\ 
    :type write_msi_msg: irq_write_msi_msg_t

.. _`platform_msi_domain_alloc_irqs.return`:

Return
------

Zero for success, or an error code in case of failure

.. _`platform_msi_domain_free_irqs`:

platform_msi_domain_free_irqs
=============================

.. c:function:: void platform_msi_domain_free_irqs(struct device *dev)

    Free MSI interrupts for \ ``dev``\ 

    :param dev:
        The device for which to free interrupts
    :type dev: struct device \*

.. _`platform_msi_get_host_data`:

platform_msi_get_host_data
==========================

.. c:function:: void *platform_msi_get_host_data(struct irq_domain *domain)

    Query the private data associated with a platform-msi domain

    :param domain:
        The platform-msi domain
    :type domain: struct irq_domain \*

.. _`platform_msi_get_host_data.description`:

Description
-----------

Returns the private data provided when calling
platform_msi_create_device_domain.

.. _`__platform_msi_create_device_domain`:

\__platform_msi_create_device_domain
====================================

.. c:function:: struct irq_domain *__platform_msi_create_device_domain(struct device *dev, unsigned int nvec, bool is_tree, irq_write_msi_msg_t write_msi_msg, const struct irq_domain_ops *ops, void *host_data)

    Create a platform-msi domain

    :param dev:
        The device generating the MSIs
    :type dev: struct device \*

    :param nvec:
        The number of MSIs that need to be allocated
    :type nvec: unsigned int

    :param is_tree:
        *undescribed*
    :type is_tree: bool

    :param write_msi_msg:
        Callback to write an interrupt message for \ ``dev``\ 
    :type write_msi_msg: irq_write_msi_msg_t

    :param ops:
        The hierarchy domain operations to use
    :type ops: const struct irq_domain_ops \*

    :param host_data:
        Private data associated to this domain
    :type host_data: void \*

.. _`__platform_msi_create_device_domain.description`:

Description
-----------

Returns an irqdomain for \ ``nvec``\  interrupts

.. _`platform_msi_domain_free`:

platform_msi_domain_free
========================

.. c:function:: void platform_msi_domain_free(struct irq_domain *domain, unsigned int virq, unsigned int nvec)

    Free interrupts associated with a platform-msi domain

    :param domain:
        The platform-msi domain
    :type domain: struct irq_domain \*

    :param virq:
        The base irq from which to perform the free operation
    :type virq: unsigned int

    :param nvec:
        How many interrupts to free from \ ``virq``\ 
    :type nvec: unsigned int

.. _`platform_msi_domain_alloc`:

platform_msi_domain_alloc
=========================

.. c:function:: int platform_msi_domain_alloc(struct irq_domain *domain, unsigned int virq, unsigned int nr_irqs)

    Allocate interrupts associated with a platform-msi domain

    :param domain:
        The platform-msi domain
    :type domain: struct irq_domain \*

    :param virq:
        The base irq from which to perform the allocate operation
    :type virq: unsigned int

    :param nr_irqs:
        *undescribed*
    :type nr_irqs: unsigned int

.. _`platform_msi_domain_alloc.description`:

Description
-----------

Return 0 on success, or an error code on failure. Must be called
with irq_domain_mutex held (which can only be done as part of a
top-level interrupt allocation).

.. This file was automatic generated / don't edit.

