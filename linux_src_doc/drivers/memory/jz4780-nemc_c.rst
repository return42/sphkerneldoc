.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/memory/jz4780-nemc.c

.. _`jz4780_nemc_num_banks`:

jz4780_nemc_num_banks
=====================

.. c:function:: unsigned int jz4780_nemc_num_banks(struct device *dev)

    count the number of banks referenced by a device

    :param dev:
        device to count banks for, must be a child of the NEMC.
    :type dev: struct device \*

.. _`jz4780_nemc_num_banks.return`:

Return
------

The number of unique NEMC banks referred to by the specified NEMC
child device. Unique here means that a device that references the same bank
multiple times in the its "reg" property will only count once.

.. _`jz4780_nemc_set_type`:

jz4780_nemc_set_type
====================

.. c:function:: void jz4780_nemc_set_type(struct device *dev, unsigned int bank, enum jz4780_nemc_bank_type type)

    set the type of device connected to a bank

    :param dev:
        child device of the NEMC.
    :type dev: struct device \*

    :param bank:
        bank number to configure.
    :type bank: unsigned int

    :param type:
        type of device connected to the bank.
    :type type: enum jz4780_nemc_bank_type

.. _`jz4780_nemc_assert`:

jz4780_nemc_assert
==================

.. c:function:: void jz4780_nemc_assert(struct device *dev, unsigned int bank, bool assert)

    (de-)assert a NAND device's chip enable pin

    :param dev:
        child device of the NEMC.
    :type dev: struct device \*

    :param bank:
        bank number of device.
    :type bank: unsigned int

    :param assert:
        whether the chip enable pin should be asserted.
    :type assert: bool

.. _`jz4780_nemc_assert.description`:

Description
-----------

(De-)asserts the chip enable pin for the NAND device connected to the
specified bank.

.. This file was automatic generated / don't edit.

