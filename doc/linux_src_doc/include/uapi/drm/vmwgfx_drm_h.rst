.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/drm/vmwgfx_drm.h

.. _`drm_vmw_param_num_streams`:

DRM_VMW_PARAM_NUM_STREAMS
=========================

.. c:function::  DRM_VMW_PARAM_NUM_STREAMS()

    get device information.

.. _`drm_vmw_param_num_streams.drm_vmw_param_fifo_offset`:

DRM_VMW_PARAM_FIFO_OFFSET
-------------------------

Offset to use to map the first page of the FIFO read-only.
The fifo is mapped using the \ :c:func:`mmap`\  system call on the drm device.

.. _`drm_vmw_param_num_streams.drm_vmw_param_overlay_ioctl`:

DRM_VMW_PARAM_OVERLAY_IOCTL
---------------------------

Does the driver support the overlay ioctl.

.. _`drm_vmw_handle_type`:

enum drm_vmw_handle_type
========================

.. c:type:: enum drm_vmw_handle_type

    handle type for ref ioctls

.. _`drm_vmw_handle_type.definition`:

Definition
----------

.. code-block:: c

    enum drm_vmw_handle_type {
        DRM_VMW_HANDLE_LEGACY,
        DRM_VMW_HANDLE_PRIME
    };

.. _`drm_vmw_handle_type.constants`:

Constants
---------

DRM_VMW_HANDLE_LEGACY
    *undescribed*

DRM_VMW_HANDLE_PRIME
    *undescribed*

.. _`drm_vmw_getparam_arg`:

struct drm_vmw_getparam_arg
===========================

.. c:type:: struct drm_vmw_getparam_arg


.. _`drm_vmw_getparam_arg.definition`:

Definition
----------

.. code-block:: c

    struct drm_vmw_getparam_arg {
        __u64 value;
        __u32 param;
        __u32 pad64;
    }

.. _`drm_vmw_getparam_arg.members`:

Members
-------

value
    Returned value. //Out

param
    Parameter to query. //In.

pad64
    *undescribed*

.. _`drm_vmw_getparam_arg.description`:

Description
-----------

Argument to the DRM_VMW_GET_PARAM Ioctl.

.. _`drm_vmw_surface_arg`:

struct drm_vmw_surface_arg
==========================

.. c:type:: struct drm_vmw_surface_arg


.. _`drm_vmw_surface_arg.definition`:

Definition
----------

.. code-block:: c

    struct drm_vmw_surface_arg {
        __s32 sid;
        enum drm_vmw_handle_type handle_type;
    }

.. _`drm_vmw_surface_arg.members`:

Members
-------

sid
    Surface id of created surface or surface to destroy or reference.

handle_type
    Handle type for DRM_VMW_REF_SURFACE Ioctl.

.. _`drm_vmw_surface_arg.description`:

Description
-----------

Output data from the DRM_VMW_CREATE_SURFACE Ioctl.
Input argument to the DRM_VMW_UNREF_SURFACE Ioctl.
Input argument to the DRM_VMW_REF_SURFACE Ioctl.

.. _`drm_vmw_size`:

struct drm_vmw_size
===================

.. c:type:: struct drm_vmw_size


.. _`drm_vmw_size.definition`:

Definition
----------

.. code-block:: c

    struct drm_vmw_size {
        __u32 width;
        __u32 height;
        __u32 depth;
        __u32 pad64;
    }

.. _`drm_vmw_size.members`:

Members
-------

width
    *undescribed*

height
    *undescribed*

depth
    *undescribed*

pad64
    *undescribed*

.. _`drm_vmw_size.description`:

Description
-----------

\ ``width``\  - mip level width
\ ``height``\  - mip level height
\ ``depth``\  - mip level depth

Description of a mip level.
Input data to the DRM_WMW_CREATE_SURFACE Ioctl.

.. _`drm_vmw_surface_create_arg`:

union drm_vmw_surface_create_arg
================================

.. c:type:: struct drm_vmw_surface_create_arg


.. _`drm_vmw_surface_create_arg.definition`:

Definition
----------

.. code-block:: c

    union drm_vmw_surface_create_arg {
        struct drm_vmw_surface_arg rep;
        struct drm_vmw_surface_create_req req;
    }

.. _`drm_vmw_surface_create_arg.members`:

Members
-------

rep
    Output data as described above.

req
    Input data as described above.

.. _`drm_vmw_surface_create_arg.description`:

Description
-----------

Argument to the DRM_VMW_CREATE_SURFACE Ioctl.

.. _`drm_vmw_execbuf_version`:

DRM_VMW_EXECBUF_VERSION
=======================

.. c:function::  DRM_VMW_EXECBUF_VERSION()

    Unreference a host surface.

.. _`drm_vmw_execbuf_version.description`:

Description
-----------

Clear a reference previously put on a host surface.
When all references are gone, including the one implicitly placed
on creation,
a destroy surface command will be queued for the host.
Does not wait for completion.

.. _`drm_vmw_fence_rep`:

struct drm_vmw_fence_rep
========================

.. c:type:: struct drm_vmw_fence_rep


.. _`drm_vmw_fence_rep.definition`:

Definition
----------

.. code-block:: c

    struct drm_vmw_fence_rep {
        __u32 handle;
        __u32 mask;
        __u32 seqno;
        __u32 passed_seqno;
        __u32 pad64;
        __s32 error;
    }

.. _`drm_vmw_fence_rep.members`:

Members
-------

handle
    Fence object handle for fence associated with a command submission.

mask
    Fence flags relevant for this fence object.

seqno
    Fence sequence number in fifo. A fence object with a lower
    seqno will signal the EXEC flag before a fence object with a higher
    seqno. This can be used by user-space to avoid kernel calls to determine
    whether a fence has signaled the EXEC flag. Note that \ ``seqno``\  will
    wrap at 32-bit.

passed_seqno
    The highest seqno number processed by the hardware
    so far. This can be used to mark user-space fence objects as signaled, and
    to determine whether a fence seqno might be stale.

pad64
    *undescribed*

error
    This member should've been set to -EFAULT on submission.

.. _`drm_vmw_fence_rep.the-following-actions-should-be-take-on-completion`:

The following actions should be take on completion
--------------------------------------------------

error == -EFAULT: Fence communication failed. The host is synchronized.
Use the last fence id read from the FIFO fence register.
error != 0 && error != -EFAULT:
Fence submission failed. The host is synchronized. Use the fence_seq member.
error == 0: All is OK, The host may not be synchronized.
Use the fence_seq member.

Input / Output data to the DRM_VMW_EXECBUF Ioctl.

.. _`drm_vmw_dmabuf_rep`:

struct drm_vmw_dmabuf_rep
=========================

.. c:type:: struct drm_vmw_dmabuf_rep


.. _`drm_vmw_dmabuf_rep.definition`:

Definition
----------

.. code-block:: c

    struct drm_vmw_dmabuf_rep {
        __u64 map_handle;
        __u32 handle;
        __u32 cur_gmr_id;
        __u32 cur_gmr_offset;
        __u32 pad64;
    }

.. _`drm_vmw_dmabuf_rep.members`:

Members
-------

map_handle
    Offset to use in the \ :c:func:`mmap`\  call used to map the buffer.

handle
    Handle unique to this buffer. Used for unreferencing.

cur_gmr_id
    GMR id to use in the command stream when this buffer is
    referenced. See not above.

cur_gmr_offset
    Offset to use in the command stream when this buffer is
    referenced. See note above.

pad64
    *undescribed*

.. _`drm_vmw_dmabuf_rep.description`:

Description
-----------

Output data from the DRM_VMW_ALLOC_DMABUF Ioctl.

.. _`drm_vmw_alloc_dmabuf_arg`:

union drm_vmw_alloc_dmabuf_arg
==============================

.. c:type:: struct drm_vmw_alloc_dmabuf_arg


.. _`drm_vmw_alloc_dmabuf_arg.definition`:

Definition
----------

.. code-block:: c

    union drm_vmw_alloc_dmabuf_arg {
        struct drm_vmw_alloc_dmabuf_req req;
        struct drm_vmw_dmabuf_rep rep;
    }

.. _`drm_vmw_alloc_dmabuf_arg.members`:

Members
-------

req
    Input data as described above.

rep
    Output data as described above.

.. _`drm_vmw_alloc_dmabuf_arg.description`:

Description
-----------

Argument to the DRM_VMW_ALLOC_DMABUF Ioctl.

.. _`drm_vmw_control_stream_arg`:

struct drm_vmw_control_stream_arg
=================================

.. c:type:: struct drm_vmw_control_stream_arg


.. _`drm_vmw_control_stream_arg.definition`:

Definition
----------

.. code-block:: c

    struct drm_vmw_control_stream_arg {
        __u32 stream_id;
        __u32 enabled;
        __u32 flags;
        __u32 color_key;
        __u32 handle;
        __u32 offset;
        __s32 format;
        __u32 size;
        __u32 width;
        __u32 height;
        __u32 pitch[3];
        __u32 pad64;
        struct drm_vmw_rect src;
        struct drm_vmw_rect dst;
    }

.. _`drm_vmw_control_stream_arg.members`:

Members
-------

stream_id
    Stearm to control

enabled
    If false all following arguments are ignored.

flags
    *undescribed*

color_key
    *undescribed*

handle
    Handle to buffer for getting data from.

offset
    Offset from start of dma buffer to overlay.

format
    Format of the overlay as understood by the host.

size
    Size of the overlay in bytes.

width
    Width of the overlay.

height
    Height of the overlay.

pitch
    Array of pitches, the two last are only used for YUV12 formats.

pad64
    *undescribed*

src
    Source rect, must be within the defined area above.

dst
    Destination rect, x and y may be negative.

.. _`drm_vmw_control_stream_arg.description`:

Description
-----------

Argument to the DRM_VMW_CONTROL_STREAM Ioctl.

.. _`drm_vmw_cursor_bypass_all`:

DRM_VMW_CURSOR_BYPASS_ALL
=========================

.. c:function::  DRM_VMW_CURSOR_BYPASS_ALL()

    Give extra information about cursor bypass.

.. _`drm_vmw_cursor_bypass_arg`:

struct drm_vmw_cursor_bypass_arg
================================

.. c:type:: struct drm_vmw_cursor_bypass_arg


.. _`drm_vmw_cursor_bypass_arg.definition`:

Definition
----------

.. code-block:: c

    struct drm_vmw_cursor_bypass_arg {
        __u32 flags;
        __u32 crtc_id;
        __s32 xpos;
        __s32 ypos;
        __s32 xhot;
        __s32 yhot;
    }

.. _`drm_vmw_cursor_bypass_arg.members`:

Members
-------

flags
    Flags.

crtc_id
    Crtc id, only used if DMR_CURSOR_BYPASS_ALL isn't passed.

xpos
    X position of cursor.

ypos
    Y position of cursor.

xhot
    X hotspot.

yhot
    Y hotspot.

.. _`drm_vmw_cursor_bypass_arg.description`:

Description
-----------

Argument to the DRM_VMW_CURSOR_BYPASS Ioctl.

.. _`drm_vmw_fence_flag_exec`:

DRM_VMW_FENCE_FLAG_EXEC
=======================

.. c:function::  DRM_VMW_FENCE_FLAG_EXEC()

.. _`drm_vmw_fence_flag_exec.description`:

Description
-----------

Waits for a fence object to signal. The wait is interruptible, so that
signals may be delivered during the interrupt. The wait may timeout,
in which case the calls returns -EBUSY. If the wait is restarted,
that is restarting without resetting \ ``cookie_valid``\  to zero,
the timeout is computed from the first call.

The flags argument to the DRM_VMW_FENCE_WAIT ioctl indicates what to wait
on:

.. _`drm_vmw_fence_flag_exec.drm_vmw_fence_flag_exec`:

DRM_VMW_FENCE_FLAG_EXEC
-----------------------

All commands ahead of the fence in the command
stream
have executed.

.. _`drm_vmw_fence_flag_exec.drm_vmw_fence_flag_query`:

DRM_VMW_FENCE_FLAG_QUERY
------------------------

All query results resulting from query finish
commands
in the buffer given to the EXECBUF ioctl returning the fence object handle
are available to user-space.

.. _`drm_vmw_fence_flag_exec.drm_vmw_wait_option_unref`:

DRM_VMW_WAIT_OPTION_UNREF
-------------------------

If this wait option is given, and the
fenc wait ioctl returns 0, the fence object has been unreferenced after
the wait.

.. _`drm_vmw_fence_wait_arg`:

struct drm_vmw_fence_wait_arg
=============================

.. c:type:: struct drm_vmw_fence_wait_arg


.. _`drm_vmw_fence_wait_arg.definition`:

Definition
----------

.. code-block:: c

    struct drm_vmw_fence_wait_arg {
        __u32 handle;
        __s32 cookie_valid;
        __u64 kernel_cookie;
        __u64 timeout_us;
        __s32 lazy;
        __s32 flags;
        __s32 wait_options;
        __s32 pad64;
    }

.. _`drm_vmw_fence_wait_arg.members`:

Members
-------

handle
    Fence object handle as returned by the DRM_VMW_EXECBUF ioctl.

cookie_valid
    Must be reset to 0 on first call. Left alone on restart.

kernel_cookie
    Set to 0 on first call. Left alone on restart.

timeout_us
    Wait timeout in microseconds. 0 for indefinite timeout.

lazy
    Set to 1 if timing is not critical. Allow more than a kernel tick
    before returning.

flags
    Fence flags to wait on.

wait_options
    Options that control the behaviour of the wait ioctl.

pad64
    *undescribed*

.. _`drm_vmw_fence_wait_arg.description`:

Description
-----------

Input argument to the DRM_VMW_FENCE_WAIT ioctl.

.. _`drm_vmw_event_fence_signaled`:

DRM_VMW_EVENT_FENCE_SIGNALED
============================

.. c:function::  DRM_VMW_EVENT_FENCE_SIGNALED()

.. _`drm_vmw_event_fence_signaled.description`:

Description
-----------

Queues an event on a fence to be delivered on the drm character device
when the fence has signaled the DRM_VMW_FENCE_FLAG_EXEC flag.
Optionally the approximate time when the fence signaled is
given by the event.

.. _`drm_vmw_fence_event_arg`:

struct drm_vmw_fence_event_arg
==============================

.. c:type:: struct drm_vmw_fence_event_arg


.. _`drm_vmw_fence_event_arg.definition`:

Definition
----------

.. code-block:: c

    struct drm_vmw_fence_event_arg {
        __u64 fence_rep;
        __u64 user_data;
        __u32 handle;
        __u32 flags;
    }

.. _`drm_vmw_fence_event_arg.members`:

Members
-------

fence_rep
    Pointer to fence_rep structure cast to \__u64 or 0 if
    the fence is not supposed to be referenced by user-space.

user_data
    *undescribed*

handle
    Attach the event to this fence only.

flags
    A set of flags as defined above.

.. _`drm_vmw_shader_create_arg`:

struct drm_vmw_shader_create_arg
================================

.. c:type:: struct drm_vmw_shader_create_arg


.. _`drm_vmw_shader_create_arg.definition`:

Definition
----------

.. code-block:: c

    struct drm_vmw_shader_create_arg {
        enum drm_vmw_shader_type shader_type;
        __u32 size;
        __u32 buffer_handle;
        __u32 shader_handle;
        __u64 offset;
    }

.. _`drm_vmw_shader_create_arg.members`:

Members
-------

shader_type
    Shader type of the shader to create.

size
    Size of the byte-code in bytes.
    where the shader byte-code starts

buffer_handle
    Buffer handle identifying the buffer containing the
    shader byte-code

shader_handle
    On successful completion contains a handle that
    can be used to subsequently identify the shader.

offset
    Offset in bytes into the buffer given by \ ``buffer_handle``\ ,

.. _`drm_vmw_shader_create_arg.description`:

Description
-----------

Input / Output argument to the DRM_VMW_CREATE_SHADER Ioctl.

.. _`drm_vmw_gb_surface_create_req`:

struct drm_vmw_gb_surface_create_req
====================================

.. c:type:: struct drm_vmw_gb_surface_create_req


.. _`drm_vmw_gb_surface_create_req.definition`:

Definition
----------

.. code-block:: c

    struct drm_vmw_gb_surface_create_req {
        __u32 svga3d_flags;
        __u32 format;
        __u32 mip_levels;
        enum drm_vmw_surface_flags drm_surface_flags;
        __u32 multisample_count;
        __u32 autogen_filter;
        __u32 buffer_handle;
        __u32 array_size;
        struct drm_vmw_size base_size;
    }

.. _`drm_vmw_gb_surface_create_req.members`:

Members
-------

svga3d_flags
    SVGA3d surface flags for the device.

format
    SVGA3d format.

mip_levels
    *undescribed*

drm_surface_flags
    *undescribed*

multisample_count
    *undescribed*

autogen_filter
    *undescribed*

buffer_handle
    *undescribed*

array_size
    *undescribed*

base_size
    *undescribed*

.. _`drm_vmw_gb_surface_create_req.description`:

Description
-----------

Input argument to the  DRM_VMW_GB_SURFACE_CREATE Ioctl.
Part of output argument for the DRM_VMW_GB_SURFACE_REF Ioctl.

.. _`drm_vmw_gb_surface_create_rep`:

struct drm_vmw_gb_surface_create_rep
====================================

.. c:type:: struct drm_vmw_gb_surface_create_rep


.. _`drm_vmw_gb_surface_create_rep.definition`:

Definition
----------

.. code-block:: c

    struct drm_vmw_gb_surface_create_rep {
        __u32 handle;
        __u32 backup_size;
        __u32 buffer_handle;
        __u32 buffer_size;
        __u64 buffer_map_handle;
    }

.. _`drm_vmw_gb_surface_create_rep.members`:

Members
-------

handle
    Surface handle.

backup_size
    Size of backup buffers for this surface.

buffer_handle
    Handle of backup buffer. SVGA3D_INVALID_ID if none.

buffer_size
    Actual size of the buffer identified by
    \ ``buffer_handle``\ 

buffer_map_handle
    Offset into device address space for the buffer
    identified by \ ``buffer_handle``\ .

.. _`drm_vmw_gb_surface_create_rep.description`:

Description
-----------

Part of output argument for the DRM_VMW_GB_SURFACE_REF ioctl.
Output argument for the DRM_VMW_GB_SURFACE_CREATE ioctl.

.. _`drm_vmw_gb_surface_create_arg`:

union drm_vmw_gb_surface_create_arg
===================================

.. c:type:: struct drm_vmw_gb_surface_create_arg


.. _`drm_vmw_gb_surface_create_arg.definition`:

Definition
----------

.. code-block:: c

    union drm_vmw_gb_surface_create_arg {
        struct drm_vmw_gb_surface_create_rep rep;
        struct drm_vmw_gb_surface_create_req req;
    }

.. _`drm_vmw_gb_surface_create_arg.members`:

Members
-------

rep
    Output argument as described above.

req
    Input argument as described above.

.. _`drm_vmw_gb_surface_create_arg.description`:

Description
-----------

Argument to the DRM_VMW_GB_SURFACE_CREATE ioctl.

.. _`drm_vmw_gb_surface_reference_arg`:

union drm_vmw_gb_surface_reference_arg
======================================

.. c:type:: struct drm_vmw_gb_surface_reference_arg


.. _`drm_vmw_gb_surface_reference_arg.definition`:

Definition
----------

.. code-block:: c

    union drm_vmw_gb_surface_reference_arg {
        struct drm_vmw_gb_surface_ref_rep rep;
        struct drm_vmw_surface_arg req;
    }

.. _`drm_vmw_gb_surface_reference_arg.members`:

Members
-------

rep
    Output data as described above at "struct drm_vmw_gb_surface_ref_rep"

req
    Input data as described above at "struct drm_vmw_surface_arg"

.. _`drm_vmw_gb_surface_reference_arg.description`:

Description
-----------

Argument to the DRM_VMW_GB_SURFACE_REF Ioctl.

.. _`drm_vmw_synccpu_op`:

enum drm_vmw_synccpu_op
=======================

.. c:type:: enum drm_vmw_synccpu_op

    Synccpu operations:

.. _`drm_vmw_synccpu_op.definition`:

Definition
----------

.. code-block:: c

    enum drm_vmw_synccpu_op {
        drm_vmw_synccpu_grab,
        drm_vmw_synccpu_release
    };

.. _`drm_vmw_synccpu_op.constants`:

Constants
---------

drm_vmw_synccpu_grab
    Grab the buffer for CPU operations

drm_vmw_synccpu_release
    Release a previous grab.

.. _`drm_vmw_synccpu_arg`:

struct drm_vmw_synccpu_arg
==========================

.. c:type:: struct drm_vmw_synccpu_arg


.. _`drm_vmw_synccpu_arg.definition`:

Definition
----------

.. code-block:: c

    struct drm_vmw_synccpu_arg {
        enum drm_vmw_synccpu_op op;
        enum drm_vmw_synccpu_flags flags;
        __u32 handle;
        __u32 pad64;
    }

.. _`drm_vmw_synccpu_arg.members`:

Members
-------

op
    The synccpu operation as described above.

flags
    Flags as described above.

handle
    Handle identifying the buffer object.

pad64
    *undescribed*

.. _`drm_vmw_extended_context_arg`:

union drm_vmw_extended_context_arg
==================================

.. c:type:: struct drm_vmw_extended_context_arg


.. _`drm_vmw_extended_context_arg.definition`:

Definition
----------

.. code-block:: c

    union drm_vmw_extended_context_arg {
        enum drm_vmw_extended_context req;
        struct drm_vmw_context_arg rep;
    }

.. _`drm_vmw_extended_context_arg.members`:

Members
-------

req
    Context type.

rep
    Context identifier.

.. _`drm_vmw_extended_context_arg.description`:

Description
-----------

Argument to the DRM_VMW_CREATE_EXTENDED_CONTEXT Ioctl.

.. This file was automatic generated / don't edit.

