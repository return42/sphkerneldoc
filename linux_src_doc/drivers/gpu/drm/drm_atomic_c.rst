.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_atomic.c

.. _`drm_atomic_state_default_release`:

drm_atomic_state_default_release
================================

.. c:function:: void drm_atomic_state_default_release(struct drm_atomic_state *state)

    release memory initialized by drm_atomic_state_init

    :param struct drm_atomic_state \*state:
        atomic state

.. _`drm_atomic_state_default_release.description`:

Description
-----------

Free all the memory allocated by drm_atomic_state_init.
This is useful for drivers that subclass the atomic state.

.. _`drm_atomic_state_init`:

drm_atomic_state_init
=====================

.. c:function:: int drm_atomic_state_init(struct drm_device *dev, struct drm_atomic_state *state)

    init new atomic state

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_atomic_state \*state:
        atomic state

.. _`drm_atomic_state_init.description`:

Description
-----------

Default implementation for filling in a new atomic state.
This is useful for drivers that subclass the atomic state.

.. _`drm_atomic_state_alloc`:

drm_atomic_state_alloc
======================

.. c:function:: struct drm_atomic_state *drm_atomic_state_alloc(struct drm_device *dev)

    allocate atomic state

    :param struct drm_device \*dev:
        DRM device

.. _`drm_atomic_state_alloc.description`:

Description
-----------

This allocates an empty atomic state to track updates.

.. _`drm_atomic_state_default_clear`:

drm_atomic_state_default_clear
==============================

.. c:function:: void drm_atomic_state_default_clear(struct drm_atomic_state *state)

    clear base atomic state

    :param struct drm_atomic_state \*state:
        atomic state

.. _`drm_atomic_state_default_clear.description`:

Description
-----------

Default implementation for clearing atomic state.
This is useful for drivers that subclass the atomic state.

.. _`drm_atomic_state_clear`:

drm_atomic_state_clear
======================

.. c:function:: void drm_atomic_state_clear(struct drm_atomic_state *state)

    clear state object

    :param struct drm_atomic_state \*state:
        atomic state

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

    :param struct kref \*ref:
        This atomic state to deallocate

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

    :param struct drm_atomic_state \*state:
        global atomic state object

    :param struct drm_crtc \*crtc:
        crtc to get state object for

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

.. _`drm_atomic_set_mode_for_crtc`:

drm_atomic_set_mode_for_crtc
============================

.. c:function:: int drm_atomic_set_mode_for_crtc(struct drm_crtc_state *state, const struct drm_display_mode *mode)

    set mode for CRTC

    :param struct drm_crtc_state \*state:
        the CRTC whose incoming state to update

    :param const struct drm_display_mode \*mode:
        kernel-internal mode to use for the CRTC, or NULL to disable

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

    :param struct drm_crtc_state \*state:
        the CRTC whose incoming state to update

    :param struct drm_property_blob \*blob:
        pointer to blob property to use for mode

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

.. _`drm_atomic_crtc_set_property`:

drm_atomic_crtc_set_property
============================

.. c:function:: int drm_atomic_crtc_set_property(struct drm_crtc *crtc, struct drm_crtc_state *state, struct drm_property *property, uint64_t val)

    set property on CRTC

    :param struct drm_crtc \*crtc:
        the drm CRTC to set a property on

    :param struct drm_crtc_state \*state:
        the state object to update with the new property value

    :param struct drm_property \*property:
        the property to set

    :param uint64_t val:
        the new property value

.. _`drm_atomic_crtc_set_property.description`:

Description
-----------

This function handles generic/core properties and calls out to driver's
\ :c:type:`drm_crtc_funcs.atomic_set_property <drm_crtc_funcs>`\  for driver properties. To ensure
consistent behavior you must call this function rather than the driver hook
directly.

.. _`drm_atomic_crtc_set_property.return`:

Return
------

Zero on success, error code on failure

.. _`drm_atomic_crtc_get_property`:

drm_atomic_crtc_get_property
============================

.. c:function:: int drm_atomic_crtc_get_property(struct drm_crtc *crtc, const struct drm_crtc_state *state, struct drm_property *property, uint64_t *val)

    get property value from CRTC state

    :param struct drm_crtc \*crtc:
        the drm CRTC to set a property on

    :param const struct drm_crtc_state \*state:
        the state object to get the property value from

    :param struct drm_property \*property:
        the property to set

    :param uint64_t \*val:
        return location for the property value

.. _`drm_atomic_crtc_get_property.description`:

Description
-----------

This function handles generic/core properties and calls out to driver's
\ :c:type:`drm_crtc_funcs.atomic_get_property <drm_crtc_funcs>`\  for driver properties. To ensure
consistent behavior you must call this function rather than the driver hook
directly.

.. _`drm_atomic_crtc_get_property.return`:

Return
------

Zero on success, error code on failure

.. _`drm_atomic_crtc_check`:

drm_atomic_crtc_check
=====================

.. c:function:: int drm_atomic_crtc_check(struct drm_crtc *crtc, struct drm_crtc_state *state)

    check crtc state

    :param struct drm_crtc \*crtc:
        crtc to check

    :param struct drm_crtc_state \*state:
        crtc state to check

.. _`drm_atomic_crtc_check.description`:

Description
-----------

Provides core sanity checks for crtc state.

.. _`drm_atomic_crtc_check.return`:

Return
------

Zero on success, error code on failure

.. _`drm_atomic_get_plane_state`:

drm_atomic_get_plane_state
==========================

.. c:function:: struct drm_plane_state *drm_atomic_get_plane_state(struct drm_atomic_state *state, struct drm_plane *plane)

    get plane state

    :param struct drm_atomic_state \*state:
        global atomic state object

    :param struct drm_plane \*plane:
        plane to get state object for

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

.. _`drm_atomic_plane_set_property`:

drm_atomic_plane_set_property
=============================

.. c:function:: int drm_atomic_plane_set_property(struct drm_plane *plane, struct drm_plane_state *state, struct drm_property *property, uint64_t val)

    set property on plane

    :param struct drm_plane \*plane:
        the drm plane to set a property on

    :param struct drm_plane_state \*state:
        the state object to update with the new property value

    :param struct drm_property \*property:
        the property to set

    :param uint64_t val:
        the new property value

.. _`drm_atomic_plane_set_property.description`:

Description
-----------

This function handles generic/core properties and calls out to driver's
\ :c:type:`drm_plane_funcs.atomic_set_property <drm_plane_funcs>`\  for driver properties.  To ensure
consistent behavior you must call this function rather than the driver hook
directly.

.. _`drm_atomic_plane_set_property.return`:

Return
------

Zero on success, error code on failure

.. _`drm_atomic_plane_get_property`:

drm_atomic_plane_get_property
=============================

.. c:function:: int drm_atomic_plane_get_property(struct drm_plane *plane, const struct drm_plane_state *state, struct drm_property *property, uint64_t *val)

    get property value from plane state

    :param struct drm_plane \*plane:
        the drm plane to set a property on

    :param const struct drm_plane_state \*state:
        the state object to get the property value from

    :param struct drm_property \*property:
        the property to set

    :param uint64_t \*val:
        return location for the property value

.. _`drm_atomic_plane_get_property.description`:

Description
-----------

This function handles generic/core properties and calls out to driver's
\ :c:type:`drm_plane_funcs.atomic_get_property <drm_plane_funcs>`\  for driver properties.  To ensure
consistent behavior you must call this function rather than the driver hook
directly.

.. _`drm_atomic_plane_get_property.return`:

Return
------

Zero on success, error code on failure

.. _`drm_atomic_plane_check`:

drm_atomic_plane_check
======================

.. c:function:: int drm_atomic_plane_check(struct drm_plane *plane, struct drm_plane_state *state)

    check plane state

    :param struct drm_plane \*plane:
        plane to check

    :param struct drm_plane_state \*state:
        plane state to check

.. _`drm_atomic_plane_check.description`:

Description
-----------

Provides core sanity checks for plane state.

.. _`drm_atomic_plane_check.return`:

Return
------

Zero on success, error code on failure

.. _`drm_atomic_private_obj_init`:

drm_atomic_private_obj_init
===========================

.. c:function:: void drm_atomic_private_obj_init(struct drm_private_obj *obj, struct drm_private_state *state, const struct drm_private_state_funcs *funcs)

    initialize private object

    :param struct drm_private_obj \*obj:
        private object

    :param struct drm_private_state \*state:
        initial private object state

    :param const struct drm_private_state_funcs \*funcs:
        pointer to the struct of function pointers that identify the object
        type

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

    :param struct drm_private_obj \*obj:
        private object

.. _`drm_atomic_private_obj_fini.description`:

Description
-----------

Finalize the private object.

.. _`drm_atomic_get_private_obj_state`:

drm_atomic_get_private_obj_state
================================

.. c:function:: struct drm_private_state *drm_atomic_get_private_obj_state(struct drm_atomic_state *state, struct drm_private_obj *obj)

    get private object state

    :param struct drm_atomic_state \*state:
        global atomic state

    :param struct drm_private_obj \*obj:
        private object to get the state for

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

    :param struct drm_atomic_state \*state:
        global atomic state object

    :param struct drm_connector \*connector:
        connector to get state object for

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

.. _`drm_atomic_connector_set_property`:

drm_atomic_connector_set_property
=================================

.. c:function:: int drm_atomic_connector_set_property(struct drm_connector *connector, struct drm_connector_state *state, struct drm_property *property, uint64_t val)

    set property on connector.

    :param struct drm_connector \*connector:
        the drm connector to set a property on

    :param struct drm_connector_state \*state:
        the state object to update with the new property value

    :param struct drm_property \*property:
        the property to set

    :param uint64_t val:
        the new property value

.. _`drm_atomic_connector_set_property.description`:

Description
-----------

This function handles generic/core properties and calls out to driver's
\ :c:type:`drm_connector_funcs.atomic_set_property <drm_connector_funcs>`\  for driver properties.  To ensure
consistent behavior you must call this function rather than the driver hook
directly.

.. _`drm_atomic_connector_set_property.return`:

Return
------

Zero on success, error code on failure

.. _`drm_atomic_connector_get_property`:

drm_atomic_connector_get_property
=================================

.. c:function:: int drm_atomic_connector_get_property(struct drm_connector *connector, const struct drm_connector_state *state, struct drm_property *property, uint64_t *val)

    get property value from connector state

    :param struct drm_connector \*connector:
        the drm connector to set a property on

    :param const struct drm_connector_state \*state:
        the state object to get the property value from

    :param struct drm_property \*property:
        the property to set

    :param uint64_t \*val:
        return location for the property value

.. _`drm_atomic_connector_get_property.description`:

Description
-----------

This function handles generic/core properties and calls out to driver's
\ :c:type:`drm_connector_funcs.atomic_get_property <drm_connector_funcs>`\  for driver properties.  To ensure
consistent behavior you must call this function rather than the driver hook
directly.

.. _`drm_atomic_connector_get_property.return`:

Return
------

Zero on success, error code on failure

.. _`drm_atomic_set_crtc_for_plane`:

drm_atomic_set_crtc_for_plane
=============================

.. c:function:: int drm_atomic_set_crtc_for_plane(struct drm_plane_state *plane_state, struct drm_crtc *crtc)

    set crtc for plane

    :param struct drm_plane_state \*plane_state:
        the plane whose incoming state to update

    :param struct drm_crtc \*crtc:
        crtc to use for the plane

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

    :param struct drm_plane_state \*plane_state:
        atomic state object for the plane

    :param struct drm_framebuffer \*fb:
        fb to use for the plane

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

    :param struct drm_plane_state \*plane_state:
        atomic state object for the plane

    :param struct dma_fence \*fence:
        dma_fence to use for the plane

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

.. _`drm_atomic_set_crtc_for_connector`:

drm_atomic_set_crtc_for_connector
=================================

.. c:function:: int drm_atomic_set_crtc_for_connector(struct drm_connector_state *conn_state, struct drm_crtc *crtc)

    set crtc for connector

    :param struct drm_connector_state \*conn_state:
        atomic state object for the connector

    :param struct drm_crtc \*crtc:
        crtc to use for the connector

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

.. _`drm_atomic_add_affected_connectors`:

drm_atomic_add_affected_connectors
==================================

.. c:function:: int drm_atomic_add_affected_connectors(struct drm_atomic_state *state, struct drm_crtc *crtc)

    add connectors for crtc

    :param struct drm_atomic_state \*state:
        atomic state

    :param struct drm_crtc \*crtc:
        DRM crtc

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

    :param struct drm_atomic_state \*state:
        atomic state

    :param struct drm_crtc \*crtc:
        DRM crtc

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

    :param struct drm_atomic_state \*state:
        atomic configuration to check

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

    :param struct drm_atomic_state \*state:
        atomic configuration to check

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

    :param struct drm_atomic_state \*state:
        atomic configuration to check

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

    :param struct drm_device \*dev:
        the drm device

    :param struct drm_printer \*p:
        where to print the state to

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

.. _`drm_atomic_clean_old_fb`:

drm_atomic_clean_old_fb
=======================

.. c:function:: void drm_atomic_clean_old_fb(struct drm_device *dev, unsigned plane_mask, int ret)

    - Unset old_fb pointers and set plane->fb pointers.

    :param struct drm_device \*dev:
        drm device to check.

    :param unsigned plane_mask:
        plane mask for planes that were updated.

    :param int ret:
        return value, can be -EDEADLK for a retry.

.. _`drm_atomic_clean_old_fb.description`:

Description
-----------

Before doing an update \ :c:type:`drm_plane.old_fb <drm_plane>`\  is set to \ :c:type:`drm_plane.fb <drm_plane>`\ , but before
dropping the locks old_fb needs to be set to NULL and plane->fb updated. This
is a common operation for each atomic update, so this call is split off as a
helper.

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

