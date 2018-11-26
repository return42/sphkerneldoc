.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mtd/spinand.h

.. _`spinand_reset_op`:

SPINAND_RESET_OP
================

.. c:function::  SPINAND_RESET_OP()

.. _`spinand_cmd_prog_load_x4`:

SPINAND_CMD_PROG_LOAD_X4
========================

.. c:function::  SPINAND_CMD_PROG_LOAD_X4()

.. _`spinand_id`:

struct spinand_id
=================

.. c:type:: struct spinand_id

    SPI NAND id structure

.. _`spinand_id.definition`:

Definition
----------

.. code-block:: c

    struct spinand_id {
        u8 data[SPINAND_MAX_ID_LEN];
        int len;
    }

.. _`spinand_id.members`:

Members
-------

data
    buffer containing the id bytes. Currently 4 bytes large, but can
    be extended if required

len
    ID length

.. _`spinand_id.description`:

Description
-----------

struct_spinand_id->data contains all bytes returned after a READ_ID command,
including dummy bytes if the chip does not emit ID bytes right after the
READ_ID command. The responsibility to extract real ID bytes is left to
struct_manufacurer_ops->detect().

.. _`spinand_manufacturer_ops`:

struct spinand_manufacturer_ops
===============================

.. c:type:: struct spinand_manufacturer_ops

    SPI NAND manufacturer specific operations

.. _`spinand_manufacturer_ops.definition`:

Definition
----------

.. code-block:: c

    struct spinand_manufacturer_ops {
        int (*detect)(struct spinand_device *spinand);
        int (*init)(struct spinand_device *spinand);
        void (*cleanup)(struct spinand_device *spinand);
    }

.. _`spinand_manufacturer_ops.members`:

Members
-------

detect
    detect a SPI NAND device. Every time a SPI NAND device is probed
    the core calls the struct_manufacurer_ops->detect() hook of each
    registered manufacturer until one of them return 1. Note that
    the first thing to check in this hook is that the manufacturer ID
    in struct_spinand_device->id matches the manufacturer whose
    ->detect() hook has been called. Should return 1 if there's a
    match, 0 if the manufacturer ID does not match and a negative
    error code otherwise. When true is returned, the core assumes
    that properties of the NAND chip (spinand->base.memorg and
    spinand->base.eccreq) have been filled

init
    initialize a SPI NAND device

cleanup
    cleanup a SPI NAND device

.. _`spinand_manufacturer_ops.description`:

Description
-----------

Each SPI NAND manufacturer driver should implement this interface so that
NAND chips coming from this vendor can be detected and initialized properly.

.. _`spinand_manufacturer`:

struct spinand_manufacturer
===========================

.. c:type:: struct spinand_manufacturer

    SPI NAND manufacturer instance

.. _`spinand_manufacturer.definition`:

Definition
----------

.. code-block:: c

    struct spinand_manufacturer {
        u8 id;
        char *name;
        const struct spinand_manufacturer_ops *ops;
    }

.. _`spinand_manufacturer.members`:

Members
-------

id
    manufacturer ID

name
    manufacturer name

ops
    manufacturer operations

.. _`spinand_op_variants`:

struct spinand_op_variants
==========================

.. c:type:: struct spinand_op_variants

    SPI NAND operation variants

.. _`spinand_op_variants.definition`:

Definition
----------

.. code-block:: c

    struct spinand_op_variants {
        const struct spi_mem_op *ops;
        unsigned int nops;
    }

.. _`spinand_op_variants.members`:

Members
-------

ops
    the list of variants for a given operation

nops
    the number of variants

.. _`spinand_op_variants.description`:

Description
-----------

Some operations like read-from-cache/write-to-cache have several variants
depending on the number of IO lines you use to transfer data or address
cycles. This structure is a way to describe the different variants supported
by a chip and let the core pick the best one based on the SPI mem controller
capabilities.

.. _`spinand_info`:

struct spinand_info
===================

.. c:type:: struct spinand_info

    Structure used to describe SPI NAND chips

.. _`spinand_info.definition`:

Definition
----------

.. code-block:: c

    struct spinand_info {
        const char *model;
        u8 devid;
        u32 flags;
        struct nand_memory_organization memorg;
        struct nand_ecc_req eccreq;
        struct spinand_ecc_info eccinfo;
        struct {
            const struct spinand_op_variants *read_cache;
            const struct spinand_op_variants *write_cache;
            const struct spinand_op_variants *update_cache;
        } op_variants;
        int (*select_target)(struct spinand_device *spinand, unsigned int target);
    }

.. _`spinand_info.members`:

Members
-------

model
    model name

devid
    device ID

flags
    OR-ing of the SPINAND_XXX flags

memorg
    memory organization

eccreq
    ECC requirements

eccinfo
    on-die ECC info

op_variants
    operations variants

op_variants.read_cache
    variants of the read-cache operation

op_variants.write_cache
    variants of the write-cache operation

op_variants.update_cache
    variants of the update-cache operation

select_target
    function used to select a target/die. Required only for
    multi-die chips

.. _`spinand_info.description`:

Description
-----------

Each SPI NAND manufacturer driver should have a spinand_info table
describing all the chips supported by the driver.

.. _`spinand_device`:

struct spinand_device
=====================

.. c:type:: struct spinand_device

    SPI NAND device instance

.. _`spinand_device.definition`:

Definition
----------

.. code-block:: c

    struct spinand_device {
        struct nand_device base;
        struct spi_mem *spimem;
        struct mutex lock;
        struct spinand_id id;
        u32 flags;
        struct {
            const struct spi_mem_op *read_cache;
            const struct spi_mem_op *write_cache;
            const struct spi_mem_op *update_cache;
        } op_templates;
        int (*select_target)(struct spinand_device *spinand, unsigned int target);
        unsigned int cur_target;
        struct spinand_ecc_info eccinfo;
        u8 *cfg_cache;
        u8 *databuf;
        u8 *oobbuf;
        u8 *scratchbuf;
        const struct spinand_manufacturer *manufacturer;
        void *priv;
    }

.. _`spinand_device.members`:

Members
-------

base
    NAND device instance

spimem
    pointer to the SPI mem object

lock
    lock used to serialize accesses to the NAND

id
    NAND ID as returned by READ_ID

flags
    NAND flags

op_templates
    various SPI mem op templates

op_templates.read_cache
    read cache op template

op_templates.write_cache
    write cache op template

op_templates.update_cache
    update cache op template

select_target
    select a specific target/die. Usually called before sending
    a command addressing a page or an eraseblock embedded in
    this die. Only required if your chip exposes several dies

cur_target
    currently selected target/die

eccinfo
    on-die ECC information

cfg_cache
    config register cache. One entry per die

databuf
    bounce buffer for data

oobbuf
    bounce buffer for OOB data

scratchbuf
    buffer used for everything but page accesses. This is needed
    because the spi-mem interface explicitly requests that buffers
    passed in spi_mem_op be DMA-able, so we can't based the bufs on
    the stack

manufacturer
    SPI NAND manufacturer information

priv
    manufacturer private data

.. _`mtd_to_spinand`:

mtd_to_spinand
==============

.. c:function:: struct spinand_device *mtd_to_spinand(struct mtd_info *mtd)

    Get the SPI NAND device attached to an MTD instance

    :param mtd:
        MTD instance
    :type mtd: struct mtd_info \*

.. _`mtd_to_spinand.return`:

Return
------

the SPI NAND device attached to \ ``mtd``\ .

.. _`spinand_to_mtd`:

spinand_to_mtd
==============

.. c:function:: struct mtd_info *spinand_to_mtd(struct spinand_device *spinand)

    Get the MTD device embedded in a SPI NAND device

    :param spinand:
        SPI NAND device
    :type spinand: struct spinand_device \*

.. _`spinand_to_mtd.return`:

Return
------

the MTD device embedded in \ ``spinand``\ .

.. _`nand_to_spinand`:

nand_to_spinand
===============

.. c:function:: struct spinand_device *nand_to_spinand(struct nand_device *nand)

    Get the SPI NAND device embedding an NAND object

    :param nand:
        NAND object
    :type nand: struct nand_device \*

.. _`nand_to_spinand.return`:

Return
------

the SPI NAND device embedding \ ``nand``\ .

.. _`spinand_to_nand`:

spinand_to_nand
===============

.. c:function:: struct nand_device *spinand_to_nand(struct spinand_device *spinand)

    Get the NAND device embedded in a SPI NAND object

    :param spinand:
        SPI NAND device
    :type spinand: struct spinand_device \*

.. _`spinand_to_nand.return`:

Return
------

the NAND device embedded in \ ``spinand``\ .

.. _`spinand_set_of_node`:

spinand_set_of_node
===================

.. c:function:: void spinand_set_of_node(struct spinand_device *spinand, struct device_node *np)

    Attach a DT node to a SPI NAND device

    :param spinand:
        SPI NAND device
    :type spinand: struct spinand_device \*

    :param np:
        DT node
    :type np: struct device_node \*

.. _`spinand_set_of_node.description`:

Description
-----------

Attach a DT node to a SPI NAND device.

.. This file was automatic generated / don't edit.

