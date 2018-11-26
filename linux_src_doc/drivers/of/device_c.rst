.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/of/device.c

.. _`of_match_device`:

of_match_device
===============

.. c:function:: const struct of_device_id *of_match_device(const struct of_device_id *matches, const struct device *dev)

    Tell if a struct device matches an of_device_id list

    :param matches:
        *undescribed*
    :type matches: const struct of_device_id \*

    :param dev:
        the of device structure to match against
    :type dev: const struct device \*

.. _`of_match_device.description`:

Description
-----------

Used by a driver to check whether an platform_device present in the
system is in its list of supported devices.

.. _`of_dma_configure`:

of_dma_configure
================

.. c:function:: int of_dma_configure(struct device *dev, struct device_node *np, bool force_dma)

    Setup DMA configuration

    :param dev:
        Device to apply DMA configuration
    :type dev: struct device \*

    :param np:
        Pointer to OF node having DMA configuration
    :type np: struct device_node \*

    :param force_dma:
        Whether device is to be set up by \ :c:func:`of_dma_configure`\  even if
        DMA capability is not explicitly described by firmware.
    :type force_dma: bool

.. _`of_dma_configure.description`:

Description
-----------

Try to get devices's DMA configuration from DT and update it
accordingly.

If platform code needs to use its own special DMA configuration, it
can use a platform bus notifier and handle BUS_NOTIFY_ADD_DEVICE events
to fix up DMA configuration.

.. _`of_device_modalias`:

of_device_modalias
==================

.. c:function:: ssize_t of_device_modalias(struct device *dev, char *str, ssize_t len)

    Fill buffer with newline terminated modalias string

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param str:
        *undescribed*
    :type str: char \*

    :param len:
        *undescribed*
    :type len: ssize_t

.. _`of_device_uevent`:

of_device_uevent
================

.. c:function:: void of_device_uevent(struct device *dev, struct kobj_uevent_env *env)

    Display OF related uevent information

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param env:
        *undescribed*
    :type env: struct kobj_uevent_env \*

.. This file was automatic generated / don't edit.

