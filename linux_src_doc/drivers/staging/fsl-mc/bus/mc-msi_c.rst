.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fsl-mc/bus/mc-msi.c

.. _`fsl_mc_msi_create_irq_domain`:

fsl_mc_msi_create_irq_domain
============================

.. c:function:: struct irq_domain *fsl_mc_msi_create_irq_domain(struct fwnode_handle *fwnode, struct msi_domain_info *info, struct irq_domain *parent)

    Create a fsl-mc MSI interrupt domain

    :param struct fwnode_handle \*fwnode:
        *undescribed*

    :param struct msi_domain_info \*info:
        MSI domain info

    :param struct irq_domain \*parent:
        Parent irq domain

.. _`fsl_mc_msi_create_irq_domain.description`:

Description
-----------

Updates the domain and chip ops and creates a fsl-mc MSI
interrupt domain.

.. _`fsl_mc_msi_create_irq_domain.return`:

Return
------

A domain pointer or NULL in case of failure.

.. This file was automatic generated / don't edit.

