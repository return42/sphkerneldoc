.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_bridge.h

.. _`drm_bridge_funcs`:

struct drm_bridge_funcs
=======================

.. c:type:: struct drm_bridge_funcs

    drm_bridge control functions

.. _`drm_bridge_funcs.definition`:

Definition
----------

.. code-block:: c

    struct drm_bridge_funcs {
        int (*attach)(struct drm_bridge *bridge);
        void (*detach)(struct drm_bridge *bridge);
        enum drm_mode_status (*mode_valid)(struct drm_bridge *bridge, const struct drm_display_mode *mode);
        bool (*mode_fixup)(struct drm_bridge *bridge,const struct drm_display_mode *mode, struct drm_display_mode *adjusted_mode);
        void (*disable)(struct drm_bridge *bridge);
        void (*post_disable)(struct drm_bridge *bridge);
        void (*mode_set)(struct drm_bridge *bridge,struct drm_display_mode *mode, struct drm_display_mode *adjusted_mode);
        void (*pre_enable)(struct drm_bridge *bridge);
        void (*enable)(struct drm_bridge *bridge);
    }

.. _`drm_bridge_funcs.members`:

Members
-------

attach

    This callback is invoked whenever our bridge is being attached to a
    \ :c:type:`struct drm_encoder <drm_encoder>`\ .

    The attach callback is optional.

    RETURNS:

    Zero on success, error code on failure.

detach

    This callback is invoked whenever our bridge is being detached from a
    \ :c:type:`struct drm_encoder <drm_encoder>`\ .

    The detach callback is optional.

mode_valid

    This callback is used to check if a specific mode is valid in this
    bridge. This should be implemented if the bridge has some sort of
    restriction in the modes it can display. For example, a given bridge
    may be responsible to set a clock value. If the clock can not
    produce all the values for the available modes then this callback
    can be used to restrict the number of modes to only the ones that
    can be displayed.

    This hook is used by the probe helpers to filter the mode list in
    \ :c:func:`drm_helper_probe_single_connector_modes`\ , and it is used by the
    atomic helpers to validate modes supplied by userspace in
    \ :c:func:`drm_atomic_helper_check_modeset`\ .

    This function is optional.

    NOTE:

    Since this function is both called from the check phase of an atomic
    commit, and the mode validation in the probe paths it is not allowed
    to look at anything else but the passed-in mode, and validate it
    against configuration-invariant hardward constraints. Any further
    limits which depend upon the configuration can only be checked in
    \ ``mode_fixup``\ .

    RETURNS:

    drm_mode_status Enum

mode_fixup

    This callback is used to validate and adjust a mode. The paramater
    mode is the display mode that should be fed to the next element in
    the display chain, either the final \ :c:type:`struct drm_connector <drm_connector>`\  or the next
    \ :c:type:`struct drm_bridge <drm_bridge>`\ . The parameter adjusted_mode is the input mode the bridge
    requires. It can be modified by this callback and does not need to
    match mode. See also \ :c:type:`drm_crtc_state.adjusted_mode <drm_crtc_state>`\  for more details.

    This is the only hook that allows a bridge to reject a modeset. If
    this function passes all other callbacks must succeed for this
    configuration.

    The mode_fixup callback is optional.

    NOTE:

    This function is called in the check phase of atomic modesets, which
    can be aborted for any reason (including on userspace's request to
    just check whether a configuration would be possible). Drivers MUST
    NOT touch any persistent state (hardware or software) or data
    structures except the passed in \ ``state``\  parameter.

    Also beware that userspace can request its own custom modes, neither
    core nor helpers filter modes to the list of probe modes reported by
    the GETCONNECTOR IOCTL and stored in \ :c:type:`drm_connector.modes <drm_connector>`\ . To ensure
    that modes are filtered consistently put any bridge constraints and
    limits checks into \ ``mode_valid``\ .

    RETURNS:

    True if an acceptable configuration is possible, false if the modeset
    operation should be rejected.

disable

    This callback should disable the bridge. It is called right before
    the preceding element in the display pipe is disabled. If the
    preceding element is a bridge this means it's called before that
    bridge's \ ``disable``\  vfunc. If the preceding element is a \ :c:type:`struct drm_encoder <drm_encoder>`\ 
    it's called right before the \ :c:type:`drm_encoder_helper_funcs.disable <drm_encoder_helper_funcs>`\ ,
    \ :c:type:`drm_encoder_helper_funcs.prepare <drm_encoder_helper_funcs>`\  or \ :c:type:`drm_encoder_helper_funcs.dpms <drm_encoder_helper_funcs>`\ 
    hook.

    The bridge can assume that the display pipe (i.e. clocks and timing
    signals) feeding it is still running when this callback is called.

    The disable callback is optional.

post_disable

    This callback should disable the bridge. It is called right after the
    preceding element in the display pipe is disabled. If the preceding
    element is a bridge this means it's called after that bridge's
    \ ``post_disable``\  function. If the preceding element is a \ :c:type:`struct drm_encoder <drm_encoder>`\ 
    it's called right after the encoder's
    \ :c:type:`drm_encoder_helper_funcs.disable <drm_encoder_helper_funcs>`\ , \ :c:type:`drm_encoder_helper_funcs.prepare <drm_encoder_helper_funcs>`\ 
    or \ :c:type:`drm_encoder_helper_funcs.dpms <drm_encoder_helper_funcs>`\  hook.

    The bridge must assume that the display pipe (i.e. clocks and timing
    singals) feeding it is no longer running when this callback is
    called.

    The post_disable callback is optional.

mode_set

    This callback should set the given mode on the bridge. It is called
    after the \ ``mode_set``\  callback for the preceding element in the display
    pipeline has been called already. If the bridge is the first element
    then this would be \ :c:type:`drm_encoder_helper_funcs.mode_set <drm_encoder_helper_funcs>`\ . The display
    pipe (i.e.  clocks and timing signals) is off when this function is
    called.

pre_enable

    This callback should enable the bridge. It is called right before
    the preceding element in the display pipe is enabled. If the
    preceding element is a bridge this means it's called before that
    bridge's \ ``pre_enable``\  function. If the preceding element is a
    \ :c:type:`struct drm_encoder <drm_encoder>`\  it's called right before the encoder's
    \ :c:type:`drm_encoder_helper_funcs.enable <drm_encoder_helper_funcs>`\ , \ :c:type:`drm_encoder_helper_funcs.commit <drm_encoder_helper_funcs>`\  or
    \ :c:type:`drm_encoder_helper_funcs.dpms <drm_encoder_helper_funcs>`\  hook.

    The display pipe (i.e. clocks and timing signals) feeding this bridge
    will not yet be running when this callback is called. The bridge must
    not enable the display link feeding the next bridge in the chain (if
    there is one) when this callback is called.

    The pre_enable callback is optional.

enable

    This callback should enable the bridge. It is called right after
    the preceding element in the display pipe is enabled. If the
    preceding element is a bridge this means it's called after that
    bridge's \ ``enable``\  function. If the preceding element is a
    \ :c:type:`struct drm_encoder <drm_encoder>`\  it's called right after the encoder's
    \ :c:type:`drm_encoder_helper_funcs.enable <drm_encoder_helper_funcs>`\ , \ :c:type:`drm_encoder_helper_funcs.commit <drm_encoder_helper_funcs>`\  or
    \ :c:type:`drm_encoder_helper_funcs.dpms <drm_encoder_helper_funcs>`\  hook.

    The bridge can assume that the display pipe (i.e. clocks and timing
    signals) feeding it is running when this callback is called. This
    callback must enable the display link feeding the next bridge in the
    chain if there is one.

    The enable callback is optional.

.. _`drm_bridge_timings`:

struct drm_bridge_timings
=========================

.. c:type:: struct drm_bridge_timings

    timing information for the bridge

.. _`drm_bridge_timings.definition`:

Definition
----------

.. code-block:: c

    struct drm_bridge_timings {
        u32 sampling_edge;
        u32 setup_time_ps;
        u32 hold_time_ps;
    }

.. _`drm_bridge_timings.members`:

Members
-------

sampling_edge

    Tells whether the bridge samples the digital input signal
    from the display engine on the positive or negative edge of the
    clock, this should reuse the DRM_BUS_FLAG_PIXDATA_[POS|NEG]EDGE
    bitwise flags from the DRM connector (bit 2 and 3 valid).

setup_time_ps

    Defines the time in picoseconds the input data lines must be
    stable before the clock edge.

hold_time_ps

    Defines the time in picoseconds taken for the bridge to sample the
    input signal after the clock edge.

.. _`drm_bridge`:

struct drm_bridge
=================

.. c:type:: struct drm_bridge

    central DRM bridge control structure

.. _`drm_bridge.definition`:

Definition
----------

.. code-block:: c

    struct drm_bridge {
        struct drm_device *dev;
        struct drm_encoder *encoder;
        struct drm_bridge *next;
    #ifdef CONFIG_OF
        struct device_node *of_node;
    #endif
        struct list_head list;
        const struct drm_bridge_timings *timings;
        const struct drm_bridge_funcs *funcs;
        void *driver_private;
    }

.. _`drm_bridge.members`:

Members
-------

dev
    DRM device this bridge belongs to

encoder
    encoder to which this bridge is connected

next
    the next bridge in the encoder chain

of_node
    device node pointer to the bridge

list
    to keep track of all added bridges

timings
    the timing specification for the bridge, if any (may
    be NULL)

funcs
    control functions

driver_private
    pointer to the bridge driver's internal context

.. This file was automatic generated / don't edit.

