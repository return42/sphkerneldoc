.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/ezchip/nps_enet.h

.. _`nps_enet_priv`:

struct nps_enet_priv
====================

.. c:type:: struct nps_enet_priv

    Storage of ENET's private information.

.. _`nps_enet_priv.definition`:

Definition
----------

.. code-block:: c

    struct nps_enet_priv {
        void __iomem *regs_base;
        s32 irq;
        struct sk_buff *tx_skb;
        struct napi_struct napi;
        u32 ge_mac_cfg_2_value;
        u32 ge_mac_cfg_3_value;
    }

.. _`nps_enet_priv.members`:

Members
-------

regs_base
    Base address of ENET memory-mapped control registers.

irq
    For RX/TX IRQ number.

tx_skb
    socket buffer of sent frame.

napi
    Structure for NAPI.

ge_mac_cfg_2_value
    *undescribed*

ge_mac_cfg_3_value
    *undescribed*

.. _`nps_enet_reg_set`:

nps_enet_reg_set
================

.. c:function:: void nps_enet_reg_set(struct nps_enet_priv *priv, s32 reg, s32 value)

    Sets ENET register with provided value.

    :param struct nps_enet_priv \*priv:
        Pointer to EZchip ENET private data structure.

    :param s32 reg:
        Register offset from base address.

    :param s32 value:
        Value to set in register.

.. _`nps_enet_reg_get`:

nps_enet_reg_get
================

.. c:function:: u32 nps_enet_reg_get(struct nps_enet_priv *priv, s32 reg)

    Gets value of specified ENET register.

    :param struct nps_enet_priv \*priv:
        Pointer to EZchip ENET private data structure.

    :param s32 reg:
        Register offset from base address.

.. _`nps_enet_reg_get.return`:

Return
------

Value of requested register.

.. This file was automatic generated / don't edit.

