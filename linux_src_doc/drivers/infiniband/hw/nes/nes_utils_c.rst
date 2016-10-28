.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/infiniband/hw/nes/nes_utils.c

.. _`nes_read_eeprom_values`:

nes_read_eeprom_values
======================

.. c:function:: int nes_read_eeprom_values(struct nes_device *nesdev, struct nes_adapter *nesadapter)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_adapter \*nesadapter:
        *undescribed*

.. _`nes_read16_eeprom`:

nes_read16_eeprom
=================

.. c:function:: u16 nes_read16_eeprom(void __iomem *addr, u16 offset)

    :param void __iomem \*addr:
        *undescribed*

    :param u16 offset:
        *undescribed*

.. _`nes_write_1g_phy_reg`:

nes_write_1G_phy_reg
====================

.. c:function:: void nes_write_1G_phy_reg(struct nes_device *nesdev, u8 phy_reg, u8 phy_addr, u16 data)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param u8 phy_reg:
        *undescribed*

    :param u8 phy_addr:
        *undescribed*

    :param u16 data:
        *undescribed*

.. _`nes_read_1g_phy_reg`:

nes_read_1G_phy_reg
===================

.. c:function:: void nes_read_1G_phy_reg(struct nes_device *nesdev, u8 phy_reg, u8 phy_addr, u16 *data)

    This routine only issues the read, the data must be read separately.

    :param struct nes_device \*nesdev:
        *undescribed*

    :param u8 phy_reg:
        *undescribed*

    :param u8 phy_addr:
        *undescribed*

    :param u16 \*data:
        *undescribed*

.. _`nes_write_10g_phy_reg`:

nes_write_10G_phy_reg
=====================

.. c:function:: void nes_write_10G_phy_reg(struct nes_device *nesdev, u16 phy_addr, u8 dev_addr, u16 phy_reg, u16 data)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param u16 phy_addr:
        *undescribed*

    :param u8 dev_addr:
        *undescribed*

    :param u16 phy_reg:
        *undescribed*

    :param u16 data:
        *undescribed*

.. _`nes_read_10g_phy_reg`:

nes_read_10G_phy_reg
====================

.. c:function:: void nes_read_10G_phy_reg(struct nes_device *nesdev, u8 phy_addr, u8 dev_addr, u16 phy_reg)

    This routine only issues the read, the data must be read separately.

    :param struct nes_device \*nesdev:
        *undescribed*

    :param u8 phy_addr:
        *undescribed*

    :param u8 dev_addr:
        *undescribed*

    :param u16 phy_reg:
        *undescribed*

.. _`nes_get_cqp_request`:

nes_get_cqp_request
===================

.. c:function:: struct nes_cqp_request *nes_get_cqp_request(struct nes_device *nesdev)

    :param struct nes_device \*nesdev:
        *undescribed*

.. _`nes_post_cqp_request`:

nes_post_cqp_request
====================

.. c:function:: void nes_post_cqp_request(struct nes_device *nesdev, struct nes_cqp_request *cqp_request)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param struct nes_cqp_request \*cqp_request:
        *undescribed*

.. _`nes_arp_table`:

nes_arp_table
=============

.. c:function:: int nes_arp_table(struct nes_device *nesdev, u32 ip_addr, u8 *mac_addr, u32 action)

    :param struct nes_device \*nesdev:
        *undescribed*

    :param u32 ip_addr:
        *undescribed*

    :param u8 \*mac_addr:
        *undescribed*

    :param u32 action:
        *undescribed*

.. _`nes_mh_fix`:

nes_mh_fix
==========

.. c:function:: void nes_mh_fix(unsigned long parm)

    :param unsigned long parm:
        *undescribed*

.. _`nes_clc`:

nes_clc
=======

.. c:function:: void nes_clc(unsigned long parm)

    :param unsigned long parm:
        *undescribed*

.. _`nes_dump_mem`:

nes_dump_mem
============

.. c:function:: void nes_dump_mem(unsigned int dump_debug_level, void *addr, int length)

    :param unsigned int dump_debug_level:
        *undescribed*

    :param void \*addr:
        *undescribed*

    :param int length:
        *undescribed*

.. This file was automatic generated / don't edit.

