.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/soc/uniphier/aio-dma.c

.. _`uniphier_aiodma_soc_register_platform`:

uniphier_aiodma_soc_register_platform
=====================================

.. c:function:: int uniphier_aiodma_soc_register_platform(struct platform_device *pdev)

    register the AIO DMA

    :param pdev:
        the platform device
    :type pdev: struct platform_device \*

.. _`uniphier_aiodma_soc_register_platform.description`:

Description
-----------

Register and setup the DMA of AIO to transfer the sound data to device.
This function need to call once at driver startup and need NOT to call
unregister function.

.. _`uniphier_aiodma_soc_register_platform.return`:

Return
------

Zero if successful, otherwise a negative value on error.

.. This file was automatic generated / don't edit.

