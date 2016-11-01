.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_irq.h

.. _`drm_pending_vblank_event`:

struct drm_pending_vblank_event
===============================

.. c:type:: struct drm_pending_vblank_event

    pending vblank event tracking

.. _`drm_pending_vblank_event.definition`:

Definition
----------

.. code-block:: c

    struct drm_pending_vblank_event {
        struct drm_pending_event base;
        unsigned int pipe;
        struct drm_event_vblank event;
    }

.. _`drm_pending_vblank_event.members`:

Members
-------

base
    Base structure for tracking pending DRM events.

pipe
    drm_crtc_index() of the \ :c:type:`struct drm_crtc <drm_crtc>`\  this event is for.

event
    Actual event which will be sent to userspace.

.. _`drm_vblank_crtc`:

struct drm_vblank_crtc
======================

.. c:type:: struct drm_vblank_crtc

    vblank tracking for a CRTC

.. _`drm_vblank_crtc.definition`:

Definition
----------

.. code-block:: c

    struct drm_vblank_crtc {
        struct drm_device *dev;
        wait_queue_head_t queue;
        struct timer_list disable_timer;
        seqlock_t seqlock;
        u32 count;
        struct timeval time;
        atomic_t refcount;
        u32 last;
        unsigned int inmodeset;
        unsigned int pipe;
        int framedur_ns;
        int linedur_ns;
        bool enabled;
    }

.. _`drm_vblank_crtc.members`:

Members
-------

dev
    Pointer to the \ :c:type:`struct drm_device <drm_device>`\ .

queue
    Wait queue for vblank waiters.

disable_timer
    Disable timer for the delayed vblank disablinghysteresis logic. Vblank disabling is controlled through the
    drm_vblank_offdelay module option and the setting of the
    max_vblank_count value in the \ :c:type:`struct drm_device <drm_device>`\  structure.

seqlock
    Protect vblank count and time.

count
    Current software vblank counter.

time
    Vblank timestamp corresponding to \ ``count``\ .

refcount
    Number of users/waiters of the vblank interrupt. Only whenthis refcount reaches 0 can the hardware interrupt be disabled using
    \ ``disable_timer``\ .

last
    Protected by dev->vbl_lock, used for wraparound handling.

inmodeset
    Tracks whether the vblank is disabled due to a modeset.For legacy driver bit 2 additionally tracks whether an additional
    temporary vblank reference has been acquired to paper over the
    hardware counter resetting/jumping. KMS drivers should instead just
    call \ :c:func:`drm_crtc_vblank_off`\  and \ :c:func:`drm_crtc_vblank_on`\ , which explicitly
    save and restore the vblank count.

pipe
    drm_crtc_index() of the \ :c:type:`struct drm_crtc <drm_crtc>`\  corresponding to thisstructure.

framedur_ns
    Frame/Field duration in ns, used \ :c:func:`bydrm_calc_vbltimestamp_from_scanoutpos`\  and computed by
    \ :c:func:`drm_calc_timestamping_constants`\ .

linedur_ns
    Line duration in ns, used \ :c:func:`bydrm_calc_vbltimestamp_from_scanoutpos`\  and computed by
    \ :c:func:`drm_calc_timestamping_constants`\ .

enabled
    Tracks the enabling state of the corresponding \ :c:type:`struct drm_crtc <drm_crtc>`\  toavoid double-disabling and hence corrupting saved state. Needed by
    drivers not using atomic KMS, since those might go through their CRTC
    disabling functions multiple times.

.. _`drm_vblank_crtc.description`:

Description
-----------

This structure tracks the vblank state for one CRTC.

Note that for historical reasons - the vblank handling code is still shared
with legacy/non-kms drivers - this is a free-standing structure not directly
connected to struct \ :c:type:`struct drm_crtc <drm_crtc>`\ . But all public interface functions are taking
a struct \ :c:type:`struct drm_crtc <drm_crtc>`\  to hide this implementation detail.

.. _`drm_crtc_vblank_waitqueue`:

drm_crtc_vblank_waitqueue
=========================

.. c:function:: wait_queue_head_t *drm_crtc_vblank_waitqueue(struct drm_crtc *crtc)

    get vblank waitqueue for the CRTC

    :param struct drm_crtc \*crtc:
        which CRTC's vblank waitqueue to retrieve

.. _`drm_crtc_vblank_waitqueue.description`:

Description
-----------

This function returns a pointer to the vblank waitqueue for the CRTC.
Drivers can use this to implement vblank waits using \ :c:func:`wait_event`\  and related
functions.

.. This file was automatic generated / don't edit.

