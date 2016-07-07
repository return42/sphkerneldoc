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
state. Which could break assumptions the driver's ->atomic_check likely
relies on.

Hence we must clear all cached state and completely start over, using this
function.

.. _`drm_atomic_state_free`:

drm_atomic_state_free
=====================

.. c:function:: void drm_atomic_state_free(struct drm_atomic_state *state)

    free all memory for an atomic state

    :param struct drm_atomic_state \*state:
        atomic state to deallocate

.. _`drm_atomic_state_free.description`:

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

.. c:function:: int drm_atomic_set_mode_for_crtc(struct drm_crtc_state *state, struct drm_display_mode *mode)

    set mode for CRTC

    :param struct drm_crtc_state \*state:
        the CRTC whose incoming state to update

    :param struct drm_display_mode \*mode:
        kernel-internal mode to use for the CRTC, or NULL to disable

.. _`drm_atomic_set_mode_for_crtc.description`:

Description
-----------

Set a mode (originating from the kernel) on the desired CRTC state. Does
not change any other state properties, including enable, active, or
mode_changed.

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

.. _`drm_atomic_replace_property_blob`:

drm_atomic_replace_property_blob
================================

.. c:function:: void drm_atomic_replace_property_blob(struct drm_property_blob **blob, struct drm_property_blob *new_blob, bool *replaced)

    replace a blob property

    :param struct drm_property_blob \*\*blob:
        a pointer to the member blob to be replaced

    :param struct drm_property_blob \*new_blob:
        the new blob to replace with

    :param bool \*replaced:
        whether the blob has been replaced

.. _`drm_atomic_replace_property_blob.return`:

Return
------

Zero on success, error code on failure

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

Use this instead of calling crtc->atomic_set_property directly.
This function handles generic/core properties and calls out to
driver's ->\ :c:func:`atomic_set_property`\  for driver properties.  To ensure
consistent behavior you must call this function rather than the
driver hook directly.

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

This function handles generic/core properties and calls out to
driver's ->\ :c:func:`atomic_get_property`\  for driver properties.  To ensure
consistent behavior you must call this function rather than the
driver hook directly.

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

Use this instead of calling plane->atomic_set_property directly.
This function handles generic/core properties and calls out to
driver's ->\ :c:func:`atomic_set_property`\  for driver properties.  To ensure
consistent behavior you must call this function rather than the
driver hook directly.

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

This function handles generic/core properties and calls out to
driver's ->\ :c:func:`atomic_get_property`\  for driver properties.  To ensure
consistent behavior you must call this function rather than the
driver hook directly.

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

Use this instead of calling connector->atomic_set_property directly.
This function handles generic/core properties and calls out to
driver's ->\ :c:func:`atomic_set_property`\  for driver properties.  To ensure
consistent behavior you must call this function rather than the
driver hook directly.

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

This function handles generic/core properties and calls out to
driver's ->\ :c:func:`atomic_get_property`\  for driver properties.  To ensure
consistent behavior you must call this function rather than the
driver hook directly.

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

.. _`drm_atomic_legacy_backoff`:

drm_atomic_legacy_backoff
=========================

.. c:function:: void drm_atomic_legacy_backoff(struct drm_atomic_state *state)

    locking backoff for legacy ioctls

    :param struct drm_atomic_state \*state:
        atomic state

.. _`drm_atomic_legacy_backoff.description`:

Description
-----------

This function should be used by legacy entry points which don't understand
-EDEADLK semantics. For simplicity this one will grab all modeset locks after
the slowpath completed.

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

Also note that on successful execution ownership of \ ``state``\  is transferred
from the caller of this function to the function itself. The caller must not
free or in any other way access \ ``state``\ . If the function fails then the caller
must clean up \ ``state``\  itself.

.. _`drm_atomic_commit.return`:

Return
------

0 on success, negative error code on failure.

.. _`drm_atomic_nonblocking_commit`:

drm_atomic_nonblocking_commit
=============================

.. c:function:: int drm_atomic_nonblocking_commit(struct drm_atomic_state *state)

    atomic\ :c:type:`struct nonblocking <nonblocking>` configuration commit

    :param struct drm_atomic_state \*state:
        atomic configuration to check

.. _`drm_atomic_nonblocking_commit.description`:

Description
-----------

Note that this function can return -EDEADLK if the driver needed to acquire
more locks but encountered a deadlock. The caller must then do the usual w/w
backoff dance and restart. All other errors are fatal.

Also note that on successful execution ownership of \ ``state``\  is transferred
from the caller of this function to the function itself. The caller must not
free or in any other way access \ ``state``\ . If the function fails then the caller
must clean up \ ``state``\  itself.

.. _`drm_atomic_nonblocking_commit.return`:

Return
------

0 on success, negative error code on failure.

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

Before doing an update plane->old_fb is set to plane->fb,
but before dropping the locks old_fb needs to be set to NULL
and plane->fb updated. This is a common operation for each
atomic update, so this call is split off as a helper.

.. This file was automatic generated / don't edit.

