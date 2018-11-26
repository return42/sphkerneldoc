.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/sys_soc.h

.. _`soc_device_register`:

soc_device_register
===================

.. c:function:: struct soc_device *soc_device_register(struct soc_device_attribute *soc_plat_dev_attr)

    register SoC as a device

    :param soc_plat_dev_attr:
        Attributes passed from platform to be attributed to a SoC
    :type soc_plat_dev_attr: struct soc_device_attribute \*

.. _`soc_device_unregister`:

soc_device_unregister
=====================

.. c:function:: void soc_device_unregister(struct soc_device *soc_dev)

    unregister SoC device

    :param soc_dev:
        *undescribed*
    :type soc_dev: struct soc_device \*

.. _`soc_device_to_device`:

soc_device_to_device
====================

.. c:function:: struct device *soc_device_to_device(struct soc_device *soc)

    helper function to fetch struct device

    :param soc:
        Previously registered SoC device container
    :type soc: struct soc_device \*

.. This file was automatic generated / don't edit.

