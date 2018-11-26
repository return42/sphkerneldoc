.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/stmpe.c

.. _`stmpe_platform_data`:

struct stmpe_platform_data
==========================

.. c:type:: struct stmpe_platform_data

    STMPE platform data

.. _`stmpe_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct stmpe_platform_data {
        int id;
        unsigned int blocks;
        unsigned int irq_trigger;
        bool autosleep;
        bool irq_over_gpio;
        int irq_gpio;
        int autosleep_timeout;
    }

.. _`stmpe_platform_data.members`:

Members
-------

id
    device id to distinguish between multiple STMPEs on the same board

blocks
    bitmask of blocks to enable (use STMPE_BLOCK\_\*)

irq_trigger
    IRQ trigger to use for the interrupt to the host

autosleep
    bool to enable/disable stmpe autosleep

irq_over_gpio
    true if gpio is used to get irq

irq_gpio
    gpio number over which irq will be requested (significant only if
    irq_over_gpio is true)

autosleep_timeout
    inactivity timeout in milliseconds for autosleep

.. _`stmpe_enable`:

stmpe_enable
============

.. c:function:: int stmpe_enable(struct stmpe *stmpe, unsigned int blocks)

    enable blocks on an STMPE device

    :param stmpe:
        Device to work on
    :type stmpe: struct stmpe \*

    :param blocks:
        Mask of blocks (enum stmpe_block values) to enable
    :type blocks: unsigned int

.. _`stmpe_disable`:

stmpe_disable
=============

.. c:function:: int stmpe_disable(struct stmpe *stmpe, unsigned int blocks)

    disable blocks on an STMPE device

    :param stmpe:
        Device to work on
    :type stmpe: struct stmpe \*

    :param blocks:
        Mask of blocks (enum stmpe_block values) to enable
    :type blocks: unsigned int

.. _`stmpe_reg_read`:

stmpe_reg_read
==============

.. c:function:: int stmpe_reg_read(struct stmpe *stmpe, u8 reg)

    read a single STMPE register

    :param stmpe:
        Device to read from
    :type stmpe: struct stmpe \*

    :param reg:
        Register to read
    :type reg: u8

.. _`stmpe_reg_write`:

stmpe_reg_write
===============

.. c:function:: int stmpe_reg_write(struct stmpe *stmpe, u8 reg, u8 val)

    write a single STMPE register

    :param stmpe:
        Device to write to
    :type stmpe: struct stmpe \*

    :param reg:
        Register to write
    :type reg: u8

    :param val:
        Value to write
    :type val: u8

.. _`stmpe_set_bits`:

stmpe_set_bits
==============

.. c:function:: int stmpe_set_bits(struct stmpe *stmpe, u8 reg, u8 mask, u8 val)

    set the value of a bitfield in a STMPE register

    :param stmpe:
        Device to write to
    :type stmpe: struct stmpe \*

    :param reg:
        Register to write
    :type reg: u8

    :param mask:
        Mask of bits to set
    :type mask: u8

    :param val:
        Value to set
    :type val: u8

.. _`stmpe_block_read`:

stmpe_block_read
================

.. c:function:: int stmpe_block_read(struct stmpe *stmpe, u8 reg, u8 length, u8 *values)

    read multiple STMPE registers

    :param stmpe:
        Device to read from
    :type stmpe: struct stmpe \*

    :param reg:
        First register
    :type reg: u8

    :param length:
        Number of registers
    :type length: u8

    :param values:
        Buffer to write to
    :type values: u8 \*

.. _`stmpe_block_write`:

stmpe_block_write
=================

.. c:function:: int stmpe_block_write(struct stmpe *stmpe, u8 reg, u8 length, const u8 *values)

    write multiple STMPE registers

    :param stmpe:
        Device to write to
    :type stmpe: struct stmpe \*

    :param reg:
        First register
    :type reg: u8

    :param length:
        Number of registers
    :type length: u8

    :param values:
        Values to write
    :type values: const u8 \*

.. _`stmpe_set_altfunc`:

stmpe_set_altfunc
=================

.. c:function:: int stmpe_set_altfunc(struct stmpe *stmpe, u32 pins, enum stmpe_block block)

    set the alternate function for STMPE pins

    :param stmpe:
        Device to configure
    :type stmpe: struct stmpe \*

    :param pins:
        Bitmask of pins to affect
    :type pins: u32

    :param block:
        block to enable alternate functions for
    :type block: enum stmpe_block

.. _`stmpe_set_altfunc.description`:

Description
-----------

\ ``pins``\  is assumed to have a bit set for each of the bits whose alternate
function is to be changed, numbered according to the GPIOXY numbers.

If the GPIO module is not enabled, this function automatically enables it in
order to perform the change.

.. This file was automatic generated / don't edit.

