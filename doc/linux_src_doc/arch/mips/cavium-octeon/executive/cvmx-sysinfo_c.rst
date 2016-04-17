.. -*- coding: utf-8; mode: rst -*-

==============
cvmx-sysinfo.c
==============


.. _`cvmx_sysinfo_get`:

cvmx_sysinfo_get
================

.. c:function:: struct cvmx_sysinfo *cvmx_sysinfo_get ( void)

    :param void:
        no arguments



.. _`cvmx_sysinfo_get.description`:

Description
-----------


by the bootloader.  This provides the core mask of the cores
running the same application image, as well as the physical
memory regions available to the core.

Returns  Pointer to the boot information structure



.. _`cvmx_sysinfo_minimal_initialize`:

cvmx_sysinfo_minimal_initialize
===============================

.. c:function:: int cvmx_sysinfo_minimal_initialize (void *phy_mem_desc_ptr, uint16_t board_type, uint8_t board_rev_major, uint8_t board_rev_minor, uint32_t cpu_clock_hz)

    simple executive environments (such as Linux kernel, u-boot, etc.) to configure the minimal fields that are required to use simple executive files directly.

    :param void \*phy_mem_desc_ptr:
        Pointer to global physical memory descriptor
        (bootmem descriptor) ``board_type``\ : Octeon board
        type enumeration

    :param uint16_t board_type:

        *undescribed*

    :param uint8_t board_rev_major:
        Board major revision

    :param uint8_t board_rev_minor:
        Board minor revision

    :param uint32_t cpu_clock_hz:
        CPU clock freqency in hertz



.. _`cvmx_sysinfo_minimal_initialize.description`:

Description
-----------


Locking (if required) must be handled outside of this
function



.. _`cvmx_sysinfo_minimal_initialize.returns-0`:

Returns 0
---------

Failure



.. _`cvmx_sysinfo_minimal_initialize.1`:

1
-

success

