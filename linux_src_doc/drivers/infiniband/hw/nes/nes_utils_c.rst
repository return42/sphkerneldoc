.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/nes/nes_utils.c

.. _`nes_read_eeprom_values`:

nes_read_eeprom_values
======================

.. c:function:: int nes_read_eeprom_values(struct nes_device *nesdev, struct nes_adapter *nesadapter)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param nesadapter:
        *undescribed*
    :type nesadapter: struct nes_adapter \*

.. _`nes_read16_eeprom`:

nes_read16_eeprom
=================

.. c:function:: u16 nes_read16_eeprom(void __iomem *addr, u16 offset)

    :param addr:
        *undescribed*
    :type addr: void __iomem \*

    :param offset:
        *undescribed*
    :type offset: u16

.. _`nes_write_1g_phy_reg`:

nes_write_1G_phy_reg
====================

.. c:function:: void nes_write_1G_phy_reg(struct nes_device *nesdev, u8 phy_reg, u8 phy_addr, u16 data)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param phy_reg:
        *undescribed*
    :type phy_reg: u8

    :param phy_addr:
        *undescribed*
    :type phy_addr: u8

    :param data:
        *undescribed*
    :type data: u16

.. _`nes_read_1g_phy_reg`:

nes_read_1G_phy_reg
===================

.. c:function:: void nes_read_1G_phy_reg(struct nes_device *nesdev, u8 phy_reg, u8 phy_addr, u16 *data)

    This routine only issues the read, the data must be read separately.

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param phy_reg:
        *undescribed*
    :type phy_reg: u8

    :param phy_addr:
        *undescribed*
    :type phy_addr: u8

    :param data:
        *undescribed*
    :type data: u16 \*

.. _`nes_write_10g_phy_reg`:

nes_write_10G_phy_reg
=====================

.. c:function:: void nes_write_10G_phy_reg(struct nes_device *nesdev, u16 phy_addr, u8 dev_addr, u16 phy_reg, u16 data)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param phy_addr:
        *undescribed*
    :type phy_addr: u16

    :param dev_addr:
        *undescribed*
    :type dev_addr: u8

    :param phy_reg:
        *undescribed*
    :type phy_reg: u16

    :param data:
        *undescribed*
    :type data: u16

.. _`nes_read_10g_phy_reg`:

nes_read_10G_phy_reg
====================

.. c:function:: void nes_read_10G_phy_reg(struct nes_device *nesdev, u8 phy_addr, u8 dev_addr, u16 phy_reg)

    This routine only issues the read, the data must be read separately.

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param phy_addr:
        *undescribed*
    :type phy_addr: u8

    :param dev_addr:
        *undescribed*
    :type dev_addr: u8

    :param phy_reg:
        *undescribed*
    :type phy_reg: u16

.. _`nes_get_cqp_request`:

nes_get_cqp_request
===================

.. c:function:: struct nes_cqp_request *nes_get_cqp_request(struct nes_device *nesdev)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

.. _`nes_post_cqp_request`:

nes_post_cqp_request
====================

.. c:function:: void nes_post_cqp_request(struct nes_device *nesdev, struct nes_cqp_request *cqp_request)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param cqp_request:
        *undescribed*
    :type cqp_request: struct nes_cqp_request \*

.. _`nes_arp_table`:

nes_arp_table
=============

.. c:function:: int nes_arp_table(struct nes_device *nesdev, u32 ip_addr, u8 *mac_addr, u32 action)

    :param nesdev:
        *undescribed*
    :type nesdev: struct nes_device \*

    :param ip_addr:
        *undescribed*
    :type ip_addr: u32

    :param mac_addr:
        *undescribed*
    :type mac_addr: u8 \*

    :param action:
        *undescribed*
    :type action: u32

.. _`nes_mh_fix`:

nes_mh_fix
==========

.. c:function:: void nes_mh_fix(struct timer_list *t)

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`nes_clc`:

nes_clc
=======

.. c:function:: void nes_clc(struct timer_list *t)

    :param t:
        *undescribed*
    :type t: struct timer_list \*

.. _`nes_dump_mem`:

nes_dump_mem
============

.. c:function:: void nes_dump_mem(unsigned int dump_debug_level, void *addr, int length)

    :param dump_debug_level:
        *undescribed*
    :type dump_debug_level: unsigned int

    :param addr:
        *undescribed*
    :type addr: void \*

    :param length:
        *undescribed*
    :type length: int

.. This file was automatic generated / don't edit.

