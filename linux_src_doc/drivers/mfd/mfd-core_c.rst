.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/mfd-core.c

.. _`devm_mfd_add_devices`:

devm_mfd_add_devices
====================

.. c:function:: int devm_mfd_add_devices(struct device *dev, int id, const struct mfd_cell *cells, int n_devs, struct resource *mem_base, int irq_base, struct irq_domain *domain)

    Resource managed version of \ :c:func:`mfd_add_devices`\ 

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param id:
        *undescribed*
    :type id: int

    :param cells:
        *undescribed*
    :type cells: const struct mfd_cell \*

    :param n_devs:
        *undescribed*
    :type n_devs: int

    :param mem_base:
        *undescribed*
    :type mem_base: struct resource \*

    :param irq_base:
        *undescribed*
    :type irq_base: int

    :param domain:
        *undescribed*
    :type domain: struct irq_domain \*

.. _`devm_mfd_add_devices.description`:

Description
-----------

Returns 0 on success or an appropriate negative error number on failure.
All child-devices of the MFD will automatically be removed when it gets
unbinded.

.. This file was automatic generated / don't edit.

