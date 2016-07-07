.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/stmpe.c

.. _`stmpe_enable`:

stmpe_enable
============

.. c:function:: int stmpe_enable(struct stmpe *stmpe, unsigned int blocks)

    enable blocks on an STMPE device

    :param struct stmpe \*stmpe:
        Device to work on

    :param unsigned int blocks:
        Mask of blocks (enum stmpe_block values) to enable

.. _`stmpe_disable`:

stmpe_disable
=============

.. c:function:: int stmpe_disable(struct stmpe *stmpe, unsigned int blocks)

    disable blocks on an STMPE device

    :param struct stmpe \*stmpe:
        Device to work on

    :param unsigned int blocks:
        Mask of blocks (enum stmpe_block values) to enable

.. _`stmpe_reg_read`:

stmpe_reg_read
==============

.. c:function:: int stmpe_reg_read(struct stmpe *stmpe, u8 reg)

    read a single STMPE register

    :param struct stmpe \*stmpe:
        Device to read from

    :param u8 reg:
        Register to read

.. _`stmpe_reg_write`:

stmpe_reg_write
===============

.. c:function:: int stmpe_reg_write(struct stmpe *stmpe, u8 reg, u8 val)

    write a single STMPE register

    :param struct stmpe \*stmpe:
        Device to write to

    :param u8 reg:
        Register to write

    :param u8 val:
        Value to write

.. _`stmpe_set_bits`:

stmpe_set_bits
==============

.. c:function:: int stmpe_set_bits(struct stmpe *stmpe, u8 reg, u8 mask, u8 val)

    set the value of a bitfield in a STMPE register

    :param struct stmpe \*stmpe:
        Device to write to

    :param u8 reg:
        Register to write

    :param u8 mask:
        Mask of bits to set

    :param u8 val:
        Value to set

.. _`stmpe_block_read`:

stmpe_block_read
================

.. c:function:: int stmpe_block_read(struct stmpe *stmpe, u8 reg, u8 length, u8 *values)

    read multiple STMPE registers

    :param struct stmpe \*stmpe:
        Device to read from

    :param u8 reg:
        First register

    :param u8 length:
        Number of registers

    :param u8 \*values:
        Buffer to write to

.. _`stmpe_block_write`:

stmpe_block_write
=================

.. c:function:: int stmpe_block_write(struct stmpe *stmpe, u8 reg, u8 length, const u8 *values)

    write multiple STMPE registers

    :param struct stmpe \*stmpe:
        Device to write to

    :param u8 reg:
        First register

    :param u8 length:
        Number of registers

    :param const u8 \*values:
        Values to write

.. _`stmpe_set_altfunc`:

stmpe_set_altfunc
=================

.. c:function:: int stmpe_set_altfunc(struct stmpe *stmpe, u32 pins, enum stmpe_block block)

    set the alternate function for STMPE pins

    :param struct stmpe \*stmpe:
        Device to configure

    :param u32 pins:
        Bitmask of pins to affect

    :param enum stmpe_block block:
        block to enable alternate functions for

.. _`stmpe_set_altfunc.description`:

Description
-----------

\ ``pins``\  is assumed to have a bit set for each of the bits whose alternate
function is to be changed, numbered according to the GPIOXY numbers.

If the GPIO module is not enabled, this function automatically enables it in
order to perform the change.

.. This file was automatic generated / don't edit.

