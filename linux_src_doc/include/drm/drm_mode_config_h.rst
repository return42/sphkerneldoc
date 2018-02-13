.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_mode_config.h

.. _`drm_mode_config_funcs`:

struct drm_mode_config_funcs
============================

.. c:type:: struct drm_mode_config_funcs

    basic driver provided mode setting functions

.. _`drm_mode_config_funcs.definition`:

Definition
----------

.. code-block:: c

    struct drm_mode_config_funcs {
        struct drm_framebuffer *(*fb_create)(struct drm_device *dev,struct drm_file *file_priv, const struct drm_mode_fb_cmd2 *mode_cmd);
        const struct drm_format_info *(*get_format_info)(const struct drm_mode_fb_cmd2 *mode_cmd);
        void (*output_poll_changed)(struct drm_device *dev);
        int (*atomic_check)(struct drm_device *dev, struct drm_atomic_state *state);
        int (*atomic_commit)(struct drm_device *dev,struct drm_atomic_state *state, bool nonblock);
        struct drm_atomic_state *(*atomic_state_alloc)(struct drm_device *dev);
        void (*atomic_state_clear)(struct drm_atomic_state *state);
        void (*atomic_state_free)(struct drm_atomic_state *state);
    }

.. _`drm_mode_config_funcs.members`:

Members
-------

fb_create

    Create a new framebuffer object. The core does basic checks on the
    requested metadata, but most of that is left to the driver. See
    \ :c:type:`struct drm_mode_fb_cmd2 <drm_mode_fb_cmd2>`\  for details.

    If the parameters are deemed valid and the backing storage objects in
    the underlying memory manager all exist, then the driver allocates
    a new \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\  structure, subclassed to contain
    driver-specific information (like the internal native buffer object
    references). It also needs to fill out all relevant metadata, which
    should be done by calling \ :c:func:`drm_helper_mode_fill_fb_struct`\ .

    The initialization is finalized by calling \ :c:func:`drm_framebuffer_init`\ ,
    which registers the framebuffer and makes it accessible to other
    threads.

    RETURNS:

    A new framebuffer with an initial reference count of 1 or a negative
    error code encoded with \ :c:func:`ERR_PTR`\ .

get_format_info

    Allows a driver to return custom format information for special
    fb layouts (eg. ones with auxiliary compression control planes).

    RETURNS:

    The format information specific to the given fb metadata, or
    NULL if none is found.

output_poll_changed

    Callback used by helpers to inform the driver of output configuration
    changes.

    Drivers implementing fbdev emulation with the helpers can call
    drm_fb_helper_hotplug_changed from this hook to inform the fbdev
    helper of output changes.

    FIXME:

    Except that there's no vtable for device-level helper callbacks
    there's no reason this is a core function.

atomic_check

    This is the only hook to validate an atomic modeset update. This
    function must reject any modeset and state changes which the hardware
    or driver doesn't support. This includes but is of course not limited
    to:

     - Checking that the modes, framebuffers, scaling and placement
       requirements and so on are within the limits of the hardware.

     - Checking that any hidden shared resources are not oversubscribed.
       This can be shared PLLs, shared lanes, overall memory bandwidth,
       display fifo space (where shared between planes or maybe even
       CRTCs).

     - Checking that virtualized resources exported to userspace are not
       oversubscribed. For various reasons it can make sense to expose
       more planes, crtcs or encoders than which are physically there. One
       example is dual-pipe operations (which generally should be hidden
       from userspace if when lockstepped in hardware, exposed otherwise),
       where a plane might need 1 hardware plane (if it's just on one
       pipe), 2 hardware planes (when it spans both pipes) or maybe even
       shared a hardware plane with a 2nd plane (if there's a compatible
       plane requested on the area handled by the other pipe).

     - Check that any transitional state is possible and that if
       requested, the update can indeed be done in the vblank period
       without temporarily disabling some functions.

     - Check any other constraints the driver or hardware might have.

     - This callback also needs to correctly fill out the \ :c:type:`struct drm_crtc_state <drm_crtc_state>`\ 
       in this update to make sure that \ :c:func:`drm_atomic_crtc_needs_modeset`\ 
       reflects the nature of the possible update and returns true if and
       only if the update cannot be applied without tearing within one
       vblank on that CRTC. The core uses that information to reject
       updates which require a full modeset (i.e. blanking the screen, or
       at least pausing updates for a substantial amount of time) if
       userspace has disallowed that in its request.

     - The driver also does not need to repeat basic input validation
       like done for the corresponding legacy entry points. The core does
       that before calling this hook.

    See the documentation of \ ``atomic_commit``\  for an exhaustive list of
    error conditions which don't have to be checked at the in this
    callback.

    See the documentation for \ :c:type:`struct drm_atomic_state <drm_atomic_state>`\  for how exactly
    an atomic modeset update is described.

    Drivers using the atomic helpers can implement this hook using
    \ :c:func:`drm_atomic_helper_check`\ , or one of the exported sub-functions of
    it.

    RETURNS:

    0 on success or one of the below negative error codes:

     - -EINVAL, if any of the above constraints are violated.

     - -EDEADLK, when returned from an attempt to acquire an additional
       \ :c:type:`struct drm_modeset_lock <drm_modeset_lock>`\  through \ :c:func:`drm_modeset_lock`\ .

     - -ENOMEM, if allocating additional state sub-structures failed due
       to lack of memory.

     - -EINTR, -EAGAIN or -ERESTARTSYS, if the IOCTL should be restarted.
       This can either be due to a pending signal, or because the driver
       needs to completely bail out to recover from an exceptional
       situation like a GPU hang. From a userspace point all errors are
       treated equally.

atomic_commit

    This is the only hook to commit an atomic modeset update. The core
    guarantees that \ ``atomic_check``\  has been called successfully before
    calling this function, and that nothing has been changed in the
    interim.

    See the documentation for \ :c:type:`struct drm_atomic_state <drm_atomic_state>`\  for how exactly
    an atomic modeset update is described.

    Drivers using the atomic helpers can implement this hook using
    \ :c:func:`drm_atomic_helper_commit`\ , or one of the exported sub-functions of
    it.

    Nonblocking commits (as indicated with the nonblock parameter) must
    do any preparatory work which might result in an unsuccessful commit
    in the context of this callback. The only exceptions are hardware
    errors resulting in -EIO. But even in that case the driver must
    ensure that the display pipe is at least running, to avoid
    compositors crashing when pageflips don't work. Anything else,
    specifically committing the update to the hardware, should be done
    without blocking the caller. For updates which do not require a
    modeset this must be guaranteed.

    The driver must wait for any pending rendering to the new
    framebuffers to complete before executing the flip. It should also
    wait for any pending rendering from other drivers if the underlying
    buffer is a shared dma-buf. Nonblocking commits must not wait for
    rendering in the context of this callback.

    An application can request to be notified when the atomic commit has
    completed. These events are per-CRTC and can be distinguished by the
    CRTC index supplied in \ :c:type:`struct drm_event <drm_event>`\  to userspace.

    The drm core will supply a \ :c:type:`struct drm_event <drm_event>`\  in each CRTC's
    \ :c:type:`drm_crtc_state.event <drm_crtc_state>`\ . See the documentation for
    \ :c:type:`drm_crtc_state.event <drm_crtc_state>`\  for more details about the precise semantics of
    this event.

    NOTE:

    Drivers are not allowed to shut down any display pipe successfully
    enabled through an atomic commit on their own. Doing so can result in
    compositors crashing if a page flip is suddenly rejected because the
    pipe is off.

    RETURNS:

    0 on success or one of the below negative error codes:

     - -EBUSY, if a nonblocking updated is requested and there is
       an earlier updated pending. Drivers are allowed to support a queue
       of outstanding updates, but currently no driver supports that.
       Note that drivers must wait for preceding updates to complete if a
       synchronous update is requested, they are not allowed to fail the
       commit in that case.

     - -ENOMEM, if the driver failed to allocate memory. Specifically
       this can happen when trying to pin framebuffers, which must only
       be done when committing the state.

     - -ENOSPC, as a refinement of the more generic -ENOMEM to indicate
       that the driver has run out of vram, iommu space or similar GPU
       address space needed for framebuffer.

     - -EIO, if the hardware completely died.

     - -EINTR, -EAGAIN or -ERESTARTSYS, if the IOCTL should be restarted.
       This can either be due to a pending signal, or because the driver
       needs to completely bail out to recover from an exceptional
       situation like a GPU hang. From a userspace point of view all errors are
       treated equally.

    This list is exhaustive. Specifically this hook is not allowed to
    return -EINVAL (any invalid requests should be caught in
    \ ``atomic_check``\ ) or -EDEADLK (this function must not acquire
    additional modeset locks).

atomic_state_alloc

    This optional hook can be used by drivers that want to subclass struct
    \ :c:type:`struct drm_atomic_state <drm_atomic_state>`\  to be able to track their own driver-private global
    state easily. If this hook is implemented, drivers must also
    implement \ ``atomic_state_clear``\  and \ ``atomic_state_free``\ .

    Subclassing of \ :c:type:`struct drm_atomic_state <drm_atomic_state>`\  is deprecated in favour of using
    \ :c:type:`struct drm_private_state <drm_private_state>`\  and \ :c:type:`struct drm_private_obj <drm_private_obj>`\ .

    RETURNS:

    A new \ :c:type:`struct drm_atomic_state <drm_atomic_state>`\  on success or NULL on failure.

atomic_state_clear

    This hook must clear any driver private state duplicated into the
    passed-in \ :c:type:`struct drm_atomic_state <drm_atomic_state>`\ . This hook is called when the caller
    encountered a \ :c:type:`struct drm_modeset_lock <drm_modeset_lock>`\  deadlock and needs to drop all
    already acquired locks as part of the deadlock avoidance dance
    implemented in \ :c:func:`drm_modeset_backoff`\ .

    Any duplicated state must be invalidated since a concurrent atomic
    update might change it, and the drm atomic interfaces always apply
    updates as relative changes to the current state.

    Drivers that implement this must call \ :c:func:`drm_atomic_state_default_clear`\ 
    to clear common state.

    Subclassing of \ :c:type:`struct drm_atomic_state <drm_atomic_state>`\  is deprecated in favour of using
    \ :c:type:`struct drm_private_state <drm_private_state>`\  and \ :c:type:`struct drm_private_obj <drm_private_obj>`\ .

atomic_state_free

    This hook needs driver private resources and the \ :c:type:`struct drm_atomic_state <drm_atomic_state>`\ 
    itself. Note that the core first calls \ :c:func:`drm_atomic_state_clear`\  to
    avoid code duplicate between the clear and free hooks.

    Drivers that implement this must call
    \ :c:func:`drm_atomic_state_default_release`\  to release common resources.

    Subclassing of \ :c:type:`struct drm_atomic_state <drm_atomic_state>`\  is deprecated in favour of using
    \ :c:type:`struct drm_private_state <drm_private_state>`\  and \ :c:type:`struct drm_private_obj <drm_private_obj>`\ .

.. _`drm_mode_config_funcs.description`:

Description
-----------

Some global (i.e. not per-CRTC, connector, etc) mode setting functions that
involve drivers.

.. _`drm_mode_config`:

struct drm_mode_config
======================

.. c:type:: struct drm_mode_config

    Mode configuration control structure

.. _`drm_mode_config.definition`:

Definition
----------

.. code-block:: c

    struct drm_mode_config {
        struct mutex mutex;
        struct drm_modeset_lock connection_mutex;
        struct drm_modeset_acquire_ctx *acquire_ctx;
        struct mutex idr_mutex;
        struct idr crtc_idr;
        struct idr tile_idr;
        struct mutex fb_lock;
        int num_fb;
        struct list_head fb_list;
        spinlock_t connector_list_lock;
        int num_connector;
        struct ida connector_ida;
        struct list_head connector_list;
        struct llist_head connector_free_list;
        struct work_struct connector_free_work;
        int num_encoder;
        struct list_head encoder_list;
        int num_total_plane;
        struct list_head plane_list;
        int num_crtc;
        struct list_head crtc_list;
        struct list_head property_list;
        int min_width, min_height;
        int max_width, max_height;
        const struct drm_mode_config_funcs *funcs;
        resource_size_t fb_base;
        bool poll_enabled;
        bool poll_running;
        bool delayed_event;
        struct delayed_work output_poll_work;
        struct mutex blob_lock;
        struct list_head property_blob_list;
        struct drm_property *edid_property;
        struct drm_property *dpms_property;
        struct drm_property *path_property;
        struct drm_property *tile_property;
        struct drm_property *link_status_property;
        struct drm_property *plane_type_property;
        struct drm_property *prop_src_x;
        struct drm_property *prop_src_y;
        struct drm_property *prop_src_w;
        struct drm_property *prop_src_h;
        struct drm_property *prop_crtc_x;
        struct drm_property *prop_crtc_y;
        struct drm_property *prop_crtc_w;
        struct drm_property *prop_crtc_h;
        struct drm_property *prop_fb_id;
        struct drm_property *prop_in_fence_fd;
        struct drm_property *prop_out_fence_ptr;
        struct drm_property *prop_crtc_id;
        struct drm_property *prop_active;
        struct drm_property *prop_mode_id;
        struct drm_property *dvi_i_subconnector_property;
        struct drm_property *dvi_i_select_subconnector_property;
        struct drm_property *tv_subconnector_property;
        struct drm_property *tv_select_subconnector_property;
        struct drm_property *tv_mode_property;
        struct drm_property *tv_left_margin_property;
        struct drm_property *tv_right_margin_property;
        struct drm_property *tv_top_margin_property;
        struct drm_property *tv_bottom_margin_property;
        struct drm_property *tv_brightness_property;
        struct drm_property *tv_contrast_property;
        struct drm_property *tv_flicker_reduction_property;
        struct drm_property *tv_overscan_property;
        struct drm_property *tv_saturation_property;
        struct drm_property *tv_hue_property;
        struct drm_property *scaling_mode_property;
        struct drm_property *aspect_ratio_property;
        struct drm_property *degamma_lut_property;
        struct drm_property *degamma_lut_size_property;
        struct drm_property *ctm_property;
        struct drm_property *gamma_lut_property;
        struct drm_property *gamma_lut_size_property;
        struct drm_property *suggested_x_property;
        struct drm_property *suggested_y_property;
        struct drm_property *non_desktop_property;
        struct drm_property *panel_orientation_property;
        uint32_t preferred_depth, prefer_shadow;
        bool async_page_flip;
        bool allow_fb_modifiers;
        struct drm_property *modifiers_property;
        uint32_t cursor_width, cursor_height;
        struct drm_atomic_state *suspend_state;
        const struct drm_mode_config_helper_funcs *helper_private;
    }

.. _`drm_mode_config.members`:

Members
-------

mutex

    This is the big scary modeset BKL which protects everything that
    isn't protect otherwise. Scope is unclear and fuzzy, try to remove
    anything from under it's protection and move it into more well-scoped
    locks.

    The one important thing this protects is the use of \ ``acquire_ctx``\ .

connection_mutex

    This protects connector state and the connector to encoder to CRTC
    routing chain.

    For atomic drivers specifically this protects \ :c:type:`drm_connector.state <drm_connector>`\ .

acquire_ctx

    Global implicit acquire context used by atomic drivers for legacy
    IOCTLs. Deprecated, since implicit locking contexts make it
    impossible to use driver-private \ :c:type:`struct drm_modeset_lock <drm_modeset_lock>`\ . Users of
    this must hold \ ``mutex``\ .

idr_mutex

    Mutex for KMS ID allocation and management. Protects both \ ``crtc_idr``\ 
    and \ ``tile_idr``\ .

crtc_idr

    Main KMS ID tracking object. Use this idr for all IDs, fb, crtc,
    connector, modes - just makes life easier to have only one.

tile_idr

    Use this idr for allocating new IDs for tiled sinks like use in some
    high-res DP MST screens.

fb_lock
    Mutex to protect fb the global \ ``fb_list``\  and \ ``num_fb``\ .

num_fb
    Number of entries on \ ``fb_list``\ .

fb_list
    List of all \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\ .

connector_list_lock
    Protects \ ``num_connector``\  and@connector_list and \ ``connector_free_list``\ .

num_connector
    Number of connectors on this device. Protected by@connector_list_lock.

connector_ida
    ID allocator for connector indices.

connector_list

    List of connector objects linked with \ :c:type:`drm_connector.head <drm_connector>`\ . Protected
    by \ ``connector_list_lock``\ . Only use \ :c:func:`drm_for_each_connector_iter`\  and
    \ :c:type:`struct drm_connector_list_iter <drm_connector_list_iter>`\  to walk this list.

connector_free_list

    List of connector objects linked with \ :c:type:`drm_connector.free_head <drm_connector>`\ .
    Protected by \ ``connector_list_lock``\ . Used by
    \ :c:func:`drm_for_each_connector_iter`\  and
    \ :c:type:`struct drm_connector_list_iter <drm_connector_list_iter>`\  to savely free connectors using
    \ ``connector_free_work``\ .

connector_free_work
    Work to clean up \ ``connector_free_list``\ .

num_encoder

    Number of encoders on this device. This is invariant over the
    lifetime of a device and hence doesn't need any locks.

encoder_list

    List of encoder objects linked with \ :c:type:`drm_encoder.head <drm_encoder>`\ . This is
    invariant over the lifetime of a device and hence doesn't need any
    locks.

num_total_plane

    Number of universal (i.e. with primary/curso) planes on this device.
    This is invariant over the lifetime of a device and hence doesn't
    need any locks.

plane_list

    List of plane objects linked with \ :c:type:`drm_plane.head <drm_plane>`\ . This is invariant
    over the lifetime of a device and hence doesn't need any locks.

num_crtc

    Number of CRTCs on this device linked with \ :c:type:`drm_crtc.head <drm_crtc>`\ . This is invariant over the lifetime
    of a device and hence doesn't need any locks.

crtc_list

    List of CRTC objects linked with \ :c:type:`drm_crtc.head <drm_crtc>`\ . This is invariant
    over the lifetime of a device and hence doesn't need any locks.

property_list

    List of property type objects linked with \ :c:type:`drm_property.head <drm_property>`\ . This is
    invariant over the lifetime of a device and hence doesn't need any
    locks.

min_width
    minimum pixel width on this device

min_height
    minimum pixel height on this device

max_width
    maximum pixel width on this device

max_height
    maximum pixel height on this device

funcs
    core driver provided mode setting functions

fb_base
    base address of the framebuffer

poll_enabled
    track polling support for this device

poll_running
    track polling status for this device

delayed_event
    track delayed poll uevent deliver for this device

output_poll_work
    delayed work for polling in process context

blob_lock

    Mutex for blob property allocation and management, protects
    \ ``property_blob_list``\  and \ :c:type:`drm_file.blobs <drm_file>`\ .

property_blob_list

    List of all the blob property objects linked with
    \ :c:type:`drm_property_blob.head <drm_property_blob>`\ . Protected by \ ``blob_lock``\ .

edid_property
    Default connector property to hold the EDID of thecurrently connected sink, if any.

dpms_property
    Default connector property to control theconnector's DPMS state.

path_property
    Default connector property to hold the DP MST pathfor the port.

tile_property
    Default connector property to store the tileposition of a tiled screen, for sinks which need to be driven with
    multiple CRTCs.

link_status_property
    Default connector property for link statusof a connector

plane_type_property
    Default plane property to differentiateCURSOR, PRIMARY and OVERLAY legacy uses of planes.

prop_src_x
    Default atomic plane property for the plane sourceposition in the connected \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\ .

prop_src_y
    Default atomic plane property for the plane sourceposition in the connected \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\ .

prop_src_w
    Default atomic plane property for the plane sourceposition in the connected \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\ .

prop_src_h
    Default atomic plane property for the plane sourceposition in the connected \ :c:type:`struct drm_framebuffer <drm_framebuffer>`\ .

prop_crtc_x
    Default atomic plane property for the plane destinationposition in the \ :c:type:`struct drm_crtc <drm_crtc>`\  is is being shown on.

prop_crtc_y
    Default atomic plane property for the plane destinationposition in the \ :c:type:`struct drm_crtc <drm_crtc>`\  is is being shown on.

prop_crtc_w
    Default atomic plane property for the plane destinationposition in the \ :c:type:`struct drm_crtc <drm_crtc>`\  is is being shown on.

prop_crtc_h
    Default atomic plane property for the plane destinationposition in the \ :c:type:`struct drm_crtc <drm_crtc>`\  is is being shown on.

prop_fb_id
    Default atomic plane property to specify the&drm_framebuffer.

prop_in_fence_fd
    Sync File fd representing the incoming fencesfor a Plane.

prop_out_fence_ptr
    Sync File fd pointer representing theoutgoing fences for a CRTC. Userspace should provide a pointer to a
    value of type s32, and then cast that pointer to u64.

prop_crtc_id
    Default atomic plane property to specify the&drm_crtc.

prop_active
    Default atomic CRTC property to control the activestate, which is the simplified implementation for DPMS in atomic
    drivers.

prop_mode_id
    Default atomic CRTC property to set the mode for aCRTC. A 0 mode implies that the CRTC is entirely disabled - all
    connectors must be of and active must be set to disabled, too.

dvi_i_subconnector_property
    Optional DVI-I property todifferentiate between analog or digital mode.

dvi_i_select_subconnector_property
    Optional DVI-I property toselect between analog or digital mode.

tv_subconnector_property
    Optional TV property to differentiatebetween different TV connector types.

tv_select_subconnector_property
    Optional TV property to selectbetween different TV connector types.

tv_mode_property
    Optional TV property to selectthe output TV mode.

tv_left_margin_property
    Optional TV property to set the leftmargin.

tv_right_margin_property
    Optional TV property to set the rightmargin.

tv_top_margin_property
    Optional TV property to set the rightmargin.

tv_bottom_margin_property
    Optional TV property to set the rightmargin.

tv_brightness_property
    Optional TV property to set thebrightness.

tv_contrast_property
    Optional TV property to set thecontrast.

tv_flicker_reduction_property
    Optional TV property to control theflicker reduction mode.

tv_overscan_property
    Optional TV property to control the overscansetting.

tv_saturation_property
    Optional TV property to set thesaturation.

tv_hue_property
    Optional TV property to set the hue.

scaling_mode_property
    Optional connector property to control theupscaling, mostly used for built-in panels.

aspect_ratio_property
    Optional connector property to control theHDMI infoframe aspect ratio setting.

degamma_lut_property
    Optional CRTC property to set the LUT used toconvert the framebuffer's colors to linear gamma.

degamma_lut_size_property
    Optional CRTC property for the size ofthe degamma LUT as supported by the driver (read-only).

ctm_property
    Optional CRTC property to set thematrix used to convert colors after the lookup in the
    degamma LUT.

gamma_lut_property
    Optional CRTC property to set the LUT used toconvert the colors, after the CTM matrix, to the gamma space of the
    connected screen.

gamma_lut_size_property
    Optional CRTC property for the size of thegamma LUT as supported by the driver (read-only).

suggested_x_property
    Optional connector property with a hint forthe position of the output on the host's screen.

suggested_y_property
    Optional connector property with a hint forthe position of the output on the host's screen.

non_desktop_property
    Optional connector property with a hintthat device isn't a standard display, and the console/desktop,
    should not be displayed on it.

panel_orientation_property
    Optional connector property indicatinghow the lcd-panel is mounted inside the casing (e.g. normal or
    upside-down).

preferred_depth
    preferred RBG pixel depth, used by fb helpers

prefer_shadow
    hint to userspace to prefer shadow-fb rendering

async_page_flip
    Does this device support async flips on the primaryplane?

allow_fb_modifiers

    Whether the driver supports fb modifiers in the ADDFB2.1 ioctl call.

modifiers_property
    Plane property to list support modifier/formatcombination.

cursor_width
    hint to userspace for max cursor width

cursor_height
    hint to userspace for max cursor height

suspend_state

    Atomic state when suspended.
    Set by \ :c:func:`drm_mode_config_helper_suspend`\  and cleared by
    \ :c:func:`drm_mode_config_helper_resume`\ .

helper_private
    mid-layer private data

.. _`drm_mode_config.description`:

Description
-----------

Core mode resource tracking structure.  All CRTC, encoders, and connectors
enumerated by the driver are added here, as are global properties.  Some
global restrictions are also here, e.g. dimension restrictions.

.. This file was automatic generated / don't edit.

