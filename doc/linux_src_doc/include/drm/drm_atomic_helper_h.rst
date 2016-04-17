.. -*- coding: utf-8; mode: rst -*-

===================
drm_atomic_helper.h
===================


.. _`drm_atomic_crtc_for_each_plane`:

drm_atomic_crtc_for_each_plane
==============================

.. c:function:: drm_atomic_crtc_for_each_plane ( plane,  crtc)

    iterate over planes currently attached to CRTC

    :param plane:
        the loop cursor

    :param crtc:
        the crtc whose planes are iterated



.. _`drm_atomic_crtc_for_each_plane.description`:

Description
-----------

This iterates over the current state, useful (for example) when applying
atomic state after it has been checked and swapped.  To iterate over the
planes which \*will\* be attached (for ->:c:func:`atomic_check`) see
:c:func:`drm_crtc_for_each_pending_plane`



.. _`drm_atomic_crtc_state_for_each_plane`:

drm_atomic_crtc_state_for_each_plane
====================================

.. c:function:: drm_atomic_crtc_state_for_each_plane ( plane,  crtc_state)

    iterate over attached planes in new state

    :param plane:
        the loop cursor

    :param crtc_state:
        the incoming crtc-state



.. _`drm_atomic_crtc_state_for_each_plane.description`:

Description
-----------

Similar to :c:func:`drm_crtc_for_each_plane`, but iterates the planes that will be
attached if the specified state is applied.  Useful during (for example)
->:c:func:`atomic_check` operations, to validate the incoming state

