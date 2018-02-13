.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/virt/vboxguest/vmmdev.h

.. _`vmmdev_mouse_status`:

struct vmmdev_mouse_status
==========================

.. c:type:: struct vmmdev_mouse_status

    Mouse status request structure.

.. _`vmmdev_mouse_status.definition`:

Definition
----------

.. code-block:: c

    struct vmmdev_mouse_status {
        struct vmmdev_request_header header;
        u32 mouse_features;
        s32 pointer_pos_x;
        s32 pointer_pos_y;
    }

.. _`vmmdev_mouse_status.members`:

Members
-------

header
    *undescribed*

mouse_features
    *undescribed*

pointer_pos_x
    *undescribed*

pointer_pos_y
    *undescribed*

.. _`vmmdev_mouse_status.description`:

Description
-----------

Used by VMMDEVREQ_GET_MOUSE_STATUS and VMMDEVREQ_SET_MOUSE_STATUS.

.. _`vmmdev_host_version`:

struct vmmdev_host_version
==========================

.. c:type:: struct vmmdev_host_version

    VirtualBox host version request structure.

.. _`vmmdev_host_version.definition`:

Definition
----------

.. code-block:: c

    struct vmmdev_host_version {
        struct vmmdev_request_header header;
        u16 major;
        u16 minor;
        u32 build;
        u32 revision;
        u32 features;
    }

.. _`vmmdev_host_version.members`:

Members
-------

header
    *undescribed*

major
    *undescribed*

minor
    *undescribed*

build
    *undescribed*

revision
    *undescribed*

features
    *undescribed*

.. _`vmmdev_host_version.description`:

Description
-----------

VBG uses this to detect the precense of new features in the interface.

.. _`vmmdev_mask`:

struct vmmdev_mask
==================

.. c:type:: struct vmmdev_mask

    Structure to set / clear bits in a mask used for VMMDEVREQ_SET_GUEST_CAPABILITIES and VMMDEVREQ_CTL_GUEST_FILTER_MASK.

.. _`vmmdev_mask.definition`:

Definition
----------

.. code-block:: c

    struct vmmdev_mask {
        struct vmmdev_request_header header;
        u32 or_mask;
        u32 not_mask;
    }

.. _`vmmdev_mask.members`:

Members
-------

header
    *undescribed*

or_mask
    *undescribed*

not_mask
    *undescribed*

.. _`vmmdev_hgcm_cancel2`:

struct vmmdev_hgcm_cancel2
==========================

.. c:type:: struct vmmdev_hgcm_cancel2

    HGCM cancel request structure, version 2.

.. _`vmmdev_hgcm_cancel2.definition`:

Definition
----------

.. code-block:: c

    struct vmmdev_hgcm_cancel2 {
        struct vmmdev_request_header header;
        u32 phys_req_to_cancel;
    }

.. _`vmmdev_hgcm_cancel2.members`:

Members
-------

header
    *undescribed*

phys_req_to_cancel
    *undescribed*

.. _`vmmdev_hgcm_cancel2.description`:

Description
-----------

After the request header.rc will be:

VINF_SUCCESS when cancelled.
VERR_NOT_FOUND if the specified request cannot be found.
VERR_INVALID_PARAMETER if the address is invalid valid.

.. This file was automatic generated / don't edit.

