.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_fbc.c

.. _`frame-buffer-compression--fbc-`:

Frame Buffer Compression (FBC)
==============================

FBC tries to save memory bandwidth (and so power consumption) by
compressing the amount of memory used by the display. It is total
transparent to user space and completely handled in the kernel.

The benefits of FBC are mostly visible with solid backgrounds and
variation-less patterns. It comes from keeping the memory footprint small
and having fewer memory pages opened and accessed for refreshing the display.

i915 is responsible to reserve stolen memory for FBC and configure its
offset on proper registers. The hardware takes care of all
compress/decompress. However there are many known cases where we have to
forcibly disable it to allow proper screen updates.

.. _`intel_fbc_is_active`:

intel_fbc_is_active
===================

.. c:function:: bool intel_fbc_is_active(struct drm_i915_private *dev_priv)

    Is FBC active?

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_fbc_is_active.description`:

Description
-----------

This function is used to verify the current state of FBC.

FIXME: This should be tracked in the plane config eventually
instead of queried at runtime for most callers.

.. _`__intel_fbc_disable`:

__intel_fbc_disable
===================

.. c:function:: void __intel_fbc_disable(struct drm_i915_private *dev_priv)

    disable FBC

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`__intel_fbc_disable.description`:

Description
-----------

This is the low level function that actually disables FBC. Callers should
grab the FBC lock.

.. _`intel_fbc_choose_crtc`:

intel_fbc_choose_crtc
=====================

.. c:function:: void intel_fbc_choose_crtc(struct drm_i915_private *dev_priv, struct intel_atomic_state *state)

    select a CRTC to enable FBC on

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param state:
        the atomic state structure
    :type state: struct intel_atomic_state \*

.. _`intel_fbc_choose_crtc.description`:

Description
-----------

This function looks at the proposed state for CRTCs and planes, then chooses
which pipe is going to have FBC by setting intel_crtc_state->enable_fbc to
true.

Later, intel_fbc_enable is going to look for state->enable_fbc and then maybe
enable FBC for the chosen CRTC. If it does, it will set dev_priv->fbc.crtc.

.. _`intel_fbc_enable`:

intel_fbc_enable
================

.. c:function:: void intel_fbc_enable(struct intel_crtc *crtc, struct intel_crtc_state *crtc_state, struct intel_plane_state *plane_state)

    tries to enable FBC on the CRTC

    :param crtc:
        the CRTC
    :type crtc: struct intel_crtc \*

    :param crtc_state:
        corresponding \ :c:type:`struct drm_crtc_state <drm_crtc_state>`\  for \ ``crtc``\ 
    :type crtc_state: struct intel_crtc_state \*

    :param plane_state:
        corresponding \ :c:type:`struct drm_plane_state <drm_plane_state>`\  for the primary plane of \ ``crtc``\ 
    :type plane_state: struct intel_plane_state \*

.. _`intel_fbc_enable.description`:

Description
-----------

This function checks if the given CRTC was chosen for FBC, then enables it if
possible. Notice that it doesn't activate FBC. It is valid to call
intel_fbc_enable multiple times for the same pipe without an
intel_fbc_disable in the middle, as long as it is deactivated.

.. _`intel_fbc_disable`:

intel_fbc_disable
=================

.. c:function:: void intel_fbc_disable(struct intel_crtc *crtc)

    disable FBC if it's associated with crtc

    :param crtc:
        the CRTC
    :type crtc: struct intel_crtc \*

.. _`intel_fbc_disable.description`:

Description
-----------

This function disables FBC if it's associated with the provided CRTC.

.. _`intel_fbc_global_disable`:

intel_fbc_global_disable
========================

.. c:function:: void intel_fbc_global_disable(struct drm_i915_private *dev_priv)

    globally disable FBC

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_fbc_global_disable.description`:

Description
-----------

This function disables FBC regardless of which CRTC is associated with it.

.. _`intel_fbc_handle_fifo_underrun_irq`:

intel_fbc_handle_fifo_underrun_irq
==================================

.. c:function:: void intel_fbc_handle_fifo_underrun_irq(struct drm_i915_private *dev_priv)

    disable FBC when we get a FIFO underrun

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_fbc_handle_fifo_underrun_irq.description`:

Description
-----------

Without FBC, most underruns are harmless and don't really cause too many
problems, except for an annoying message on dmesg. With FBC, underruns can
become black screens or even worse, especially when paired with bad
watermarks. So in order for us to be on the safe side, completely disable FBC
in case we ever detect a FIFO underrun on any pipe. An underrun on any pipe
already suggests that watermarks may be bad, so try to be as safe as
possible.

This function is called from the IRQ handler.

.. _`intel_fbc_init_pipe_state`:

intel_fbc_init_pipe_state
=========================

.. c:function:: void intel_fbc_init_pipe_state(struct drm_i915_private *dev_priv)

    initialize FBC's CRTC visibility tracking

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_fbc_init_pipe_state.description`:

Description
-----------

The FBC code needs to track CRTC visibility since the older platforms can't
have FBC enabled while multiple pipes are used. This function does the
initial setup at driver load to make sure FBC is matching the real hardware.

.. _`intel_fbc_init`:

intel_fbc_init
==============

.. c:function:: void intel_fbc_init(struct drm_i915_private *dev_priv)

    Initialize FBC

    :param dev_priv:
        the i915 device
    :type dev_priv: struct drm_i915_private \*

.. _`intel_fbc_init.description`:

Description
-----------

This function might be called during PM init process.

.. This file was automatic generated / don't edit.

