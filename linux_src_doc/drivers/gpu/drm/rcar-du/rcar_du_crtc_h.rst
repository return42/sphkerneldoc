.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/rcar-du/rcar_du_crtc.h

.. _`rcar_du_crtc`:

struct rcar_du_crtc
===================

.. c:type:: struct rcar_du_crtc

    the CRTC, representing a DU superposition processor

.. _`rcar_du_crtc.definition`:

Definition
----------

.. code-block:: c

    struct rcar_du_crtc {
        struct drm_crtc crtc;
        struct clk *clock;
        struct clk *extclock;
        unsigned int mmio_offset;
        unsigned int index;
        bool initialized;
        bool vblank_enable;
        struct drm_pending_vblank_event *event;
        wait_queue_head_t flip_wait;
        spinlock_t vblank_lock;
        wait_queue_head_t vblank_wait;
        unsigned int vblank_count;
        unsigned int outputs;
        struct rcar_du_group *group;
        struct rcar_du_vsp *vsp;
        unsigned int vsp_pipe;
    }

.. _`rcar_du_crtc.members`:

Members
-------

crtc
    base DRM CRTC

clock
    the CRTC functional clock

extclock
    external pixel dot clock (optional)

mmio_offset
    offset of the CRTC registers in the DU MMIO block

index
    CRTC software and hardware index

initialized
    whether the CRTC has been initialized and clocks enabled

vblank_enable
    whether vblank events are enabled on this CRTC

event
    event to post when the pending page flip completes

flip_wait
    wait queue used to signal page flip completion

vblank_lock
    protects vblank_wait and vblank_count

vblank_wait
    wait queue used to signal vertical blanking

vblank_count
    number of vertical blanking interrupts to wait for

outputs
    bitmask of the outputs (enum rcar_du_output) driven by this CRTC

group
    CRTC group this CRTC belongs to

vsp
    VSP feeding video to this CRTC

vsp_pipe
    index of the VSP pipeline feeding video to this CRTC

.. This file was automatic generated / don't edit.

