.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/edac/i7300_edac.c

.. _`get_err_from_table`:

get_err_from_table
==================

.. c:function:: const char *get_err_from_table(const char  *table, int size, int pos)

    Gets the error message from a table

    :param table:
        table name (array of char \*)
    :type table: const char  \*

    :param size:
        number of elements at the table
    :type size: int

    :param pos:
        position of the element to be returned
    :type pos: int

.. _`get_err_from_table.description`:

Description
-----------

This is a small routine that gets the pos-th element of a table. If the
element doesn't exist (or it is empty), it returns "reserved".
Instead of calling it directly, the better is to call via the macro
\ :c:func:`GET_ERR_FROM_TABLE`\ , that automatically checks the table size via
\ :c:func:`ARRAY_SIZE`\  macro

.. _`i7300_process_error_global`:

i7300_process_error_global
==========================

.. c:function:: void i7300_process_error_global(struct mem_ctl_info *mci)

    Retrieve the hardware error information from the hardware global error registers and sends it to dmesg

    :param mci:
        struct mem_ctl_info pointer
    :type mci: struct mem_ctl_info \*

.. _`i7300_process_fbd_error`:

i7300_process_fbd_error
=======================

.. c:function:: void i7300_process_fbd_error(struct mem_ctl_info *mci)

    Retrieve the hardware error information from the FBD error registers and sends it via EDAC error API calls

    :param mci:
        struct mem_ctl_info pointer
    :type mci: struct mem_ctl_info \*

.. _`i7300_check_error`:

i7300_check_error
=================

.. c:function:: void i7300_check_error(struct mem_ctl_info *mci)

    Calls the error checking subroutines

    :param mci:
        struct mem_ctl_info pointer
    :type mci: struct mem_ctl_info \*

.. _`i7300_clear_error`:

i7300_clear_error
=================

.. c:function:: void i7300_clear_error(struct mem_ctl_info *mci)

    Clears the error registers

    :param mci:
        struct mem_ctl_info pointer
    :type mci: struct mem_ctl_info \*

.. _`i7300_enable_error_reporting`:

i7300_enable_error_reporting
============================

.. c:function:: void i7300_enable_error_reporting(struct mem_ctl_info *mci)

    Enable the memory reporting logic at the hardware

    :param mci:
        struct mem_ctl_info pointer
    :type mci: struct mem_ctl_info \*

.. _`decode_mtr`:

decode_mtr
==========

.. c:function:: int decode_mtr(struct i7300_pvt *pvt, int slot, int ch, int branch, struct i7300_dimm_info *dinfo, struct dimm_info *dimm)

    Decodes the MTR descriptor, filling the edac structs

    :param pvt:
        pointer to the private data struct used by i7300 driver
    :type pvt: struct i7300_pvt \*

    :param slot:
        DIMM slot (0 to 7)
    :type slot: int

    :param ch:
        Channel number within the branch (0 or 1)
    :type ch: int

    :param branch:
        Branch number (0 or 1)
    :type branch: int

    :param dinfo:
        Pointer to DIMM info where dimm size is stored
    :type dinfo: struct i7300_dimm_info \*

    :param dimm:
        *undescribed*
    :type dimm: struct dimm_info \*

.. _`print_dimm_size`:

print_dimm_size
===============

.. c:function:: void print_dimm_size(struct i7300_pvt *pvt)

    Prints dump of the memory organization

    :param pvt:
        pointer to the private data struct used by i7300 driver
    :type pvt: struct i7300_pvt \*

.. _`print_dimm_size.description`:

Description
-----------

Useful for debug. If debug is disabled, this routine do nothing

.. _`i7300_init_csrows`:

i7300_init_csrows
=================

.. c:function:: int i7300_init_csrows(struct mem_ctl_info *mci)

    Initialize the 'csrows' table within the mci control structure with the addressing of memory.

    :param mci:
        struct mem_ctl_info pointer
    :type mci: struct mem_ctl_info \*

.. _`decode_mir`:

decode_mir
==========

.. c:function:: void decode_mir(int mir_no, u16 mir)

    Decodes Memory Interleave Register (MIR) info

    :param mir_no:
        *undescribed*
    :type mir_no: int

    :param mir:
        array with the MIR data cached on the driver
    :type mir: u16

.. _`i7300_get_mc_regs`:

i7300_get_mc_regs
=================

.. c:function:: int i7300_get_mc_regs(struct mem_ctl_info *mci)

    Get the contents of the MC enumeration registers

    :param mci:
        struct mem_ctl_info pointer
    :type mci: struct mem_ctl_info \*

.. _`i7300_get_mc_regs.description`:

Description
-----------

Data read is cached internally for its usage when needed

.. _`i7300_put_devices`:

i7300_put_devices
=================

.. c:function:: void i7300_put_devices(struct mem_ctl_info *mci)

    Release the PCI devices

    :param mci:
        struct mem_ctl_info pointer
    :type mci: struct mem_ctl_info \*

.. _`i7300_get_devices`:

i7300_get_devices
=================

.. c:function:: int i7300_get_devices(struct mem_ctl_info *mci)

    Find and perform 'get' operation on the MCH's device/functions we want to reference for this driver

    :param mci:
        struct mem_ctl_info pointer
    :type mci: struct mem_ctl_info \*

.. _`i7300_get_devices.i7300-devices-used-by-this-driver`:

I7300 devices used by this driver
---------------------------------

Device 16, functions 0,1 and 2:   PCI_DEVICE_ID_INTEL_I7300_MCH_ERR

.. _`i7300_get_devices.device-21-function-0`:

Device 21 function 0
--------------------

PCI_DEVICE_ID_INTEL_I7300_MCH_FB0

.. _`i7300_get_devices.device-22-function-0`:

Device 22 function 0
--------------------

PCI_DEVICE_ID_INTEL_I7300_MCH_FB1

.. _`i7300_init_one`:

i7300_init_one
==============

.. c:function:: int i7300_init_one(struct pci_dev *pdev, const struct pci_device_id *id)

    Probe for one instance of the device

    :param pdev:
        struct pci_dev pointer
    :type pdev: struct pci_dev \*

    :param id:
        struct pci_device_id pointer - currently unused
    :type id: const struct pci_device_id \*

.. _`i7300_remove_one`:

i7300_remove_one
================

.. c:function:: void i7300_remove_one(struct pci_dev *pdev)

    Remove the driver

    :param pdev:
        struct pci_dev pointer
    :type pdev: struct pci_dev \*

.. _`i7300_init`:

i7300_init
==========

.. c:function:: int i7300_init( void)

    Registers the driver

    :param void:
        no arguments
    :type void: 

.. _`i7300_exit`:

i7300_exit
==========

.. c:function:: void __exit i7300_exit( void)

    Unregisters the driver

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

