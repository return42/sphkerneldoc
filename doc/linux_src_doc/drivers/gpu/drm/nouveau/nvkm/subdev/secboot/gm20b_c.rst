.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nvkm/subdev/secboot/gm20b.c

.. _`gm20b_secboot_fixup_bl_desc`:

gm20b_secboot_fixup_bl_desc
===========================

.. c:function:: void gm20b_secboot_fixup_bl_desc(const struct gm200_flcn_bl_desc *desc, void *ret)

    adapt BL descriptor to format used by GM20B FW

    :param const struct gm200_flcn_bl_desc \*desc:
        *undescribed*

    :param void \*ret:
        *undescribed*

.. _`gm20b_secboot_fixup_bl_desc.description`:

Description
-----------

There is only a slight format difference (DMA addresses being 32-bits and
256B-aligned) to address.

.. _`gm20b_tegra_read_wpr`:

gm20b_tegra_read_wpr
====================

.. c:function:: int gm20b_tegra_read_wpr(struct gm200_secboot *gsb)

    read the WPR registers on Tegra

    :param struct gm200_secboot \*gsb:
        *undescribed*

.. _`gm20b_tegra_read_wpr.description`:

Description
-----------

On dGPU, we can manage the WPR region ourselves, but on Tegra the WPR region
is reserved from system memory by the bootloader and irreversibly locked.
This function reads the address and size of the pre-configured WPR region.

.. This file was automatic generated / don't edit.

