.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ps3/ps3-lpm.c

.. _`ps3_lpm_shadow_regs`:

struct ps3_lpm_shadow_regs
==========================

.. c:type:: struct ps3_lpm_shadow_regs

    Performance monitor shadow registers.

.. _`ps3_lpm_shadow_regs.definition`:

Definition
----------

.. code-block:: c

    struct ps3_lpm_shadow_regs {
        u64 pm_control;
        u64 pm_start_stop;
        u64 group_control;
        u64 debug_bus_control;
    }

.. _`ps3_lpm_shadow_regs.members`:

Members
-------

pm_control
    Shadow of the processor's pm_control register.

pm_start_stop
    Shadow of the processor's pm_start_stop register.

group_control
    Shadow of the processor's group_control register.

debug_bus_control
    Shadow of the processor's debug_bus_control register.

.. _`ps3_lpm_shadow_regs.description`:

Description
-----------

The logical performance monitor provides a write-only interface to
these processor registers.  These shadow variables cache the processor
register values for reading.

The initial value of the shadow registers at lpm creation is
PS3_LPM_SHADOW_REG_INIT.

.. _`ps3_lpm_priv`:

struct ps3_lpm_priv
===================

.. c:type:: struct ps3_lpm_priv

    Private lpm device data.

.. _`ps3_lpm_priv.definition`:

Definition
----------

.. code-block:: c

    struct ps3_lpm_priv {
        atomic_t open;
        u64 rights;
        u64 node_id;
        u64 pu_id;
        u64 lpm_id;
        u64 outlet_id;
        u64 tb_count;
        void *tb_cache;
        u64 tb_cache_size;
        void *tb_cache_internal;
        struct ps3_lpm_shadow_regs shadow;
        struct ps3_system_bus_device *sbd;
    }

.. _`ps3_lpm_priv.members`:

Members
-------

open
    An atomic variable indicating the lpm driver has been opened.

rights
    The lpm rigths granted by the system policy module.  A logical
    OR of enum ps3_lpm_rights.

node_id
    The node id of a BE processor whose performance monitor this
    lpar has the right to use.

pu_id
    The lv1 id of the logical PU.

lpm_id
    The lv1 id of this lpm instance.

outlet_id
    The outlet created by lv1 for this lpm instance.

tb_count
    The number of bytes of data held in the lv1 trace buffer.

tb_cache
    Kernel buffer to receive the data from the lv1 trace buffer.
    Must be 128 byte aligned.

tb_cache_size
    Size of the kernel \ ``tb_cache``\  buffer.  Must be 128 byte
    aligned.

tb_cache_internal
    An unaligned buffer allocated by this driver to be
    used for the trace buffer cache when \ :c:func:`ps3_lpm_open`\  is called with a
    NULL tb_cache argument.  Otherwise unused.

shadow
    Processor register shadow of type struct ps3_lpm_shadow_regs.

sbd
    The struct ps3_system_bus_device attached to this driver.

.. _`ps3_lpm_priv.description`:

Description
-----------

The trace buffer is a buffer allocated and used internally to the lv1
hypervisor to collect trace data.  The trace buffer cache is a guest
buffer that accepts the trace data from the trace buffer.

.. _`ps3_read_phys_ctr`:

ps3_read_phys_ctr
=================

.. c:function:: u32 ps3_read_phys_ctr(u32 cpu, u32 phys_ctr)

    Read physical counter registers.

    :param cpu:
        *undescribed*
    :type cpu: u32

    :param phys_ctr:
        *undescribed*
    :type phys_ctr: u32

.. _`ps3_read_phys_ctr.description`:

Description
-----------

Each physical counter can act as one 32 bit counter or as two 16 bit
counters.

.. _`ps3_write_phys_ctr`:

ps3_write_phys_ctr
==================

.. c:function:: void ps3_write_phys_ctr(u32 cpu, u32 phys_ctr, u32 val)

    Write physical counter registers.

    :param cpu:
        *undescribed*
    :type cpu: u32

    :param phys_ctr:
        *undescribed*
    :type phys_ctr: u32

    :param val:
        *undescribed*
    :type val: u32

.. _`ps3_write_phys_ctr.description`:

Description
-----------

Each physical counter can act as one 32 bit counter or as two 16 bit
counters.

.. _`ps3_read_ctr`:

ps3_read_ctr
============

.. c:function:: u32 ps3_read_ctr(u32 cpu, u32 ctr)

    Read counter.

    :param cpu:
        *undescribed*
    :type cpu: u32

    :param ctr:
        *undescribed*
    :type ctr: u32

.. _`ps3_read_ctr.description`:

Description
-----------

Read 16 or 32 bits depending on the current size of the counter.
Counters 4, 5, 6 & 7 are always 16 bit.

.. _`ps3_write_ctr`:

ps3_write_ctr
=============

.. c:function:: void ps3_write_ctr(u32 cpu, u32 ctr, u32 val)

    Write counter.

    :param cpu:
        *undescribed*
    :type cpu: u32

    :param ctr:
        *undescribed*
    :type ctr: u32

    :param val:
        *undescribed*
    :type val: u32

.. _`ps3_write_ctr.description`:

Description
-----------

Write 16 or 32 bits depending on the current size of the counter.
Counters 4, 5, 6 & 7 are always 16 bit.

.. _`ps3_read_pm07_control`:

ps3_read_pm07_control
=====================

.. c:function:: u32 ps3_read_pm07_control(u32 cpu, u32 ctr)

    Read counter control registers.

    :param cpu:
        *undescribed*
    :type cpu: u32

    :param ctr:
        *undescribed*
    :type ctr: u32

.. _`ps3_read_pm07_control.description`:

Description
-----------

Each logical counter has a corresponding control register.

.. _`ps3_write_pm07_control`:

ps3_write_pm07_control
======================

.. c:function:: void ps3_write_pm07_control(u32 cpu, u32 ctr, u32 val)

    Write counter control registers.

    :param cpu:
        *undescribed*
    :type cpu: u32

    :param ctr:
        *undescribed*
    :type ctr: u32

    :param val:
        *undescribed*
    :type val: u32

.. _`ps3_write_pm07_control.description`:

Description
-----------

Each logical counter has a corresponding control register.

.. _`ps3_read_pm`:

ps3_read_pm
===========

.. c:function:: u32 ps3_read_pm(u32 cpu, enum pm_reg_name reg)

    Read Other LPM control registers.

    :param cpu:
        *undescribed*
    :type cpu: u32

    :param reg:
        *undescribed*
    :type reg: enum pm_reg_name

.. _`ps3_write_pm`:

ps3_write_pm
============

.. c:function:: void ps3_write_pm(u32 cpu, enum pm_reg_name reg, u32 val)

    Write Other LPM control registers.

    :param cpu:
        *undescribed*
    :type cpu: u32

    :param reg:
        *undescribed*
    :type reg: enum pm_reg_name

    :param val:
        *undescribed*
    :type val: u32

.. _`ps3_get_ctr_size`:

ps3_get_ctr_size
================

.. c:function:: u32 ps3_get_ctr_size(u32 cpu, u32 phys_ctr)

    Get the size of a physical counter.

    :param cpu:
        *undescribed*
    :type cpu: u32

    :param phys_ctr:
        *undescribed*
    :type phys_ctr: u32

.. _`ps3_get_ctr_size.description`:

Description
-----------

Returns either 16 or 32.

.. _`ps3_set_ctr_size`:

ps3_set_ctr_size
================

.. c:function:: void ps3_set_ctr_size(u32 cpu, u32 phys_ctr, u32 ctr_size)

    Set the size of a physical counter to 16 or 32 bits.

    :param cpu:
        *undescribed*
    :type cpu: u32

    :param phys_ctr:
        *undescribed*
    :type phys_ctr: u32

    :param ctr_size:
        *undescribed*
    :type ctr_size: u32

.. _`ps3_enable_pm`:

ps3_enable_pm
=============

.. c:function:: void ps3_enable_pm(u32 cpu)

    Enable the entire performance monitoring unit.

    :param cpu:
        *undescribed*
    :type cpu: u32

.. _`ps3_enable_pm.description`:

Description
-----------

When we enable the LPM, all pending writes to counters get committed.

.. _`ps3_disable_pm`:

ps3_disable_pm
==============

.. c:function:: void ps3_disable_pm(u32 cpu)

    Disable the entire performance monitoring unit.

    :param cpu:
        *undescribed*
    :type cpu: u32

.. _`ps3_lpm_copy_tb`:

ps3_lpm_copy_tb
===============

.. c:function:: int ps3_lpm_copy_tb(unsigned long offset, void *buf, unsigned long count, unsigned long *bytes_copied)

    Copy data from the trace buffer to a kernel buffer.

    :param offset:
        Offset in bytes from the start of the trace buffer.
    :type offset: unsigned long

    :param buf:
        Copy destination.
    :type buf: void \*

    :param count:
        Maximum count of bytes to copy.
    :type count: unsigned long

    :param bytes_copied:
        Pointer to a variable that will receive the number of
        bytes copied to \ ``buf``\ .
    :type bytes_copied: unsigned long \*

.. _`ps3_lpm_copy_tb.description`:

Description
-----------

On error \ ``buf``\  will contain any successfully copied trace buffer data
and bytes_copied will be set to the number of bytes successfully copied.

.. _`ps3_lpm_copy_tb_to_user`:

ps3_lpm_copy_tb_to_user
=======================

.. c:function:: int ps3_lpm_copy_tb_to_user(unsigned long offset, void __user *buf, unsigned long count, unsigned long *bytes_copied)

    Copy data from the trace buffer to a user buffer.

    :param offset:
        Offset in bytes from the start of the trace buffer.
    :type offset: unsigned long

    :param buf:
        A \__user copy destination.
    :type buf: void __user \*

    :param count:
        Maximum count of bytes to copy.
    :type count: unsigned long

    :param bytes_copied:
        Pointer to a variable that will receive the number of
        bytes copied to \ ``buf``\ .
    :type bytes_copied: unsigned long \*

.. _`ps3_lpm_copy_tb_to_user.description`:

Description
-----------

On error \ ``buf``\  will contain any successfully copied trace buffer data
and bytes_copied will be set to the number of bytes successfully copied.

.. _`ps3_get_and_clear_pm_interrupts`:

ps3_get_and_clear_pm_interrupts
===============================

.. c:function:: u32 ps3_get_and_clear_pm_interrupts(u32 cpu)

    :param cpu:
        *undescribed*
    :type cpu: u32

.. _`ps3_get_and_clear_pm_interrupts.description`:

Description
-----------

Clearing interrupts for the entire performance monitoring unit.
Reading pm_status clears the interrupt bits.

.. _`ps3_enable_pm_interrupts`:

ps3_enable_pm_interrupts
========================

.. c:function:: void ps3_enable_pm_interrupts(u32 cpu, u32 thread, u32 mask)

    :param cpu:
        *undescribed*
    :type cpu: u32

    :param thread:
        *undescribed*
    :type thread: u32

    :param mask:
        *undescribed*
    :type mask: u32

.. _`ps3_enable_pm_interrupts.description`:

Description
-----------

Enabling interrupts for the entire performance monitoring unit.
Enables the interrupt bits in the pm_status register.

.. _`ps3_disable_pm_interrupts`:

ps3_disable_pm_interrupts
=========================

.. c:function:: void ps3_disable_pm_interrupts(u32 cpu)

    :param cpu:
        *undescribed*
    :type cpu: u32

.. _`ps3_disable_pm_interrupts.description`:

Description
-----------

Disabling interrupts for the entire performance monitoring unit.

.. _`ps3_lpm_open`:

ps3_lpm_open
============

.. c:function:: int ps3_lpm_open(enum ps3_lpm_tb_type tb_type, void *tb_cache, u64 tb_cache_size)

    Open the logical performance monitor device.

    :param tb_type:
        Specifies the type of trace buffer lv1 should use for this lpm
        instance, specified by one of enum ps3_lpm_tb_type.
    :type tb_type: enum ps3_lpm_tb_type

    :param tb_cache:
        Optional user supplied buffer to use as the trace buffer cache.
        If NULL, the driver will allocate and manage an internal buffer.
        Unused when when \ ``tb_type``\  is PS3_LPM_TB_TYPE_NONE.
    :type tb_cache: void \*

    :param tb_cache_size:
        The size in bytes of the user supplied \ ``tb_cache``\  buffer.
        Unused when \ ``tb_cache``\  is NULL or \ ``tb_type``\  is PS3_LPM_TB_TYPE_NONE.
    :type tb_cache_size: u64

.. _`ps3_lpm_close`:

ps3_lpm_close
=============

.. c:function:: int ps3_lpm_close( void)

    Close the lpm device.

    :param void:
        no arguments
    :type void: 

.. This file was automatic generated / don't edit.

