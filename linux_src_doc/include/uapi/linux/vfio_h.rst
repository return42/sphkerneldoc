.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/vfio.h

.. _`vfio_get_api_version`:

VFIO_GET_API_VERSION
====================

.. c:function::  VFIO_GET_API_VERSION()

    _IO(VFIO_TYPE, VFIO_BASE + 0)

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

    _IOW(VFIO_TYPE, VFIO_BASE + 1, \__u32)

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

    _IOW(VFIO_TYPE, VFIO_BASE + 2, \__s32)

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

    _IOW(VFIO_TYPE, VFIO_BASE + 4, \__s32)

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

    _IO(VFIO_TYPE, VFIO_BASE + 5)

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

    _IOW(VFIO_TYPE, VFIO_BASE + 6, char)

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

.. _`vfio_device_reset`:

VFIO_DEVICE_RESET
=================

.. c:function::  VFIO_DEVICE_RESET()

    _IO(VFIO_TYPE, VFIO_BASE + 11)

.. _`vfio_device_reset.description`:

Description
-----------

Reset a device.

.. _`vfio_iommu_spapr_unregister_memory`:

VFIO_IOMMU_SPAPR_UNREGISTER_MEMORY
==================================

.. c:function::  VFIO_IOMMU_SPAPR_UNREGISTER_MEMORY()

    _IOW(VFIO_TYPE, VFIO_BASE + 18, struct vfio_iommu_spapr_register_memory)

.. _`vfio_iommu_spapr_unregister_memory.description`:

Description
-----------

Unregisters user space memory registered with
VFIO_IOMMU_SPAPR_REGISTER_MEMORY.
Uses vfio_iommu_spapr_register_memory for parameters.

.. This file was automatic generated / don't edit.

