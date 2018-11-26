.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/spi-nor/spi-nor.c

.. _`spi_nor_div_by_erase_size`:

spi_nor_div_by_erase_size
=========================

.. c:function:: u64 spi_nor_div_by_erase_size(const struct spi_nor_erase_type *erase, u64 dividend, u32 *remainder)

    calculate remainder and update new dividend

    :param erase:
        pointer to a structure that describes a SPI NOR erase type
    :type erase: const struct spi_nor_erase_type \*

    :param dividend:
        dividend value
    :type dividend: u64

    :param remainder:
        pointer to u32 remainder (will be updated)
    :type remainder: u32 \*

.. _`spi_nor_div_by_erase_size.return`:

Return
------

the result of the division

.. _`spi_nor_find_best_erase_type`:

spi_nor_find_best_erase_type
============================

.. c:function:: const struct spi_nor_erase_type *spi_nor_find_best_erase_type(const struct spi_nor_erase_map *map, const struct spi_nor_erase_region *region, u64 addr, u32 len)

    find the best erase type for the given offset in the serial flash memory and the number of bytes to erase. The region in which the address fits is expected to be provided.

    :param map:
        the erase map of the SPI NOR
    :type map: const struct spi_nor_erase_map \*

    :param region:
        pointer to a structure that describes a SPI NOR erase region
    :type region: const struct spi_nor_erase_region \*

    :param addr:
        offset in the serial flash memory
    :type addr: u64

    :param len:
        number of bytes to erase
    :type len: u32

.. _`spi_nor_find_best_erase_type.return`:

Return
------

a pointer to the best fitted erase type, NULL otherwise.

.. _`spi_nor_region_next`:

spi_nor_region_next
===================

.. c:function:: struct spi_nor_erase_region *spi_nor_region_next(struct spi_nor_erase_region *region)

    get the next spi nor region

    :param region:
        pointer to a structure that describes a SPI NOR erase region
    :type region: struct spi_nor_erase_region \*

.. _`spi_nor_region_next.return`:

Return
------

the next spi nor region or NULL if last region.

.. _`spi_nor_find_erase_region`:

spi_nor_find_erase_region
=========================

.. c:function:: struct spi_nor_erase_region *spi_nor_find_erase_region(const struct spi_nor_erase_map *map, u64 addr)

    find the region of the serial flash memory in which the offset fits

    :param map:
        the erase map of the SPI NOR
    :type map: const struct spi_nor_erase_map \*

    :param addr:
        offset in the serial flash memory
    :type addr: u64

.. _`spi_nor_find_erase_region.return`:

Return
------

a pointer to the spi_nor_erase_region struct, ERR_PTR(-errno)
otherwise.

.. _`spi_nor_init_erase_cmd`:

spi_nor_init_erase_cmd
======================

.. c:function:: struct spi_nor_erase_command *spi_nor_init_erase_cmd(const struct spi_nor_erase_region *region, const struct spi_nor_erase_type *erase)

    initialize an erase command

    :param region:
        pointer to a structure that describes a SPI NOR erase region
    :type region: const struct spi_nor_erase_region \*

    :param erase:
        pointer to a structure that describes a SPI NOR erase type
    :type erase: const struct spi_nor_erase_type \*

.. _`spi_nor_init_erase_cmd.return`:

Return
------

the pointer to the allocated erase command, ERR_PTR(-errno)
otherwise.

.. _`spi_nor_destroy_erase_cmd_list`:

spi_nor_destroy_erase_cmd_list
==============================

.. c:function:: void spi_nor_destroy_erase_cmd_list(struct list_head *erase_list)

    destroy erase command list

    :param erase_list:
        list of erase commands
    :type erase_list: struct list_head \*

.. _`spi_nor_init_erase_cmd_list`:

spi_nor_init_erase_cmd_list
===========================

.. c:function:: int spi_nor_init_erase_cmd_list(struct spi_nor *nor, struct list_head *erase_list, u64 addr, u32 len)

    initialize erase command list

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: struct spi_nor \*

    :param erase_list:
        list of erase commands to be executed once we validate that the
        erase can be performed
    :type erase_list: struct list_head \*

    :param addr:
        offset in the serial flash memory
    :type addr: u64

    :param len:
        number of bytes to erase
    :type len: u32

.. _`spi_nor_init_erase_cmd_list.description`:

Description
-----------

Builds the list of best fitted erase commands and verifies if the erase can
be performed.

.. _`spi_nor_init_erase_cmd_list.return`:

Return
------

0 on success, -errno otherwise.

.. _`spi_nor_erase_multi_sectors`:

spi_nor_erase_multi_sectors
===========================

.. c:function:: int spi_nor_erase_multi_sectors(struct spi_nor *nor, u64 addr, u32 len)

    perform a non-uniform erase

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: struct spi_nor \*

    :param addr:
        offset in the serial flash memory
    :type addr: u64

    :param len:
        number of bytes to erase
    :type len: u32

.. _`spi_nor_erase_multi_sectors.description`:

Description
-----------

Build a list of best fitted erase commands and execute it once we validate
that the erase can be performed.

.. _`spi_nor_erase_multi_sectors.return`:

Return
------

0 on success, -errno otherwise.

.. _`macronix_quad_enable`:

macronix_quad_enable
====================

.. c:function:: int macronix_quad_enable(struct spi_nor *nor)

    set QE bit in Status Register.

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: struct spi_nor \*

.. _`macronix_quad_enable.description`:

Description
-----------

Set the Quad Enable (QE) bit in the Status Register.

bit 6 of the Status Register is the QE bit for Macronix like QSPI memories.

.. _`macronix_quad_enable.return`:

Return
------

0 on success, -errno otherwise.

.. _`spansion_quad_enable`:

spansion_quad_enable
====================

.. c:function:: int spansion_quad_enable(struct spi_nor *nor)

    set QE bit in Configuraiton Register.

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: struct spi_nor \*

.. _`spansion_quad_enable.description`:

Description
-----------

Set the Quad Enable (QE) bit in the Configuration Register.
This function is kept for legacy purpose because it has been used for a
long time without anybody complaining but it should be considered as
deprecated and maybe buggy.
First, this function doesn't care about the previous values of the Status
and Configuration Registers when it sets the QE bit (bit 1) in the

.. _`spansion_quad_enable.configuration-register`:

Configuration Register
----------------------

all other bits are cleared, which may have unwanted
side effects like removing some block protections.
Secondly, it uses the Read Configuration Register (35h) instruction though
some very old and few memories don't support this instruction. If a pull-up
resistor is present on the MISO/IO1 line, we might still be able to pass the
"read back" test because the QSPI memory doesn't recognize the command,
so leaves the MISO/IO1 line state unchanged, hence \ :c:func:`read_cr`\  returns 0xFF.

bit 1 of the Configuration Register is the QE bit for Spansion like QSPI
memories.

.. _`spansion_quad_enable.return`:

Return
------

0 on success, -errno otherwise.

.. _`spansion_no_read_cr_quad_enable`:

spansion_no_read_cr_quad_enable
===============================

.. c:function:: int spansion_no_read_cr_quad_enable(struct spi_nor *nor)

    set QE bit in Configuration Register.

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: struct spi_nor \*

.. _`spansion_no_read_cr_quad_enable.description`:

Description
-----------

Set the Quad Enable (QE) bit in the Configuration Register.
This function should be used with QSPI memories not supporting the Read
Configuration Register (35h) instruction.

bit 1 of the Configuration Register is the QE bit for Spansion like QSPI
memories.

.. _`spansion_no_read_cr_quad_enable.return`:

Return
------

0 on success, -errno otherwise.

.. _`spansion_read_cr_quad_enable`:

spansion_read_cr_quad_enable
============================

.. c:function:: int spansion_read_cr_quad_enable(struct spi_nor *nor)

    set QE bit in Configuration Register.

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: struct spi_nor \*

.. _`spansion_read_cr_quad_enable.description`:

Description
-----------

Set the Quad Enable (QE) bit in the Configuration Register.
This function should be used with QSPI memories supporting the Read
Configuration Register (35h) instruction.

bit 1 of the Configuration Register is the QE bit for Spansion like QSPI
memories.

.. _`spansion_read_cr_quad_enable.return`:

Return
------

0 on success, -errno otherwise.

.. _`sr2_bit7_quad_enable`:

sr2_bit7_quad_enable
====================

.. c:function:: int sr2_bit7_quad_enable(struct spi_nor *nor)

    set QE bit in Status Register 2.

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: struct spi_nor \*

.. _`sr2_bit7_quad_enable.description`:

Description
-----------

Set the Quad Enable (QE) bit in the Status Register 2.

This is one of the procedures to set the QE bit described in the SFDP
(JESD216 rev B) specification but no manufacturer using this procedure has
been identified yet, hence the name of the function.

.. _`sr2_bit7_quad_enable.return`:

Return
------

0 on success, -errno otherwise.

.. _`spi_nor_read_raw`:

spi_nor_read_raw
================

.. c:function:: int spi_nor_read_raw(struct spi_nor *nor, u32 addr, size_t len, u8 *buf)

    raw read of serial flash memory. read_opcode, addr_width and read_dummy members of the struct spi_nor should be previously set.

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: struct spi_nor \*

    :param addr:
        offset in the serial flash memory
    :type addr: u32

    :param len:
        number of bytes to read
    :type len: size_t

    :param buf:
        buffer where the data is copied into (dma-safe memory)
    :type buf: u8 \*

.. _`spi_nor_read_raw.return`:

Return
------

0 on success, -errno otherwise.

.. _`spi_nor_read_sfdp`:

spi_nor_read_sfdp
=================

.. c:function:: int spi_nor_read_sfdp(struct spi_nor *nor, u32 addr, size_t len, void *buf)

    read Serial Flash Discoverable Parameters.

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: struct spi_nor \*

    :param addr:
        offset in the SFDP area to start reading data from
    :type addr: u32

    :param len:
        number of bytes to read
    :type len: size_t

    :param buf:
        buffer where the SFDP data are copied into (dma-safe memory)
    :type buf: void \*

.. _`spi_nor_read_sfdp.description`:

Description
-----------

Whatever the actual numbers of bytes for address and dummy cycles are
for (Fast) Read commands, the Read SFDP (5Ah) instruction is always
followed by a 3-byte address and 8 dummy clock cycles.

.. _`spi_nor_read_sfdp.return`:

Return
------

0 on success, -errno otherwise.

.. _`spi_nor_read_sfdp_dma_unsafe`:

spi_nor_read_sfdp_dma_unsafe
============================

.. c:function:: int spi_nor_read_sfdp_dma_unsafe(struct spi_nor *nor, u32 addr, size_t len, void *buf)

    read Serial Flash Discoverable Parameters.

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: struct spi_nor \*

    :param addr:
        offset in the SFDP area to start reading data from
    :type addr: u32

    :param len:
        number of bytes to read
    :type len: size_t

    :param buf:
        buffer where the SFDP data are copied into
    :type buf: void \*

.. _`spi_nor_read_sfdp_dma_unsafe.description`:

Description
-----------

Wrap \ :c:func:`spi_nor_read_sfdp`\  using a kmalloc'ed bounce buffer as \ ``buf``\  is now not
guaranteed to be dma-safe.

.. _`spi_nor_read_sfdp_dma_unsafe.return`:

Return
------

-ENOMEM if \ :c:func:`kmalloc`\  fails, the return code of \ :c:func:`spi_nor_read_sfdp`\ 
otherwise.

.. _`spi_nor_set_erase_type`:

spi_nor_set_erase_type
======================

.. c:function:: void spi_nor_set_erase_type(struct spi_nor_erase_type *erase, u32 size, u8 opcode)

    set a SPI NOR erase type

    :param erase:
        pointer to a structure that describes a SPI NOR erase type
    :type erase: struct spi_nor_erase_type \*

    :param size:
        the size of the sector/block erased by the erase type
    :type size: u32

    :param opcode:
        the SPI command op code to erase the sector/block
    :type opcode: u8

.. _`spi_nor_set_erase_settings_from_bfpt`:

spi_nor_set_erase_settings_from_bfpt
====================================

.. c:function:: void spi_nor_set_erase_settings_from_bfpt(struct spi_nor_erase_type *erase, u32 size, u8 opcode, u8 i)

    set erase type settings from BFPT

    :param erase:
        pointer to a structure that describes a SPI NOR erase type
    :type erase: struct spi_nor_erase_type \*

    :param size:
        the size of the sector/block erased by the erase type
    :type size: u32

    :param opcode:
        the SPI command op code to erase the sector/block
    :type opcode: u8

    :param i:
        erase type index as sorted in the Basic Flash Parameter Table
    :type i: u8

.. _`spi_nor_set_erase_settings_from_bfpt.description`:

Description
-----------

The supported Erase Types will be sorted at init in ascending order, with
the smallest Erase Type size being the first member in the erase_type array
of the spi_nor_erase_map structure. Save the Erase Type index as sorted in
the Basic Flash Parameter Table since it will be used later on to
synchronize with the supported Erase Types defined in SFDP optional tables.

.. _`spi_nor_map_cmp_erase_type`:

spi_nor_map_cmp_erase_type
==========================

.. c:function:: int spi_nor_map_cmp_erase_type(const void *l, const void *r)

    compare the map's erase types by size

    :param l:
        member in the left half of the map's erase_type array
    :type l: const void \*

    :param r:
        member in the right half of the map's erase_type array
    :type r: const void \*

.. _`spi_nor_map_cmp_erase_type.description`:

Description
-----------

Comparison function used in the \ :c:func:`sort`\  call to sort in ascending order the
map's erase types, the smallest erase type size being the first member in the
sorted erase_type array.

.. _`spi_nor_map_cmp_erase_type.return`:

Return
------

the result of \ ``l->size``\  - \ ``r->size``\ 

.. _`spi_nor_sort_erase_mask`:

spi_nor_sort_erase_mask
=======================

.. c:function:: u8 spi_nor_sort_erase_mask(struct spi_nor_erase_map *map, u8 erase_mask)

    sort erase mask

    :param map:
        the erase map of the SPI NOR
    :type map: struct spi_nor_erase_map \*

    :param erase_mask:
        the erase type mask to be sorted
    :type erase_mask: u8

.. _`spi_nor_sort_erase_mask.description`:

Description
-----------

Replicate the sort done for the map's erase types in BFPT: sort the erase
mask in ascending order with the smallest erase type size starting from
BIT(0) in the sorted erase mask.

.. _`spi_nor_sort_erase_mask.return`:

Return
------

sorted erase mask.

.. _`spi_nor_regions_sort_erase_types`:

spi_nor_regions_sort_erase_types
================================

.. c:function:: void spi_nor_regions_sort_erase_types(struct spi_nor_erase_map *map)

    sort erase types in each region

    :param map:
        the erase map of the SPI NOR
    :type map: struct spi_nor_erase_map \*

.. _`spi_nor_regions_sort_erase_types.description`:

Description
-----------

Function assumes that the erase types defined in the erase map are already
sorted in ascending order, with the smallest erase type size being the first
member in the erase_type array. It replicates the sort done for the map's
erase types. Each region's erase bitmask will indicate which erase types are
supported from the sorted erase types defined in the erase map.
Sort the all region's erase type at init in order to speed up the process of
finding the best erase command at runtime.

.. _`spi_nor_init_uniform_erase_map`:

spi_nor_init_uniform_erase_map
==============================

.. c:function:: void spi_nor_init_uniform_erase_map(struct spi_nor_erase_map *map, u8 erase_mask, u64 flash_size)

    Initialize uniform erase map

    :param map:
        the erase map of the SPI NOR
    :type map: struct spi_nor_erase_map \*

    :param erase_mask:
        bitmask encoding erase types that can erase the entire
        flash memory
    :type erase_mask: u8

    :param flash_size:
        the spi nor flash memory size
    :type flash_size: u64

.. _`spi_nor_parse_bfpt`:

spi_nor_parse_bfpt
==================

.. c:function:: int spi_nor_parse_bfpt(struct spi_nor *nor, const struct sfdp_parameter_header *bfpt_header, struct spi_nor_flash_parameter *params)

    read and parse the Basic Flash Parameter Table.

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: struct spi_nor \*

    :param bfpt_header:
        pointer to the 'struct sfdp_parameter_header' describing
        the Basic Flash Parameter Table length and version
    :type bfpt_header: const struct sfdp_parameter_header \*

    :param params:
        pointer to the 'struct spi_nor_flash_parameter' to be
        filled
    :type params: struct spi_nor_flash_parameter \*

.. _`spi_nor_parse_bfpt.description`:

Description
-----------

The Basic Flash Parameter Table is the main and only mandatory table as
defined by the SFDP (JESD216) specification.
It provides us with the total size (memory density) of the data array and
the number of address bytes for Fast Read, Page Program and Sector Erase
commands.
For Fast READ commands, it also gives the number of mode clock cycles and
wait states (regrouped in the number of dummy clock cycles) for each
supported instruction op code.
For Page Program, the page size is now available since JESD216 rev A, however
the supported instruction op codes are still not provided.
For Sector Erase commands, this table stores the supported instruction op
codes and the associated sector sizes.
Finally, the Quad Enable Requirements (QER) are also available since JESD216
rev A. The QER bits encode the manufacturer dependent procedure to be
executed to set the Quad Enable (QE) bit in some internal register of the
Quad SPI memory. Indeed the QE bit, when it exists, must be set before
sending any Quad SPI command to the memory. Actually, setting the QE bit
tells the memory to reassign its WP# and HOLD#/RESET# pins to functions IO2
and IO3 hence enabling 4 (Quad) I/O lines.

.. _`spi_nor_parse_bfpt.return`:

Return
------

0 on success, -errno otherwise.

.. _`spi_nor_smpt_addr_width`:

spi_nor_smpt_addr_width
=======================

.. c:function:: u8 spi_nor_smpt_addr_width(const struct spi_nor *nor, const u32 settings)

    return the address width used in the configuration detection command.

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: const struct spi_nor \*

    :param settings:
        configuration detection command descriptor, dword1
    :type settings: const u32

.. _`spi_nor_smpt_read_dummy`:

spi_nor_smpt_read_dummy
=======================

.. c:function:: u8 spi_nor_smpt_read_dummy(const struct spi_nor *nor, const u32 settings)

    return the configuration detection command read latency, in clock cycles.

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: const struct spi_nor \*

    :param settings:
        configuration detection command descriptor, dword1
    :type settings: const u32

.. _`spi_nor_smpt_read_dummy.return`:

Return
------

the number of dummy cycles for an SMPT read

.. _`spi_nor_get_map_in_use`:

spi_nor_get_map_in_use
======================

.. c:function:: const u32 *spi_nor_get_map_in_use(struct spi_nor *nor, const u32 *smpt, u8 smpt_len)

    get the configuration map in use

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: struct spi_nor \*

    :param smpt:
        pointer to the sector map parameter table
    :type smpt: const u32 \*

    :param smpt_len:
        sector map parameter table length
    :type smpt_len: u8

.. _`spi_nor_get_map_in_use.return`:

Return
------

pointer to the map in use, ERR_PTR(-errno) otherwise.

.. _`spi_nor_region_check_overlay`:

spi_nor_region_check_overlay
============================

.. c:function:: void spi_nor_region_check_overlay(struct spi_nor_erase_region *region, const struct spi_nor_erase_type *erase, const u8 erase_type)

    set overlay bit when the region is overlaid

    :param region:
        pointer to a structure that describes a SPI NOR erase region
    :type region: struct spi_nor_erase_region \*

    :param erase:
        pointer to a structure that describes a SPI NOR erase type
    :type erase: const struct spi_nor_erase_type \*

    :param erase_type:
        erase type bitmask
    :type erase_type: const u8

.. _`spi_nor_init_non_uniform_erase_map`:

spi_nor_init_non_uniform_erase_map
==================================

.. c:function:: int spi_nor_init_non_uniform_erase_map(struct spi_nor *nor, const u32 *smpt)

    initialize the non-uniform erase map

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: struct spi_nor \*

    :param smpt:
        pointer to the sector map parameter table
    :type smpt: const u32 \*

.. _`spi_nor_init_non_uniform_erase_map.return`:

Return
------

0 on success, -errno otherwise.

.. _`spi_nor_parse_smpt`:

spi_nor_parse_smpt
==================

.. c:function:: int spi_nor_parse_smpt(struct spi_nor *nor, const struct sfdp_parameter_header *smpt_header)

    parse Sector Map Parameter Table

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: struct spi_nor \*

    :param smpt_header:
        sector map parameter table header
    :type smpt_header: const struct sfdp_parameter_header \*

.. _`spi_nor_parse_smpt.description`:

Description
-----------

This table is optional, but when available, we parse it to identify the
location and size of sectors within the main data array of the flash memory
device and to identify which Erase Types are supported by each sector.

.. _`spi_nor_parse_smpt.return`:

Return
------

0 on success, -errno otherwise.

.. _`spi_nor_parse_sfdp`:

spi_nor_parse_sfdp
==================

.. c:function:: int spi_nor_parse_sfdp(struct spi_nor *nor, struct spi_nor_flash_parameter *params)

    parse the Serial Flash Discoverable Parameters.

    :param nor:
        pointer to a 'struct spi_nor'
    :type nor: struct spi_nor \*

    :param params:
        pointer to the 'struct spi_nor_flash_parameter' to be
        filled
    :type params: struct spi_nor_flash_parameter \*

.. _`spi_nor_parse_sfdp.description`:

Description
-----------

The Serial Flash Discoverable Parameters are described by the JEDEC JESD216
specification. This is a standard which tends to supported by almost all
(Q)SPI memory manufacturers. Those hard-coded tables allow us to learn at
runtime the main parameters needed to perform basic SPI flash operations such
as Fast Read, Page Program or Sector Erase commands.

.. _`spi_nor_parse_sfdp.return`:

Return
------

0 on success, -errno otherwise.

.. _`spi_nor_select_uniform_erase`:

spi_nor_select_uniform_erase
============================

.. c:function:: const struct spi_nor_erase_type *spi_nor_select_uniform_erase(struct spi_nor_erase_map *map, const u32 wanted_size)

    select optimum uniform erase type

    :param map:
        the erase map of the SPI NOR
    :type map: struct spi_nor_erase_map \*

    :param wanted_size:
        the erase type size to search for. Contains the value of
        info->sector_size or of the "small sector" size in case
        CONFIG_MTD_SPI_NOR_USE_4K_SECTORS is defined.
    :type wanted_size: const u32

.. _`spi_nor_select_uniform_erase.description`:

Description
-----------

Once the optimum uniform sector erase command is found, disable all the
other.

.. _`spi_nor_select_uniform_erase.return`:

Return
------

pointer to erase type on success, NULL otherwise.

.. This file was automatic generated / don't edit.

