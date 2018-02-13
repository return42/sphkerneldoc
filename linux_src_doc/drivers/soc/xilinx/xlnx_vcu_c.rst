.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/xilinx/xlnx_vcu.c

.. _`xvcu_device`:

struct xvcu_device
==================

.. c:type:: struct xvcu_device

    Xilinx VCU init device structure

.. _`xvcu_device.definition`:

Definition
----------

.. code-block:: c

    struct xvcu_device {
        struct device *dev;
        struct clk *pll_ref;
        struct clk *aclk;
        void __iomem *logicore_reg_ba;
        void __iomem *vcu_slcr_ba;
        u32 coreclk;
    }

.. _`xvcu_device.members`:

Members
-------

dev
    Platform device

pll_ref
    pll ref clock source

aclk
    axi clock source

logicore_reg_ba
    logicore reg base address

vcu_slcr_ba
    vcu_slcr Register base address

coreclk
    core clock frequency

.. _`xvcu_pll_cfg`:

struct xvcu_pll_cfg
===================

.. c:type:: struct xvcu_pll_cfg

    Helper data

.. _`xvcu_pll_cfg.definition`:

Definition
----------

.. code-block:: c

    struct xvcu_pll_cfg {
        u32 fbdiv;
        u32 cp;
        u32 res;
        u32 lfhf;
        u32 lock_dly;
        u32 lock_cnt;
    }

.. _`xvcu_pll_cfg.members`:

Members
-------

fbdiv
    The integer portion of the feedback divider to the PLL

cp
    PLL charge pump control

res
    PLL loop filter resistor control

lfhf
    PLL loop filter high frequency capacitor control

lock_dly
    Lock circuit configuration settings for lock windowsize

lock_cnt
    Lock circuit counter setting

.. _`xvcu_read`:

xvcu_read
=========

.. c:function:: u32 xvcu_read(void __iomem *iomem, u32 offset)

    Read from the VCU register space

    :param void __iomem \*iomem:
        vcu reg space base address

    :param u32 offset:
        vcu reg offset from base

.. _`xvcu_read.return`:

Return
------

Returns 32bit value from VCU register specified

.. _`xvcu_write`:

xvcu_write
==========

.. c:function:: void xvcu_write(void __iomem *iomem, u32 offset, u32 value)

    Write to the VCU register space

    :param void __iomem \*iomem:
        vcu reg space base address

    :param u32 offset:
        vcu reg offset from base

    :param u32 value:
        Value to write

.. _`xvcu_write_field_reg`:

xvcu_write_field_reg
====================

.. c:function:: void xvcu_write_field_reg(void __iomem *iomem, int offset, u32 field, u32 mask, int shift)

    Write to the vcu reg field

    :param void __iomem \*iomem:
        vcu reg space base address

    :param int offset:
        vcu reg offset from base

    :param u32 field:
        vcu reg field to write to

    :param u32 mask:
        vcu reg mask

    :param int shift:
        vcu reg number of bits to shift the bitfield

.. _`xvcu_set_vcu_pll_info`:

xvcu_set_vcu_pll_info
=====================

.. c:function:: int xvcu_set_vcu_pll_info(struct xvcu_device *xvcu)

    Set the VCU PLL info

    :param struct xvcu_device \*xvcu:
        Pointer to the xvcu_device structure

.. _`xvcu_set_vcu_pll_info.description`:

Description
-----------

Programming the VCU PLL based on the user configuration
(ref clock freq, core clock freq, mcu clock freq).
Core clock frequency has higher priority than mcu clock frequency
Errors in following cases
- When mcu or clock clock get from logicoreIP is 0
- When VCU PLL DIV related bits value other than 1
- When proper data not found for given data
- When sis570_1 clocksource related operation failed

.. _`xvcu_set_vcu_pll_info.return`:

Return
------

Returns status, either success or error+reason

.. _`xvcu_set_pll`:

xvcu_set_pll
============

.. c:function:: int xvcu_set_pll(struct xvcu_device *xvcu)

    PLL init sequence

    :param struct xvcu_device \*xvcu:
        Pointer to the xvcu_device structure

.. _`xvcu_set_pll.description`:

Description
-----------

Call the api to set the PLL info and once that is done then
init the PLL sequence to make the PLL stable.

.. _`xvcu_set_pll.return`:

Return
------

Returns status, either success or error+reason

.. _`xvcu_probe`:

xvcu_probe
==========

.. c:function:: int xvcu_probe(struct platform_device *pdev)

    Probe existence of the logicoreIP and initialize PLL

    :param struct platform_device \*pdev:
        Pointer to the platform_device structure

.. _`xvcu_probe.return`:

Return
------

Returns 0 on success
Negative error code otherwise

.. _`xvcu_remove`:

xvcu_remove
===========

.. c:function:: int xvcu_remove(struct platform_device *pdev)

    Insert gasket isolation and disable the clock

    :param struct platform_device \*pdev:
        Pointer to the platform_device structure

.. _`xvcu_remove.return`:

Return
------

Returns 0 on success
Negative error code otherwise

.. This file was automatic generated / don't edit.

