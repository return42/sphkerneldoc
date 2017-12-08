.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_bridge.c

.. _`overview`:

overview
========

&struct drm_bridge represents a device that hangs on to an encoder. These are
handy when a regular \ :c:type:`struct drm_encoder <drm_encoder>`\  entity isn't enough to represent the entire
encoder chain.

A bridge is always attached to a single \ :c:type:`struct drm_encoder <drm_encoder>`\  at a time, but can be
either connected to it directly, or through an intermediate bridge::

    encoder ---> bridge B ---> bridge A

Here, the output of the encoder feeds to bridge B, and that furthers feeds to
bridge A.

The driver using the bridge is responsible to make the associations between
the encoder and bridges. Once these links are made, the bridges will
participate along with encoder functions to perform mode_set/enable/disable
through the ops provided in \ :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>`\ .

drm_bridge, like drm_panel, aren't drm_mode_object entities like planes,
CRTCs, encoders or connectors and hence are not visible to userspace. They
just provide additional hooks to get the desired output at the end of the
encoder chain.

Bridges can also be chained up using the \ :c:type:`drm_bridge.next <drm_bridge>`\  pointer.

Both legacy CRTC helpers and the new atomic modeset helpers support bridges.

.. _`drm_bridge_add`:

drm_bridge_add
==============

.. c:function:: void drm_bridge_add(struct drm_bridge *bridge)

    add the given bridge to the global bridge list

    :param struct drm_bridge \*bridge:
        bridge control structure

.. _`drm_bridge_remove`:

drm_bridge_remove
=================

.. c:function:: void drm_bridge_remove(struct drm_bridge *bridge)

    remove the given bridge from the global bridge list

    :param struct drm_bridge \*bridge:
        bridge control structure

.. _`drm_bridge_attach`:

drm_bridge_attach
=================

.. c:function:: int drm_bridge_attach(struct drm_encoder *encoder, struct drm_bridge *bridge, struct drm_bridge *previous)

    attach the bridge to an encoder's chain

    :param struct drm_encoder \*encoder:
        DRM encoder

    :param struct drm_bridge \*bridge:
        bridge to attach

    :param struct drm_bridge \*previous:
        previous bridge in the chain (optional)

.. _`drm_bridge_attach.description`:

Description
-----------

Called by a kms driver to link the bridge to an encoder's chain. The previous
argument specifies the previous bridge in the chain. If NULL, the bridge is
linked directly at the encoder's output. Otherwise it is linked at the
previous bridge's output.

If non-NULL the previous bridge must be already attached by a call to this
function.

.. _`drm_bridge_attach.return`:

Return
------

Zero on success, error code on failure

.. _`bridge-callbacks`:

bridge callbacks
================

The \ :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>`\  ops are populated by the bridge driver. The DRM
internals (atomic and CRTC helpers) use the helpers defined in drm_bridge.c
These helpers call a specific \ :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>`\  op for all the bridges
during encoder configuration.

For detailed specification of the bridge callbacks see \ :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>`\ .

.. _`drm_bridge_mode_fixup`:

drm_bridge_mode_fixup
=====================

.. c:function:: bool drm_bridge_mode_fixup(struct drm_bridge *bridge, const struct drm_display_mode *mode, struct drm_display_mode *adjusted_mode)

    fixup proposed mode for all bridges in the encoder chain

    :param struct drm_bridge \*bridge:
        bridge control structure

    :param const struct drm_display_mode \*mode:
        desired mode to be set for the bridge

    :param struct drm_display_mode \*adjusted_mode:
        updated mode that works for this bridge

.. _`drm_bridge_mode_fixup.description`:

Description
-----------

Calls \ :c:type:`drm_bridge_funcs.mode_fixup <drm_bridge_funcs>`\  for all the bridges in the
encoder chain, starting from the first bridge to the last.

.. _`drm_bridge_mode_fixup.note`:

Note
----

the bridge passed should be the one closest to the encoder

.. _`drm_bridge_mode_fixup.return`:

Return
------

true on success, false on failure

.. _`drm_bridge_mode_valid`:

drm_bridge_mode_valid
=====================

.. c:function:: enum drm_mode_status drm_bridge_mode_valid(struct drm_bridge *bridge, const struct drm_display_mode *mode)

    validate the mode against all bridges in the encoder chain.

    :param struct drm_bridge \*bridge:
        bridge control structure

    :param const struct drm_display_mode \*mode:
        desired mode to be validated

.. _`drm_bridge_mode_valid.description`:

Description
-----------

Calls \ :c:type:`drm_bridge_funcs.mode_valid <drm_bridge_funcs>`\  for all the bridges in the encoder
chain, starting from the first bridge to the last. If at least one bridge
does not accept the mode the function returns the error code.

.. _`drm_bridge_mode_valid.note`:

Note
----

the bridge passed should be the one closest to the encoder.

.. _`drm_bridge_mode_valid.return`:

Return
------

MODE_OK on success, drm_mode_status Enum error code on failure

.. _`drm_bridge_disable`:

drm_bridge_disable
==================

.. c:function:: void drm_bridge_disable(struct drm_bridge *bridge)

    disables all bridges in the encoder chain

    :param struct drm_bridge \*bridge:
        bridge control structure

.. _`drm_bridge_disable.description`:

Description
-----------

Calls \ :c:type:`drm_bridge_funcs.disable <drm_bridge_funcs>`\  op for all the bridges in the encoder
chain, starting from the last bridge to the first. These are called before
calling the encoder's prepare op.

.. _`drm_bridge_disable.note`:

Note
----

the bridge passed should be the one closest to the encoder

.. _`drm_bridge_post_disable`:

drm_bridge_post_disable
=======================

.. c:function:: void drm_bridge_post_disable(struct drm_bridge *bridge)

    cleans up after disabling all bridges in the encoder chain

    :param struct drm_bridge \*bridge:
        bridge control structure

.. _`drm_bridge_post_disable.description`:

Description
-----------

Calls \ :c:type:`drm_bridge_funcs.post_disable <drm_bridge_funcs>`\  op for all the bridges in the
encoder chain, starting from the first bridge to the last. These are called
after completing the encoder's prepare op.

.. _`drm_bridge_post_disable.note`:

Note
----

the bridge passed should be the one closest to the encoder

.. _`drm_bridge_mode_set`:

drm_bridge_mode_set
===================

.. c:function:: void drm_bridge_mode_set(struct drm_bridge *bridge, struct drm_display_mode *mode, struct drm_display_mode *adjusted_mode)

    set proposed mode for all bridges in the encoder chain

    :param struct drm_bridge \*bridge:
        bridge control structure

    :param struct drm_display_mode \*mode:
        desired mode to be set for the bridge

    :param struct drm_display_mode \*adjusted_mode:
        updated mode that works for this bridge

.. _`drm_bridge_mode_set.description`:

Description
-----------

Calls \ :c:type:`drm_bridge_funcs.mode_set <drm_bridge_funcs>`\  op for all the bridges in the
encoder chain, starting from the first bridge to the last.

.. _`drm_bridge_mode_set.note`:

Note
----

the bridge passed should be the one closest to the encoder

.. _`drm_bridge_pre_enable`:

drm_bridge_pre_enable
=====================

.. c:function:: void drm_bridge_pre_enable(struct drm_bridge *bridge)

    prepares for enabling all bridges in the encoder chain

    :param struct drm_bridge \*bridge:
        bridge control structure

.. _`drm_bridge_pre_enable.description`:

Description
-----------

Calls \ :c:type:`drm_bridge_funcs.pre_enable <drm_bridge_funcs>`\  op for all the bridges in the encoder
chain, starting from the last bridge to the first. These are called
before calling the encoder's commit op.

.. _`drm_bridge_pre_enable.note`:

Note
----

the bridge passed should be the one closest to the encoder

.. _`drm_bridge_enable`:

drm_bridge_enable
=================

.. c:function:: void drm_bridge_enable(struct drm_bridge *bridge)

    enables all bridges in the encoder chain

    :param struct drm_bridge \*bridge:
        bridge control structure

.. _`drm_bridge_enable.description`:

Description
-----------

Calls \ :c:type:`drm_bridge_funcs.enable <drm_bridge_funcs>`\  op for all the bridges in the encoder
chain, starting from the first bridge to the last. These are called
after completing the encoder's commit op.

Note that the bridge passed should be the one closest to the encoder

.. _`of_drm_find_bridge`:

of_drm_find_bridge
==================

.. c:function:: struct drm_bridge *of_drm_find_bridge(struct device_node *np)

    find the bridge corresponding to the device node in the global bridge list

    :param struct device_node \*np:
        device node

.. _`of_drm_find_bridge.return`:

Return
------

drm_bridge control struct on success, NULL on failure

.. This file was automatic generated / don't edit.

