.. -*- coding: utf-8; mode: rst -*-

==============
dm355evm_msp.c
==============


.. _`dm355evm_msp_write`:

dm355evm_msp_write
==================

.. c:function:: int dm355evm_msp_write (u8 value, u8 reg)

    Writes a register in dm355evm_msp

    :param u8 value:
        the value to be written

    :param u8 reg:
        register address



.. _`dm355evm_msp_write.description`:

Description
-----------

Returns result of operation - 0 is success, else negative errno



.. _`dm355evm_msp_read`:

dm355evm_msp_read
=================

.. c:function:: int dm355evm_msp_read (u8 reg)

    Reads a register from dm355evm_msp

    :param u8 reg:
        register address



.. _`dm355evm_msp_read.description`:

Description
-----------

Returns result of operation - value, or negative errno

