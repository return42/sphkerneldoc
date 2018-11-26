.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/mach-rockchip/platsmp.c

.. _`rockchip_smp_prepare_sram`:

rockchip_smp_prepare_sram
=========================

.. c:function:: int rockchip_smp_prepare_sram(struct device_node *node)

    populate necessary sram block Starting cores execute the code residing at the start of the on-chip sram after power-on. Therefore make sure, this sram region is reserved and big enough. After this check, copy the trampoline code that directs the core to the real startup code in ram into the sram-region.

    :param node:
        mmio-sram device node
    :type node: struct device_node \*

.. This file was automatic generated / don't edit.

