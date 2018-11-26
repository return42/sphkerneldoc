.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/spi/core.c

.. _`spinand_upd_cfg`:

spinand_upd_cfg
===============

.. c:function:: int spinand_upd_cfg(struct spinand_device *spinand, u8 mask, u8 val)

    Update the configuration register

    :param spinand:
        the spinand device
    :type spinand: struct spinand_device \*

    :param mask:
        the mask encoding the bits to update in the config reg
    :type mask: u8

    :param val:
        the new value to apply
    :type val: u8

.. _`spinand_upd_cfg.description`:

Description
-----------

Update the configuration register.

.. _`spinand_upd_cfg.return`:

Return
------

0 on success, a negative error code otherwise.

.. _`spinand_select_target`:

spinand_select_target
=====================

.. c:function:: int spinand_select_target(struct spinand_device *spinand, unsigned int target)

    Select a specific NAND target/die

    :param spinand:
        the spinand device
    :type spinand: struct spinand_device \*

    :param target:
        the target/die to select
    :type target: unsigned int

.. _`spinand_select_target.description`:

Description
-----------

Select a new target/die. If chip only has one die, this function is a NOOP.

.. _`spinand_select_target.return`:

Return
------

0 on success, a negative error code otherwise.

.. _`spinand_match_and_init`:

spinand_match_and_init
======================

.. c:function:: int spinand_match_and_init(struct spinand_device *spinand, const struct spinand_info *table, unsigned int table_size, u8 devid)

    Try to find a match between a device ID and an entry in a spinand_info table

    :param spinand:
        SPI NAND object
    :type spinand: struct spinand_device \*

    :param table:
        SPI NAND device description table
    :type table: const struct spinand_info \*

    :param table_size:
        size of the device description table
    :type table_size: unsigned int

    :param devid:
        *undescribed*
    :type devid: u8

.. _`spinand_match_and_init.description`:

Description
-----------

Should be used by SPI NAND manufacturer drivers when they want to find a
match between a device ID retrieved through the READ_ID command and an
entry in the SPI NAND description table. If a match is found, the spinand
object will be initialized with information provided by the matching
spinand_info entry.

.. _`spinand_match_and_init.return`:

Return
------

0 on success, a negative error code otherwise.

.. This file was automatic generated / don't edit.

