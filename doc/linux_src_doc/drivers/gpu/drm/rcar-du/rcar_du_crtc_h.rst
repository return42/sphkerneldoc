.. -*- coding: utf-8; mode: rst -*-

==============
rcar_du_crtc.h
==============


.. _`rcar_du_crtc`:

struct rcar_du_crtc
===================

.. c:type:: rcar_du_crtc

    the CRTC, representing a DU superposition processor


.. _`rcar_du_crtc.definition`:

Definition
----------

.. code-block:: c

  struct rcar_du_crtc {
    struct drm_crtc crtc;
    struct clk * clock;
    struct clk * extclock;
    unsigned int mmio_offset;
    unsigned int index;
    bool started;
    struct drm_pending_vblank_event * event;
    wait_queue_head_t flip_wait;
    unsigned int outputs;
    struct rcar_du_group * group;
  };


.. _`rcar_du_crtc.members`:

Members
-------

:``crtc``:
    base DRM CRTC

:``clock``:
    the CRTC functional clock

:``extclock``:
    external pixel dot clock (optional)

:``mmio_offset``:
    offset of the CRTC registers in the DU MMIO block

:``index``:
    CRTC software and hardware index

:``started``:
    whether the CRTC has been started and is running

:``event``:
    event to post when the pending page flip completes

:``flip_wait``:
    wait queue used to signal page flip completion

:``outputs``:
    bitmask of the outputs (enum rcar_du_output) driven by this CRTC

:``group``:
    CRTC group this CRTC belongs to


