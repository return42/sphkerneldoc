.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/parisc/kernel/firmware.c

.. _`f_extend`:

f_extend
========

.. c:function:: unsigned long f_extend(unsigned long address)

    Convert PDC addresses to kernel addresses.

    :param unsigned long address:
        Address returned from PDC.

.. _`f_extend.description`:

Description
-----------

This function is used to convert PDC addresses into kernel addresses
when the PDC address size and kernel address size are different.

.. _`convert_to_wide`:

convert_to_wide
===============

.. c:function:: void convert_to_wide(unsigned long *addr)

    Convert the return buffer addresses into kernel addresses.

    :param unsigned long \*addr:
        *undescribed*

.. _`convert_to_wide.description`:

Description
-----------

This function is used to convert the return buffer addresses retrieved from PDC
into kernel addresses when the PDC address size and kernel address size are
different.

.. _`set_firmware_width`:

set_firmware_width
==================

.. c:function:: void set_firmware_width( void)

    Determine if the firmware is wide or narrow.

    :param  void:
        no arguments

.. _`set_firmware_width.description`:

Description
-----------

This function must be called before any pdc\_\* function that uses the
convert_to_wide function.

.. _`pdc_emergency_unlock`:

pdc_emergency_unlock
====================

.. c:function:: void pdc_emergency_unlock( void)

    Unlock the linux pdc lock

    :param  void:
        no arguments

.. _`pdc_emergency_unlock.description`:

Description
-----------

This call unlocks the linux pdc lock in case we need some PDC functions
(like pdc_add_valid) during kernel stack dump.

.. _`pdc_add_valid`:

pdc_add_valid
=============

.. c:function:: int pdc_add_valid(unsigned long address)

    Verify address can be accessed without causing a HPMC.

    :param unsigned long address:
        Address to be verified.

.. _`pdc_add_valid.description`:

Description
-----------

This PDC call attempts to read from the specified address and verifies
if the address is valid.

The return value is PDC_OK (0) in case accessing this address is valid.

.. _`pdc_chassis_info`:

pdc_chassis_info
================

.. c:function:: int pdc_chassis_info(struct pdc_chassis_info *chassis_info, void *led_info, unsigned long len)

    Return chassis information.

    :param struct pdc_chassis_info \*chassis_info:
        The memory buffer address.

    :param void \*led_info:
        *undescribed*

    :param unsigned long len:
        The size of the memory buffer address.

.. _`pdc_chassis_info.description`:

Description
-----------

An HVERSION dependent call for returning the chassis information.

.. _`pdc_pat_chassis_send_log`:

pdc_pat_chassis_send_log
========================

.. c:function:: int pdc_pat_chassis_send_log(unsigned long state, unsigned long data)

    Sends a PDC PAT CHASSIS log message.

    :param unsigned long state:
        *undescribed*

    :param unsigned long data:
        *undescribed*

.. _`pdc_pat_chassis_send_log.description`:

Description
-----------

Must be correctly formatted or expect system crash

.. _`pdc_chassis_disp`:

pdc_chassis_disp
================

.. c:function:: int pdc_chassis_disp(unsigned long disp)

    Updates chassis code

    :param unsigned long disp:
        *undescribed*

.. _`pdc_chassis_warn`:

pdc_chassis_warn
================

.. c:function:: int pdc_chassis_warn(unsigned long *warn)

    Fetches chassis warnings

    :param unsigned long \*warn:
        *undescribed*

.. _`pdc_coproc_cfg`:

pdc_coproc_cfg
==============

.. c:function:: int pdc_coproc_cfg(struct pdc_coproc_cfg *pdc_coproc_info)

    To identify coprocessors attached to the processor.

    :param struct pdc_coproc_cfg \*pdc_coproc_info:
        Return buffer address.

.. _`pdc_coproc_cfg.description`:

Description
-----------

This PDC call returns the presence and status of all the coprocessors
attached to the processor.

.. _`pdc_iodc_read`:

pdc_iodc_read
=============

.. c:function:: int pdc_iodc_read(unsigned long *actcnt, unsigned long hpa, unsigned int index, void *iodc_data, unsigned int iodc_data_size)

    Read data from the modules IODC.

    :param unsigned long \*actcnt:
        The actual number of bytes.

    :param unsigned long hpa:
        The HPA of the module for the iodc read.

    :param unsigned int index:
        The iodc entry point.

    :param void \*iodc_data:
        A buffer memory for the iodc options.

    :param unsigned int iodc_data_size:
        Size of the memory buffer.

.. _`pdc_iodc_read.description`:

Description
-----------

This PDC call reads from the IODC of the module specified by the hpa
argument.

.. _`pdc_system_map_find_mods`:

pdc_system_map_find_mods
========================

.. c:function:: int pdc_system_map_find_mods(struct pdc_system_map_mod_info *pdc_mod_info, struct pdc_module_path *mod_path, long mod_index)

    Locate unarchitected modules.

    :param struct pdc_system_map_mod_info \*pdc_mod_info:
        Return buffer address.

    :param struct pdc_module_path \*mod_path:
        pointer to dev path structure.

    :param long mod_index:
        fixed address module index.

.. _`pdc_system_map_find_mods.description`:

Description
-----------

To locate and identify modules which reside at fixed I/O addresses, which
do not self-identify via architected bus walks.

.. _`pdc_system_map_find_addrs`:

pdc_system_map_find_addrs
=========================

.. c:function:: int pdc_system_map_find_addrs(struct pdc_system_map_addr_info *pdc_addr_info, long mod_index, long addr_index)

    Retrieve additional address ranges.

    :param struct pdc_system_map_addr_info \*pdc_addr_info:
        Return buffer address.

    :param long mod_index:
        Fixed address module index.

    :param long addr_index:
        Address range index.

.. _`pdc_system_map_find_addrs.description`:

Description
-----------

Retrieve additional information about subsequent address ranges for modules
with multiple address ranges.

.. _`pdc_model_info`:

pdc_model_info
==============

.. c:function:: int pdc_model_info(struct pdc_model *model)

    Return model information about the processor.

    :param struct pdc_model \*model:
        The return buffer.

.. _`pdc_model_info.description`:

Description
-----------

Returns the version numbers, identifiers, and capabilities from the processor module.

.. _`pdc_model_sysmodel`:

pdc_model_sysmodel
==================

.. c:function:: int pdc_model_sysmodel(char *name)

    Get the system model name.

    :param char \*name:
        A char array of at least 81 characters.

.. _`pdc_model_sysmodel.description`:

Description
-----------

Get system model name from PDC ROM (e.g. 9000/715 or 9000/778/B160L).
Using OS_ID_HPUX will return the equivalent of the 'modelname' command
on HP/UX.

.. _`pdc_model_versions`:

pdc_model_versions
==================

.. c:function:: int pdc_model_versions(unsigned long *versions, int id)

    Identify the version number of each processor.

    :param unsigned long \*versions:
        *undescribed*

    :param int id:
        The id of the processor to check.

.. _`pdc_model_versions.description`:

Description
-----------

Returns the version number for each processor component.

This comment was here before, but I do not know what it means :( -RB
id: 0 = cpu revision, 1 = boot-rom-version

.. _`pdc_model_cpuid`:

pdc_model_cpuid
===============

.. c:function:: int pdc_model_cpuid(unsigned long *cpu_id)

    Returns the CPU_ID.

    :param unsigned long \*cpu_id:
        The return buffer.

.. _`pdc_model_cpuid.description`:

Description
-----------

Returns the CPU_ID value which uniquely identifies the cpu portion of
the processor module.

.. _`pdc_model_capabilities`:

pdc_model_capabilities
======================

.. c:function:: int pdc_model_capabilities(unsigned long *capabilities)

    Returns the platform capabilities.

    :param unsigned long \*capabilities:
        The return buffer.

.. _`pdc_model_capabilities.description`:

Description
-----------

Returns information about platform support for 32- and/or 64-bit
OSes, IO-PDIR coherency, and virtual aliasing.

.. _`pdc_cache_info`:

pdc_cache_info
==============

.. c:function:: int pdc_cache_info(struct pdc_cache_info *cache_info)

    Return cache and TLB information.

    :param struct pdc_cache_info \*cache_info:
        The return buffer.

.. _`pdc_cache_info.description`:

Description
-----------

Returns information about the processor's cache and TLB.

.. _`pdc_spaceid_bits`:

pdc_spaceid_bits
================

.. c:function:: int pdc_spaceid_bits(unsigned long *space_bits)

    Return whether Space ID hashing is turned on.

    :param unsigned long \*space_bits:
        Should be 0, if not, bad mojo!

.. _`pdc_spaceid_bits.description`:

Description
-----------

Returns information about Space ID hashing.

.. _`pdc_btlb_info`:

pdc_btlb_info
=============

.. c:function:: int pdc_btlb_info(struct pdc_btlb_info *btlb)

    Return block TLB information.

    :param struct pdc_btlb_info \*btlb:
        The return buffer.

.. _`pdc_btlb_info.description`:

Description
-----------

Returns information about the hardware Block TLB.

.. _`pdc_mem_map_hpa`:

pdc_mem_map_hpa
===============

.. c:function:: int pdc_mem_map_hpa(struct pdc_memory_map *address, struct pdc_module_path *mod_path)

    Find fixed module information.

    :param struct pdc_memory_map \*address:
        The return buffer

    :param struct pdc_module_path \*mod_path:
        pointer to dev path structure.

.. _`pdc_mem_map_hpa.description`:

Description
-----------

This call was developed for S700 workstations to allow the kernel to find
the I/O devices (Core I/O). In the future (Kittyhawk and beyond) this
call will be replaced (on workstations) by the architected PDC_SYSTEM_MAP
call.

This call is supported by all existing S700 workstations (up to  Gecko).

.. _`pdc_lan_station_id`:

pdc_lan_station_id
==================

.. c:function:: int pdc_lan_station_id(char *lan_addr, unsigned long hpa)

    Get the LAN address.

    :param char \*lan_addr:
        The return buffer.

    :param unsigned long hpa:
        The network device HPA.

.. _`pdc_lan_station_id.description`:

Description
-----------

Get the LAN station address when it is not directly available from the LAN hardware.

.. _`pdc_stable_read`:

pdc_stable_read
===============

.. c:function:: int pdc_stable_read(unsigned long staddr, void *memaddr, unsigned long count)

    Read data from Stable Storage.

    :param unsigned long staddr:
        Stable Storage address to access.

    :param void \*memaddr:
        The memory address where Stable Storage data shall be copied.

    :param unsigned long count:
        number of bytes to transfer. count is multiple of 4.

.. _`pdc_stable_read.description`:

Description
-----------

This PDC call reads from the Stable Storage address supplied in staddr
and copies count bytes to the memory address memaddr.
The call will fail if staddr+count > PDC_STABLE size.

.. _`pdc_stable_write`:

pdc_stable_write
================

.. c:function:: int pdc_stable_write(unsigned long staddr, void *memaddr, unsigned long count)

    Write data to Stable Storage.

    :param unsigned long staddr:
        Stable Storage address to access.

    :param void \*memaddr:
        The memory address where Stable Storage data shall be read from.

    :param unsigned long count:
        number of bytes to transfer. count is multiple of 4.

.. _`pdc_stable_write.description`:

Description
-----------

This PDC call reads count bytes from the supplied memaddr address,
and copies count bytes to the Stable Storage address staddr.
The call will fail if staddr+count > PDC_STABLE size.

.. _`pdc_stable_get_size`:

pdc_stable_get_size
===================

.. c:function:: int pdc_stable_get_size(unsigned long *size)

    Get Stable Storage size in bytes.

    :param unsigned long \*size:
        pointer where the size will be stored.

.. _`pdc_stable_get_size.description`:

Description
-----------

This PDC call returns the number of bytes in the processor's Stable
Storage, which is the number of contiguous bytes implemented in Stable
Storage starting from staddr=0. size in an unsigned 64-bit integer
which is a multiple of four.

.. _`pdc_stable_verify_contents`:

pdc_stable_verify_contents
==========================

.. c:function:: int pdc_stable_verify_contents( void)

    Checks that Stable Storage contents are valid.

    :param  void:
        no arguments

.. _`pdc_stable_verify_contents.description`:

Description
-----------

This PDC call is meant to be used to check the integrity of the current
contents of Stable Storage.

.. _`pdc_stable_initialize`:

pdc_stable_initialize
=====================

.. c:function:: int pdc_stable_initialize( void)

    Sets Stable Storage contents to zero and initialize the validity indicator.

    :param  void:
        no arguments

.. _`pdc_stable_initialize.description`:

Description
-----------

This PDC call will erase all contents of Stable Storage. Use with care!

.. _`pdc_get_initiator`:

pdc_get_initiator
=================

.. c:function:: int pdc_get_initiator(struct hardware_path *hwpath, struct pdc_initiator *initiator)

    Get the SCSI Interface Card params (SCSI ID, SDTR, SE or LVD)

    :param struct hardware_path \*hwpath:
        fully bc.mod style path to the device.

    :param struct pdc_initiator \*initiator:
        the array to return the result into

.. _`pdc_get_initiator.description`:

Description
-----------

Get the SCSI operational parameters from PDC.
Needed since HPUX never used BIOS or symbios card NVRAM.
Most ncr/sym cards won't have an entry and just use whatever
capabilities of the card are (eg Ultra, LVD). But there are
several cases where it's useful:
o set SCSI id for Multi-initiator clusters,
o cable too long (ie SE scsi 10Mhz won't support 6m length),
o bus width exported is less than what the interface chip supports.

.. _`pdc_pci_irt_size`:

pdc_pci_irt_size
================

.. c:function:: int pdc_pci_irt_size(unsigned long *num_entries, unsigned long hpa)

    Get the number of entries in the interrupt routing table.

    :param unsigned long \*num_entries:
        The return value.

    :param unsigned long hpa:
        The HPA for the device.

.. _`pdc_pci_irt_size.description`:

Description
-----------

This PDC function returns the number of entries in the specified cell's
interrupt table.
Similar to PDC_PAT stuff - but added for Forte/Allegro boxes

.. _`pdc_pci_irt`:

pdc_pci_irt
===========

.. c:function:: int pdc_pci_irt(unsigned long num_entries, unsigned long hpa, void *tbl)

    Get the PCI interrupt routing table.

    :param unsigned long num_entries:
        The number of entries in the table.

    :param unsigned long hpa:
        The Hard Physical Address of the device.

    :param void \*tbl:
        *undescribed*

.. _`pdc_pci_irt.description`:

Description
-----------

Get the PCI interrupt routing table for the device at the given HPA.
Similar to PDC_PAT stuff - but added for Forte/Allegro boxes

.. _`pdc_pci_config_read`:

pdc_pci_config_read
===================

.. c:function:: unsigned int pdc_pci_config_read(void *hpa, unsigned long cfg_addr)

    read PCI config space. \ ``hpa``\          token from PDC to indicate which PCI device \ ``pci_addr``\     configuration space address to read from

    :param void \*hpa:
        *undescribed*

    :param unsigned long cfg_addr:
        *undescribed*

.. _`pdc_pci_config_read.description`:

Description
-----------

Read PCI Configuration space \*before\* linux PCI subsystem is running.

.. _`pdc_pci_config_write`:

pdc_pci_config_write
====================

.. c:function:: void pdc_pci_config_write(void *hpa, unsigned long cfg_addr, unsigned int val)

    read PCI config space. \ ``hpa``\          token from PDC to indicate which PCI device \ ``pci_addr``\     configuration space address to write \ ``val``\          value we want in the 32-bit register

    :param void \*hpa:
        *undescribed*

    :param unsigned long cfg_addr:
        *undescribed*

    :param unsigned int val:
        *undescribed*

.. _`pdc_pci_config_write.description`:

Description
-----------

Write PCI Configuration space \*before\* linux PCI subsystem is running.

.. _`pdc_tod_read`:

pdc_tod_read
============

.. c:function:: int pdc_tod_read(struct pdc_tod *tod)

    Read the Time-Of-Day clock.

    :param struct pdc_tod \*tod:
        The return buffer:

.. _`pdc_tod_read.description`:

Description
-----------

Read the Time-Of-Day clock

.. _`pdc_tod_set`:

pdc_tod_set
===========

.. c:function:: int pdc_tod_set(unsigned long sec, unsigned long usec)

    Set the Time-Of-Day clock.

    :param unsigned long sec:
        The number of seconds since epoch.

    :param unsigned long usec:
        The number of micro seconds.

.. _`pdc_tod_set.description`:

Description
-----------

Set the Time-Of-Day clock.

.. _`pdc_iodc_print`:

pdc_iodc_print
==============

.. c:function:: int pdc_iodc_print(const unsigned char *str, unsigned count)

    Console print using IODC.

    :param const unsigned char \*str:
        the string to output.

    :param unsigned count:
        length of str

.. _`pdc_iodc_print.note-that-only-these-special-chars-are-architected-for-console-iodc-io`:

Note that only these special chars are architected for console IODC io
----------------------------------------------------------------------

BEL, BS, CR, and LF. Others are passed through.
Since the HP console requires CR+LF to perform a 'newline', we translate
"\n" to "\r\n".

.. _`pdc_iodc_getc`:

pdc_iodc_getc
=============

.. c:function:: int pdc_iodc_getc( void)

    Read a character (non-blocking) from the PDC console.

    :param  void:
        no arguments

.. _`pdc_iodc_getc.description`:

Description
-----------

Read a character (non-blocking) from the PDC console, returns -1 if
key is not present.

.. _`pdc_pat_cell_get_number`:

pdc_pat_cell_get_number
=======================

.. c:function:: int pdc_pat_cell_get_number(struct pdc_pat_cell_num *cell_info)

    Returns the cell number.

    :param struct pdc_pat_cell_num \*cell_info:
        The return buffer.

.. _`pdc_pat_cell_get_number.description`:

Description
-----------

This PDC call returns the cell number of the cell from which the call
is made.

.. _`pdc_pat_cell_module`:

pdc_pat_cell_module
===================

.. c:function:: int pdc_pat_cell_module(unsigned long *actcnt, unsigned long ploc, unsigned long mod, unsigned long view_type, void *mem_addr)

    Retrieve the cell's module information.

    :param unsigned long \*actcnt:
        The number of bytes written to mem_addr.

    :param unsigned long ploc:
        The physical location.

    :param unsigned long mod:
        The module index.

    :param unsigned long view_type:
        The view of the address type.

    :param void \*mem_addr:
        The return buffer.

.. _`pdc_pat_cell_module.description`:

Description
-----------

This PDC call returns information about each module attached to the cell
at the specified location.

.. _`pdc_pat_cpu_get_number`:

pdc_pat_cpu_get_number
======================

.. c:function:: int pdc_pat_cpu_get_number(struct pdc_pat_cpu_num *cpu_info, unsigned long hpa)

    Retrieve the cpu number.

    :param struct pdc_pat_cpu_num \*cpu_info:
        The return buffer.

    :param unsigned long hpa:
        The Hard Physical Address of the CPU.

.. _`pdc_pat_cpu_get_number.description`:

Description
-----------

Retrieve the cpu number for the cpu at the specified HPA.

.. _`pdc_pat_get_irt_size`:

pdc_pat_get_irt_size
====================

.. c:function:: int pdc_pat_get_irt_size(unsigned long *num_entries, unsigned long cell_num)

    Retrieve the number of entries in the cell's interrupt table.

    :param unsigned long \*num_entries:
        The return value.

    :param unsigned long cell_num:
        The target cell.

.. _`pdc_pat_get_irt_size.description`:

Description
-----------

This PDC function returns the number of entries in the specified cell's
interrupt table.

.. _`pdc_pat_get_irt`:

pdc_pat_get_irt
===============

.. c:function:: int pdc_pat_get_irt(void *r_addr, unsigned long cell_num)

    Retrieve the cell's interrupt table.

    :param void \*r_addr:
        The return buffer.

    :param unsigned long cell_num:
        The target cell.

.. _`pdc_pat_get_irt.description`:

Description
-----------

This PDC function returns the actual interrupt table for the specified cell.

.. _`pdc_pat_pd_get_addr_map`:

pdc_pat_pd_get_addr_map
=======================

.. c:function:: int pdc_pat_pd_get_addr_map(unsigned long *actual_len, void *mem_addr, unsigned long count, unsigned long offset)

    Retrieve information about memory address ranges.

    :param unsigned long \*actual_len:
        *undescribed*

    :param void \*mem_addr:
        Pointer to the memory buffer.

    :param unsigned long count:
        The number of bytes to read from the buffer.

    :param unsigned long offset:
        The offset with respect to the beginning of the buffer.

.. _`pdc_pat_io_pci_cfg_read`:

pdc_pat_io_pci_cfg_read
=======================

.. c:function:: int pdc_pat_io_pci_cfg_read(unsigned long pci_addr, int pci_size, u32 *mem_addr)

    Read PCI configuration space.

    :param unsigned long pci_addr:
        PCI configuration space address for which the read request is being made.

    :param int pci_size:
        Size of read in bytes. Valid values are 1, 2, and 4.

    :param u32 \*mem_addr:
        Pointer to return memory buffer.

.. _`pdc_pat_io_pci_cfg_write`:

pdc_pat_io_pci_cfg_write
========================

.. c:function:: int pdc_pat_io_pci_cfg_write(unsigned long pci_addr, int pci_size, u32 val)

    Retrieve information about memory address ranges.

    :param unsigned long pci_addr:
        PCI configuration space address for which the write  request is being made.

    :param int pci_size:
        Size of write in bytes. Valid values are 1, 2, and 4.

    :param u32 val:
        *undescribed*

.. _`pdc_pat_mem_pdt_info`:

pdc_pat_mem_pdt_info
====================

.. c:function:: int pdc_pat_mem_pdt_info(struct pdc_pat_mem_retinfo *rinfo)

    Retrieve information about page deallocation table

    :param struct pdc_pat_mem_retinfo \*rinfo:
        memory pdt information

.. _`pdc_pat_mem_pdt_cell_info`:

pdc_pat_mem_pdt_cell_info
=========================

.. c:function:: int pdc_pat_mem_pdt_cell_info(struct pdc_pat_mem_cell_pdt_retinfo *rinfo, unsigned long cell)

    Retrieve information about page deallocation table of a cell

    :param struct pdc_pat_mem_cell_pdt_retinfo \*rinfo:
        memory pdt information

    :param unsigned long cell:
        cell number

.. _`pdc_pat_mem_read_cell_pdt`:

pdc_pat_mem_read_cell_pdt
=========================

.. c:function:: int pdc_pat_mem_read_cell_pdt(struct pdc_pat_mem_read_pd_retinfo *pret, unsigned long *pdt_entries_ptr, unsigned long max_entries)

    Read PDT entries from (old) PAT firmware

    :param struct pdc_pat_mem_read_pd_retinfo \*pret:
        array of PDT entries

    :param unsigned long \*pdt_entries_ptr:
        ptr to hold number of PDT entries

    :param unsigned long max_entries:
        maximum number of entries to be read

.. _`pdc_pat_mem_read_pd_pdt`:

pdc_pat_mem_read_pd_pdt
=======================

.. c:function:: int pdc_pat_mem_read_pd_pdt(struct pdc_pat_mem_read_pd_retinfo *pret, unsigned long *pdt_entries_ptr, unsigned long count, unsigned long offset)

    Read PDT entries from (newer) PAT firmware

    :param struct pdc_pat_mem_read_pd_retinfo \*pret:
        array of PDT entries

    :param unsigned long \*pdt_entries_ptr:
        ptr to hold number of PDT entries

    :param unsigned long count:
        number of bytes to read

    :param unsigned long offset:
        offset to start (in bytes)

.. _`pdc_pat_mem_get_dimm_phys_location`:

pdc_pat_mem_get_dimm_phys_location
==================================

.. c:function:: int pdc_pat_mem_get_dimm_phys_location(struct pdc_pat_mem_phys_mem_location *pret, unsigned long phys_addr)

    Get physical DIMM slot via PAT firmware

    :param struct pdc_pat_mem_phys_mem_location \*pret:
        ptr to hold returned information

    :param unsigned long phys_addr:
        physical address to examine

.. This file was automatic generated / don't edit.

