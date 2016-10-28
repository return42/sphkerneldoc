.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mtd/partitions.h

.. _`mtd_part_parser_data`:

struct mtd_part_parser_data
===========================

.. c:type:: struct mtd_part_parser_data

    used to pass data to MTD partition parsers.

.. _`mtd_part_parser_data.definition`:

Definition
----------

.. code-block:: c

    struct mtd_part_parser_data {
        unsigned long origin;
    }

.. _`mtd_part_parser_data.members`:

Members
-------

origin
    for RedBoot, start address of MTD device

.. This file was automatic generated / don't edit.

