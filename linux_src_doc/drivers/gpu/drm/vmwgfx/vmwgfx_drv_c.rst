.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/vmwgfx_drv.c

.. _`drm_ioctl_vmw_get_param`:

DRM_IOCTL_VMW_GET_PARAM
=======================

.. c:function::  DRM_IOCTL_VMW_GET_PARAM()

.. _`vmw_ioctl_def`:

VMW_IOCTL_DEF
=============

.. c:function::  VMW_IOCTL_DEF( ioctl,  func,  flags)

    DRM_COMMAND_BASE.

    :param ioctl:
        *undescribed*
    :type ioctl: 

    :param func:
        *undescribed*
    :type func: 

    :param flags:
        *undescribed*
    :type flags: 

.. _`vmw_dummy_query_bo_create`:

vmw_dummy_query_bo_create
=========================

.. c:function:: int vmw_dummy_query_bo_create(struct vmw_private *dev_priv)

    create a bo to hold a dummy query result

    :param dev_priv:
        A device private structure.
    :type dev_priv: struct vmw_private \*

.. _`vmw_dummy_query_bo_create.description`:

Description
-----------

This function creates a small buffer object that holds the query
result for dummy queries emitted as query barriers.
The function will then map the first page and initialize a pending
occlusion query result structure, Finally it will unmap the buffer.
No interruptible waits are done within this function.

Returns an error if bo creation or initialization fails.

.. _`vmw_request_device_late`:

vmw_request_device_late
=======================

.. c:function:: int vmw_request_device_late(struct vmw_private *dev_priv)

    Perform late device setup

    :param dev_priv:
        Pointer to device private.
    :type dev_priv: struct vmw_private \*

.. _`vmw_request_device_late.description`:

Description
-----------

This function performs setup of otables and enables large command
buffer submission. These tasks are split out to a separate function
because it reverts vmw_release_device_early and is intended to be used
by an error path in the hibernation code.

.. _`vmw_release_device_early`:

vmw_release_device_early
========================

.. c:function:: void vmw_release_device_early(struct vmw_private *dev_priv)

    Early part of fifo takedown.

    :param dev_priv:
        Pointer to device private struct.
    :type dev_priv: struct vmw_private \*

.. _`vmw_release_device_early.description`:

Description
-----------

This is the first part of command submission takedown, to be called before
buffer management is taken down.

.. _`vmw_release_device_late`:

vmw_release_device_late
=======================

.. c:function:: void vmw_release_device_late(struct vmw_private *dev_priv)

    Late part of fifo takedown.

    :param dev_priv:
        Pointer to device private struct.
    :type dev_priv: struct vmw_private \*

.. _`vmw_release_device_late.description`:

Description
-----------

This is the last part of the command submission takedown, to be called when
command submission is no longer needed. It may wait on pending fences.

.. _`vmw_get_initial_size`:

vmw_get_initial_size
====================

.. c:function:: void vmw_get_initial_size(struct vmw_private *dev_priv)

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

.. _`vmw_get_initial_size.description`:

Description
-----------

It does so by reading SVGA_REG_[WIDTH\|HEIGHT] regs and then
clamping the value to fb_max_[width\|height] fields and the
VMW_MIN_INITIAL_[WIDTH\|HEIGHT].
If the values appear to be invalid, set them to
VMW_MIN_INITIAL_[WIDTH\|HEIGHT].

.. _`vmw_dma_select_mode`:

vmw_dma_select_mode
===================

.. c:function:: int vmw_dma_select_mode(struct vmw_private *dev_priv)

    Determine how DMA mappings should be set up for this system.

    :param dev_priv:
        Pointer to a struct vmw_private
    :type dev_priv: struct vmw_private \*

.. _`vmw_dma_select_mode.description`:

Description
-----------

This functions tries to determine the IOMMU setup and what actions
need to be taken by the driver to make system pages visible to the
device.
If this function decides that DMA is not possible, it returns -EINVAL.
The driver may then try to disable features of the device that require
DMA.

.. _`vmw_dma_masks`:

vmw_dma_masks
=============

.. c:function:: int vmw_dma_masks(struct vmw_private *dev_priv)

    set required page- and dma masks

    :param dev_priv:
        *undescribed*
    :type dev_priv: struct vmw_private \*

.. _`vmw_dma_masks.description`:

Description
-----------

With 32-bit we can only handle 32 bit PFNs. Optionally set that
restriction also for 64-bit systems.

.. _`__vmw_svga_enable`:

\__vmw_svga_enable
==================

.. c:function:: void __vmw_svga_enable(struct vmw_private *dev_priv)

    Enable SVGA mode, FIFO and use of VRAM.

    :param dev_priv:
        Pointer to device private struct.
        Needs the reservation sem to be held in non-exclusive mode.
    :type dev_priv: struct vmw_private \*

.. _`vmw_svga_enable`:

vmw_svga_enable
===============

.. c:function:: void vmw_svga_enable(struct vmw_private *dev_priv)

    Enable SVGA mode, FIFO and use of VRAM.

    :param dev_priv:
        Pointer to device private struct.
    :type dev_priv: struct vmw_private \*

.. _`__vmw_svga_disable`:

\__vmw_svga_disable
===================

.. c:function:: void __vmw_svga_disable(struct vmw_private *dev_priv)

    Disable SVGA mode and use of VRAM.

    :param dev_priv:
        Pointer to device private struct.
        Needs the reservation sem to be held in exclusive mode.
        Will not empty VRAM. VRAM must be emptied by caller.
    :type dev_priv: struct vmw_private \*

.. _`vmw_svga_disable`:

vmw_svga_disable
================

.. c:function:: void vmw_svga_disable(struct vmw_private *dev_priv)

    Disable SVGA_MODE, and use of VRAM. Keep the fifo running.

    :param dev_priv:
        Pointer to device private struct.
        Will empty VRAM.
    :type dev_priv: struct vmw_private \*

.. This file was automatic generated / don't edit.

