.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/vfio.h

.. _`vfio_get_api_version`:

VFIO_GET_API_VERSION
====================

.. c:function::  VFIO_GET_API_VERSION()

    \_IO(VFIO_TYPE, VFIO_BASE + 0)

.. _`vfio_get_api_version.description`:

Description
-----------

Report the version of the VFIO API.  This allows us to bump the entire
API version should we later need to add or change features in incompatible
ways.

.. _`vfio_get_api_version.return`:

Return
------

VFIO_API_VERSION

.. _`vfio_get_api_version.availability`:

Availability
------------

Always

.. _`vfio_check_extension`:

VFIO_CHECK_EXTENSION
====================

.. c:function::  VFIO_CHECK_EXTENSION()

    \_IOW(VFIO_TYPE, VFIO_BASE + 1, \__u32)

.. _`vfio_check_extension.description`:

Description
-----------

Check whether an extension is supported.

.. _`vfio_check_extension.return`:

Return
------

0 if not supported, 1 (or some other positive integer) if supported.

.. _`vfio_check_extension.availability`:

Availability
------------

Always

.. _`vfio_set_iommu`:

VFIO_SET_IOMMU
==============

.. c:function::  VFIO_SET_IOMMU()

    \_IOW(VFIO_TYPE, VFIO_BASE + 2, \__s32)

.. _`vfio_set_iommu.description`:

Description
-----------

Set the iommu to the given type.  The type must be supported by an
iommu driver as verified by calling CHECK_EXTENSION using the same
type.  A group must be set to this file descriptor before this
ioctl is available.  The IOMMU interfaces enabled by this call are
specific to the value set.

.. _`vfio_set_iommu.return`:

Return
------

0 on success, -errno on failure

.. _`vfio_set_iommu.availability`:

Availability
------------

When VFIO group attached

.. _`vfio_group_set_container`:

VFIO_GROUP_SET_CONTAINER
========================

.. c:function::  VFIO_GROUP_SET_CONTAINER()

    \_IOW(VFIO_TYPE, VFIO_BASE + 4, \__s32)

.. _`vfio_group_set_container.description`:

Description
-----------

Set the container for the VFIO group to the open VFIO file
descriptor provided.  Groups may only belong to a single
container.  Containers may, at their discretion, support multiple
groups.  Only when a container is set are all of the interfaces
of the VFIO file descriptor and the VFIO group file descriptor
available to the user.

.. _`vfio_group_set_container.return`:

Return
------

0 on success, -errno on failure.

.. _`vfio_group_set_container.availability`:

Availability
------------

Always

.. _`vfio_group_unset_container`:

VFIO_GROUP_UNSET_CONTAINER
==========================

.. c:function::  VFIO_GROUP_UNSET_CONTAINER()

    \_IO(VFIO_TYPE, VFIO_BASE + 5)

.. _`vfio_group_unset_container.description`:

Description
-----------

Remove the group from the attached container.  This is the
opposite of the SET_CONTAINER call and returns the group to
an initial state.  All device file descriptors must be released
prior to calling this interface.  When removing the last group
from a container, the IOMMU will be disabled and all state lost,
effectively also returning the VFIO file descriptor to an initial
state.

.. _`vfio_group_unset_container.return`:

Return
------

0 on success, -errno on failure.

.. _`vfio_group_unset_container.availability`:

Availability
------------

When attached to container

.. _`vfio_group_get_device_fd`:

VFIO_GROUP_GET_DEVICE_FD
========================

.. c:function::  VFIO_GROUP_GET_DEVICE_FD()

    \_IOW(VFIO_TYPE, VFIO_BASE + 6, char)

.. _`vfio_group_get_device_fd.description`:

Description
-----------

Return a new file descriptor for the device object described by
the provided string.  The string should match a device listed in
the devices subdirectory of the IOMMU group sysfs entry.  The
group containing the device must already be added to this context.

.. _`vfio_group_get_device_fd.return`:

Return
------

new file descriptor on success, -errno on failure.

.. _`vfio_group_get_device_fd.availability`:

Availability
------------

When attached to container

.. _`vfio_region_gfx_edid`:

struct vfio_region_gfx_edid
===========================

.. c:type:: struct vfio_region_gfx_edid

    EDID region layout.

.. _`vfio_region_gfx_edid.definition`:

Definition
----------

.. code-block:: c

    struct vfio_region_gfx_edid {
        __u32 edid_offset;
        __u32 edid_max_size;
        __u32 edid_size;
        __u32 max_xres;
        __u32 max_yres;
        __u32 link_state;
    #define VFIO_DEVICE_GFX_LINK_STATE_UP 1
    #define VFIO_DEVICE_GFX_LINK_STATE_DOWN 2
    }

.. _`vfio_region_gfx_edid.members`:

Members
-------

edid_offset
    location of the edid blob, relative to the
    start of the region (readonly).

edid_max_size
    max size of the edid blob (readonly).

edid_size
    actual edid size (read/write).

max_xres
    max display width (0 == no limitation, readonly).

max_yres
    max display height (0 == no limitation, readonly).

link_state
    display link state (read/write).

.. _`vfio_region_gfx_edid.description`:

Description
-----------

Set display link state and EDID blob.

The EDID blob has monitor information such as brand, name, serial
number, physical size, supported video modes and more.

This special region allows userspace (typically qemu) set a virtual
EDID for the virtual monitor, which allows a flexible display
configuration.

.. _`vfio_region_gfx_edid.for-the-edid-blob-spec-look-here`:

For the edid blob spec look here
--------------------------------

https://en.wikipedia.org/wiki/Extended_Display_Identification_Data

.. _`vfio_region_gfx_edid.on-linux-systems-you-can-find-the-edid-blob-in-sysfs`:

On linux systems you can find the EDID blob in sysfs
----------------------------------------------------

/sys/class/drm/${card}/${connector}/edid

You can use the edid-decode ulility (comes with xorg-x11-utils) to
decode the EDID blob.

.. _`vfio_region_gfx_edid.vfio_device_gfx_link_state_up`:

VFIO_DEVICE_GFX_LINK_STATE_UP
-----------------------------

Monitor is turned on.

.. _`vfio_region_gfx_edid.vfio_device_gfx_link_state_down`:

VFIO_DEVICE_GFX_LINK_STATE_DOWN
-------------------------------

Monitor is turned off.

.. _`vfio_region_gfx_edid.edid-update-protocol`:

EDID update protocol
--------------------

(1) set link-state to down.
(2) update edid blob and size.
(3) set link-state to up.

.. _`vfio_device_reset`:

VFIO_DEVICE_RESET
=================

.. c:function::  VFIO_DEVICE_RESET()

    \_IO(VFIO_TYPE, VFIO_BASE + 11)

.. _`vfio_device_reset.description`:

Description
-----------

Reset a device.

.. _`vfio_device_get_gfx_dmabuf`:

VFIO_DEVICE_GET_GFX_DMABUF
==========================

.. c:function::  VFIO_DEVICE_GET_GFX_DMABUF()

    \_IOW(VFIO_TYPE, VFIO_BASE + 15, \__u32)

.. _`vfio_device_get_gfx_dmabuf.description`:

Description
-----------

Return a new dma-buf file descriptor for an exposed guest framebuffer
described by the provided dmabuf_id. The dmabuf_id is returned from VFIO_
DEVICE_QUERY_GFX_PLANE as a token of the exposed guest framebuffer.

.. _`vfio_iommu_spapr_unregister_memory`:

VFIO_IOMMU_SPAPR_UNREGISTER_MEMORY
==================================

.. c:function::  VFIO_IOMMU_SPAPR_UNREGISTER_MEMORY()

    \_IOW(VFIO_TYPE, VFIO_BASE + 18, struct vfio_iommu_spapr_register_memory)

.. _`vfio_iommu_spapr_unregister_memory.description`:

Description
-----------

Unregisters user space memory registered with
VFIO_IOMMU_SPAPR_REGISTER_MEMORY.
Uses vfio_iommu_spapr_register_memory for parameters.

.. This file was automatic generated / don't edit.

