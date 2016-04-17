.. -*- coding: utf-8; mode: rst -*-

=========
sys_soc.h
=========


.. _`soc_device_register`:

soc_device_register
===================

.. c:function:: struct soc_device *soc_device_register (struct soc_device_attribute *soc_plat_dev_attr)

    register SoC as a device

    :param struct soc_device_attribute \*soc_plat_dev_attr:
        Attributes passed from platform to be attributed to a SoC



.. _`soc_device_unregister`:

soc_device_unregister
=====================

.. c:function:: void soc_device_unregister (struct soc_device *soc_dev)

    unregister SoC device

    :param struct soc_device \*soc_dev:

        *undescribed*



.. _`soc_device_to_device`:

soc_device_to_device
====================

.. c:function:: struct device *soc_device_to_device (struct soc_device *soc)

    helper function to fetch struct device

    :param struct soc_device \*soc:
        Previously registered SoC device container

