.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/spi/flash.h

.. _`flash_platform_data`:

struct flash_platform_data
==========================

.. c:type:: struct flash_platform_data

    board-specific flash data

.. _`flash_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct flash_platform_data {
        char *name;
        struct mtd_partition *parts;
        unsigned int nr_parts;
        char *type;
    }

.. _`flash_platform_data.members`:

Members
-------

name
    optional flash device name (eg, as used with mtdparts=)

parts
    optional array of mtd_partitions for static partitioning

nr_parts
    number of mtd_partitions for static partitoning

type
    optional flash device type (e.g. m25p80 vs m25p64), for use
    with chips that can't be queried for JEDEC or other IDs

.. _`flash_platform_data.description`:

Description
-----------

Board init code (in arch/.../mach-xxx/board-yyy.c files) can
provide information about SPI flash parts (such as DataFlash) to
help set up the device and its appropriate default partitioning.

Note that for DataFlash, sizes for pages, blocks, and sectors are
rarely powers of two; and partitions should be sector-aligned.

.. This file was automatic generated / don't edit.

