.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/broadcom/bnx2x/bnx2x_link.c

.. _`bnx2x_get_emac_base`:

bnx2x_get_emac_base
===================

.. c:function:: u32 bnx2x_get_emac_base(struct bnx2x *bp, u32 mdc_mdio_access, u8 port)

    retrive emac base address

    :param bp:
        driver handle
    :type bp: struct bnx2x \*

    :param mdc_mdio_access:
        access type
    :type mdc_mdio_access: u32

    :param port:
        port id
    :type port: u8

.. _`bnx2x_get_emac_base.description`:

Description
-----------

This function selects the MDC/MDIO access (through emac0 or
emac1) depend on the mdc_mdio_access, port, port swapped. Each
phy has a default access mode, which could also be overridden
by nvram configuration. This parameter, whether this is the
default phy configuration, or the nvram overrun
configuration, is passed here as mdc_mdio_access and selects
the emac_base for the CL45 read/writes operations

.. This file was automatic generated / don't edit.

