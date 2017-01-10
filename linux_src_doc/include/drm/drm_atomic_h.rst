.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_atomic.h

.. _`drm_crtc_commit`:

struct drm_crtc_commit
======================

.. c:type:: struct drm_crtc_commit

    track modeset commits on a CRTC

.. _`drm_crtc_commit.definition`:

Definition
----------

.. code-block:: c

    struct drm_crtc_commit {
        struct drm_crtc *crtc;
        struct kref ref;
        struct completion flip_done;
        struct completion hw_done;
        struct completion cleanup_done;
        struct list_head commit_entry;
        struct drm_pending_vblank_event *event;
    }

.. _`drm_crtc_commit.members`:

Members
-------

crtc

    DRM CRTC for this commit.

ref

    Reference count for this structure. Needed to allow blocking on
    completions without the risk of the completion disappearing
    meanwhile.

flip_done

    Will be signaled when the hardware has flipped to the new set of
    buffers. Signals at the same time as when the drm event for this
    commit is sent to userspace, or when an out-fence is singalled. Note
    that for most hardware, in most cases this happens after \ ``hw_done``\  is
    signalled.

hw_done

    Will be signalled when all hw register changes for this commit have
    been written out. Especially when disabling a pipe this can be much
    later than than \ ``flip_done``\ , since that can signal already when the
    screen goes black, whereas to fully shut down a pipe more register
    I/O is required.

    Note that this does not need to include separately reference-counted
    resources like backing storage buffer pinning, or runtime pm
    management.

cleanup_done

    Will be signalled after old buffers have been cleaned up by calling
    \ :c:func:`drm_atomic_helper_cleanup_planes`\ . Since this can only happen after
    a vblank wait completed it might be a bit later. This completion is
    useful to throttle updates and avoid hardware updates getting ahead
    of the buffer cleanup too much.

commit_entry

    Entry on the per-CRTC commit_list. Protected by crtc->commit_lock.

event

    \ :c:type:`struct drm_pending_vblank_event <drm_pending_vblank_event>`\  pointer to clean up private events.

.. _`drm_crtc_commit.description`:

Description
-----------

This structure is used to track pending modeset changes and atomic commit on
a per-CRTC basis. Since updating the list should never block this structure
is reference counted to allow waiters to safely wait on an event to complete,
without holding any locks.

It has 3 different events in total to allow a fine-grained synchronization
between outstanding updates::

     atomic commit thread                    hardware

     write new state into hardware   ---->   ...
     signal hw_done
                                             switch to new state on next
     ...                                     v/hblank

     wait for buffers to show up             ...

     ...                                     send completion irq
                                             irq handler signals flip_done
     cleanup old buffers

     signal cleanup_done

     wait for flip_done              <----
     clean up atomic state

The important bit to know is that cleanup_done is the terminal event, but the
ordering between flip_done and hw_done is entirely up to the specific driver
and modeset state change.

For an implementation of how to use this look at
\ :c:func:`drm_atomic_helper_setup_commit`\  from the atomic helper library.

.. _`drm_atomic_state`:

struct drm_atomic_state
=======================

.. c:type:: struct drm_atomic_state

    the global state object for atomic updates

.. _`drm_atomic_state.definition`:

Definition
----------

.. code-block:: c

    struct drm_atomic_state {
        struct kref ref;
        struct drm_device *dev;
        bool allow_modeset:1;
        bool legacy_cursor_update:1;
        bool legacy_set_config:1;
        struct __drm_planes_state *planes;
        struct __drm_crtcs_state *crtcs;
        int num_connector;
        struct __drm_connnectors_state *connectors;
        struct drm_modeset_acquire_ctx *acquire_ctx;
        struct work_struct commit_work;
    }

.. _`drm_atomic_state.members`:

Members
-------

ref
    count of all references to this state (will not be freed until zero)

dev
    parent DRM device

allow_modeset
    allow full modeset

legacy_cursor_update
    hint to enforce legacy cursor IOCTL semantics

legacy_set_config
    Disable conflicting encoders instead of failing with -EINVAL.

planes
    pointer to array of structures with per-plane data

crtcs
    pointer to array of CRTC pointers

num_connector
    size of the \ ``connectors``\  and \ ``connector_states``\  arrays

connectors
    pointer to array of structures with per-connector data

acquire_ctx
    acquire context for this atomic modeset state update

commit_work

    Work item which can be used by the driver or helpers to execute the
    commit without blocking.

.. _`drm_atomic_state_get`:

drm_atomic_state_get
====================

.. c:function:: struct drm_atomic_state *drm_atomic_state_get(struct drm_atomic_state *state)

    acquire a reference to the atomic state

    :param struct drm_atomic_state \*state:
        The atomic state

.. _`drm_atomic_state_get.description`:

Description
-----------

Returns a new reference to the \ ``state``\ 

.. _`drm_atomic_state_put`:

drm_atomic_state_put
====================

.. c:function:: void drm_atomic_state_put(struct drm_atomic_state *state)

    release a reference to the atomic state

    :param struct drm_atomic_state \*state:
        The atomic state

.. _`drm_atomic_state_put.description`:

Description
-----------

This releases a reference to \ ``state``\  which is freed after removing the
final reference. No locking required and callable from any context.

.. _`drm_atomic_get_existing_crtc_state`:

drm_atomic_get_existing_crtc_state
==================================

.. c:function:: struct drm_crtc_state *drm_atomic_get_existing_crtc_state(struct drm_atomic_state *state, struct drm_crtc *crtc)

    get crtc state, if it exists

    :param struct drm_atomic_state \*state:
        global atomic state object

    :param struct drm_crtc \*crtc:
        crtc to grab

.. _`drm_atomic_get_existing_crtc_state.description`:

Description
-----------

This function returns the crtc state for the given crtc, or NULL
if the crtc is not part of the global atomic state.

.. _`drm_atomic_get_existing_plane_state`:

drm_atomic_get_existing_plane_state
===================================

.. c:function:: struct drm_plane_state *drm_atomic_get_existing_plane_state(struct drm_atomic_state *state, struct drm_plane *plane)

    get plane state, if it exists

    :param struct drm_atomic_state \*state:
        global atomic state object

    :param struct drm_plane \*plane:
        plane to grab

.. _`drm_atomic_get_existing_plane_state.description`:

Description
-----------

This function returns the plane state for the given plane, or NULL
if the plane is not part of the global atomic state.

.. _`drm_atomic_get_existing_connector_state`:

drm_atomic_get_existing_connector_state
=======================================

.. c:function:: struct drm_connector_state *drm_atomic_get_existing_connector_state(struct drm_atomic_state *state, struct drm_connector *connector)

    get connector state, if it exists

    :param struct drm_atomic_state \*state:
        global atomic state object

    :param struct drm_connector \*connector:
        connector to grab

.. _`drm_atomic_get_existing_connector_state.description`:

Description
-----------

This function returns the connector state for the given connector,
or NULL if the connector is not part of the global atomic state.

.. _`__drm_atomic_get_current_plane_state`:

__drm_atomic_get_current_plane_state
====================================

.. c:function:: const struct drm_plane_state *__drm_atomic_get_current_plane_state(struct drm_atomic_state *state, struct drm_plane *plane)

    get current plane state

    :param struct drm_atomic_state \*state:
        global atomic state object

    :param struct drm_plane \*plane:
        plane to grab

.. _`__drm_atomic_get_current_plane_state.description`:

Description
-----------

This function returns the plane state for the given plane, either from
\ ``state``\ , or if the plane isn't part of the atomic state update, from \ ``plane``\ .
This is useful in atomic check callbacks, when drivers need to peek at, but
not change, state of other planes, since it avoids threading an error code
back up the call chain.

.. _`__drm_atomic_get_current_plane_state.warning`:

WARNING
-------


Note that this function is in general unsafe since it doesn't check for the
required locking for access state structures. Drivers must ensure that it is
safe to access the returned state structure through other means. One common
example is when planes are fixed to a single CRTC, and the driver knows that
the CRTC lock is held already. In that case holding the CRTC lock gives a
read-lock on all planes connected to that CRTC. But if planes can be
reassigned things get more tricky. In that case it's better to use
drm_atomic_get_plane_state and wire up full error handling.

.. _`__drm_atomic_get_current_plane_state.return`:

Return
------


Read-only pointer to the current plane state.

.. _`drm_atomic_crtc_needs_modeset`:

drm_atomic_crtc_needs_modeset
=============================

.. c:function:: bool drm_atomic_crtc_needs_modeset(const struct drm_crtc_state *state)

    compute combined modeset need

    :param const struct drm_crtc_state \*state:
        &drm_crtc_state for the CRTC

.. _`drm_atomic_crtc_needs_modeset.description`:

Description
-----------

To give drivers flexibility struct \ :c:type:`struct drm_crtc_state <drm_crtc_state>`\  has 3 booleans to track

.. _`drm_atomic_crtc_needs_modeset.whether-the-state-crtc-changed-enough-to-need-a-full-modeset-cycle`:

whether the state CRTC changed enough to need a full modeset cycle
------------------------------------------------------------------

connectors_changed, mode_changed and active_changed. This helper simply
combines these three to compute the overall need for a modeset for \ ``state``\ .

The atomic helper code sets these booleans, but drivers can and should
change them appropriately to accurately represent whether a modeset is
really needed. In general, drivers should avoid full modesets whenever
possible.

For example if the CRTC mode has changed, and the hardware is able to enact
the requested mode change without going through a full modeset, the driver
should clear mode_changed during its ->atomic_check.

.. This file was automatic generated / don't edit.

