.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/stmpe.h

.. _`stmpe_variant_block`:

struct stmpe_variant_block
==========================

.. c:type:: struct stmpe_variant_block

    information about block

.. _`stmpe_variant_block.definition`:

Definition
----------

.. code-block:: c

    struct stmpe_variant_block {
        const struct mfd_cell *cell;
        int irq;
        enum stmpe_block block;
    }

.. _`stmpe_variant_block.members`:

Members
-------

cell
    base mfd cell

irq
    interrupt number to be added to each IORESOURCE_IRQ
    in the cell

block
    block id; used for identification with platform data and for
    enable and altfunc callbacks

.. _`stmpe_variant_info`:

struct stmpe_variant_info
=========================

.. c:type:: struct stmpe_variant_info

    variant-specific information

.. _`stmpe_variant_info.definition`:

Definition
----------

.. code-block:: c

    struct stmpe_variant_info {
        const char *name;
        u16 id_val;
        u16 id_mask;
        int num_gpios;
        int af_bits;
        const u8 *regs;
        struct stmpe_variant_block *blocks;
        int num_blocks;
        int num_irqs;
        int (*enable)(struct stmpe *stmpe, unsigned int blocks, bool enable);
        int (*get_altfunc)(struct stmpe *stmpe, enum stmpe_block block);
        int (*enable_autosleep)(struct stmpe *stmpe, int autosleep_timeout);
    }

.. _`stmpe_variant_info.members`:

Members
-------

name
    part name

id_val
    content of CHIPID register

id_mask
    bits valid in CHIPID register for comparison with id_val

num_gpios
    number of GPIOS

af_bits
    number of bits used to specify the alternate function

regs
    variant specific registers.

blocks
    list of blocks present on this device

num_blocks
    number of blocks present on this device

num_irqs
    number of internal IRQs available on this device

enable
    callback to enable the specified blocks.
    Called with the I/O lock held.

get_altfunc
    callback to get the alternate function number for the
    specific block

enable_autosleep
    callback to configure autosleep with specified timeout

.. _`stmpe_client_info`:

struct stmpe_client_info
========================

.. c:type:: struct stmpe_client_info

    i2c or spi specific routines/info

.. _`stmpe_client_info.definition`:

Definition
----------

.. code-block:: c

    struct stmpe_client_info {
        void *data;
        int irq;
        void *client;
        struct device *dev;
        int (*read_byte)(struct stmpe *stmpe, u8 reg);
        int (*write_byte)(struct stmpe *stmpe, u8 reg, u8 val);
        int (*read_block)(struct stmpe *stmpe, u8 reg, u8 len, u8 *values);
        int (*write_block)(struct stmpe *stmpe, u8 reg, u8 len, const u8 *values);
        void (*init)(struct stmpe *stmpe);
    }

.. _`stmpe_client_info.members`:

Members
-------

data
    client specific data

irq
    *undescribed*

client
    *undescribed*

dev
    *undescribed*

read_byte
    read single byte

write_byte
    write single byte

read_block
    read block or multiple bytes

write_block
    write block or multiple bytes

init
    client init routine, called during probe

.. This file was automatic generated / don't edit.

