.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/drm/v3d_drm.h

.. _`drm_v3d_submit_cl`:

struct drm_v3d_submit_cl
========================

.. c:type:: struct drm_v3d_submit_cl

    ioctl argument for submitting commands to the 3D engine.

.. _`drm_v3d_submit_cl.definition`:

Definition
----------

.. code-block:: c

    struct drm_v3d_submit_cl {
        __u32 bcl_start;
        __u32 bcl_end;
        __u32 rcl_start;
        __u32 rcl_end;
        __u32 in_sync_bcl;
        __u32 in_sync_rcl;
        __u32 out_sync;
        __u32 qma;
        __u32 qms;
        __u32 qts;
        __u64 bo_handles;
        __u32 bo_handle_count;
        __u32 pad;
    }

.. _`drm_v3d_submit_cl.members`:

Members
-------

bcl_start
    *undescribed*

bcl_end
    *undescribed*

rcl_start
    *undescribed*

rcl_end
    *undescribed*

in_sync_bcl
    *undescribed*

in_sync_rcl
    *undescribed*

out_sync
    *undescribed*

qma
    *undescribed*

qms
    *undescribed*

qts
    *undescribed*

bo_handles
    *undescribed*

bo_handle_count
    *undescribed*

pad
    *undescribed*

.. _`drm_v3d_submit_cl.description`:

Description
-----------

This asks the kernel to have the GPU execute an optional binner
command list, and a render command list.

.. _`drm_v3d_wait_bo`:

struct drm_v3d_wait_bo
======================

.. c:type:: struct drm_v3d_wait_bo

    ioctl argument for waiting for completion of the last DRM_V3D_SUBMIT_CL on a BO.

.. _`drm_v3d_wait_bo.definition`:

Definition
----------

.. code-block:: c

    struct drm_v3d_wait_bo {
        __u32 handle;
        __u32 pad;
        __u64 timeout_ns;
    }

.. _`drm_v3d_wait_bo.members`:

Members
-------

handle
    *undescribed*

pad
    *undescribed*

timeout_ns
    *undescribed*

.. _`drm_v3d_wait_bo.description`:

Description
-----------

This is useful for cases where multiple processes might be
rendering to a BO and you want to wait for all rendering to be
completed.

.. _`drm_v3d_create_bo`:

struct drm_v3d_create_bo
========================

.. c:type:: struct drm_v3d_create_bo

    ioctl argument for creating V3D BOs.

.. _`drm_v3d_create_bo.definition`:

Definition
----------

.. code-block:: c

    struct drm_v3d_create_bo {
        __u32 size;
        __u32 flags;
        __u32 handle;
        __u32 offset;
    }

.. _`drm_v3d_create_bo.members`:

Members
-------

size
    *undescribed*

flags
    *undescribed*

handle
    *undescribed*

offset
    *undescribed*

.. _`drm_v3d_create_bo.description`:

Description
-----------

There are currently no values for the flags argument, but it may be
used in a future extension.

.. _`drm_v3d_mmap_bo`:

struct drm_v3d_mmap_bo
======================

.. c:type:: struct drm_v3d_mmap_bo

    ioctl argument for mapping V3D BOs.

.. _`drm_v3d_mmap_bo.definition`:

Definition
----------

.. code-block:: c

    struct drm_v3d_mmap_bo {
        __u32 handle;
        __u32 flags;
        __u64 offset;
    }

.. _`drm_v3d_mmap_bo.members`:

Members
-------

handle
    *undescribed*

flags
    *undescribed*

offset
    *undescribed*

.. _`drm_v3d_mmap_bo.description`:

Description
-----------

This doesn't actually perform an mmap.  Instead, it returns the
offset you need to use in an mmap on the DRM device node.  This
means that tools like valgrind end up knowing about the mapped
memory.

There are currently no values for the flags argument, but it may be
used in a future extension.

.. This file was automatic generated / don't edit.

