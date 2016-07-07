.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/mfd-core.c

.. _`devm_mfd_add_devices`:

devm_mfd_add_devices
====================

.. c:function:: int devm_mfd_add_devices(struct device *dev, int id, const struct mfd_cell *cells, int n_devs, struct resource *mem_base, int irq_base, struct irq_domain *domain)

    Resource managed version of \ :c:func:`mfd_add_devices`\ 

    :param struct device \*dev:
        *undescribed*

    :param int id:
        *undescribed*

    :param const struct mfd_cell \*cells:
        *undescribed*

    :param int n_devs:
        *undescribed*

    :param struct resource \*mem_base:
        *undescribed*

    :param int irq_base:
        *undescribed*

    :param struct irq_domain \*domain:
        *undescribed*

.. _`devm_mfd_add_devices.description`:

Description
-----------

Returns 0 on success or an appropriate negative error number on failure.
All child-devices of the MFD will automatically be removed when it gets
unbinded.

.. This file was automatic generated / don't edit.

