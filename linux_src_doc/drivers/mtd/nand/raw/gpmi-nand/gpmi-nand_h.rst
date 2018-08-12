.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/raw/gpmi-nand/gpmi-nand.h

.. _`bch_geometry`:

struct bch_geometry
===================

.. c:type:: struct bch_geometry

    BCH geometry description.

.. _`bch_geometry.definition`:

Definition
----------

.. code-block:: c

    struct bch_geometry {
        unsigned int gf_len;
        unsigned int ecc_strength;
        unsigned int page_size;
        unsigned int metadata_size;
        unsigned int ecc_chunk_size;
        unsigned int ecc_chunk_count;
        unsigned int payload_size;
        unsigned int auxiliary_size;
        unsigned int auxiliary_status_offset;
        unsigned int block_mark_byte_offset;
        unsigned int block_mark_bit_offset;
    }

.. _`bch_geometry.members`:

Members
-------

gf_len
    The length of Galois Field. (e.g., 13 or 14)

ecc_strength
    A number that describes the strength of the ECC
    algorithm.

page_size
    The size, in bytes, of a physical page, including
    both data and OOB.

metadata_size
    The size, in bytes, of the metadata.

ecc_chunk_size
    The size, in bytes, of a single ECC chunk. Note
    the first chunk in the page includes both data and
    metadata, so it's a bit larger than this value.

ecc_chunk_count
    The number of ECC chunks in the page,

payload_size
    The size, in bytes, of the payload buffer.

auxiliary_size
    The size, in bytes, of the auxiliary buffer.

auxiliary_status_offset
    The offset into the auxiliary buffer at which
    the ECC status appears.

block_mark_byte_offset
    The byte offset in the ECC-based page view at
    which the underlying physical block mark appears.

block_mark_bit_offset
    The bit offset into the ECC-based page view at
    which the underlying physical block mark appears.

.. _`boot_rom_geometry`:

struct boot_rom_geometry
========================

.. c:type:: struct boot_rom_geometry

    Boot ROM geometry description.

.. _`boot_rom_geometry.definition`:

Definition
----------

.. code-block:: c

    struct boot_rom_geometry {
        unsigned int stride_size_in_pages;
        unsigned int search_area_stride_exponent;
    }

.. _`boot_rom_geometry.members`:

Members
-------

stride_size_in_pages
    The size of a boot block stride, in pages.

search_area_stride_exponent
    The logarithm to base 2 of the size of a
    search area in boot block strides.

.. _`gpmi_nfc_hardware_timing`:

struct gpmi_nfc_hardware_timing
===============================

.. c:type:: struct gpmi_nfc_hardware_timing

    GPMI hardware timing parameters.

.. _`gpmi_nfc_hardware_timing.definition`:

Definition
----------

.. code-block:: c

    struct gpmi_nfc_hardware_timing {
        bool must_apply_timings;
        unsigned long int clk_rate;
        u32 timing0;
        u32 timing1;
        u32 ctrl1n;
    }

.. _`gpmi_nfc_hardware_timing.members`:

Members
-------

must_apply_timings
    Whether controller timings have already been
    applied or not (useful only while there is
    support for only one chip select)

clk_rate
    The clock rate that must be used to derive the
    following parameters

timing0
    HW_GPMI_TIMING0 register

timing1
    HW_GPMI_TIMING1 register

ctrl1n
    HW_GPMI_CTRL1n register

.. This file was automatic generated / don't edit.

