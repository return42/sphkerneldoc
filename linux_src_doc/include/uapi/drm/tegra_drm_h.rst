.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/drm/tegra_drm.h

.. _`drm_tegra_gem_create`:

struct drm_tegra_gem_create
===========================

.. c:type:: struct drm_tegra_gem_create

    parameters for the GEM object creation IOCTL

.. _`drm_tegra_gem_create.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_gem_create {
        __u64 size;
        __u32 flags;
        __u32 handle;
    }

.. _`drm_tegra_gem_create.members`:

Members
-------

size

    The size, in bytes, of the buffer object to be created.

flags

    A bitmask of flags that influence the creation of GEM objects:

    DRM_TEGRA_GEM_CREATE_TILED
    Use the 16x16 tiling format for this buffer.

    DRM_TEGRA_GEM_CREATE_BOTTOM_UP
    The buffer has a bottom-up layout.

handle

    The handle of the created GEM object. Set by the kernel upon
    successful completion of the IOCTL.

.. _`drm_tegra_gem_mmap`:

struct drm_tegra_gem_mmap
=========================

.. c:type:: struct drm_tegra_gem_mmap

    parameters for the GEM mmap IOCTL

.. _`drm_tegra_gem_mmap.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_gem_mmap {
        __u32 handle;
        __u32 pad;
        __u64 offset;
    }

.. _`drm_tegra_gem_mmap.members`:

Members
-------

handle

    Handle of the GEM object to obtain an mmap offset for.

pad

    Structure padding that may be used in the future. Must be 0.

offset

    The mmap offset for the given GEM object. Set by the kernel upon
    successful completion of the IOCTL.

.. _`drm_tegra_syncpt_read`:

struct drm_tegra_syncpt_read
============================

.. c:type:: struct drm_tegra_syncpt_read

    parameters for the read syncpoint IOCTL

.. _`drm_tegra_syncpt_read.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_syncpt_read {
        __u32 id;
        __u32 value;
    }

.. _`drm_tegra_syncpt_read.members`:

Members
-------

id

    ID of the syncpoint to read the current value from.

value

    The current syncpoint value. Set by the kernel upon successful
    completion of the IOCTL.

.. _`drm_tegra_syncpt_incr`:

struct drm_tegra_syncpt_incr
============================

.. c:type:: struct drm_tegra_syncpt_incr

    parameters for the increment syncpoint IOCTL

.. _`drm_tegra_syncpt_incr.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_syncpt_incr {
        __u32 id;
        __u32 pad;
    }

.. _`drm_tegra_syncpt_incr.members`:

Members
-------

id

    ID of the syncpoint to increment.

pad

    Structure padding that may be used in the future. Must be 0.

.. _`drm_tegra_syncpt_wait`:

struct drm_tegra_syncpt_wait
============================

.. c:type:: struct drm_tegra_syncpt_wait

    parameters for the wait syncpoint IOCTL

.. _`drm_tegra_syncpt_wait.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_syncpt_wait {
        __u32 id;
        __u32 thresh;
        __u32 timeout;
        __u32 value;
    }

.. _`drm_tegra_syncpt_wait.members`:

Members
-------

id

    ID of the syncpoint to wait on.

thresh

    Threshold value for which to wait.

timeout

    Timeout, in milliseconds, to wait.

value

    The new syncpoint value after the wait. Set by the kernel upon
    successful completion of the IOCTL.

.. _`drm_tegra_open_channel`:

struct drm_tegra_open_channel
=============================

.. c:type:: struct drm_tegra_open_channel

    parameters for the open channel IOCTL

.. _`drm_tegra_open_channel.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_open_channel {
        __u32 client;
        __u32 pad;
        __u64 context;
    }

.. _`drm_tegra_open_channel.members`:

Members
-------

client

    The client ID for this channel.

pad

    Structure padding that may be used in the future. Must be 0.

context

    The application context of this channel. Set by the kernel upon
    successful completion of the IOCTL. This context needs to be passed
    to the DRM_TEGRA_CHANNEL_CLOSE or the DRM_TEGRA_SUBMIT IOCTLs.

.. _`drm_tegra_close_channel`:

struct drm_tegra_close_channel
==============================

.. c:type:: struct drm_tegra_close_channel

    parameters for the close channel IOCTL

.. _`drm_tegra_close_channel.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_close_channel {
        __u64 context;
    }

.. _`drm_tegra_close_channel.members`:

Members
-------

context

    The application context of this channel. This is obtained from the
    DRM_TEGRA_OPEN_CHANNEL IOCTL.

.. _`drm_tegra_get_syncpt`:

struct drm_tegra_get_syncpt
===========================

.. c:type:: struct drm_tegra_get_syncpt

    parameters for the get syncpoint IOCTL

.. _`drm_tegra_get_syncpt.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_get_syncpt {
        __u64 context;
        __u32 index;
        __u32 id;
    }

.. _`drm_tegra_get_syncpt.members`:

Members
-------

context

    The application context identifying the channel for which to obtain
    the syncpoint ID.

index

    Index of the client syncpoint for which to obtain the ID.

id

    The ID of the given syncpoint. Set by the kernel upon successful
    completion of the IOCTL.

.. _`drm_tegra_get_syncpt_base`:

struct drm_tegra_get_syncpt_base
================================

.. c:type:: struct drm_tegra_get_syncpt_base

    parameters for the get wait base IOCTL

.. _`drm_tegra_get_syncpt_base.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_get_syncpt_base {
        __u64 context;
        __u32 syncpt;
        __u32 id;
    }

.. _`drm_tegra_get_syncpt_base.members`:

Members
-------

context

    The application context identifying for which channel to obtain the
    wait base.

syncpt

    ID of the syncpoint for which to obtain the wait base.

id

    The ID of the wait base corresponding to the client syncpoint. Set
    by the kernel upon successful completion of the IOCTL.

.. _`drm_tegra_syncpt`:

struct drm_tegra_syncpt
=======================

.. c:type:: struct drm_tegra_syncpt

    syncpoint increment operation

.. _`drm_tegra_syncpt.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_syncpt {
        __u32 id;
        __u32 incrs;
    }

.. _`drm_tegra_syncpt.members`:

Members
-------

id

    ID of the syncpoint to operate on.

incrs

    Number of increments to perform for the syncpoint.

.. _`drm_tegra_cmdbuf`:

struct drm_tegra_cmdbuf
=======================

.. c:type:: struct drm_tegra_cmdbuf

    structure describing a command buffer

.. _`drm_tegra_cmdbuf.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_cmdbuf {
        __u32 handle;
        __u32 offset;
        __u32 words;
        __u32 pad;
    }

.. _`drm_tegra_cmdbuf.members`:

Members
-------

handle

    Handle to a GEM object containing the command buffer.

offset

    Offset, in bytes, into the GEM object identified by \ ``handle``\  at
    which the command buffer starts.

words

    Number of 32-bit words in this command buffer.

pad

    Structure padding that may be used in the future. Must be 0.

.. _`drm_tegra_reloc`:

struct drm_tegra_reloc
======================

.. c:type:: struct drm_tegra_reloc

    GEM object relocation structure

.. _`drm_tegra_reloc.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_reloc {
        struct {
            __u32 handle;
            __u32 offset;
        } cmdbuf;
        struct {
            __u32 handle;
            __u32 offset;
        } target;
        __u32 shift;
        __u32 pad;
    }

.. _`drm_tegra_reloc.members`:

Members
-------

cmdbuf
    *undescribed*

cmdbuf.handle

    Handle to the GEM object containing the command buffer for
    which to perform this GEM object relocation.

cmdbuf.offset

    Offset, in bytes, into the command buffer at which to
    insert the relocated address.

target
    *undescribed*

target.handle

    Handle to the GEM object to be relocated.

target.offset

    Offset, in bytes, into the target GEM object at which the
    relocated data starts.

shift

    The number of bits by which to shift relocated addresses.

pad

    Structure padding that may be used in the future. Must be 0.

.. _`drm_tegra_waitchk`:

struct drm_tegra_waitchk
========================

.. c:type:: struct drm_tegra_waitchk

    wait check structure

.. _`drm_tegra_waitchk.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_waitchk {
        __u32 handle;
        __u32 offset;
        __u32 syncpt;
        __u32 thresh;
    }

.. _`drm_tegra_waitchk.members`:

Members
-------

handle

    Handle to the GEM object containing a command stream on which to
    perform the wait check.

offset

    Offset, in bytes, of the location in the command stream to perform
    the wait check on.

syncpt

    ID of the syncpoint to wait check.

thresh

    Threshold value for which to check.

.. _`drm_tegra_submit`:

struct drm_tegra_submit
=======================

.. c:type:: struct drm_tegra_submit

    job submission structure

.. _`drm_tegra_submit.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_submit {
        __u64 context;
        __u32 num_syncpts;
        __u32 num_cmdbufs;
        __u32 num_relocs;
        __u32 num_waitchks;
        __u32 waitchk_mask;
        __u32 timeout;
        __u64 syncpts;
        __u64 cmdbufs;
        __u64 relocs;
        __u64 waitchks;
        __u32 fence;
        __u32 reserved[5];
    }

.. _`drm_tegra_submit.members`:

Members
-------

context

    The application context identifying the channel to use for the
    execution of this job.

num_syncpts

    The number of syncpoints operated on by this job. This defines the
    length of the array pointed to by \ ``syncpts``\ .

num_cmdbufs

    The number of command buffers to execute as part of this job. This
    defines the length of the array pointed to by \ ``cmdbufs``\ .

num_relocs

    The number of relocations to perform before executing this job.
    This defines the length of the array pointed to by \ ``relocs``\ .

num_waitchks

    The number of wait checks to perform as part of this job. This
    defines the length of the array pointed to by \ ``waitchks``\ .

waitchk_mask

    Bitmask of valid wait checks.

timeout

    Timeout, in milliseconds, before this job is cancelled.

syncpts

    A pointer to an array of \ :c:type:`struct drm_tegra_syncpt <drm_tegra_syncpt>`\  structures that
    specify the syncpoint operations performed as part of this job.
    The number of elements in the array must be equal to the value
    given by \ ``num_syncpts``\ .

cmdbufs

    A pointer to an array of \ :c:type:`struct drm_tegra_cmdbuf <drm_tegra_cmdbuf>`\  structures that
    define the command buffers to execute as part of this job. The
    number of elements in the array must be equal to the value given
    by \ ``num_syncpts``\ .

relocs

    A pointer to an array of \ :c:type:`struct drm_tegra_reloc <drm_tegra_reloc>`\  structures that
    specify the relocations that need to be performed before executing
    this job. The number of elements in the array must be equal to the
    value given by \ ``num_relocs``\ .

waitchks

    A pointer to an array of \ :c:type:`struct drm_tegra_waitchk <drm_tegra_waitchk>`\  structures that
    specify the wait checks to be performed while executing this job.
    The number of elements in the array must be equal to the value
    given by \ ``num_waitchks``\ .

fence

    The threshold of the syncpoint associated with this job after it
    has been completed. Set by the kernel upon successful completion of
    the IOCTL. This can be used with the DRM_TEGRA_SYNCPT_WAIT IOCTL to
    wait for this job to be finished.

reserved

    This field is reserved for future use. Must be 0.

.. _`drm_tegra_gem_set_tiling`:

struct drm_tegra_gem_set_tiling
===============================

.. c:type:: struct drm_tegra_gem_set_tiling

    parameters for the set tiling IOCTL

.. _`drm_tegra_gem_set_tiling.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_gem_set_tiling {
        __u32 handle;
        __u32 mode;
        __u32 value;
        __u32 pad;
    }

.. _`drm_tegra_gem_set_tiling.members`:

Members
-------

handle

    Handle to the GEM object for which to set the tiling parameters.

mode

    The tiling mode to set. Must be one of:

    DRM_TEGRA_GEM_TILING_MODE_PITCH
    pitch linear format

    DRM_TEGRA_GEM_TILING_MODE_TILED
    16x16 tiling format

    DRM_TEGRA_GEM_TILING_MODE_BLOCK
    16Bx2 tiling format

value

    The value to set for the tiling mode parameter.

pad

    Structure padding that may be used in the future. Must be 0.

.. _`drm_tegra_gem_get_tiling`:

struct drm_tegra_gem_get_tiling
===============================

.. c:type:: struct drm_tegra_gem_get_tiling

    parameters for the get tiling IOCTL

.. _`drm_tegra_gem_get_tiling.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_gem_get_tiling {
        __u32 handle;
        __u32 mode;
        __u32 value;
        __u32 pad;
    }

.. _`drm_tegra_gem_get_tiling.members`:

Members
-------

handle

    Handle to the GEM object for which to query the tiling parameters.

mode

    The tiling mode currently associated with the GEM object. Set by
    the kernel upon successful completion of the IOCTL.

value

    The tiling mode parameter currently associated with the GEM object.
    Set by the kernel upon successful completion of the IOCTL.

pad

    Structure padding that may be used in the future. Must be 0.

.. _`drm_tegra_gem_set_flags`:

struct drm_tegra_gem_set_flags
==============================

.. c:type:: struct drm_tegra_gem_set_flags

    parameters for the set flags IOCTL

.. _`drm_tegra_gem_set_flags.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_gem_set_flags {
        __u32 handle;
        __u32 flags;
    }

.. _`drm_tegra_gem_set_flags.members`:

Members
-------

handle

    Handle to the GEM object for which to set the flags.

flags

    The flags to set for the GEM object.

.. _`drm_tegra_gem_get_flags`:

struct drm_tegra_gem_get_flags
==============================

.. c:type:: struct drm_tegra_gem_get_flags

    parameters for the get flags IOCTL

.. _`drm_tegra_gem_get_flags.definition`:

Definition
----------

.. code-block:: c

    struct drm_tegra_gem_get_flags {
        __u32 handle;
        __u32 flags;
    }

.. _`drm_tegra_gem_get_flags.members`:

Members
-------

handle

    Handle to the GEM object for which to query the flags.

flags

    The flags currently associated with the GEM object. Set by the
    kernel upon successful completion of the IOCTL.

.. This file was automatic generated / don't edit.

