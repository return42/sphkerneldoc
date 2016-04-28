.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-drm-crtc-helper-funcs:

============================
struct drm_crtc_helper_funcs
============================

*man struct drm_crtc_helper_funcs(9)*

*4.6.0-rc5*

helper operations for CRTCs


Synopsis
========

.. code-block:: c

    struct drm_crtc_helper_funcs {
      void (* dpms) (struct drm_crtc *crtc, int mode);
      void (* prepare) (struct drm_crtc *crtc);
      void (* commit) (struct drm_crtc *crtc);
      bool (* mode_fixup) (struct drm_crtc *crtc,const struct drm_display_mode *mode,struct drm_display_mode *adjusted_mode);
      int (* mode_set) (struct drm_crtc *crtc, struct drm_display_mode *mode,struct drm_display_mode *adjusted_mode, int x, int y,struct drm_framebuffer *old_fb);
      void (* mode_set_nofb) (struct drm_crtc *crtc);
      int (* mode_set_base) (struct drm_crtc *crtc, int x, int y,struct drm_framebuffer *old_fb);
      int (* mode_set_base_atomic) (struct drm_crtc *crtc,struct drm_framebuffer *fb, int x, int y,enum mode_set_atomic);
      void (* load_lut) (struct drm_crtc *crtc);
      void (* disable) (struct drm_crtc *crtc);
      void (* enable) (struct drm_crtc *crtc);
      int (* atomic_check) (struct drm_crtc *crtc,struct drm_crtc_state *state);
      void (* atomic_begin) (struct drm_crtc *crtc,struct drm_crtc_state *old_crtc_state);
      void (* atomic_flush) (struct drm_crtc *crtc,struct drm_crtc_state *old_crtc_state);
    };


Members
=======

dpms
    Callback to control power levels on the CRTC. If the mode passed in
    is unsupported, the provider must use the next lowest power level.
    This is used by the legacy CRTC helpers to implement DPMS
    functionality in ``drm_helper_connector_dpms``.

    This callback is also used to disable a CRTC by calling it with
    DRM_MODE_DPMS_OFF if the ``disable`` hook isn't used.

    This callback is used by the legacy CRTC helpers. Atomic helpers
    also support using this hook for enabling and disabling a CRTC to
    facilitate transitions to atomic, but it is deprecated. Instead
    ``enable`` and ``disable`` should be used.

prepare
    This callback should prepare the CRTC for a subsequent modeset,
    which in practice means the driver should disable the CRTC if it is
    running. Most drivers ended up implementing this by calling their
    ``dpms`` hook with DRM_MODE_DPMS_OFF.

    This callback is used by the legacy CRTC helpers. Atomic helpers
    also support using this hook for disabling a CRTC to facilitate
    transitions to atomic, but it is deprecated. Instead ``disable``
    should be used.

commit
    This callback should commit the new mode on the CRTC after a
    modeset, which in practice means the driver should enable the CRTC.
    Most drivers ended up implementing this by calling their ``dpms``
    hook with DRM_MODE_DPMS_ON.

    This callback is used by the legacy CRTC helpers. Atomic helpers
    also support using this hook for enabling a CRTC to facilitate
    transitions to atomic, but it is deprecated. Instead ``enable``
    should be used.

mode_fixup
    This callback is used to validate a mode. The parameter mode is the
    display mode that userspace requested, adjusted_mode is the mode
    the encoders need to be fed with. Note that this is the inverse
    semantics of the meaning for the ``drm_encoder`` and ``drm_bridge``
    ->``mode_fixup`` functions. If the CRTC cannot support the requested
    conversion from mode to adjusted_mode it should reject the modeset.

    This function is used by both legacy CRTC helpers and atomic
    helpers. With atomic helpers it is optional.

    NOTE:

    This function is called in the check phase of atomic modesets, which
    can be aborted for any reason (including on userspace's request to
    just check whether a configuration would be possible). Atomic
    drivers MUST NOT touch any persistent state (hardware or software)
    or data structures except the passed in adjusted_mode parameter.

    This is in contrast to the legacy CRTC helpers where this was
    allowed.

    Atomic drivers which need to inspect and adjust more state should
    instead use the ``atomic_check`` callback.

    Also beware that neither core nor helpers filter modes before
    passing them to the driver: While the list of modes that is
    advertised to userspace is filtered using the connector's
    ->``mode_valid`` callback, neither the core nor the helpers do any
    filtering on modes passed in from userspace when setting a mode. It
    is therefore possible for userspace to pass in a mode that was
    previously filtered out using ->``mode_valid`` or add a custom mode
    that wasn't probed from EDID or similar to begin with. Even though
    this is an advanced feature and rarely used nowadays, some users
    rely on being able to specify modes manually so drivers must be
    prepared to deal with it. Specifically this means that all drivers
    need not only validate modes in ->``mode_valid`` but also in
    ->``mode_fixup`` to make sure invalid modes passed in from userspace
    are rejected.

    RETURNS:

    True if an acceptable configuration is possible, false if the
    modeset operation should be rejected.

mode_set
    This callback is used by the legacy CRTC helpers to set a new mode,
    position and framebuffer. Since it ties the primary plane to every
    mode change it is incompatible with universal plane support. And
    since it can't update other planes it's incompatible with atomic
    modeset support.

    This callback is only used by CRTC helpers and deprecated.

    RETURNS:

    0 on success or a negative error code on failure.

mode_set_nofb
    This callback is used to update the display mode of a CRTC without
    changing anything of the primary plane configuration. This fits the
    requirement of atomic and hence is used by the atomic helpers. It is
    also used by the transitional plane helpers to implement a
    ``mode_set`` hook in ``drm_helper_crtc_mode_set``.

    Note that the display pipe is completely off when this function is
    called. Atomic drivers which need hardware to be running before they
    program the new display mode (e.g. because they implement runtime
    PM) should not use this hook. This is because the helper library
    calls this hook only once per mode change and not every time the
    display pipeline is suspended using either DPMS or the new “ACTIVE”
    property. Which means register values set in this callback might get
    reset when the CRTC is suspended, but not restored. Such drivers
    should instead move all their CRTC setup into the ``enable``
    callback.

    This callback is optional.

mode_set_base
    This callback is used by the legacy CRTC helpers to set a new
    framebuffer and scanout position. It is optional and used as an
    optimized fast-path instead of a full mode set operation with all
    the resulting flickering. If it is not present
    ``drm_crtc_helper_set_config`` will fall back to a full modeset,
    using the ->``mode_set`` callback. Since it can't update other
    planes it's incompatible with atomic modeset support.

    This callback is only used by the CRTC helpers and deprecated.

    RETURNS:

    0 on success or a negative error code on failure.

mode_set_base_atomic
    This callback is used by the fbdev helpers to set a new framebuffer
    and scanout without sleeping, i.e. from an atomic calling context.
    It is only used to implement kgdb support.

    This callback is optional and only needed for kgdb support in the
    fbdev helpers.

    RETURNS:

    0 on success or a negative error code on failure.

load_lut
    Load a LUT prepared with the ``gamma_set`` functions from
    ``drm_fb_helper_funcs``.

    This callback is optional and is only used by the fbdev emulation
    helpers.

    FIXME:

    This callback is functionally redundant with the core gamma table
    support and simply exists because the fbdev hasn't yet been
    refactored to use the core gamma table interfaces.

disable
    This callback should be used to disable the CRTC. With the atomic
    drivers it is called after all encoders connected to this CRTC have
    been shut off already using their own ->disable hook. If that
    sequence is too simple drivers can just add their own hooks and call
    it from this CRTC callback here by looping over all encoders
    connected to it using ``for_each_encoder_on_crtc``.

    This hook is used both by legacy CRTC helpers and atomic helpers.
    Atomic drivers don't need to implement it if there's no need to
    disable anything at the CRTC level. To ensure that runtime PM
    handling (using either DPMS or the new “ACTIVE” property) works
    ``disable`` must be the inverse of ``enable`` for atomic drivers.

    NOTE:

    With legacy CRTC helpers there's a big semantic difference between
    ``disable`` and other hooks (like ``prepare`` or ``dpms``) used to
    shut down a CRTC: ``disable`` is only called when also logically
    disabling the display pipeline and needs to release any resources
    acquired in ``mode_set`` (like shared PLLs, or again release pinned
    framebuffers).

    Therefore ``disable`` must be the inverse of ``mode_set`` plus
    ``commit`` for drivers still using legacy CRTC helpers, which is
    different from the rules under atomic.

enable
    This callback should be used to enable the CRTC. With the atomic
    drivers it is called before all encoders connected to this CRTC are
    enabled through the encoder's own ->enable hook. If that sequence is
    too simple drivers can just add their own hooks and call it from
    this CRTC callback here by looping over all encoders connected to it
    using ``for_each_encoder_on_crtc``.

    This hook is used only by atomic helpers, for symmetry with
    ``disable``. Atomic drivers don't need to implement it if there's no
    need to enable anything at the CRTC level. To ensure that runtime PM
    handling (using either DPMS or the new “ACTIVE” property) works
    ``enable`` must be the inverse of ``disable`` for atomic drivers.

atomic_check
    Drivers should check plane-update related CRTC constraints in this
    hook. They can also check mode related limitations but need to be
    aware of the calling order, since this hook is used by
    ``drm_atomic_helper_check_planes`` whereas the preparations needed
    to check output routing and the display mode is done in
    ``drm_atomic_helper_check_modeset``. Therefore drivers that want to
    check output routing and display mode constraints in this callback
    must ensure that ``drm_atomic_helper_check_modeset`` has been called
    beforehand. This is calling order used by the default helper
    implementation in ``drm_atomic_helper_check``.

    When using ``drm_atomic_helper_check_planes`` CRTCs'
    ->``atomic_check`` hooks are called after the ones for planes, which
    allows drivers to assign shared resources requested by planes in the
    CRTC callback here. For more complicated dependencies the driver can
    call the provided check helpers multiple times until the computed
    state has a final configuration and everything has been checked.

    This function is also allowed to inspect any other object's state
    and can add more state objects to the atomic commit if needed. Care
    must be taken though to ensure that state check\ ``compute``
    functions for these added states are all called, and derived state
    in other objects all updated. Again the recommendation is to just
    call check helpers until a maximal configuration is reached.

    This callback is used by the atomic modeset helpers and by the
    transitional plane helpers, but it is optional.

    NOTE:

    This function is called in the check phase of an atomic update. The
    driver is not allowed to change anything outside of the
    free-standing state objects passed-in or assembled in the overall
    ``drm_atomic_state`` update tracking structure.

    RETURNS:

    0 on success, -EINVAL if the state or the transition can't be
    supported, -ENOMEM on memory allocation failure and -EDEADLK if an
    attempt to obtain another state object ran into a
    ``drm_modeset_lock`` deadlock.

atomic_begin
    Drivers should prepare for an atomic update of multiple planes on a
    CRTC in this hook. Depending upon hardware this might be vblank
    evasion, blocking updates by setting bits or doing preparatory work
    for e.g. manual update display.

    This hook is called before any plane commit functions are called.

    Note that the power state of the display pipe when this function is
    called depends upon the exact helpers and calling sequence the
    driver has picked. See ``drm_atomic_commit_planes`` for a discussion
    of the tradeoffs and variants of plane commit helpers.

    This callback is used by the atomic modeset helpers and by the
    transitional plane helpers, but it is optional.

atomic_flush
    Drivers should finalize an atomic update of multiple planes on a
    CRTC in this hook. Depending upon hardware this might include
    checking that vblank evasion was successful, unblocking updates by
    setting bits or setting the GO bit to flush out all updates.

    Simple hardware or hardware with special requirements can commit and
    flush out all updates for all planes from this hook and forgo all
    the other commit hooks for plane updates.

    This hook is called after any plane commit functions are called.

    Note that the power state of the display pipe when this function is
    called depends upon the exact helpers and calling sequence the
    driver has picked. See ``drm_atomic_commit_planes`` for a discussion
    of the tradeoffs and variants of plane commit helpers.

    This callback is used by the atomic modeset helpers and by the
    transitional plane helpers, but it is optional.


overview
========

These hooks are used by the legacy CRTC helpers, the transitional plane
helpers and the new atomic modesetting helpers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
