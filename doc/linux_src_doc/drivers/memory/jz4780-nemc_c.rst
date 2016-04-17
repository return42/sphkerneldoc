.. -*- coding: utf-8; mode: rst -*-

=============
jz4780-nemc.c
=============


.. _`jz4780_nemc_num_banks`:

jz4780_nemc_num_banks
=====================

.. c:function:: unsigned int jz4780_nemc_num_banks (struct device *dev)

    count the number of banks referenced by a device

    :param struct device \*dev:
        device to count banks for, must be a child of the NEMC.



.. _`jz4780_nemc_num_banks.return`:

Return
------

The number of unique NEMC banks referred to by the specified NEMC
child device. Unique here means that a device that references the same bank
multiple times in the its "reg" property will only count once.



.. _`jz4780_nemc_set_type`:

jz4780_nemc_set_type
====================

.. c:function:: void jz4780_nemc_set_type (struct device *dev, unsigned int bank, enum jz4780_nemc_bank_type type)

    set the type of device connected to a bank

    :param struct device \*dev:
        child device of the NEMC.

    :param unsigned int bank:
        bank number to configure.

    :param enum jz4780_nemc_bank_type type:
        type of device connected to the bank.



.. _`jz4780_nemc_assert`:

jz4780_nemc_assert
==================

.. c:function:: void jz4780_nemc_assert (struct device *dev, unsigned int bank, bool assert)

    (de-)assert a NAND device's chip enable pin

    :param struct device \*dev:
        child device of the NEMC.

    :param unsigned int bank:
        bank number of device.

    :param bool assert:
        whether the chip enable pin should be asserted.



.. _`jz4780_nemc_assert.description`:

Description
-----------

(De-)asserts the chip enable pin for the NAND device connected to the
specified bank.

