.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_atomic.c

.. _`drm_atomic_state_default_release`:

drm_atomic_state_default_release
================================

.. c:function:: void drm_atomic_state_default_release(struct drm_atomic_state *state)

    release memory initialized by drm_atomic_state_init

    :param state:
        atomic state
    :type state: struct drm_atomic_state \*

.. _`drm_atomic_state_default_release.description`:

Description
-----------

Free all the memory allocated by drm_atomic_state_init.
This should only be used by drivers which are still subclassing
\ :c:type:`struct drm_atomic_state <drm_atomic_state>`\  and haven't switched to \ :c:type:`struct drm_private_state <drm_private_state>`\  yet.

.. _`drm_atomic_state_init`:

drm_atomic_state_init
=====================

.. c:function:: int drm_atomic_state_init(struct drm_device *dev, struct drm_atomic_state *state)

    init new atomic state

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param state:
        atomic state
    :type state: struct drm_atomic_state \*

.. _`drm_atomic_state_init.description`:

Description
-----------

Default implementation for filling in a new atomic state.
This should only be used by drivers which are still subclassing
\ :c:type:`struct drm_atomic_state <drm_atomic_state>`\  and haven't switched to \ :c:type:`struct drm_private_state <drm_private_state>`\  yet.

.. _`drm_atomic_state_alloc`:

drm_atomic_state_alloc
======================

.. c:function:: struct drm_atomic_state *drm_atomic_state_alloc(struct drm_device *dev)

    allocate atomic state

    :param dev:
        DRM device
    :type dev: struct drm_device \*

.. _`drm_atomic_state_alloc.description`:

Description
-----------

This allocates an empty atomic state to track updates.

.. _`drm_atomic_state_default_clear`:

drm_atomic_state_default_clear
==============================

.. c:function:: void drm_atomic_state_default_clear(struct drm_atomic_state *state)

    clear base atomic state

    :param state:
        atomic state
    :type state: struct drm_atomic_state \*

.. _`drm_atomic_state_default_clear.description`:

Description
-----------

Default implementation for clearing atomic state.
This should only be used by drivers which are still subclassing
\ :c:type:`struct drm_atomic_state <drm_atomic_state>`\  and haven't switched to \ :c:type:`struct drm_private_state <drm_private_state>`\  yet.

.. _`drm_atomic_state_clear`:

drm_atomic_state_clear
======================

.. c:function:: void drm_atomic_state_clear(struct drm_atomic_state *state)

    clear state object

    :param state:
        atomic state
    :type state: struct drm_atomic_state \*

.. _`drm_atomic_state_clear.description`:

Description
-----------

When the w/w mutex algorithm detects a deadlock we need to back off and drop
all locks. So someone else could sneak in and change the current modeset
configuration. Which means that all the state assembled in \ ``state``\  is no
longer an atomic update to the current state, but to some arbitrary earlier
state. Which could break assumptions the driver's
\ :c:type:`drm_mode_config_funcs.atomic_check <drm_mode_config_funcs>`\  likely relies on.

Hence we must clear all cached state and completely start over, using this
function.

.. _`__drm_atomic_state_free`:

__drm_atomic_state_free
=======================

.. c:function:: void __drm_atomic_state_free(struct kref *ref)

    free all memory for an atomic state

    :param ref:
        This atomic state to deallocate
    :type ref: struct kref \*

.. _`__drm_atomic_state_free.description`:

Description
-----------

This frees all memory associated with an atomic state, including all the
per-object state for planes, crtcs and connectors.

.. _`drm_atomic_get_crtc_state`:

drm_atomic_get_crtc_state
=========================

.. c:function:: struct drm_crtc_state *drm_atomic_get_crtc_state(struct drm_atomic_state *state, struct drm_crtc *crtc)

    get crtc state

    :param state:
        global atomic state object
    :type state: struct drm_atomic_state \*

    :param crtc:
        crtc to get state object for
    :type crtc: struct drm_crtc \*

.. _`drm_atomic_get_crtc_state.description`:

Description
-----------

This function returns the crtc state for the given crtc, allocating it if
needed. It will also grab the relevant crtc lock to make sure that the state
is consistent.

.. _`drm_atomic_get_crtc_state.return`:

Return
------


Either the allocated state or the error code encoded into the pointer. When
the error is EDEADLK then the w/w mutex code has detected a deadlock and the
entire atomic sequence must be restarted. All other errors are fatal.

.. _`drm_atomic_get_plane_state`:

drm_atomic_get_plane_state
==========================

.. c:function:: struct drm_plane_state *drm_atomic_get_plane_state(struct drm_atomic_state *state, struct drm_plane *plane)

    get plane state

    :param state:
        global atomic state object
    :type state: struct drm_atomic_state \*

    :param plane:
        plane to get state object for
    :type plane: struct drm_plane \*

.. _`drm_atomic_get_plane_state.description`:

Description
-----------

This function returns the plane state for the given plane, allocating it if
needed. It will also grab the relevant plane lock to make sure that the state
is consistent.

.. _`drm_atomic_get_plane_state.return`:

Return
------


Either the allocated state or the error code encoded into the pointer. When
the error is EDEADLK then the w/w mutex code has detected a deadlock and the
entire atomic sequence must be restarted. All other errors are fatal.

.. _`drm_atomic_plane_check`:

drm_atomic_plane_check
======================

.. c:function:: int drm_atomic_plane_check(struct drm_plane *plane, struct drm_plane_state *state)

    check plane state

    :param plane:
        plane to check
    :type plane: struct drm_plane \*

    :param state:
        plane state to check
    :type state: struct drm_plane_state \*

.. _`drm_atomic_plane_check.description`:

Description
-----------

Provides core sanity checks for plane state.

.. _`drm_atomic_plane_check.return`:

Return
------

Zero on success, error code on failure

.. _`handling-driver-private-state`:

handling driver private state
=============================

Very often the DRM objects exposed to userspace in the atomic modeset api
(&drm_connector, \ :c:type:`struct drm_crtc <drm_crtc>`\  and \ :c:type:`struct drm_plane <drm_plane>`\ ) do not map neatly to the
underlying hardware. Especially for any kind of shared resources (e.g. shared
clocks, scaler units, bandwidth and fifo limits shared among a group of
planes or CRTCs, and so on) it makes sense to model these as independent
objects. Drivers then need to do similar state tracking and commit ordering for
such private (since not exposed to userpace) objects as the atomic core and
helpers already provide for connectors, planes and CRTCs.

To make this easier on drivers the atomic core provides some support to track
driver private state objects using struct \ :c:type:`struct drm_private_obj <drm_private_obj>`\ , with the
associated state struct \ :c:type:`struct drm_private_state <drm_private_state>`\ .

Similar to userspace-exposed objects, private state structures can be
acquired by calling \ :c:func:`drm_atomic_get_private_obj_state`\ . Since this function
does not take care of locking, drivers should wrap it for each type of
private state object they have with the required call to \ :c:func:`drm_modeset_lock`\ 
for the corresponding \ :c:type:`struct drm_modeset_lock <drm_modeset_lock>`\ .

All private state structures contained in a \ :c:type:`struct drm_atomic_state <drm_atomic_state>`\  update can be
iterated using \ :c:func:`for_each_oldnew_private_obj_in_state`\ ,
\ :c:func:`for_each_new_private_obj_in_state`\  and \ :c:func:`for_each_old_private_obj_in_state`\ .
Drivers are recommended to wrap these for each type of driver private state
object they have, filtering on \ :c:type:`drm_private_obj.funcs <drm_private_obj>`\  using \ :c:func:`for_each_if`\ , at
least if they want to iterate over all objects of a given type.

An earlier way to handle driver private state was by subclassing struct
\ :c:type:`struct drm_atomic_state <drm_atomic_state>`\ . But since that encourages non-standard ways to implement
the check/commit split atomic requires (by using e.g. "check and rollback or
commit instead" of "duplicate state, check, then either commit or release
duplicated state) it is deprecated in favour of using \ :c:type:`struct drm_private_state <drm_private_state>`\ .

.. _`drm_atomic_private_obj_init`:

drm_atomic_private_obj_init
===========================

.. c:function:: void drm_atomic_private_obj_init(struct drm_private_obj *obj, struct drm_private_state *state, const struct drm_private_state_funcs *funcs)

    initialize private object

    :param obj:
        private object
    :type obj: struct drm_private_obj \*

    :param state:
        initial private object state
    :type state: struct drm_private_state \*

    :param funcs:
        pointer to the struct of function pointers that identify the object
        type
    :type funcs: const struct drm_private_state_funcs \*

.. _`drm_atomic_private_obj_init.description`:

Description
-----------

Initialize the private object, which can be embedded into any
driver private object that needs its own atomic state.

.. _`drm_atomic_private_obj_fini`:

drm_atomic_private_obj_fini
===========================

.. c:function:: void drm_atomic_private_obj_fini(struct drm_private_obj *obj)

    finalize private object

    :param obj:
        private object
    :type obj: struct drm_private_obj \*

.. _`drm_atomic_private_obj_fini.description`:

Description
-----------

Finalize the private object.

.. _`drm_atomic_get_private_obj_state`:

drm_atomic_get_private_obj_state
================================

.. c:function:: struct drm_private_state *drm_atomic_get_private_obj_state(struct drm_atomic_state *state, struct drm_private_obj *obj)

    get private object state

    :param state:
        global atomic state
    :type state: struct drm_atomic_state \*

    :param obj:
        private object to get the state for
    :type obj: struct drm_private_obj \*

.. _`drm_atomic_get_private_obj_state.description`:

Description
-----------

This function returns the private object state for the given private object,
allocating the state if needed. It does not grab any locks as the caller is
expected to care of any required locking.

.. _`drm_atomic_get_private_obj_state.return`:

Return
------


Either the allocated state or the error code encoded into a pointer.

.. _`drm_atomic_get_connector_state`:

drm_atomic_get_connector_state
==============================

.. c:function:: struct drm_connector_state *drm_atomic_get_connector_state(struct drm_atomic_state *state, struct drm_connector *connector)

    get connector state

    :param state:
        global atomic state object
    :type state: struct drm_atomic_state \*

    :param connector:
        connector to get state object for
    :type connector: struct drm_connector \*

.. _`drm_atomic_get_connector_state.description`:

Description
-----------

This function returns the connector state for the given connector,
allocating it if needed. It will also grab the relevant connector lock to
make sure that the state is consistent.

.. _`drm_atomic_get_connector_state.return`:

Return
------


Either the allocated state or the error code encoded into the pointer. When
the error is EDEADLK then the w/w mutex code has detected a deadlock and the
entire atomic sequence must be restarted. All other errors are fatal.

.. _`drm_atomic_add_affected_connectors`:

drm_atomic_add_affected_connectors
==================================

.. c:function:: int drm_atomic_add_affected_connectors(struct drm_atomic_state *state, struct drm_crtc *crtc)

    add connectors for crtc

    :param state:
        atomic state
    :type state: struct drm_atomic_state \*

    :param crtc:
        DRM crtc
    :type crtc: struct drm_crtc \*

.. _`drm_atomic_add_affected_connectors.description`:

Description
-----------

This function walks the current configuration and adds all connectors
currently using \ ``crtc``\  to the atomic configuration \ ``state``\ . Note that this
function must acquire the connection mutex. This can potentially cause
unneeded seralization if the update is just for the planes on one crtc. Hence
drivers and helpers should only call this when really needed (e.g. when a
full modeset needs to happen due to some change).

.. _`drm_atomic_add_affected_connectors.return`:

Return
------

0 on success or can fail with -EDEADLK or -ENOMEM. When the error is EDEADLK
then the w/w mutex code has detected a deadlock and the entire atomic
sequence must be restarted. All other errors are fatal.

.. _`drm_atomic_add_affected_planes`:

drm_atomic_add_affected_planes
==============================

.. c:function:: int drm_atomic_add_affected_planes(struct drm_atomic_state *state, struct drm_crtc *crtc)

    add planes for crtc

    :param state:
        atomic state
    :type state: struct drm_atomic_state \*

    :param crtc:
        DRM crtc
    :type crtc: struct drm_crtc \*

.. _`drm_atomic_add_affected_planes.description`:

Description
-----------

This function walks the current configuration and adds all planes
currently used by \ ``crtc``\  to the atomic configuration \ ``state``\ . This is useful
when an atomic commit also needs to check all currently enabled plane on
\ ``crtc``\ , e.g. when changing the mode. It's also useful when re-enabling a CRTC
to avoid special code to force-enable all planes.

Since acquiring a plane state will always also acquire the w/w mutex of the
current CRTC for that plane (if there is any) adding all the plane states for
a CRTC will not reduce parallism of atomic updates.

.. _`drm_atomic_add_affected_planes.return`:

Return
------

0 on success or can fail with -EDEADLK or -ENOMEM. When the error is EDEADLK
then the w/w mutex code has detected a deadlock and the entire atomic
sequence must be restarted. All other errors are fatal.

.. _`drm_atomic_check_only`:

drm_atomic_check_only
=====================

.. c:function:: int drm_atomic_check_only(struct drm_atomic_state *state)

    check whether a given config would work

    :param state:
        atomic configuration to check
    :type state: struct drm_atomic_state \*

.. _`drm_atomic_check_only.description`:

Description
-----------

Note that this function can return -EDEADLK if the driver needed to acquire
more locks but encountered a deadlock. The caller must then do the usual w/w
backoff dance and restart. All other errors are fatal.

.. _`drm_atomic_check_only.return`:

Return
------

0 on success, negative error code on failure.

.. _`drm_atomic_commit`:

drm_atomic_commit
=================

.. c:function:: int drm_atomic_commit(struct drm_atomic_state *state)

    commit configuration atomically

    :param state:
        atomic configuration to check
    :type state: struct drm_atomic_state \*

.. _`drm_atomic_commit.description`:

Description
-----------

Note that this function can return -EDEADLK if the driver needed to acquire
more locks but encountered a deadlock. The caller must then do the usual w/w
backoff dance and restart. All other errors are fatal.

This function will take its own reference on \ ``state``\ .
Callers should always release their reference with \ :c:func:`drm_atomic_state_put`\ .

.. _`drm_atomic_commit.return`:

Return
------

0 on success, negative error code on failure.

.. _`drm_atomic_nonblocking_commit`:

drm_atomic_nonblocking_commit
=============================

.. c:function:: int drm_atomic_nonblocking_commit(struct drm_atomic_state *state)

    atomic nonblocking commit

    :param state:
        atomic configuration to check
    :type state: struct drm_atomic_state \*

.. _`drm_atomic_nonblocking_commit.description`:

Description
-----------

Note that this function can return -EDEADLK if the driver needed to acquire
more locks but encountered a deadlock. The caller must then do the usual w/w
backoff dance and restart. All other errors are fatal.

This function will take its own reference on \ ``state``\ .
Callers should always release their reference with \ :c:func:`drm_atomic_state_put`\ .

.. _`drm_atomic_nonblocking_commit.return`:

Return
------

0 on success, negative error code on failure.

.. _`drm_state_dump`:

drm_state_dump
==============

.. c:function:: void drm_state_dump(struct drm_device *dev, struct drm_printer *p)

    dump entire device atomic state

    :param dev:
        the drm device
    :type dev: struct drm_device \*

    :param p:
        where to print the state to
    :type p: struct drm_printer \*

.. _`drm_state_dump.description`:

Description
-----------

Just for debugging.  Drivers might want an option to dump state
to dmesg in case of error irq's.  (Hint, you probably want to
ratelimit this!)

The caller must \ :c:func:`drm_modeset_lock_all`\ , or if this is called
from error irq handler, it should not be enabled by default.
(Ie. if you are debugging errors you might not care that this
is racey.  But calling this without all modeset locks held is
not inherently safe.)

.. This file was automatic generated / don't edit.

