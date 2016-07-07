.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/drm/vc4_drm.h

.. _`drm_vc4_submit_cl`:

struct drm_vc4_submit_cl
========================

.. c:type:: struct drm_vc4_submit_cl

    ioctl argument for submitting commands to the 3D engine.

.. _`drm_vc4_submit_cl.definition`:

Definition
----------

.. code-block:: c

    struct drm_vc4_submit_cl {
        __u64 bin_cl;
        __u64 shader_rec;
        __u64 uniforms;
        __u64 bo_handles;
        __u32 bin_cl_size;
        __u32 shader_rec_size;
        __u32 shader_rec_count;
        __u32 uniforms_size;
        __u32 bo_handle_count;
        __u16 width;
        __u16 height;
        __u8 min_x_tile;
        __u8 min_y_tile;
        __u8 max_x_tile;
        __u8 max_y_tile;
        struct drm_vc4_submit_rcl_surface color_read;
        struct drm_vc4_submit_rcl_surface color_write;
        struct drm_vc4_submit_rcl_surface zs_read;
        struct drm_vc4_submit_rcl_surface zs_write;
        struct drm_vc4_submit_rcl_surface msaa_color_write;
        struct drm_vc4_submit_rcl_surface msaa_zs_write;
        __u32 clear_color[2];
        __u32 clear_z;
        __u8 clear_s;
        __u32 pad:24;
        #define VC4_SUBMIT_CL_USE_CLEAR_COLOR (1 << 0)
        __u32 flags;
        __u64 seqno;
    }

.. _`drm_vc4_submit_cl.members`:

Members
-------

bin_cl
    *undescribed*

shader_rec
    *undescribed*

uniforms
    *undescribed*

bo_handles
    *undescribed*

bin_cl_size
    *undescribed*

shader_rec_size
    *undescribed*

shader_rec_count
    *undescribed*

uniforms_size
    *undescribed*

bo_handle_count
    *undescribed*

width
    *undescribed*

height
    *undescribed*

min_x_tile
    *undescribed*

min_y_tile
    *undescribed*

max_x_tile
    *undescribed*

max_y_tile
    *undescribed*

color_read
    *undescribed*

color_write
    *undescribed*

zs_read
    *undescribed*

zs_write
    *undescribed*

msaa_color_write
    *undescribed*

msaa_zs_write
    *undescribed*

clear_z
    *undescribed*

clear_s
    *undescribed*

pad
    *undescribed*

flags
    *undescribed*

seqno
    *undescribed*

.. _`drm_vc4_submit_cl.description`:

Description
-----------

Drivers typically use GPU BOs to store batchbuffers / command lists and
their associated state.  However, because the VC4 lacks an MMU, we have to
do validation of memory accesses by the GPU commands.  If we were to store
our commands in BOs, we'd need to do uncached readback from them to do the
validation process, which is too expensive.  Instead, userspace accumulates
commands and associated state in plain memory, then the kernel copies the
data to its own address space, and then validates and stores it in a GPU
BO.

.. _`drm_vc4_wait_seqno`:

struct drm_vc4_wait_seqno
=========================

.. c:type:: struct drm_vc4_wait_seqno

    ioctl argument for waiting for DRM_VC4_SUBMIT_CL completion using its returned seqno.

.. _`drm_vc4_wait_seqno.definition`:

Definition
----------

.. code-block:: c

    struct drm_vc4_wait_seqno {
        __u64 seqno;
        __u64 timeout_ns;
    }

.. _`drm_vc4_wait_seqno.members`:

Members
-------

seqno
    *undescribed*

timeout_ns
    *undescribed*

.. _`drm_vc4_wait_seqno.description`:

Description
-----------

timeout_ns is the timeout in nanoseconds, where "0" means "don't
block, just return the status."

.. _`drm_vc4_wait_bo`:

struct drm_vc4_wait_bo
======================

.. c:type:: struct drm_vc4_wait_bo

    ioctl argument for waiting for completion of the last DRM_VC4_SUBMIT_CL on a BO.

.. _`drm_vc4_wait_bo.definition`:

Definition
----------

.. code-block:: c

    struct drm_vc4_wait_bo {
        __u32 handle;
        __u32 pad;
        __u64 timeout_ns;
    }

.. _`drm_vc4_wait_bo.members`:

Members
-------

handle
    *undescribed*

pad
    *undescribed*

timeout_ns
    *undescribed*

.. _`drm_vc4_wait_bo.description`:

Description
-----------

This is useful for cases where multiple processes might be
rendering to a BO and you want to wait for all rendering to be
completed.

.. _`drm_vc4_create_bo`:

struct drm_vc4_create_bo
========================

.. c:type:: struct drm_vc4_create_bo

    ioctl argument for creating VC4 BOs.

.. _`drm_vc4_create_bo.definition`:

Definition
----------

.. code-block:: c

    struct drm_vc4_create_bo {
        __u32 size;
        __u32 flags;
        __u32 handle;
        __u32 pad;
    }

.. _`drm_vc4_create_bo.members`:

Members
-------

size
    *undescribed*

flags
    *undescribed*

handle
    *undescribed*

pad
    *undescribed*

.. _`drm_vc4_create_bo.description`:

Description
-----------

There are currently no values for the flags argument, but it may be
used in a future extension.

.. _`drm_vc4_mmap_bo`:

struct drm_vc4_mmap_bo
======================

.. c:type:: struct drm_vc4_mmap_bo

    ioctl argument for mapping VC4 BOs.

.. _`drm_vc4_mmap_bo.definition`:

Definition
----------

.. code-block:: c

    struct drm_vc4_mmap_bo {
        __u32 handle;
        __u32 flags;
        __u64 offset;
    }

.. _`drm_vc4_mmap_bo.members`:

Members
-------

handle
    *undescribed*

flags
    *undescribed*

offset
    *undescribed*

.. _`drm_vc4_mmap_bo.description`:

Description
-----------

This doesn't actually perform an mmap.  Instead, it returns the
offset you need to use in an mmap on the DRM device node.  This
means that tools like valgrind end up knowing about the mapped
memory.

There are currently no values for the flags argument, but it may be
used in a future extension.

.. _`drm_vc4_create_shader_bo`:

struct drm_vc4_create_shader_bo
===============================

.. c:type:: struct drm_vc4_create_shader_bo

    ioctl argument for creating VC4 shader BOs.

.. _`drm_vc4_create_shader_bo.definition`:

Definition
----------

.. code-block:: c

    struct drm_vc4_create_shader_bo {
        __u32 size;
        __u32 flags;
        __u64 data;
        __u32 handle;
        __u32 pad;
    }

.. _`drm_vc4_create_shader_bo.members`:

Members
-------

size
    *undescribed*

flags
    *undescribed*

data
    *undescribed*

handle
    *undescribed*

pad
    *undescribed*

.. _`drm_vc4_create_shader_bo.description`:

Description
-----------

Since allowing a shader to be overwritten while it's also being
executed from would allow privlege escalation, shaders must be
created using this ioctl, and they can't be mmapped later.

.. _`drm_vc4_get_hang_state`:

struct drm_vc4_get_hang_state
=============================

.. c:type:: struct drm_vc4_get_hang_state

    ioctl argument for collecting state from a GPU hang for analysis.

.. _`drm_vc4_get_hang_state.definition`:

Definition
----------

.. code-block:: c

    struct drm_vc4_get_hang_state {
        __u64 bo;
        __u32 bo_count;
        __u32 start_bin;
        __u32 start_render;
        __u32 ct0ca;
        __u32 ct0ea;
        __u32 ct1ca;
        __u32 ct1ea;
        __u32 ct0cs;
        __u32 ct1cs;
        __u32 ct0ra0;
        __u32 ct1ra0;
        __u32 bpca;
        __u32 bpcs;
        __u32 bpoa;
        __u32 bpos;
        __u32 vpmbase;
        __u32 dbge;
        __u32 fdbgo;
        __u32 fdbgb;
        __u32 fdbgr;
        __u32 fdbgs;
        __u32 errstat;
        __u32 pad[16];
    }

.. _`drm_vc4_get_hang_state.members`:

Members
-------

bo
    *undescribed*

bo_count
    *undescribed*

start_bin
    *undescribed*

start_render
    *undescribed*

ct0ca
    *undescribed*

ct0ea
    *undescribed*

ct1ca
    *undescribed*

ct1ea
    *undescribed*

ct0cs
    *undescribed*

ct1cs
    *undescribed*

ct0ra0
    *undescribed*

ct1ra0
    *undescribed*

bpca
    *undescribed*

bpcs
    *undescribed*

bpoa
    *undescribed*

bpos
    *undescribed*

vpmbase
    *undescribed*

dbge
    *undescribed*

fdbgo
    *undescribed*

fdbgb
    *undescribed*

fdbgr
    *undescribed*

fdbgs
    *undescribed*

errstat
    *undescribed*

.. This file was automatic generated / don't edit.

