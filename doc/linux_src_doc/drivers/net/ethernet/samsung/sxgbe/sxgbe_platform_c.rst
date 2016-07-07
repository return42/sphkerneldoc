.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/samsung/sxgbe/sxgbe_platform.c

.. _`sxgbe_platform_probe`:

sxgbe_platform_probe
====================

.. c:function:: int sxgbe_platform_probe(struct platform_device *pdev)

    :param struct platform_device \*pdev:
        platform device pointer

.. _`sxgbe_platform_probe.description`:

Description
-----------

platform_device probe function. It allocates
the necessary resources and invokes the main to init
the net device, register the mdio bus etc.

.. _`sxgbe_platform_remove`:

sxgbe_platform_remove
=====================

.. c:function:: int sxgbe_platform_remove(struct platform_device *pdev)

    :param struct platform_device \*pdev:
        platform device pointer

.. _`sxgbe_platform_remove.description`:

Description
-----------

this function calls the main to free the net resources
and calls the platforms hook and release the resources (e.g. mem).

.. This file was automatic generated / don't edit.

