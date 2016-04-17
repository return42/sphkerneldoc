.. -*- coding: utf-8; mode: rst -*-

============
drm_bridge.c
============


.. _`overview`:

overview
========

struct :c:type:`struct drm_bridge <drm_bridge>` represents a device that hangs on to an encoder. These are
handy when a regular :c:type:`struct drm_encoder <drm_encoder>` entity isn't enough to represent the entire
encoder chain.

A bridge is always attached to a single :c:type:`struct drm_encoder <drm_encoder>` at a time, but can be
either connected to it directly, or through an intermediate bridge::

    encoder ---> bridge B ---> bridge A

Here, the output of the encoder feeds to bridge B, and that furthers feeds to
bridge A.

The driver using the bridge is responsible to make the associations between
the encoder and bridges. Once these links are made, the bridges will
participate along with encoder functions to perform mode_set/enable/disable
through the ops provided in :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>`.

drm_bridge, like drm_panel, aren't drm_mode_object entities like planes,
CRTCs, encoders or connectors and hence are not visible to userspace. They
just provide additional hooks to get the desired output at the end of the
encoder chain.

Bridges can also be chained up using the next pointer in struct :c:type:`struct drm_bridge <drm_bridge>`.

Both legacy CRTC helpers and the new atomic modeset helpers support bridges.



.. _`drm_bridge_add`:

drm_bridge_add
==============

.. c:function:: int drm_bridge_add (struct drm_bridge *bridge)

    add the given bridge to the global bridge list

    :param struct drm_bridge \*bridge:
        bridge control structure



.. _`drm_bridge_add.returns`:

RETURNS
-------

Unconditionally returns Zero.



.. _`drm_bridge_remove`:

drm_bridge_remove
=================

.. c:function:: void drm_bridge_remove (struct drm_bridge *bridge)

    remove the given bridge from the global bridge list

    :param struct drm_bridge \*bridge:
        bridge control structure



.. _`drm_bridge_attach`:

drm_bridge_attach
=================

.. c:function:: int drm_bridge_attach (struct drm_device *dev, struct drm_bridge *bridge)

    associate given bridge to our DRM device

    :param struct drm_device \*dev:
        DRM device

    :param struct drm_bridge \*bridge:
        bridge control structure



.. _`drm_bridge_attach.description`:

Description
-----------

called by a kms driver to link one of our encoder/bridge to the given
bridge.

Note that setting up links between the bridge and our encoder/bridge
objects needs to be handled by the kms driver itself



.. _`drm_bridge_attach.returns`:

RETURNS
-------

Zero on success, error code on failure



.. _`bridge-callbacks`:

bridge callbacks
================

The :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>` ops are populated by the bridge driver. The DRM
internals (atomic and CRTC helpers) use the helpers defined in drm_bridge.c
These helpers call a specific :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>` op for all the bridges
during encoder configuration.

For detailed specification of the bridge callbacks see :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>`.



.. _`drm_bridge_mode_fixup`:

drm_bridge_mode_fixup
=====================

.. c:function:: bool drm_bridge_mode_fixup (struct drm_bridge *bridge, const struct drm_display_mode *mode, struct drm_display_mode *adjusted_mode)

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

Calls ->:c:func:`mode_fixup` :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>` op for all the bridges in the
encoder chain, starting from the first bridge to the last.



.. _`drm_bridge_mode_fixup.note`:

Note
----

the bridge passed should be the one closest to the encoder



.. _`drm_bridge_mode_fixup.returns`:

RETURNS
-------

true on success, false on failure



.. _`drm_bridge_disable`:

drm_bridge_disable
==================

.. c:function:: void drm_bridge_disable (struct drm_bridge *bridge)

    calls ->disable() &drm_bridge_funcs op for all bridges in the encoder chain.

    :param struct drm_bridge \*bridge:
        bridge control structure



.. _`drm_bridge_disable.description`:

Description
-----------

Calls ->:c:func:`disable` :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>` op for all the bridges in the encoder
chain, starting from the last bridge to the first. These are called before
calling the encoder's prepare op.



.. _`drm_bridge_disable.note`:

Note
----

the bridge passed should be the one closest to the encoder



.. _`drm_bridge_post_disable`:

drm_bridge_post_disable
=======================

.. c:function:: void drm_bridge_post_disable (struct drm_bridge *bridge)

    calls ->post_disable() &drm_bridge_funcs op for all bridges in the encoder chain.

    :param struct drm_bridge \*bridge:
        bridge control structure



.. _`drm_bridge_post_disable.description`:

Description
-----------

Calls ->:c:func:`post_disable` :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>` op for all the bridges in the
encoder chain, starting from the first bridge to the last. These are called
after completing the encoder's prepare op.



.. _`drm_bridge_post_disable.note`:

Note
----

the bridge passed should be the one closest to the encoder



.. _`drm_bridge_mode_set`:

drm_bridge_mode_set
===================

.. c:function:: void drm_bridge_mode_set (struct drm_bridge *bridge, struct drm_display_mode *mode, struct drm_display_mode *adjusted_mode)

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

Calls ->:c:func:`mode_set` :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>` op for all the bridges in the
encoder chain, starting from the first bridge to the last.



.. _`drm_bridge_mode_set.note`:

Note
----

the bridge passed should be the one closest to the encoder



.. _`drm_bridge_pre_enable`:

drm_bridge_pre_enable
=====================

.. c:function:: void drm_bridge_pre_enable (struct drm_bridge *bridge)

    calls ->pre_enable() &drm_bridge_funcs op for all bridges in the encoder chain.

    :param struct drm_bridge \*bridge:
        bridge control structure



.. _`drm_bridge_pre_enable.description`:

Description
-----------

Calls ->:c:func:`pre_enable` :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>` op for all the bridges in the encoder
chain, starting from the last bridge to the first. These are called
before calling the encoder's commit op.



.. _`drm_bridge_pre_enable.note`:

Note
----

the bridge passed should be the one closest to the encoder



.. _`drm_bridge_enable`:

drm_bridge_enable
=================

.. c:function:: void drm_bridge_enable (struct drm_bridge *bridge)

    calls ->enable() &drm_bridge_funcs op for all bridges in the encoder chain.

    :param struct drm_bridge \*bridge:
        bridge control structure



.. _`drm_bridge_enable.description`:

Description
-----------

Calls ->:c:func:`enable` :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>` op for all the bridges in the encoder
chain, starting from the first bridge to the last. These are called
after completing the encoder's commit op.

Note that the bridge passed should be the one closest to the encoder



.. _`of_drm_find_bridge`:

of_drm_find_bridge
==================

.. c:function:: struct drm_bridge *of_drm_find_bridge (struct device_node *np)

    find the bridge corresponding to the device node in the global bridge list

    :param struct device_node \*np:
        device node



.. _`of_drm_find_bridge.returns`:

RETURNS
-------

drm_bridge control struct on success, NULL on failure

