.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nvkm/subdev/secboot/gm20b.c

.. _`gm20b_secboot_tegra_read_wpr`:

gm20b_secboot_tegra_read_wpr
============================

.. c:function:: int gm20b_secboot_tegra_read_wpr(struct gm200_secboot *gsb, u32 mc_base)

    read the WPR registers on Tegra

    :param gsb:
        *undescribed*
    :type gsb: struct gm200_secboot \*

    :param mc_base:
        *undescribed*
    :type mc_base: u32

.. _`gm20b_secboot_tegra_read_wpr.description`:

Description
-----------

On dGPU, we can manage the WPR region ourselves, but on Tegra the WPR region
is reserved from system memory by the bootloader and irreversibly locked.
This function reads the address and size of the pre-configured WPR region.

.. This file was automatic generated / don't edit.

