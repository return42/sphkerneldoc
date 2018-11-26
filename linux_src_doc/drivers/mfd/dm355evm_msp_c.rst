.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/dm355evm_msp.c

.. _`dm355evm_msp_write`:

dm355evm_msp_write
==================

.. c:function:: int dm355evm_msp_write(u8 value, u8 reg)

    Writes a register in dm355evm_msp

    :param value:
        the value to be written
    :type value: u8

    :param reg:
        register address
    :type reg: u8

.. _`dm355evm_msp_write.description`:

Description
-----------

Returns result of operation - 0 is success, else negative errno

.. _`dm355evm_msp_read`:

dm355evm_msp_read
=================

.. c:function:: int dm355evm_msp_read(u8 reg)

    Reads a register from dm355evm_msp

    :param reg:
        register address
    :type reg: u8

.. _`dm355evm_msp_read.description`:

Description
-----------

Returns result of operation - value, or negative errno

.. This file was automatic generated / don't edit.

