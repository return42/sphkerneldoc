
.. _API-struct-platform-nand-chip:

=========================
struct platform_nand_chip
=========================

*man struct platform_nand_chip(9)*

*4.6.0-rc1*

chip level device structure


Synopsis
========

.. code-block:: c

    struct platform_nand_chip {
      int nr_chips;
      int chip_offset;
      int nr_partitions;
      struct mtd_partition * partitions;
      int chip_delay;
      unsigned int options;
      unsigned int bbt_options;
      const char ** part_probe_types;
    };


Members
=======

nr_chips
    max. number of chips to scan for

chip_offset
    chip number offset

nr_partitions
    number of partitions pointed to by partitions (or zero)

partitions
    mtd partition list

chip_delay
    R/B delay value in us

options
    Option flags, e.g. 16bit buswidth

bbt_options
    BBT option flags, e.g. NAND_BBT_USE_FLASH

part_probe_types
    NULL-terminated array of probe types
