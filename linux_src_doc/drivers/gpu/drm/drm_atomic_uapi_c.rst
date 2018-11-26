.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_atomic_uapi.c

.. _`overview`:

overview
========

This file contains the marshalling and demarshalling glue for the atomic UAPI
in all it's form: The monster ATOMIC IOCTL itself, code for GET_PROPERTY and
SET_PROPERTY IOCTls. Plus interface functions for compatibility helpers and
drivers which have special needs to construct their own atomic updates, e.g.
for load detect or similiar.

.. _`drm_atomic_set_mode_for_crtc`:

drm_atomic_set_mode_for_crtc
============================

.. c:function:: int drm_atomic_set_mode_for_crtc(struct drm_crtc_state *state, const struct drm_display_mode *mode)

    set mode for CRTC

    :param state:
        the CRTC whose incoming state to update
    :type state: struct drm_crtc_state \*

    :param mode:
        kernel-internal mode to use for the CRTC, or NULL to disable
    :type mode: const struct drm_display_mode \*

.. _`drm_atomic_set_mode_for_crtc.description`:

Description
-----------

Set a mode (originating from the kernel) on the desired CRTC state and update
the enable property.

.. _`drm_atomic_set_mode_for_crtc.return`:

Return
------

Zero on success, error code on failure. Cannot return -EDEADLK.

.. _`drm_atomic_set_mode_prop_for_crtc`:

drm_atomic_set_mode_prop_for_crtc
=================================

.. c:function:: int drm_atomic_set_mode_prop_for_crtc(struct drm_crtc_state *state, struct drm_property_blob *blob)

    set mode for CRTC

    :param state:
        the CRTC whose incoming state to update
    :type state: struct drm_crtc_state \*

    :param blob:
        pointer to blob property to use for mode
    :type blob: struct drm_property_blob \*

.. _`drm_atomic_set_mode_prop_for_crtc.description`:

Description
-----------

Set a mode (originating from a blob property) on the desired CRTC state.
This function will take a reference on the blob property for the CRTC state,
and release the reference held on the state's existing mode property, if any
was set.

.. _`drm_atomic_set_mode_prop_for_crtc.return`:

Return
------

Zero on success, error code on failure. Cannot return -EDEADLK.

.. _`drm_atomic_set_crtc_for_plane`:

drm_atomic_set_crtc_for_plane
=============================

.. c:function:: int drm_atomic_set_crtc_for_plane(struct drm_plane_state *plane_state, struct drm_crtc *crtc)

    set crtc for plane

    :param plane_state:
        the plane whose incoming state to update
    :type plane_state: struct drm_plane_state \*

    :param crtc:
        crtc to use for the plane
    :type crtc: struct drm_crtc \*

.. _`drm_atomic_set_crtc_for_plane.description`:

Description
-----------

Changing the assigned crtc for a plane requires us to grab the lock and state
for the new crtc, as needed. This function takes care of all these details
besides updating the pointer in the state object itself.

.. _`drm_atomic_set_crtc_for_plane.return`:

Return
------

0 on success or can fail with -EDEADLK or -ENOMEM. When the error is EDEADLK
then the w/w mutex code has detected a deadlock and the entire atomic
sequence must be restarted. All other errors are fatal.

.. _`drm_atomic_set_fb_for_plane`:

drm_atomic_set_fb_for_plane
===========================

.. c:function:: void drm_atomic_set_fb_for_plane(struct drm_plane_state *plane_state, struct drm_framebuffer *fb)

    set framebuffer for plane

    :param plane_state:
        atomic state object for the plane
    :type plane_state: struct drm_plane_state \*

    :param fb:
        fb to use for the plane
    :type fb: struct drm_framebuffer \*

.. _`drm_atomic_set_fb_for_plane.description`:

Description
-----------

Changing the assigned framebuffer for a plane requires us to grab a reference
to the new fb and drop the reference to the old fb, if there is one. This
function takes care of all these details besides updating the pointer in the
state object itself.

.. _`drm_atomic_set_fence_for_plane`:

drm_atomic_set_fence_for_plane
==============================

.. c:function:: void drm_atomic_set_fence_for_plane(struct drm_plane_state *plane_state, struct dma_fence *fence)

    set fence for plane

    :param plane_state:
        atomic state object for the plane
    :type plane_state: struct drm_plane_state \*

    :param fence:
        dma_fence to use for the plane
    :type fence: struct dma_fence \*

.. _`drm_atomic_set_fence_for_plane.description`:

Description
-----------

Helper to setup the plane_state fence in case it is not set yet.
By using this drivers doesn't need to worry if the user choose
implicit or explicit fencing.

This function will not set the fence to the state if it was set
via explicit fencing interfaces on the atomic ioctl. In that case it will
drop the reference to the fence as we are not storing it anywhere.
Otherwise, if \ :c:type:`drm_plane_state.fence <drm_plane_state>`\  is not set this function we just set it
with the received implicit fence. In both cases this function consumes a
reference for \ ``fence``\ .

This way explicit fencing can be used to overrule implicit fencing, which is
important to make explicit fencing use-cases work: One example is using one
buffer for 2 screens with different refresh rates. Implicit fencing will
clamp rendering to the refresh rate of the slower screen, whereas explicit
fence allows 2 independent render and display loops on a single buffer. If a
driver allows obeys both implicit and explicit fences for plane updates, then
it will break all the benefits of explicit fencing.

.. _`drm_atomic_set_crtc_for_connector`:

drm_atomic_set_crtc_for_connector
=================================

.. c:function:: int drm_atomic_set_crtc_for_connector(struct drm_connector_state *conn_state, struct drm_crtc *crtc)

    set crtc for connector

    :param conn_state:
        atomic state object for the connector
    :type conn_state: struct drm_connector_state \*

    :param crtc:
        crtc to use for the connector
    :type crtc: struct drm_crtc \*

.. _`drm_atomic_set_crtc_for_connector.description`:

Description
-----------

Changing the assigned crtc for a connector requires us to grab the lock and
state for the new crtc, as needed. This function takes care of all these
details besides updating the pointer in the state object itself.

.. _`drm_atomic_set_crtc_for_connector.return`:

Return
------

0 on success or can fail with -EDEADLK or -ENOMEM. When the error is EDEADLK
then the w/w mutex code has detected a deadlock and the entire atomic
sequence must be restarted. All other errors are fatal.

.. _`explicit-fencing-properties`:

explicit fencing properties
===========================

Explicit fencing allows userspace to control the buffer synchronization
between devices. A Fence or a group of fences are transfered to/from
userspace using Sync File fds and there are two DRM properties for that.
IN_FENCE_FD on each DRM Plane to send fences to the kernel and
OUT_FENCE_PTR on each DRM CRTC to receive fences from the kernel.

As a contrast, with implicit fencing the kernel keeps track of any
ongoing rendering, and automatically ensures that the atomic update waits
for any pending rendering to complete. For shared buffers represented with
a \ :c:type:`struct dma_buf <dma_buf>`\  this is tracked in \ :c:type:`struct reservation_object <reservation_object>`\ .
Implicit syncing is how Linux traditionally worked (e.g. DRI2/3 on X.org),
whereas explicit fencing is what Android wants.

"IN_FENCE_FD”:
     Use this property to pass a fence that DRM should wait on before
     proceeding with the Atomic Commit request and show the framebuffer for
     the plane on the screen. The fence can be either a normal fence or a
     merged one, the sync_file framework will handle both cases and use a
     fence_array if a merged fence is received. Passing -1 here means no
     fences to wait on.

     If the Atomic Commit request has the DRM_MODE_ATOMIC_TEST_ONLY flag
     it will only check if the Sync File is a valid one.

     On the driver side the fence is stored on the \ ``fence``\  parameter of
     \ :c:type:`struct drm_plane_state <drm_plane_state>`\ . Drivers which also support implicit fencing
     should set the implicit fence using \ :c:func:`drm_atomic_set_fence_for_plane`\ ,
     to make sure there's consistent behaviour between drivers in precedence
     of implicit vs. explicit fencing.

"OUT_FENCE_PTR”:
     Use this property to pass a file descriptor pointer to DRM. Once the
     Atomic Commit request call returns OUT_FENCE_PTR will be filled with
     the file descriptor number of a Sync File. This Sync File contains the
     CRTC fence that will be signaled when all framebuffers present on the
     Atomic Commit * request for that given CRTC are scanned out on the
     screen.

     The Atomic Commit request fails if a invalid pointer is passed. If the
     Atomic Commit request fails for any other reason the out fence fd
     returned will be -1. On a Atomic Commit with the
     DRM_MODE_ATOMIC_TEST_ONLY flag the out fence will also be set to -1.

     Note that out-fences don't have a special interface to drivers and are
     internally represented by a \ :c:type:`struct drm_pending_vblank_event <drm_pending_vblank_event>`\  in struct
     \ :c:type:`struct drm_crtc_state <drm_crtc_state>`\ , which is also used by the nonblocking atomic commit
     helpers and for the DRM event handling for existing userspace.

.. This file was automatic generated / don't edit.

