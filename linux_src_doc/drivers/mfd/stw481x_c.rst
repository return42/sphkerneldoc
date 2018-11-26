.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/stw481x.c

.. _`stw481x_get_pctl_reg`:

stw481x_get_pctl_reg
====================

.. c:function:: int stw481x_get_pctl_reg(struct stw481x *stw481x, u8 reg)

    get a power control register

    :param stw481x:
        handle to the stw481x chip
    :type stw481x: struct stw481x \*

    :param reg:
        power control register to fetch
    :type reg: u8

.. _`stw481x_get_pctl_reg.description`:

Description
-----------

The power control registers is a set of one-time-programmable registers
in its own register space, accessed by writing addess bits to these

.. _`stw481x_get_pctl_reg.two-registers`:

two registers
-------------

bits 7,6,5 of PCTL_REG_LO corresponds to the 3 LSBs of
the address and bits 8,9 of PCTL_REG_HI corresponds to the 2 MSBs of
the address, forming an address space of 5 bits, i.e. 32 registers
0x00 ... 0x1f can be obtained.

.. This file was automatic generated / don't edit.

