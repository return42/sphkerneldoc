.. -*- coding: utf-8; mode: rst -*-

===========
intel_fbc.c
===========



.. _xref_intel_fbc_is_active:

intel_fbc_is_active
===================

.. c:function:: bool intel_fbc_is_active (struct drm_i915_private * dev_priv)

    Is FBC active?

    :param struct drm_i915_private * dev_priv:
        i915 device instance



Description
-----------

This function is used to verify the current state of FBC.



FIXME
-----

This should be tracked in the plane config eventually
       instead of queried at runtime for most callers.




.. _xref_intel_fbc_choose_crtc:

intel_fbc_choose_crtc
=====================

.. c:function:: void intel_fbc_choose_crtc (struct drm_i915_private * dev_priv, struct drm_atomic_state * state)

    select a CRTC to enable FBC on

    :param struct drm_i915_private * dev_priv:
        i915 device instance

    :param struct drm_atomic_state * state:
        the atomic state structure



Description
-----------

This function looks at the proposed state for CRTCs and planes, then chooses
which pipe is going to have FBC by setting intel_crtc_state->enable_fbc to
true.


Later, intel_fbc_enable is going to look for state->enable_fbc and then maybe
enable FBC for the chosen CRTC. If it does, it will set dev_priv->fbc.crtc.




.. _xref_intel_fbc_enable:

intel_fbc_enable
================

.. c:function:: void intel_fbc_enable (struct intel_crtc * crtc)

    

    :param struct intel_crtc * crtc:
        the CRTC



Description
-----------

This function checks if the given CRTC was chosen for FBC, then enables it if
possible. Notice that it doesn't activate FBC. It is valid to call
intel_fbc_enable multiple times for the same pipe without an
intel_fbc_disable in the middle, as long as it is deactivated.




.. _xref___intel_fbc_disable:

__intel_fbc_disable
===================

.. c:function:: void __intel_fbc_disable (struct drm_i915_private * dev_priv)

    disable FBC

    :param struct drm_i915_private * dev_priv:
        i915 device instance



Description
-----------

This is the low level function that actually disables FBC. Callers should
grab the FBC lock.




.. _xref_intel_fbc_disable:

intel_fbc_disable
=================

.. c:function:: void intel_fbc_disable (struct intel_crtc * crtc)

    disable FBC if it's associated with crtc

    :param struct intel_crtc * crtc:
        the CRTC



Description
-----------

This function disables FBC if it's associated with the provided CRTC.




.. _xref_intel_fbc_global_disable:

intel_fbc_global_disable
========================

.. c:function:: void intel_fbc_global_disable (struct drm_i915_private * dev_priv)

    globally disable FBC

    :param struct drm_i915_private * dev_priv:
        i915 device instance



Description
-----------

This function disables FBC regardless of which CRTC is associated with it.




.. _xref_intel_fbc_init_pipe_state:

intel_fbc_init_pipe_state
=========================

.. c:function:: void intel_fbc_init_pipe_state (struct drm_i915_private * dev_priv)

    initialize FBC's CRTC visibility tracking

    :param struct drm_i915_private * dev_priv:
        i915 device instance



Description
-----------

The FBC code needs to track CRTC visibility since the older platforms can't
have FBC enabled while multiple pipes are used. This function does the
initial setup at driver load to make sure FBC is matching the real hardware.




.. _xref_intel_fbc_init:

intel_fbc_init
==============

.. c:function:: void intel_fbc_init (struct drm_i915_private * dev_priv)

    Initialize FBC

    :param struct drm_i915_private * dev_priv:
        the i915 device



Description
-----------

This function might be called during PM init process.


