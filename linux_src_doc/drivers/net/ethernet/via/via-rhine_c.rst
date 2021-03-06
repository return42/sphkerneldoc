.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/via/via-rhine.c

.. _`rhine_set_cam`:

rhine_set_cam
=============

.. c:function:: void rhine_set_cam(void __iomem *ioaddr, int idx, u8 *addr)

    set CAM multicast filters

    :param ioaddr:
        register block of this Rhine
    :type ioaddr: void __iomem \*

    :param idx:
        multicast CAM index [0..MCAM_SIZE-1]
    :type idx: int

    :param addr:
        multicast address (6 bytes)
    :type addr: u8 \*

.. _`rhine_set_cam.description`:

Description
-----------

Load addresses into multicast filters.

.. _`rhine_set_vlan_cam`:

rhine_set_vlan_cam
==================

.. c:function:: void rhine_set_vlan_cam(void __iomem *ioaddr, int idx, u8 *addr)

    set CAM VLAN filters

    :param ioaddr:
        register block of this Rhine
    :type ioaddr: void __iomem \*

    :param idx:
        VLAN CAM index [0..VCAM_SIZE-1]
    :type idx: int

    :param addr:
        VLAN ID (2 bytes)
    :type addr: u8 \*

.. _`rhine_set_vlan_cam.description`:

Description
-----------

Load addresses into VLAN filters.

.. _`rhine_set_cam_mask`:

rhine_set_cam_mask
==================

.. c:function:: void rhine_set_cam_mask(void __iomem *ioaddr, u32 mask)

    set multicast CAM mask

    :param ioaddr:
        register block of this Rhine
    :type ioaddr: void __iomem \*

    :param mask:
        multicast CAM mask
    :type mask: u32

.. _`rhine_set_cam_mask.description`:

Description
-----------

Mask sets multicast filters active/inactive.

.. _`rhine_set_vlan_cam_mask`:

rhine_set_vlan_cam_mask
=======================

.. c:function:: void rhine_set_vlan_cam_mask(void __iomem *ioaddr, u32 mask)

    set VLAN CAM mask

    :param ioaddr:
        register block of this Rhine
    :type ioaddr: void __iomem \*

    :param mask:
        VLAN CAM mask
    :type mask: u32

.. _`rhine_set_vlan_cam_mask.description`:

Description
-----------

Mask sets VLAN filters active/inactive.

.. _`rhine_init_cam_filter`:

rhine_init_cam_filter
=====================

.. c:function:: void rhine_init_cam_filter(struct net_device *dev)

    initialize CAM filters

    :param dev:
        network device
    :type dev: struct net_device \*

.. _`rhine_init_cam_filter.description`:

Description
-----------

Initialize (disable) hardware VLAN and multicast support on this
Rhine.

.. _`rhine_update_vcam`:

rhine_update_vcam
=================

.. c:function:: void rhine_update_vcam(struct net_device *dev)

    update VLAN CAM filters

    :param dev:
        *undescribed*
    :type dev: struct net_device \*

.. _`rhine_update_vcam.description`:

Description
-----------

Update VLAN CAM filters to match configuration change.

.. _`rhine_get_vlan_tci`:

rhine_get_vlan_tci
==================

.. c:function:: u16 rhine_get_vlan_tci(struct sk_buff *skb, int data_size)

    extract TCI from Rx data buffer

    :param skb:
        pointer to sk_buff
    :type skb: struct sk_buff \*

    :param data_size:
        used data area of the buffer including CRC
    :type data_size: int

.. _`rhine_get_vlan_tci.description`:

Description
-----------

If hardware VLAN tag extraction is enabled and the chip indicates a 802.1Q
packet, the extracted 802.1Q header (2 bytes TPID + 2 bytes TCI) is 4-byte
aligned following the CRC.

.. This file was automatic generated / don't edit.

