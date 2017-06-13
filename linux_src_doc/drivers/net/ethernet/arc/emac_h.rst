.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/arc/emac.h

.. _`arc_emac_bd`:

struct arc_emac_bd
==================

.. c:type:: struct arc_emac_bd

    EMAC buffer descriptor (BD).

.. _`arc_emac_bd.definition`:

Definition
----------

.. code-block:: c

    struct arc_emac_bd {
        __le32 info;
        dma_addr_t data;
    }

.. _`arc_emac_bd.members`:

Members
-------

info
    Contains status information on the buffer itself.

data
    32-bit byte addressable pointer to the packet data.

.. _`buffer_state`:

struct buffer_state
===================

.. c:type:: struct buffer_state

    Stores Rx/Tx buffer state.

.. _`buffer_state.definition`:

Definition
----------

.. code-block:: c

    struct buffer_state {
        struct sk_buff *skb;
         DEFINE_DMA_UNMAP_ADDRaddr;
         DEFINE_DMA_UNMAP_LENlen;
    }

.. _`buffer_state.members`:

Members
-------

skb
    *undescribed*

DEFINE_DMA_UNMAP_ADDRaddr
    *undescribed*

DEFINE_DMA_UNMAP_LENlen
    *undescribed*

.. _`arc_emac_priv`:

struct arc_emac_priv
====================

.. c:type:: struct arc_emac_priv

    Storage of EMAC's private information.

.. _`arc_emac_priv.definition`:

Definition
----------

.. code-block:: c

    struct arc_emac_priv {
        const char *drv_name;
        const char *drv_version;
        void (*set_mac_speed)(void *priv, unsigned int speed);
        struct device *dev;
        struct mii_bus *bus;
        struct arc_emac_mdio_bus_data bus_data;
        void __iomem *regs;
        struct clk *clk;
        struct napi_struct napi;
        struct arc_emac_bd *rxbd;
        struct arc_emac_bd *txbd;
        dma_addr_t rxbd_dma;
        dma_addr_t txbd_dma;
        struct buffer_state rx_buff;
        struct buffer_state tx_buff;
        unsigned int txbd_curr;
        unsigned int txbd_dirty;
        unsigned int last_rx_bd;
        unsigned int link;
        unsigned int duplex;
        unsigned int speed;
    }

.. _`arc_emac_priv.members`:

Members
-------

drv_name
    *undescribed*

drv_version
    *undescribed*

set_mac_speed
    *undescribed*

dev
    Pointer to the current device.

bus
    Pointer to the current MII bus.

bus_data
    *undescribed*

regs
    Base address of EMAC memory-mapped control registers.

clk
    *undescribed*

napi
    Structure for NAPI.

rxbd
    Pointer to Rx BD ring.

txbd
    Pointer to Tx BD ring.

rxbd_dma
    DMA handle for Rx BD ring.

txbd_dma
    DMA handle for Tx BD ring.

rx_buff
    Storage for Rx buffers states.

tx_buff
    Storage for Tx buffers states.

txbd_curr
    Index of Tx BD to use on the next "ndo_start_xmit".

txbd_dirty
    Index of Tx BD to free on the next Tx interrupt.

last_rx_bd
    Index of the last Rx BD we've got from EMAC.

link
    PHY's last seen link state.

duplex
    PHY's last set duplex mode.

speed
    PHY's last set speed.

.. _`arc_reg_set`:

arc_reg_set
===========

.. c:function:: void arc_reg_set(struct arc_emac_priv *priv, int reg, int value)

    Sets EMAC register with provided value.

    :param struct arc_emac_priv \*priv:
        Pointer to ARC EMAC private data structure.

    :param int reg:
        Register offset from base address.

    :param int value:
        Value to set in register.

.. _`arc_reg_get`:

arc_reg_get
===========

.. c:function:: unsigned int arc_reg_get(struct arc_emac_priv *priv, int reg)

    Gets value of specified EMAC register.

    :param struct arc_emac_priv \*priv:
        Pointer to ARC EMAC private data structure.

    :param int reg:
        Register offset from base address.

.. _`arc_reg_get.return`:

Return
------

Value of requested register.

.. _`arc_reg_or`:

arc_reg_or
==========

.. c:function:: void arc_reg_or(struct arc_emac_priv *priv, int reg, int mask)

    Applies mask to specified EMAC register - ("reg" \| "mask").

    :param struct arc_emac_priv \*priv:
        Pointer to ARC EMAC private data structure.

    :param int reg:
        Register offset from base address.

    :param int mask:
        Mask to apply to specified register.

.. _`arc_reg_or.description`:

Description
-----------

This function reads initial register value, then applies provided mask
to it and then writes register back.

.. _`arc_reg_clr`:

arc_reg_clr
===========

.. c:function:: void arc_reg_clr(struct arc_emac_priv *priv, int reg, int mask)

    Applies mask to specified EMAC register - ("reg" & ~"mask").

    :param struct arc_emac_priv \*priv:
        Pointer to ARC EMAC private data structure.

    :param int reg:
        Register offset from base address.

    :param int mask:
        Mask to apply to specified register.

.. _`arc_reg_clr.description`:

Description
-----------

This function reads initial register value, then applies provided mask
to it and then writes register back.

.. This file was automatic generated / don't edit.

