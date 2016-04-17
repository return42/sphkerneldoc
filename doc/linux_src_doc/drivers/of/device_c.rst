.. -*- coding: utf-8; mode: rst -*-

========
device.c
========


.. _`of_match_device`:

of_match_device
===============

.. c:function:: const struct of_device_id *of_match_device (const struct of_device_id *matches, const struct device *dev)

    Tell if a struct device matches an of_device_id list

    :param const struct of_device_id \*matches:

        *undescribed*

    :param const struct device \*dev:
        the of device structure to match against



.. _`of_match_device.description`:

Description
-----------

Used by a driver to check whether an platform_device present in the
system is in its list of supported devices.



.. _`of_dma_configure`:

of_dma_configure
================

.. c:function:: void of_dma_configure (struct device *dev, struct device_node *np)

    Setup DMA configuration

    :param struct device \*dev:
        Device to apply DMA configuration

    :param struct device_node \*np:
        Pointer to OF node having DMA configuration



.. _`of_dma_configure.description`:

Description
-----------

Try to get devices's DMA configuration from DT and update it
accordingly.

If platform code needs to use its own special DMA configuration, it
can use a platform bus notifier and handle BUS_NOTIFY_ADD_DEVICE events
to fix up DMA configuration.



.. _`of_device_uevent`:

of_device_uevent
================

.. c:function:: void of_device_uevent (struct device *dev, struct kobj_uevent_env *env)

    Display OF related uevent information

    :param struct device \*dev:

        *undescribed*

    :param struct kobj_uevent_env \*env:

        *undescribed*

