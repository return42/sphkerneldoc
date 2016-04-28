.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-drm-bridge-funcs:

=======================
struct drm_bridge_funcs
=======================

*man struct drm_bridge_funcs(9)*

*4.6.0-rc5*

drm_bridge control functions


Synopsis
========

.. code-block:: c

    struct drm_bridge_funcs {
      int (* attach) (struct drm_bridge *bridge);
      bool (* mode_fixup) (struct drm_bridge *bridge,const struct drm_display_mode *mode,struct drm_display_mode *adjusted_mode);
      void (* disable) (struct drm_bridge *bridge);
      void (* post_disable) (struct drm_bridge *bridge);
      void (* mode_set) (struct drm_bridge *bridge,struct drm_display_mode *mode,struct drm_display_mode *adjusted_mode);
      void (* pre_enable) (struct drm_bridge *bridge);
      void (* enable) (struct drm_bridge *bridge);
    };


Members
=======

attach
    Called during drm_bridge_attach

mode_fixup
    This callback is used to validate and adjust a mode. The paramater
    mode is the display mode that should be fed to the next element in
    the display chain, either the final ``drm_connector`` or the next
    ``drm_bridge``. The parameter adjusted_mode is the input mode the
    bridge requires. It can be modified by this callback and does not
    need to match mode.

    This is the only hook that allows a bridge to reject a modeset. If
    this function passes all other callbacks must succeed for this
    configuration.

    NOTE:

    This function is called in the check phase of atomic modesets, which
    can be aborted for any reason (including on userspace's request to
    just check whether a configuration would be possible). Drivers MUST
    NOT touch any persistent state (hardware or software) or data
    structures except the passed in ``state`` parameter.

    RETURNS:

    True if an acceptable configuration is possible, false if the
    modeset operation should be rejected.

disable
    This callback should disable the bridge. It is called right before
    the preceding element in the display pipe is disabled. If the
    preceding element is a bridge this means it's called before that
    bridge's ->``disable`` function. If the preceding element is a
    ``drm_encoder`` it's called right before the encoder's
    ->``disable``, ->``prepare`` or ->``dpms`` hook from struct
    ``drm_encoder_helper_funcs``.

    The bridge can assume that the display pipe (i.e. clocks and timing
    signals) feeding it is still running when this callback is called.

    The disable callback is optional.

post_disable
    This callback should disable the bridge. It is called right after
    the preceding element in the display pipe is disabled. If the
    preceding element is a bridge this means it's called after that
    bridge's ->``post_disable`` function. If the preceding element is a
    ``drm_encoder`` it's called right after the encoder's ->``disable``,
    ->``prepare`` or ->``dpms`` hook from struct
    ``drm_encoder_helper_funcs``.

    The bridge must assume that the display pipe (i.e. clocks and timing
    singals) feeding it is no longer running when this callback is
    called.

    The post_disable callback is optional.

mode_set
    This callback should set the given mode on the bridge. It is called
    after the ->``mode_set`` callback for the preceding element in the
    display pipeline has been called already. The display pipe (i.e.
    clocks and timing signals) is off when this function is called.

pre_enable
    This callback should enable the bridge. It is called right before
    the preceding element in the display pipe is enabled. If the
    preceding element is a bridge this means it's called before that
    bridge's ->``pre_enable`` function. If the preceding element is a
    ``drm_encoder`` it's called right before the encoder's ->``enable``,
    ->``commit`` or ->``dpms`` hook from struct
    ``drm_encoder_helper_funcs``.

    The display pipe (i.e. clocks and timing signals) feeding this
    bridge will not yet be running when this callback is called. The
    bridge must not enable the display link feeding the next bridge in
    the chain (if there is one) when this callback is called.

    The pre_enable callback is optional.

enable
    This callback should enable the bridge. It is called right after the
    preceding element in the display pipe is enabled. If the preceding
    element is a bridge this means it's called after that bridge's
    ->``enable`` function. If the preceding element is a ``drm_encoder``
    it's called right after the encoder's ->``enable``, ->``commit`` or
    ->``dpms`` hook from struct ``drm_encoder_helper_funcs``.

    The bridge can assume that the display pipe (i.e. clocks and timing
    signals) feeding it is running when this callback is called. This
    callback must enable the display link feeding the next bridge in the
    chain if there is one.

    The enable callback is optional.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
