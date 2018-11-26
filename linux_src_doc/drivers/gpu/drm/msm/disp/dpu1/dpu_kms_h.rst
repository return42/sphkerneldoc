.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_kms.h

.. _`dpu_debug`:

DPU_DEBUG
=========

.. c:function::  DPU_DEBUG( fmt,  ...)

    macro for kms/plane/crtc/encoder/connector logs

    :param fmt:
        Pointer to format string
    :type fmt: 

    :param ellipsis ellipsis:
        variable arguments

.. _`dpu_debug_driver`:

DPU_DEBUG_DRIVER
================

.. c:function::  DPU_DEBUG_DRIVER( fmt,  ...)

    macro for hardware driver logging

    :param fmt:
        Pointer to format string
    :type fmt: 

    :param ellipsis ellipsis:
        variable arguments

.. _`ktime_compare_safe`:

ktime_compare_safe
==================

.. c:function::  ktime_compare_safe( A,  B)

    compare two ktime structures This macro is similar to the standard \ :c:func:`ktime_compare`\  function, but attempts to also handle ktime overflows.

    :param A:
        First ktime value
    :type A: 

    :param B:
        Second ktime value
    :type B: 

.. _`ktime_compare_safe.return`:

Return
------

-1 if A < B, 0 if A == B, 1 if A > B

.. _`dpu_irq`:

struct dpu_irq
==============

.. c:type:: struct dpu_irq

    IRQ structure contains callback registration info

.. _`dpu_irq.definition`:

Definition
----------

.. code-block:: c

    struct dpu_irq {
        u32 total_irqs;
        struct list_head *irq_cb_tbl;
        atomic_t *enable_counts;
        atomic_t *irq_counts;
        spinlock_t cb_lock;
        struct dentry *debugfs_file;
    }

.. _`dpu_irq.members`:

Members
-------

total_irqs
    *undescribed*

irq_cb_tbl
    array of IRQ callbacks setting
    \ ``enable_counts``\  array of IRQ enable counts

enable_counts
    *undescribed*

irq_counts
    *undescribed*

cb_lock
    callback lock

debugfs_file
    debugfs file for irq statistics

.. _`dpu_kms_is_suspend_state`:

dpu_kms_is_suspend_state
========================

.. c:function:: bool dpu_kms_is_suspend_state(struct drm_device *dev)

    whether or not the system is pm suspended

    :param dev:
        Pointer to drm device
    :type dev: struct drm_device \*

.. _`dpu_kms_is_suspend_state.return`:

Return
------

Suspend status

.. _`dpu_kms_is_suspend_blocked`:

dpu_kms_is_suspend_blocked
==========================

.. c:function:: bool dpu_kms_is_suspend_blocked(struct drm_device *dev)

    whether or not commits are blocked due to pm suspend status

    :param dev:
        Pointer to drm device
    :type dev: struct drm_device \*

.. _`dpu_kms_is_suspend_blocked.return`:

Return
------

True if commits should be rejected due to pm suspend

.. _`dpu_debugfs_setup_regset32`:

dpu_debugfs_setup_regset32
==========================

.. c:function:: void dpu_debugfs_setup_regset32(struct dpu_debugfs_regset32 *regset, uint32_t offset, uint32_t length, struct dpu_kms *dpu_kms)

    Initialize register block definition for debugfs This function is meant to initialize dpu_debugfs_regset32 structures for use with dpu_debugfs_create_regset32.

    :param regset:
        opaque register definition structure
    :type regset: struct dpu_debugfs_regset32 \*

    :param offset:
        sub-block offset
    :type offset: uint32_t

    :param length:
        sub-block length, in bytes
    :type length: uint32_t

    :param dpu_kms:
        pointer to dpu kms structure
    :type dpu_kms: struct dpu_kms \*

.. _`dpu_debugfs_create_regset32`:

dpu_debugfs_create_regset32
===========================

.. c:function:: void *dpu_debugfs_create_regset32(const char *name, umode_t mode, void *parent, struct dpu_debugfs_regset32 *regset)

    Create register read back file for debugfs

    :param name:
        File name within debugfs
    :type name: const char \*

    :param mode:
        File mode within debugfs
    :type mode: umode_t

    :param parent:
        Parent directory entry within debugfs, can be NULL
    :type parent: void \*

    :param regset:
        Pointer to persistent register block definition
    :type regset: struct dpu_debugfs_regset32 \*

.. _`dpu_debugfs_create_regset32.description`:

Description
-----------

This function is almost identical to the standard \ :c:func:`debugfs_create_regset32`\ 
function, with the main difference being that a list of register
names/offsets do not need to be provided. The 'read' function simply outputs
sequential register values over a specified range.

Similar to the related debugfs_create_regset32 API, the structure pointed to
by regset needs to persist for the lifetime of the created file. The calling
code is responsible for initialization/management of this structure.

The structure pointed to by regset is meant to be opaque. Please use
dpu_debugfs_setup_regset32 to initialize it.

.. _`dpu_debugfs_create_regset32.return`:

Return
------

dentry pointer for newly created file, use either \ :c:func:`debugfs_remove`\ 
or \ :c:func:`debugfs_remove_recursive`\  (on a parent directory) to remove the
file

.. _`dpu_debugfs_get_root`:

dpu_debugfs_get_root
====================

.. c:function:: void *dpu_debugfs_get_root(struct dpu_kms *dpu_kms)

    Return root directory entry for KMS's debugfs

    :param dpu_kms:
        Pointer to DPU's KMS structure
    :type dpu_kms: struct dpu_kms \*

.. _`dpu_debugfs_get_root.description`:

Description
-----------

The return value should be passed as the 'parent' argument to subsequent
debugfs create calls.

.. _`dpu_debugfs_get_root.return`:

Return
------

dentry pointer for DPU's debugfs location

.. _`dpu_kms_info_max_size`:

DPU_KMS_INFO_MAX_SIZE
=====================

.. c:function::  DPU_KMS_INFO_MAX_SIZE()

    These functions/definitions allow for building up a 'dpu_info' structure containing one or more "key=value\n" entries.

.. _`dpu_enable_vblank`:

dpu_enable_vblank
=================

.. c:function:: int dpu_enable_vblank(struct msm_kms *kms, struct drm_crtc *crtc)

    :param kms:
        *undescribed*
    :type kms: struct msm_kms \*

    :param crtc:
        *undescribed*
    :type crtc: struct drm_crtc \*

.. _`dpu_kms_get_clk_rate`:

dpu_kms_get_clk_rate
====================

.. c:function:: u64 dpu_kms_get_clk_rate(struct dpu_kms *dpu_kms, char *clock_name)

    get the clock rate

    :param dpu_kms:
        poiner to dpu_kms structure
    :type dpu_kms: struct dpu_kms \*

    :param clock_name:
        clock name to get the rate
    :type clock_name: char \*

.. _`dpu_kms_get_clk_rate.return`:

Return
------

current clock rate

.. This file was automatic generated / don't edit.

