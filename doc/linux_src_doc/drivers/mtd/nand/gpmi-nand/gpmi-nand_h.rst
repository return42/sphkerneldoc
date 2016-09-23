.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/gpmi-nand/gpmi-nand.h

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

.. _`nand_timing`:

struct nand_timing
==================

.. c:type:: struct nand_timing

    Fundamental timing attributes for NAND.

.. _`nand_timing.definition`:

Definition
----------

.. code-block:: c

    struct nand_timing {
        int8_t data_setup_in_ns;
        int8_t data_hold_in_ns;
        int8_t address_setup_in_ns;
        int8_t gpmi_sample_delay_in_ns;
        int8_t tREA_in_ns;
        int8_t tRLOH_in_ns;
        int8_t tRHOH_in_ns;
    }

.. _`nand_timing.members`:

Members
-------

data_setup_in_ns
    The data setup time, in nanoseconds. Usually the
    maximum of tDS and tWP. A negative value
    indicates this characteristic isn't known.

data_hold_in_ns
    The data hold time, in nanoseconds. Usually the
    maximum of tDH, tWH and tREH. A negative value
    indicates this characteristic isn't known.

address_setup_in_ns
    The address setup time, in nanoseconds. Usually
    the maximum of tCLS, tCS and tALS. A negative
    value indicates this characteristic isn't known.

gpmi_sample_delay_in_ns
    A GPMI-specific timing parameter. A negative value
    indicates this characteristic isn't known.

tREA_in_ns
    tREA, in nanoseconds, from the data sheet. A
    negative value indicates this characteristic isn't
    known.

tRLOH_in_ns
    tRLOH, in nanoseconds, from the data sheet. A
    negative value indicates this characteristic isn't
    known.

tRHOH_in_ns
    tRHOH, in nanoseconds, from the data sheet. A
    negative value indicates this characteristic isn't
    known.

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
        uint8_t data_setup_in_cycles;
        uint8_t data_hold_in_cycles;
        uint8_t address_setup_in_cycles;
        uint16_t device_busy_timeout;
    #define GPMI_DEFAULT_BUSY_TIMEOUT 0x500
        bool use_half_periods;
        uint8_t sample_delay_factor;
        uint8_t wrn_dly_sel;
    }

.. _`gpmi_nfc_hardware_timing.members`:

Members
-------

data_setup_in_cycles
    The data setup time, in cycles.

data_hold_in_cycles
    The data hold time, in cycles.

address_setup_in_cycles
    The address setup time, in cycles.

device_busy_timeout
    The timeout waiting for NAND Ready/Busy,
    this value is the number of cycles multiplied
    by 4096.

use_half_periods
    Indicates the clock is running slowly, so the
    NFC DLL should use half-periods.

sample_delay_factor
    The sample delay factor.

wrn_dly_sel
    The delay on the GPMI write strobe.

.. _`timing_threshod`:

struct timing_threshod
======================

.. c:type:: struct timing_threshod

    Timing threshold

.. _`timing_threshod.definition`:

Definition
----------

.. code-block:: c

    struct timing_threshod {
        const unsigned int max_chip_count;
        const unsigned int max_data_setup_cycles;
        const unsigned int internal_data_setup_in_ns;
        const unsigned int max_sample_delay_factor;
        const unsigned int max_dll_clock_period_in_ns;
        const unsigned int max_dll_delay_in_ns;
        unsigned long clock_frequency_in_hz;
    }

.. _`timing_threshod.members`:

Members
-------

max_chip_count
    *undescribed*

max_data_setup_cycles
    The maximum number of data setup cycles that
    can be expressed in the hardware.

internal_data_setup_in_ns
    The time, in ns, that the NFC hardware requires
    for data read internal setup. In the Reference
    Manual, see the chapter "High-Speed NAND
    Timing" for more details.

max_sample_delay_factor
    The maximum sample delay factor that can be
    expressed in the hardware.

max_dll_clock_period_in_ns
    The maximum period of the GPMI clock that the
    sample delay DLL hardware can possibly work
    with (the DLL is unusable with longer periods).
    If the full-cycle period is greater than HALF
    this value, the DLL must be configured to use
    half-periods.

max_dll_delay_in_ns
    The maximum amount of delay, in ns, that the
    DLL can implement.

clock_frequency_in_hz
    The clock frequency, in Hz, during the current
    I/O transaction. If no I/O transaction is in
    progress, this is the clock frequency during
    the most recent I/O transaction.

.. This file was automatic generated / don't edit.

