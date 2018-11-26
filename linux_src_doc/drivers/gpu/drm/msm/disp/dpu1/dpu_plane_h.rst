.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_plane.h

.. _`dpu_plane_state`:

struct dpu_plane_state
======================

.. c:type:: struct dpu_plane_state

    Define dpu extension of drm plane state object

.. _`dpu_plane_state.definition`:

Definition
----------

.. code-block:: c

    struct dpu_plane_state {
        struct drm_plane_state base;
        struct msm_gem_address_space *aspace;
        void *input_fence;
        enum dpu_stage stage;
        uint32_t multirect_index;
        uint32_t multirect_mode;
        bool pending;
        struct dpu_hw_scaler3_cfg scaler3_cfg;
        struct dpu_hw_pixel_ext pixel_ext;
        struct dpu_hw_pipe_cdp_cfg cdp_cfg;
    }

.. _`dpu_plane_state.members`:

Members
-------

base
    base drm plane state object

aspace
    pointer to address space for input/output buffers

input_fence
    dereferenced input fence pointer

stage
    assigned by crtc blender

multirect_index
    index of the rectangle of SSPP

multirect_mode
    parallel or time multiplex multirect mode

pending
    whether the current update is still pending

scaler3_cfg
    configuration data for scaler3

pixel_ext
    configuration data for pixel extensions

cdp_cfg
    CDP configuration

.. _`dpu_multirect_plane_states`:

struct dpu_multirect_plane_states
=================================

.. c:type:: struct dpu_multirect_plane_states

    Defines multirect pair of drm plane states

.. _`dpu_multirect_plane_states.definition`:

Definition
----------

.. code-block:: c

    struct dpu_multirect_plane_states {
        const struct drm_plane_state *r0;
        const struct drm_plane_state *r1;
    }

.. _`dpu_multirect_plane_states.members`:

Members
-------

r0
    drm plane configured on rect 0

r1
    drm plane configured on rect 1

.. _`dpu_plane_pipe`:

dpu_plane_pipe
==============

.. c:function:: enum dpu_sspp dpu_plane_pipe(struct drm_plane *plane)

    return sspp identifier for the given plane

    :param plane:
        Pointer to DRM plane object
    :type plane: struct drm_plane \*

.. _`dpu_plane_pipe.return`:

Return
------

sspp identifier of the given plane

.. _`is_dpu_plane_virtual`:

is_dpu_plane_virtual
====================

.. c:function:: bool is_dpu_plane_virtual(struct drm_plane *plane)

    check for virtual plane

    :param plane:
        Pointer to DRM plane object
    :type plane: struct drm_plane \*

.. _`is_dpu_plane_virtual.return`:

Return
------

true - if the plane is virtual
false - if the plane is primary

.. _`dpu_plane_get_ctl_flush`:

dpu_plane_get_ctl_flush
=======================

.. c:function:: void dpu_plane_get_ctl_flush(struct drm_plane *plane, struct dpu_hw_ctl *ctl, u32 *flush_sspp)

    get control flush mask

    :param plane:
        Pointer to DRM plane object
    :type plane: struct drm_plane \*

    :param ctl:
        Pointer to control hardware
    :type ctl: struct dpu_hw_ctl \*

    :param flush_sspp:
        Pointer to sspp flush control word
    :type flush_sspp: u32 \*

.. _`dpu_plane_restore`:

dpu_plane_restore
=================

.. c:function:: void dpu_plane_restore(struct drm_plane *plane)

    restore hw state if previously power collapsed

    :param plane:
        Pointer to drm plane structure
    :type plane: struct drm_plane \*

.. _`dpu_plane_flush`:

dpu_plane_flush
===============

.. c:function:: void dpu_plane_flush(struct drm_plane *plane)

    final plane operations before commit flush

    :param plane:
        Pointer to drm plane structure
    :type plane: struct drm_plane \*

.. _`dpu_plane_kickoff`:

dpu_plane_kickoff
=================

.. c:function:: void dpu_plane_kickoff(struct drm_plane *plane)

    final plane operations before commit kickoff

    :param plane:
        Pointer to drm plane structure
    :type plane: struct drm_plane \*

.. _`dpu_plane_set_error`:

dpu_plane_set_error
===================

.. c:function:: void dpu_plane_set_error(struct drm_plane *plane, bool error)

    enable/disable error condition

    :param plane:
        pointer to drm_plane structure
    :type plane: struct drm_plane \*

    :param error:
        *undescribed*
    :type error: bool

.. _`dpu_plane_init`:

dpu_plane_init
==============

.. c:function:: struct drm_plane *dpu_plane_init(struct drm_device *dev, uint32_t pipe, enum drm_plane_type type, unsigned long possible_crtcs, u32 master_plane_id)

    create new dpu plane for the given pipe

    :param dev:
        Pointer to DRM device
    :type dev: struct drm_device \*

    :param pipe:
        dpu hardware pipe identifier
    :type pipe: uint32_t

    :param type:
        Plane type - PRIMARY/OVERLAY/CURSOR
    :type type: enum drm_plane_type

    :param possible_crtcs:
        bitmask of crtc that can be attached to the given pipe
    :type possible_crtcs: unsigned long

    :param master_plane_id:
        primary plane id of a multirect pipe. 0 value passed for
        a regular plane initialization. A non-zero primary plane
        id will be passed for a virtual pipe initialization.
    :type master_plane_id: u32

.. _`dpu_plane_validate_multirect_v2`:

dpu_plane_validate_multirect_v2
===============================

.. c:function:: int dpu_plane_validate_multirect_v2(struct dpu_multirect_plane_states *plane)

    validate the multirect planes against hw limitations

    :param plane:
        drm plate states of the multirect pair
    :type plane: struct dpu_multirect_plane_states \*

.. _`dpu_plane_clear_multirect`:

dpu_plane_clear_multirect
=========================

.. c:function:: void dpu_plane_clear_multirect(const struct drm_plane_state *drm_state)

    clear multirect bits for the given pipe

    :param drm_state:
        Pointer to DRM plane state
    :type drm_state: const struct drm_plane_state \*

.. _`dpu_plane_wait_input_fence`:

dpu_plane_wait_input_fence
==========================

.. c:function:: int dpu_plane_wait_input_fence(struct drm_plane *plane, uint32_t wait_ms)

    wait for input fence object

    :param plane:
        Pointer to DRM plane object
    :type plane: struct drm_plane \*

    :param wait_ms:
        Wait timeout value
    :type wait_ms: uint32_t

.. _`dpu_plane_wait_input_fence.return`:

Return
------

Zero on success

.. _`dpu_plane_color_fill`:

dpu_plane_color_fill
====================

.. c:function:: int dpu_plane_color_fill(struct drm_plane *plane, uint32_t color, uint32_t alpha)

    enables color fill on plane

    :param plane:
        Pointer to DRM plane object
    :type plane: struct drm_plane \*

    :param color:
        RGB fill color value, [23..16] Blue, [15..8] Green, [7..0] Red
    :type color: uint32_t

    :param alpha:
        8-bit fill alpha value, 255 selects 100% alpha
    :type alpha: uint32_t

.. _`dpu_plane_color_fill.return`:

Return
------

0 on success

.. _`dpu_plane_set_revalidate`:

dpu_plane_set_revalidate
========================

.. c:function:: void dpu_plane_set_revalidate(struct drm_plane *plane, bool enable)

    sets revalidate flag which forces a full validation of the plane properties in the next atomic check

    :param plane:
        Pointer to DRM plane object
    :type plane: struct drm_plane \*

    :param enable:
        Boolean to set/unset the flag
    :type enable: bool

.. This file was automatic generated / don't edit.

