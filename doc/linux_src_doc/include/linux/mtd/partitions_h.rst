.. -*- coding: utf-8; mode: rst -*-

============
partitions.h
============


.. _`mtd_part_parser_data`:

struct mtd_part_parser_data
===========================

.. c:type:: mtd_part_parser_data

    used to pass data to MTD partition parsers.


.. _`mtd_part_parser_data.definition`:

Definition
----------

.. code-block:: c

  struct mtd_part_parser_data {
    unsigned long origin;
  };


.. _`mtd_part_parser_data.members`:

Members
-------

:``origin``:
    for RedBoot, start address of MTD device


