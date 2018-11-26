.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/xilinx/ll_temac_main.c

.. _`temac_indirect_in32`:

temac_indirect_in32
===================

.. c:function:: u32 temac_indirect_in32(struct temac_local *lp, int reg)

    :param lp:
        *undescribed*
    :type lp: struct temac_local \*

    :param reg:
        *undescribed*
    :type reg: int

.. _`temac_indirect_in32.description`:

Description
-----------

lp->indirect_mutex must be held when calling this function

.. _`temac_indirect_out32`:

temac_indirect_out32
====================

.. c:function:: void temac_indirect_out32(struct temac_local *lp, int reg, u32 value)

    :param lp:
        *undescribed*
    :type lp: struct temac_local \*

    :param reg:
        *undescribed*
    :type reg: int

    :param value:
        *undescribed*
    :type value: u32

.. _`temac_indirect_out32.description`:

Description
-----------

lp->indirect_mutex must be held when calling this function

.. _`temac_dma_in32`:

temac_dma_in32
==============

.. c:function:: u32 temac_dma_in32(struct temac_local *lp, int reg)

    Memory mapped DMA read, this function expects a register input that is based on DCR word addresses which are then converted to memory mapped byte addresses

    :param lp:
        *undescribed*
    :type lp: struct temac_local \*

    :param reg:
        *undescribed*
    :type reg: int

.. _`temac_dma_out32`:

temac_dma_out32
===============

.. c:function:: void temac_dma_out32(struct temac_local *lp, int reg, u32 value)

    Memory mapped DMA read, this function expects a register input that is based on DCR word addresses which are then converted to memory mapped byte addresses

    :param lp:
        *undescribed*
    :type lp: struct temac_local \*

    :param reg:
        *undescribed*
    :type reg: int

    :param value:
        *undescribed*
    :type value: u32

.. _`temac_dma_dcr_in`:

temac_dma_dcr_in
================

.. c:function:: u32 temac_dma_dcr_in(struct temac_local *lp, int reg)

    DCR based DMA read

    :param lp:
        *undescribed*
    :type lp: struct temac_local \*

    :param reg:
        *undescribed*
    :type reg: int

.. _`temac_dma_dcr_out`:

temac_dma_dcr_out
=================

.. c:function:: void temac_dma_dcr_out(struct temac_local *lp, int reg, u32 value)

    DCR based DMA write

    :param lp:
        *undescribed*
    :type lp: struct temac_local \*

    :param reg:
        *undescribed*
    :type reg: int

    :param value:
        *undescribed*
    :type value: u32

.. _`temac_dcr_setup`:

temac_dcr_setup
===============

.. c:function:: int temac_dcr_setup(struct temac_local *lp, struct platform_device *op, struct device_node *np)

    If the DMA is DCR based, then setup the address and I/O  functions

    :param lp:
        *undescribed*
    :type lp: struct temac_local \*

    :param op:
        *undescribed*
    :type op: struct platform_device \*

    :param np:
        *undescribed*
    :type np: struct device_node \*

.. _`temac_dma_bd_release`:

temac_dma_bd_release
====================

.. c:function:: void temac_dma_bd_release(struct net_device *ndev)

    Release buffer descriptor rings

    :param ndev:
        *undescribed*
    :type ndev: struct net_device \*

.. _`temac_dma_bd_init`:

temac_dma_bd_init
=================

.. c:function:: int temac_dma_bd_init(struct net_device *ndev)

    Setup buffer descriptor rings

    :param ndev:
        *undescribed*
    :type ndev: struct net_device \*

.. _`temac_setoptions`:

temac_setoptions
================

.. c:function:: u32 temac_setoptions(struct net_device *ndev, u32 options)

    :param ndev:
        *undescribed*
    :type ndev: struct net_device \*

    :param options:
        *undescribed*
    :type options: u32

.. This file was automatic generated / don't edit.

