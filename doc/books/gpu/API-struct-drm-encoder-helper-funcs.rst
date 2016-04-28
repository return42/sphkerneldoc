.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-drm-encoder-helper-funcs:

===============================
struct drm_encoder_helper_funcs
===============================

*man struct drm_encoder_helper_funcs(9)*

*4.6.0-rc5*

helper operations for encoders


Synopsis
========

.. code-block:: c

    struct drm_encoder_helper_funcs {
      void (* dpms) (struct drm_encoder *encoder, int mode);
      bool (* mode_fixup) (struct drm_encoder *encoder,const struct drm_display_mode *mode,struct drm_display_mode *adjusted_mode);
      void (* prepare) (struct drm_encoder *encoder);
      void (* commit) (struct drm_encoder *encoder);
      void (* mode_set) (struct drm_encoder *encoder,struct drm_display_mode *mode,struct drm_display_mode *adjusted_mode);
      struct drm_crtc *(* get_crtc) (struct drm_encoder *encoder);
      enum drm_connector_status (* detect) (struct drm_encoder *encoder,struct drm_connector *connector);
      void (* disable) (struct drm_encoder *encoder);
      void (* enable) (struct drm_encoder *encoder);
      int (* atomic_check) (struct drm_encoder *encoder,struct drm_crtc_state *crtc_state,struct drm_connector_state *conn_state);
    };


Members
=======

dpms
    Callback to control power levels on the encoder. If the mode passed
    in is unsupported, the provider must use the next lowest power
    level. This is used by the legacy encoder helpers to implement DPMS
    functionality in ``drm_helper_connector_dpms``.

    This callback is also used to disable an encoder by calling it with
    DRM_MODE_DPMS_OFF if the ``disable`` hook isn't used.

    This callback is used by the legacy CRTC helpers. Atomic helpers
    also support using this hook for enabling and disabling an encoder
    to facilitate transitions to atomic, but it is deprecated. Instead
    ``enable`` and ``disable`` should be used.

mode_fixup
    This callback is used to validate and adjust a mode. The parameter
    mode is the display mode that should be fed to the next element in
    the display chain, either the final ``drm_connector`` or a
    ``drm_bridge``. The parameter adjusted_mode is the input mode the
    encoder requires. It can be modified by this callback and does not
    need to match mode.

    This function is used by both legacy CRTC helpers and atomic
    helpers. This hook is optional.

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

prepare
    This callback should prepare the encoder for a subsequent modeset,
    which in practice means the driver should disable the encoder if it
    is running. Most drivers ended up implementing this by calling their
    ``dpms`` hook with DRM_MODE_DPMS_OFF.

    This callback is used by the legacy CRTC helpers. Atomic helpers
    also support using this hook for disabling an encoder to facilitate
    transitions to atomic, but it is deprecated. Instead ``disable``
    should be used.

commit
    This callback should commit the new mode on the encoder after a
    modeset, which in practice means the driver should enable the
    encoder. Most drivers ended up implementing this by calling their
    ``dpms`` hook with DRM_MODE_DPMS_ON.

    This callback is used by the legacy CRTC helpers. Atomic helpers
    also support using this hook for enabling an encoder to facilitate
    transitions to atomic, but it is deprecated. Instead ``enable``
    should be used.

mode_set
    This callback is used to update the display mode of an encoder.

    Note that the display pipe is completely off when this function is
    called. Drivers which need hardware to be running before they
    program the new display mode (because they implement runtime PM)
    should not use this hook, because the helper library calls it only
    once and not every time the display pipeline is suspend using either
    DPMS or the new “ACTIVE” property. Such drivers should instead move
    all their encoder setup into the ->``enable`` callback.

    This callback is used both by the legacy CRTC helpers and the atomic
    modeset helpers. It is optional in the atomic helpers.

get_crtc
    This callback is used by the legacy CRTC helpers to work around
    deficiencies in its own book-keeping.

    Do not use, use atomic helpers instead, which get the book keeping
    right.

    FIXME:

    Currently only nouveau is using this, and as soon as nouveau is
    atomic we can ditch this hook.

detect
    This callback can be used by drivers who want to do detection on the
    encoder object instead of in connector functions.

    It is not used by any helper and therefore has purely
    driver-specific semantics. New drivers shouldn't use this and
    instead just implement their own private callbacks.

    FIXME:

    This should just be converted into a pile of driver vfuncs.
    Currently radeon, amdgpu and nouveau are using it.

disable
    This callback should be used to disable the encoder. With the atomic
    drivers it is called before this encoder's CRTC has been shut off
    using the CRTC's own ->disable hook. If that sequence is too simple
    drivers can just add their own driver private encoder hooks and call
    them from CRTC's callback by looping over all encoders connected to
    it using ``for_each_encoder_on_crtc``.

    This hook is used both by legacy CRTC helpers and atomic helpers.
    Atomic drivers don't need to implement it if there's no need to
    disable anything at the encoder level. To ensure that runtime PM
    handling (using either DPMS or the new “ACTIVE” property) works
    ``disable`` must be the inverse of ``enable`` for atomic drivers.

    NOTE:

    With legacy CRTC helpers there's a big semantic difference between
    ``disable`` and other hooks (like ``prepare`` or ``dpms``) used to
    shut down a encoder: ``disable`` is only called when also logically
    disabling the display pipeline and needs to release any resources
    acquired in ``mode_set`` (like shared PLLs, or again release pinned
    framebuffers).

    Therefore ``disable`` must be the inverse of ``mode_set`` plus
    ``commit`` for drivers still using legacy CRTC helpers, which is
    different from the rules under atomic.

enable
    This callback should be used to enable the encoder. With the atomic
    drivers it is called after this encoder's CRTC has been enabled
    using the CRTC's own ->enable hook. If that sequence is too simple
    drivers can just add their own driver private encoder hooks and call
    them from CRTC's callback by looping over all encoders connected to
    it using ``for_each_encoder_on_crtc``.

    This hook is used only by atomic helpers, for symmetry with
    ``disable``. Atomic drivers don't need to implement it if there's no
    need to enable anything at the encoder level. To ensure that runtime
    PM handling (using either DPMS or the new “ACTIVE” property) works
    ``enable`` must be the inverse of ``disable`` for atomic drivers.

atomic_check
    This callback is used to validate encoder state for atomic drivers.
    Since the encoder is the object connecting the CRTC and connector it
    gets passed both states, to be able to validate interactions and
    update the CRTC to match what the encoder needs for the requested
    connector.

    This function is used by the atomic helpers, but it is optional.

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


Description
===========

These hooks are used by the legacy CRTC helpers, the transitional plane
helpers and the new atomic modesetting helpers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
