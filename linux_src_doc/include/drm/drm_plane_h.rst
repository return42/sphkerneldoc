.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_plane.h

.. _`drm_plane_state`:

struct drm_plane_state
======================

.. c:type:: struct drm_plane_state

    mutable plane state

.. _`drm_plane_state.definition`:

Definition
----------

.. code-block:: c

    struct drm_plane_state {
        struct drm_plane *plane;
        struct drm_crtc *crtc;
        struct drm_framebuffer *fb;
        struct dma_fence *fence;
        int32_t crtc_x;
        int32_t crtc_y;
        uint32_t crtc_w, crtc_h;
        uint32_t src_x, src_y;
        uint32_t src_h, src_w;
        unsigned int rotation;
        unsigned int zpos;
        unsigned int normalized_zpos;
        struct drm_rect src, dst;
        bool visible;
        struct drm_crtc_commit *commit;
        struct drm_atomic_state *state;
    }

.. _`drm_plane_state.members`:

Members
-------

plane
    backpointer to the plane

crtc

    Currently bound CRTC, NULL if disabled. Do not this write directly,
    use \ :c:func:`drm_atomic_set_crtc_for_plane`\ 

fb

    Currently bound framebuffer. Do not write this directly, use
    \ :c:func:`drm_atomic_set_fb_for_plane`\ 

fence

    Optional fence to wait for before scanning out \ ``fb``\ . Do not write this
    directly, use \ :c:func:`drm_atomic_set_fence_for_plane`\ 

crtc_x

    Left position of visible portion of plane on crtc, signed dest
    location allows it to be partially off screen.

crtc_y

    Upper position of visible portion of plane on crtc, signed dest
    location allows it to be partially off screen.

crtc_w
    width of visible portion of plane on crtc

crtc_h
    height of visible portion of plane on crtc

src_x
    left position of visible portion of plane within
    plane (in 16.16)

src_y
    upper position of visible portion of plane within
    plane (in 16.16)

src_h
    height of visible portion of plane (in 16.16)

src_w
    width of visible portion of plane (in 16.16)

rotation
    rotation of the plane

zpos
    priority of the given plane on crtc (optional)
    Note that multiple active planes on the same crtc can have an identical
    zpos value. The rule to solving the conflict is to compare the plane
    object IDs; the plane with a higher ID must be stacked on top of a
    plane with a lower ID.

normalized_zpos
    normalized value of zpos: unique, range from 0 to N-1
    where N is the number of active planes for given crtc. Note that
    the driver must call \ :c:func:`drm_atomic_normalize_zpos`\  to update this before
    it can be trusted.

src
    clipped source coordinates of the plane (in 16.16)

dst
    clipped destination coordinates of the plane

visible

    Visibility of the plane. This can be false even if fb!=NULL and
    crtc!=NULL, due to clipping.

commit
    Tracks the pending commit to prevent use-after-free conditions,and for async plane updates.

    May be NULL.

state
    backpointer to global drm_atomic_state

.. _`drm_plane_funcs`:

struct drm_plane_funcs
======================

.. c:type:: struct drm_plane_funcs

    driver plane control functions

.. _`drm_plane_funcs.definition`:

Definition
----------

.. code-block:: c

    struct drm_plane_funcs {
        int (*update_plane)(struct drm_plane *plane,struct drm_crtc *crtc, struct drm_framebuffer *fb,int crtc_x, int crtc_y,unsigned int crtc_w, unsigned int crtc_h,uint32_t src_x, uint32_t src_y,uint32_t src_w, uint32_t src_h, struct drm_modeset_acquire_ctx *ctx);
        int (*disable_plane)(struct drm_plane *plane, struct drm_modeset_acquire_ctx *ctx);
        void (*destroy)(struct drm_plane *plane);
        void (*reset)(struct drm_plane *plane);
        int (*set_property)(struct drm_plane *plane, struct drm_property *property, uint64_t val);
        struct drm_plane_state *(*atomic_duplicate_state)(struct drm_plane *plane);
        void (*atomic_destroy_state)(struct drm_plane *plane, struct drm_plane_state *state);
        int (*atomic_set_property)(struct drm_plane *plane,struct drm_plane_state *state,struct drm_property *property, uint64_t val);
        int (*atomic_get_property)(struct drm_plane *plane,const struct drm_plane_state *state,struct drm_property *property, uint64_t *val);
        int (*late_register)(struct drm_plane *plane);
        void (*early_unregister)(struct drm_plane *plane);
        void (*atomic_print_state)(struct drm_printer *p, const struct drm_plane_state *state);
        bool (*format_mod_supported)(struct drm_plane *plane, uint32_t format, uint64_t modifier);
    }

.. _`drm_plane_funcs.members`:

Members
-------

update_plane

    This is the legacy entry point to enable and configure the plane for
    the given CRTC and framebuffer. It is never called to disable the
    plane, i.e. the passed-in crtc and fb paramters are never NULL.

    The source rectangle in frame buffer memory coordinates is given by
    the src_x, src_y, src_w and src_h parameters (as 16.16 fixed point
    values). Devices that don't support subpixel plane coordinates can
    ignore the fractional part.

    The destination rectangle in CRTC coordinates is given by the
    crtc_x, crtc_y, crtc_w and crtc_h parameters (as integer values).
    Devices scale the source rectangle to the destination rectangle. If
    scaling is not supported, and the source rectangle size doesn't match
    the destination rectangle size, the driver must return a
    -<errorname>EINVAL</errorname> error.

    Drivers implementing atomic modeset should use
    \ :c:func:`drm_atomic_helper_update_plane`\  to implement this hook.

    RETURNS:

    0 on success or a negative error code on failure.

disable_plane

    This is the legacy entry point to disable the plane. The DRM core
    calls this method in response to a DRM_IOCTL_MODE_SETPLANE IOCTL call
    with the frame buffer ID set to 0.  Disabled planes must not be
    processed by the CRTC.

    Drivers implementing atomic modeset should use
    \ :c:func:`drm_atomic_helper_disable_plane`\  to implement this hook.

    RETURNS:

    0 on success or a negative error code on failure.

destroy

    Clean up plane resources. This is only called at driver unload time
    through \ :c:func:`drm_mode_config_cleanup`\  since a plane cannot be hotplugged
    in DRM.

reset

    Reset plane hardware and software state to off. This function isn't
    called by the core directly, only through \ :c:func:`drm_mode_config_reset`\ .
    It's not a helper hook only for historical reasons.

    Atomic drivers can use \ :c:func:`drm_atomic_helper_plane_reset`\  to reset
    atomic state using this hook.

set_property

    This is the legacy entry point to update a property attached to the
    plane.

    This callback is optional if the driver does not support any legacy
    driver-private properties. For atomic drivers it is not used because
    property handling is done entirely in the DRM core.

    RETURNS:

    0 on success or a negative error code on failure.

atomic_duplicate_state

    Duplicate the current atomic state for this plane and return it.
    The core and helpers guarantee that any atomic state duplicated with
    this hook and still owned by the caller (i.e. not transferred to the
    driver by calling \ :c:type:`drm_mode_config_funcs.atomic_commit <drm_mode_config_funcs>`\ ) will be
    cleaned up by calling the \ ``atomic_destroy_state``\  hook in this
    structure.

    Atomic drivers which don't subclass \ :c:type:`struct drm_plane_state <drm_plane_state>`\  should use
    \ :c:func:`drm_atomic_helper_plane_duplicate_state`\ . Drivers that subclass the
    state structure to extend it with driver-private state should use
    \ :c:func:`__drm_atomic_helper_plane_duplicate_state`\  to make sure shared state is
    duplicated in a consistent fashion across drivers.

    It is an error to call this hook before \ :c:type:`drm_plane.state <drm_plane>`\  has been
    initialized correctly.

    NOTE:

    If the duplicate state references refcounted resources this hook must
    acquire a reference for each of them. The driver must release these
    references again in \ ``atomic_destroy_state``\ .

    RETURNS:

    Duplicated atomic state or NULL when the allocation failed.

atomic_destroy_state

    Destroy a state duplicated with \ ``atomic_duplicate_state``\  and release
    or unreference all resources it references

atomic_set_property

    Decode a driver-private property value and store the decoded value
    into the passed-in state structure. Since the atomic core decodes all
    standardized properties (even for extensions beyond the core set of
    properties which might not be implemented by all drivers) this
    requires drivers to subclass the state structure.

    Such driver-private properties should really only be implemented for
    truly hardware/vendor specific state. Instead it is preferred to
    standardize atomic extension and decode the properties used to expose
    such an extension in the core.

    Do not call this function directly, use
    \ :c:func:`drm_atomic_plane_set_property`\  instead.

    This callback is optional if the driver does not support any
    driver-private atomic properties.

    NOTE:

    This function is called in the state assembly phase of atomic
    modesets, which can be aborted for any reason (including on
    userspace's request to just check whether a configuration would be
    possible). Drivers MUST NOT touch any persistent state (hardware or
    software) or data structures except the passed in \ ``state``\  parameter.

    Also since userspace controls in which order properties are set this
    function must not do any input validation (since the state update is
    incomplete and hence likely inconsistent). Instead any such input
    validation must be done in the various atomic_check callbacks.

    RETURNS:

    0 if the property has been found, -EINVAL if the property isn't
    implemented by the driver (which shouldn't ever happen, the core only
    asks for properties attached to this plane). No other validation is
    allowed by the driver. The core already checks that the property
    value is within the range (integer, valid enum value, ...) the driver
    set when registering the property.

atomic_get_property

    Reads out the decoded driver-private property. This is used to
    implement the GETPLANE IOCTL.

    Do not call this function directly, use
    \ :c:func:`drm_atomic_plane_get_property`\  instead.

    This callback is optional if the driver does not support any
    driver-private atomic properties.

    RETURNS:

    0 on success, -EINVAL if the property isn't implemented by the
    driver (which should never happen, the core only asks for
    properties attached to this plane).

late_register

    This optional hook can be used to register additional userspace
    interfaces attached to the plane like debugfs interfaces.
    It is called late in the driver load sequence from \ :c:func:`drm_dev_register`\ .
    Everything added from this callback should be unregistered in
    the early_unregister callback.

    Returns:

    0 on success, or a negative error code on failure.

early_unregister

    This optional hook should be used to unregister the additional
    userspace interfaces attached to the plane from
    \ ``late_register``\ . It is called from \ :c:func:`drm_dev_unregister`\ ,
    early in the driver unload sequence to disable userspace access
    before data structures are torndown.

atomic_print_state

    If driver subclasses \ :c:type:`struct drm_plane_state <drm_plane_state>`\ , it should implement
    this optional hook for printing additional driver specific state.

    Do not call this directly, use \ :c:func:`drm_atomic_plane_print_state`\ 
    instead.

format_mod_supported

    This optional hook is used for the DRM to determine if the given
    format/modifier combination is valid for the plane. This allows the
    DRM to generate the correct format bitmask (which formats apply to
    which modifier).

    Returns:

    True if the given modifier is valid for that format on the plane.
    False otherwise.

.. _`drm_plane_type`:

enum drm_plane_type
===================

.. c:type:: enum drm_plane_type

    uapi plane type enumeration

.. _`drm_plane_type.definition`:

Definition
----------

.. code-block:: c

    enum drm_plane_type {
        DRM_PLANE_TYPE_OVERLAY,
        DRM_PLANE_TYPE_PRIMARY,
        DRM_PLANE_TYPE_CURSOR
    };

.. _`drm_plane_type.constants`:

Constants
---------

DRM_PLANE_TYPE_OVERLAY

    Overlay planes represent all non-primary, non-cursor planes. Some
    drivers refer to these types of planes as "sprites" internally.

DRM_PLANE_TYPE_PRIMARY

    Primary planes represent a "main" plane for a CRTC.  Primary planes
    are the planes operated upon by CRTC modesetting and flipping
    operations described in the \ :c:type:`drm_crtc_funcs.page_flip <drm_crtc_funcs>`\  and
    \ :c:type:`drm_crtc_funcs.set_config <drm_crtc_funcs>`\  hooks.

DRM_PLANE_TYPE_CURSOR

    Cursor planes represent a "cursor" plane for a CRTC.  Cursor planes
    are the planes operated upon by the DRM_IOCTL_MODE_CURSOR and
    DRM_IOCTL_MODE_CURSOR2 IOCTLs.

.. _`drm_plane_type.description`:

Description
-----------

For historical reasons not all planes are made the same. This enumeration is
used to tell the different types of planes apart to implement the different
uapi semantics for them. For userspace which is universal plane aware and
which is using that atomic IOCTL there's no difference between these planes
(beyong what the driver and hardware can support of course).

For compatibility with legacy userspace, only overlay planes are made
available to userspace by default. Userspace clients may set the
DRM_CLIENT_CAP_UNIVERSAL_PLANES client capability bit to indicate that they
wish to receive a universal plane list containing all plane types. See also
\ :c:func:`drm_for_each_legacy_plane`\ .

WARNING: The values of this enum is UABI since they're exposed in the "type"
property.

.. _`drm_plane`:

struct drm_plane
================

.. c:type:: struct drm_plane

    central DRM plane control structure

.. _`drm_plane.definition`:

Definition
----------

.. code-block:: c

    struct drm_plane {
        struct drm_device *dev;
        struct list_head head;
        char *name;
        struct drm_modeset_lock mutex;
        struct drm_mode_object base;
        uint32_t possible_crtcs;
        uint32_t *format_types;
        unsigned int format_count;
        bool format_default;
        uint64_t *modifiers;
        unsigned int modifier_count;
        struct drm_crtc *crtc;
        struct drm_framebuffer *fb;
        struct drm_framebuffer *old_fb;
        const struct drm_plane_funcs *funcs;
        struct drm_object_properties properties;
        enum drm_plane_type type;
        unsigned index;
        const struct drm_plane_helper_funcs *helper_private;
        struct drm_plane_state *state;
        struct drm_property *zpos_property;
        struct drm_property *rotation_property;
    }

.. _`drm_plane.members`:

Members
-------

dev
    DRM device this plane belongs to

head
    for list management

name
    human readable name, can be overwritten by the driver

mutex

    Protects modeset plane state, together with the \ :c:type:`drm_crtc.mutex <drm_crtc>`\  of
    CRTC this plane is linked to (when active, getting activated or
    getting disabled).

    For atomic drivers specifically this protects \ ``state``\ .

base
    base mode object

possible_crtcs
    pipes this plane can be bound to

format_types
    array of formats supported by this plane

format_count
    number of formats supported

format_default
    driver hasn't supplied supported formats for the plane

modifiers
    array of modifiers supported by this plane

modifier_count
    number of modifiers supported

crtc
    Currently bound CRTC, only really meaningful for non-atomicdrivers.  Atomic drivers should instead check \ :c:type:`drm_plane_state.crtc <drm_plane_state>`\ .

fb
    Currently bound framebuffer, only really meaningful fornon-atomic drivers.  Atomic drivers should instead check
    \ :c:type:`drm_plane_state.fb <drm_plane_state>`\ .

old_fb
    Temporary tracking of the old fb while a modeset is ongoing. Used by
    \ :c:func:`drm_mode_set_config_internal`\  to implement correct refcounting.

funcs
    helper functions

properties
    property tracking for this plane

type
    type of plane (overlay, primary, cursor)

index
    Position inside the mode_config.list, can be used as an arrayindex. It is invariant over the lifetime of the plane.

helper_private
    mid-layer private data

state

    Current atomic state for this plane.

    This is protected by \ ``mutex``\ . Note that nonblocking atomic commits
    access the current plane state without taking locks. Either by going
    through the \ :c:type:`struct drm_atomic_state <drm_atomic_state>`\  pointers, see
    \ :c:func:`for_each_oldnew_plane_in_state`\ , \ :c:func:`for_each_old_plane_in_state`\  and
    \ :c:func:`for_each_new_plane_in_state`\ . Or through careful ordering of atomic
    commit operations as implemented in the atomic helpers, see
    \ :c:type:`struct drm_crtc_commit <drm_crtc_commit>`\ .

zpos_property
    zpos property for this plane

rotation_property
    rotation property for this plane

.. _`drm_plane_index`:

drm_plane_index
===============

.. c:function:: unsigned int drm_plane_index(struct drm_plane *plane)

    find the index of a registered plane

    :param struct drm_plane \*plane:
        plane to find index for

.. _`drm_plane_index.description`:

Description
-----------

Given a registered plane, return the index of that plane within a DRM
device's list of planes.

.. _`drm_plane_find`:

drm_plane_find
==============

.. c:function:: struct drm_plane *drm_plane_find(struct drm_device *dev, struct drm_file *file_priv, uint32_t id)

    find a \ :c:type:`struct drm_plane <drm_plane>`\ 

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_file \*file_priv:
        drm file to check for lease against.

    :param uint32_t id:
        plane id

.. _`drm_plane_find.description`:

Description
-----------

Returns the plane with \ ``id``\ , NULL if it doesn't exist. Simple wrapper around
\ :c:func:`drm_mode_object_find`\ .

.. _`drm_for_each_plane_mask`:

drm_for_each_plane_mask
=======================

.. c:function::  drm_for_each_plane_mask( plane,  dev,  plane_mask)

    iterate over planes specified by bitmask

    :param  plane:
        the loop cursor

    :param  dev:
        the DRM device

    :param  plane_mask:
        bitmask of plane indices

.. _`drm_for_each_plane_mask.description`:

Description
-----------

Iterate over all planes specified by bitmask.

.. _`drm_for_each_legacy_plane`:

drm_for_each_legacy_plane
=========================

.. c:function::  drm_for_each_legacy_plane( plane,  dev)

    iterate over all planes for legacy userspace

    :param  plane:
        the loop cursor

    :param  dev:
        the DRM device

.. _`drm_for_each_legacy_plane.description`:

Description
-----------

Iterate over all legacy planes of \ ``dev``\ , excluding primary and cursor planes.
This is useful for implementing userspace apis when userspace is not
universal plane aware. See also \ :c:type:`enum drm_plane_type <drm_plane_type>`\ .

.. _`drm_for_each_plane`:

drm_for_each_plane
==================

.. c:function::  drm_for_each_plane( plane,  dev)

    iterate over all planes

    :param  plane:
        the loop cursor

    :param  dev:
        the DRM device

.. _`drm_for_each_plane.description`:

Description
-----------

Iterate over all planes of \ ``dev``\ , include primary and cursor planes.

.. This file was automatic generated / don't edit.

