.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_bridge.c

.. _`drm_bridge_add`:

drm_bridge_add
==============

.. c:function:: int drm_bridge_add(struct drm_bridge *bridge)

    add the given bridge to the global bridge list

    :param struct drm_bridge \*bridge:
        bridge control structure

.. _`drm_bridge_add.return`:

Return
------

Unconditionally returns Zero.

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

