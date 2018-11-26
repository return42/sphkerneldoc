.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/include/asm/fsl_hcalls.h

.. _`fh_send_nmi`:

fh_send_nmi
===========

.. c:function:: unsigned int fh_send_nmi(unsigned int vcpu_mask)

    send NMI to virtual cpu(s).

    :param vcpu_mask:
        send NMI to virtual cpu(s) specified by this mask.
    :type vcpu_mask: unsigned int

.. _`fh_send_nmi.description`:

Description
-----------

Returns 0 for success, or EINVAL for invalid vcpu_mask.

.. _`fh_partition_get_dtprop`:

fh_partition_get_dtprop
=======================

.. c:function:: unsigned int fh_partition_get_dtprop(int handle, uint64_t dtpath_addr, uint64_t propname_addr, uint64_t propvalue_addr, uint32_t *propvalue_len)

    get a property from a guest device tree.

    :param handle:
        handle of partition whose device tree is to be accessed
    :type handle: int

    :param dtpath_addr:
        physical address of device tree path to access
    :type dtpath_addr: uint64_t

    :param propname_addr:
        physical address of name of property
    :type propname_addr: uint64_t

    :param propvalue_addr:
        physical address of property value buffer
    :type propvalue_addr: uint64_t

    :param propvalue_len:
        length of buffer on entry, length of property on return
    :type propvalue_len: uint32_t \*

.. _`fh_partition_get_dtprop.description`:

Description
-----------

Returns zero on success, non-zero on error.

.. _`fh_partition_set_dtprop`:

fh_partition_set_dtprop
=======================

.. c:function:: unsigned int fh_partition_set_dtprop(int handle, uint64_t dtpath_addr, uint64_t propname_addr, uint64_t propvalue_addr, uint32_t propvalue_len)

    :param handle:
        handle of partition whose device tree is to be accessed
    :type handle: int

    :param dtpath_addr:
        physical address of device tree path to access
    :type dtpath_addr: uint64_t

    :param propname_addr:
        physical address of name of property
    :type propname_addr: uint64_t

    :param propvalue_addr:
        physical address of property value
    :type propvalue_addr: uint64_t

    :param propvalue_len:
        length of property
    :type propvalue_len: uint32_t

.. _`fh_partition_set_dtprop.description`:

Description
-----------

Returns zero on success, non-zero on error.

.. _`fh_partition_restart`:

fh_partition_restart
====================

.. c:function:: unsigned int fh_partition_restart(unsigned int partition)

    reboot the current partition

    :param partition:
        partition ID
    :type partition: unsigned int

.. _`fh_partition_restart.description`:

Description
-----------

Returns an error code if reboot failed.  Does not return if it succeeds.

.. _`fh_partition_get_status`:

fh_partition_get_status
=======================

.. c:function:: unsigned int fh_partition_get_status(unsigned int partition, unsigned int *status)

    gets the status of a partition

    :param partition:
        partition ID
    :type partition: unsigned int

    :param status:
        returned status code
    :type status: unsigned int \*

.. _`fh_partition_get_status.description`:

Description
-----------

Returns 0 for success, or an error code.

.. _`fh_partition_start`:

fh_partition_start
==================

.. c:function:: unsigned int fh_partition_start(unsigned int partition, uint32_t entry_point, int load)

    boots and starts execution of the specified partition

    :param partition:
        partition ID
    :type partition: unsigned int

    :param entry_point:
        guest physical address to start execution
    :type entry_point: uint32_t

    :param load:
        *undescribed*
    :type load: int

.. _`fh_partition_start.description`:

Description
-----------

The hypervisor creates a 1-to-1 virtual/physical IMA mapping, so at boot
time, guest physical address are the same as guest virtual addresses.

Returns 0 for success, or an error code.

.. _`fh_partition_stop`:

fh_partition_stop
=================

.. c:function:: unsigned int fh_partition_stop(unsigned int partition)

    stops another partition

    :param partition:
        partition ID
    :type partition: unsigned int

.. _`fh_partition_stop.description`:

Description
-----------

Returns 0 for success, or an error code.

.. _`fh_sg_list`:

struct fh_sg_list
=================

.. c:type:: struct fh_sg_list

    definition of the fh_partition_memcpy S/G list

.. _`fh_sg_list.definition`:

Definition
----------

.. code-block:: c

    struct fh_sg_list {
        uint64_t source;
        uint64_t target;
        uint64_t size;
        uint64_t reserved;
    }

.. _`fh_sg_list.members`:

Members
-------

source
    guest physical address to copy from

target
    guest physical address to copy to

size
    number of bytes to copy

reserved
    reserved, must be zero

.. _`fh_sg_list.description`:

Description
-----------

The scatter/gather list for \ :c:func:`fh_partition_memcpy`\  is an array of these
structures.  The array must be guest physically contiguous.

This structure must be aligned on 32-byte boundary, so that no single
strucuture can span two pages.

.. _`fh_partition_memcpy`:

fh_partition_memcpy
===================

.. c:function:: unsigned int fh_partition_memcpy(unsigned int source, unsigned int target, phys_addr_t sg_list, unsigned int count)

    copies data from one guest to another

    :param source:
        the ID of the partition to copy from
    :type source: unsigned int

    :param target:
        the ID of the partition to copy to
    :type target: unsigned int

    :param sg_list:
        guest physical address of an array of \ :c:type:`struct fh_sg_list <fh_sg_list>`\  structures
    :type sg_list: phys_addr_t

    :param count:
        the number of entries in \ ``sg_list``\ 
    :type count: unsigned int

.. _`fh_partition_memcpy.description`:

Description
-----------

Returns 0 for success, or an error code.

.. _`fh_dma_enable`:

fh_dma_enable
=============

.. c:function:: unsigned int fh_dma_enable(unsigned int liodn)

    enable DMA for the specified device

    :param liodn:
        the LIODN of the I/O device for which to enable DMA
    :type liodn: unsigned int

.. _`fh_dma_enable.description`:

Description
-----------

Returns 0 for success, or an error code.

.. _`fh_dma_disable`:

fh_dma_disable
==============

.. c:function:: unsigned int fh_dma_disable(unsigned int liodn)

    disable DMA for the specified device

    :param liodn:
        the LIODN of the I/O device for which to disable DMA
    :type liodn: unsigned int

.. _`fh_dma_disable.description`:

Description
-----------

Returns 0 for success, or an error code.

.. _`fh_vmpic_get_msir`:

fh_vmpic_get_msir
=================

.. c:function:: unsigned int fh_vmpic_get_msir(unsigned int interrupt, unsigned int *msir_val)

    returns the MPIC-MSI register value

    :param interrupt:
        the interrupt number
    :type interrupt: unsigned int

    :param msir_val:
        returned MPIC-MSI register value
    :type msir_val: unsigned int \*

.. _`fh_vmpic_get_msir.description`:

Description
-----------

Returns 0 for success, or an error code.

.. _`fh_system_reset`:

fh_system_reset
===============

.. c:function:: unsigned int fh_system_reset( void)

    reset the system

    :param void:
        no arguments
    :type void: 

.. _`fh_system_reset.description`:

Description
-----------

Returns 0 for success, or an error code.

.. _`fh_err_get_info`:

fh_err_get_info
===============

.. c:function:: unsigned int fh_err_get_info(int queue, uint32_t *bufsize, uint32_t addr_hi, uint32_t addr_lo, int peek)

    get platform error information

    :param queue:
        0 for guest error event queue
        1 for global error event queue
    :type queue: int

    :param bufsize:
        *undescribed*
    :type bufsize: uint32_t \*

    :param addr_hi:
        *undescribed*
    :type addr_hi: uint32_t

    :param addr_lo:
        *undescribed*
    :type addr_lo: uint32_t

    :param peek:
        *undescribed*
    :type peek: int

.. _`fh_err_get_info.description`:

Description
-----------

Returns 0 for success, or an error code.

.. _`fh_get_core_state`:

fh_get_core_state
=================

.. c:function:: unsigned int fh_get_core_state(unsigned int handle, unsigned int vcpu, unsigned int *state)

    get the state of a vcpu

    :param handle:
        handle of partition containing the vcpu
    :type handle: unsigned int

    :param vcpu:
        vcpu number within the partition
    :type vcpu: unsigned int

    :param state:
        the current state of the vcpu, see FH_VCPU\_\*
    :type state: unsigned int \*

.. _`fh_get_core_state.description`:

Description
-----------

Returns 0 for success, or an error code.

.. _`fh_enter_nap`:

fh_enter_nap
============

.. c:function:: unsigned int fh_enter_nap(unsigned int handle, unsigned int vcpu)

    enter nap on a vcpu

    :param handle:
        handle of partition containing the vcpu
    :type handle: unsigned int

    :param vcpu:
        vcpu number within the partition
    :type vcpu: unsigned int

.. _`fh_enter_nap.description`:

Description
-----------

Note that though the API supports entering nap on a vcpu other
than the caller, this may not be implmented and may return EINVAL.

Returns 0 for success, or an error code.

.. _`fh_exit_nap`:

fh_exit_nap
===========

.. c:function:: unsigned int fh_exit_nap(unsigned int handle, unsigned int vcpu)

    exit nap on a vcpu

    :param handle:
        handle of partition containing the vcpu
    :type handle: unsigned int

    :param vcpu:
        vcpu number within the partition
    :type vcpu: unsigned int

.. _`fh_exit_nap.description`:

Description
-----------

Returns 0 for success, or an error code.

.. _`fh_claim_device`:

fh_claim_device
===============

.. c:function:: unsigned int fh_claim_device(unsigned int handle)

    claim a "claimable" shared device

    :param handle:
        fsl,hv-device-handle of node to claim
    :type handle: unsigned int

.. _`fh_claim_device.description`:

Description
-----------

Returns 0 for success, or an error code.

.. _`fh_partition_stop_dma`:

fh_partition_stop_dma
=====================

.. c:function:: unsigned int fh_partition_stop_dma(unsigned int handle)

    :param handle:
        partition (must be stopped) whose DMA is to be disabled
    :type handle: unsigned int

.. _`fh_partition_stop_dma.description`:

Description
-----------

This applies to devices which a partition owns either privately,
or which are claimable and still actively owned by that partition,
and which do not have the no-dma-disable property.

Returns 0 for success, or an error code.

.. This file was automatic generated / don't edit.

