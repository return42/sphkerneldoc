.. -*- coding: utf-8; mode: rst -*-

============
drm_bridge.c
============



.. _xref_drm_bridge_add:

drm_bridge_add
==============

.. c:function:: int drm_bridge_add (struct drm_bridge * bridge)

    add the given bridge to the global bridge list

    :param struct drm_bridge * bridge:
        bridge control structure



RETURNS
-------

Unconditionally returns Zero.




.. _xref_drm_bridge_remove:

drm_bridge_remove
=================

.. c:function:: void drm_bridge_remove (struct drm_bridge * bridge)

    remove the given bridge from the global bridge list

    :param struct drm_bridge * bridge:
        bridge control structure




.. _xref_drm_bridge_attach:

drm_bridge_attach
=================

.. c:function:: int drm_bridge_attach (struct drm_device * dev, struct drm_bridge * bridge)

    associate given bridge to our DRM device

    :param struct drm_device * dev:
        DRM device

    :param struct drm_bridge * bridge:
        bridge control structure



Description
-----------

called by a kms driver to link one of our encoder/bridge to the given
bridge.


Note that setting up links between the bridge and our encoder/bridge
objects needs to be handled by the kms driver itself



RETURNS
-------

Zero on success, error code on failure




.. _xref_drm_bridge_mode_fixup:

drm_bridge_mode_fixup
=====================

.. c:function:: bool drm_bridge_mode_fixup (struct drm_bridge * bridge, const struct drm_display_mode * mode, struct drm_display_mode * adjusted_mode)

    fixup proposed mode for all bridges in the encoder chain

    :param struct drm_bridge * bridge:
        bridge control structure

    :param const struct drm_display_mode * mode:
        desired mode to be set for the bridge

    :param struct drm_display_mode * adjusted_mode:
        updated mode that works for this bridge



Description
-----------

Calls ->:c:func:`mode_fixup` :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>` op for all the bridges in the
encoder chain, starting from the first bridge to the last.



Note
----

the bridge passed should be the one closest to the encoder



RETURNS
-------

true on success, false on failure




.. _xref_drm_bridge_disable:

drm_bridge_disable
==================

.. c:function:: void drm_bridge_disable (struct drm_bridge * bridge)

    calls -\\\gt;disable() \\\amp;drm_bridge_funcs op for all bridges in the encoder chain.

    :param struct drm_bridge * bridge:
        bridge control structure



Description
-----------

Calls ->:c:func:`disable` :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>` op for all the bridges in the encoder
chain, starting from the last bridge to the first. These are called before
calling the encoder's prepare op.



Note
----

the bridge passed should be the one closest to the encoder




.. _xref_drm_bridge_post_disable:

drm_bridge_post_disable
=======================

.. c:function:: void drm_bridge_post_disable (struct drm_bridge * bridge)

    calls -\\\gt;post_disable() \\\amp;drm_bridge_funcs op for all bridges in the encoder chain.

    :param struct drm_bridge * bridge:
        bridge control structure



Description
-----------

Calls ->:c:func:`post_disable` :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>` op for all the bridges in the
encoder chain, starting from the first bridge to the last. These are called
after completing the encoder's prepare op.



Note
----

the bridge passed should be the one closest to the encoder




.. _xref_drm_bridge_mode_set:

drm_bridge_mode_set
===================

.. c:function:: void drm_bridge_mode_set (struct drm_bridge * bridge, struct drm_display_mode * mode, struct drm_display_mode * adjusted_mode)

    set proposed mode for all bridges in the encoder chain

    :param struct drm_bridge * bridge:
        bridge control structure

    :param struct drm_display_mode * mode:
        desired mode to be set for the bridge

    :param struct drm_display_mode * adjusted_mode:
        updated mode that works for this bridge



Description
-----------

Calls ->:c:func:`mode_set` :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>` op for all the bridges in the
encoder chain, starting from the first bridge to the last.



Note
----

the bridge passed should be the one closest to the encoder




.. _xref_drm_bridge_pre_enable:

drm_bridge_pre_enable
=====================

.. c:function:: void drm_bridge_pre_enable (struct drm_bridge * bridge)

    calls -\\\gt;pre_enable() \\\amp;drm_bridge_funcs op for all bridges in the encoder chain.

    :param struct drm_bridge * bridge:
        bridge control structure



Description
-----------

Calls ->:c:func:`pre_enable` :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>` op for all the bridges in the encoder
chain, starting from the last bridge to the first. These are called
before calling the encoder's commit op.



Note
----

the bridge passed should be the one closest to the encoder




.. _xref_drm_bridge_enable:

drm_bridge_enable
=================

.. c:function:: void drm_bridge_enable (struct drm_bridge * bridge)

    calls -\\\gt;enable() \\\amp;drm_bridge_funcs op for all bridges in the encoder chain.

    :param struct drm_bridge * bridge:
        bridge control structure



Description
-----------

Calls ->:c:func:`enable` :c:type:`struct drm_bridge_funcs <drm_bridge_funcs>` op for all the bridges in the encoder
chain, starting from the first bridge to the last. These are called
after completing the encoder's commit op.


Note that the bridge passed should be the one closest to the encoder




.. _xref_of_drm_find_bridge:

of_drm_find_bridge
==================

.. c:function:: struct drm_bridge * of_drm_find_bridge (struct device_node * np)

    find the bridge corresponding to the device node in the global bridge list

    :param struct device_node * np:
        device node



RETURNS
-------

drm_bridge control struct on success, NULL on failure


