.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_runtime_pm.c

.. _`runtime-pm`:

runtime pm
==========

The i915 driver supports dynamic enabling and disabling of entire hardware
blocks at runtime. This is especially important on the display side where
software is supposed to control many power gates manually on recent hardware,
since on the GT side a lot of the power management is done by the hardware.
But even there some manual control at the device level is required.

Since i915 supports a diverse set of platforms with a unified codebase and
hardware engineers just love to shuffle functionality around between power
domains there's a sizeable amount of indirection required. This file provides
generic functions to the driver for grabbing and releasing references for
abstract power domains. It then maps those to the actual power wells
present for a given platform.

.. _`__intel_display_power_is_enabled`:

__intel_display_power_is_enabled
================================

.. c:function:: bool __intel_display_power_is_enabled(struct drm_i915_private *dev_priv, enum intel_display_power_domain domain)

    unlocked check for a power domain

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param domain:
        power domain to check
    :type domain: enum intel_display_power_domain

.. _`__intel_display_power_is_enabled.description`:

Description
-----------

This is the unlocked version of \ :c:func:`intel_display_power_is_enabled`\  and should
only be used from error capture and recovery code where deadlocks are
possible.

.. _`__intel_display_power_is_enabled.return`:

Return
------

True when the power domain is enabled, false otherwise.

.. _`intel_display_power_is_enabled`:

intel_display_power_is_enabled
==============================

.. c:function:: bool intel_display_power_is_enabled(struct drm_i915_private *dev_priv, enum intel_display_power_domain domain)

    check for a power domain

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param domain:
        power domain to check
    :type domain: enum intel_display_power_domain

.. _`intel_display_power_is_enabled.description`:

Description
-----------

This function can be used to check the hw power domain state. It is mostly
used in hardware state readout functions. Everywhere else code should rely
upon explicit power domain reference counting to ensure that the hardware
block is powered up before accessing it.

Callers must hold the relevant modesetting locks to ensure that concurrent
threads can't disable the power well while the caller tries to read a few
registers.

.. _`intel_display_power_is_enabled.return`:

Return
------

True when the power domain is enabled, false otherwise.

.. _`gen9_set_dc_state`:

gen9_set_dc_state
=================

.. c:function:: void gen9_set_dc_state(struct drm_i915_private *dev_priv, uint32_t state)

    set target display C power state

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param state:
        target DC power state
        - DC_STATE_DISABLE
        - DC_STATE_EN_UPTO_DC5
        - DC_STATE_EN_UPTO_DC6
        - DC_STATE_EN_DC9
    :type state: uint32_t

.. _`gen9_set_dc_state.description`:

Description
-----------

Signal to DMC firmware/HW the target DC power state passed in \ ``state``\ .
DMC/HW can turn off individual display clocks and power rails when entering
a deeper DC power state (higher in number) and turns these back when exiting
that state to a shallower power state (lower in number). The HW will decide
when to actually enter a given state on an on-demand basis, for instance
depending on the active state of display pipes. The state of display
registers backed by affected power rails are saved/restored as needed.

Based on the above enabling a deeper DC power state is asynchronous wrt.
enabling it. Disabling a deeper power state is synchronous: for instance
setting \ ``DC_STATE_DISABLE``\  won't complete until all HW resources are turned
back on and register state is restored. This is guaranteed by the MMIO write
to DC_STATE_EN blocking until the state is restored.

.. _`intel_display_power_get`:

intel_display_power_get
=======================

.. c:function:: void intel_display_power_get(struct drm_i915_private *dev_priv, enum intel_display_power_domain domain)

    grab a power domain reference

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param domain:
        power domain to reference
    :type domain: enum intel_display_power_domain

.. _`intel_display_power_get.description`:

Description
-----------

This function grabs a power domain reference for \ ``domain``\  and ensures that the
power domain and all its parents are powered up. Therefore users should only
grab a reference to the innermost power domain they need.

Any power domain reference obtained by this function must have a symmetric
call to \ :c:func:`intel_display_power_put`\  to release the reference again.

.. _`intel_display_power_get_if_enabled`:

intel_display_power_get_if_enabled
==================================

.. c:function:: bool intel_display_power_get_if_enabled(struct drm_i915_private *dev_priv, enum intel_display_power_domain domain)

    grab a reference for an enabled display power domain

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param domain:
        power domain to reference
    :type domain: enum intel_display_power_domain

.. _`intel_display_power_get_if_enabled.description`:

Description
-----------

This function grabs a power domain reference for \ ``domain``\  and ensures that the
power domain and all its parents are powered up. Therefore users should only
grab a reference to the innermost power domain they need.

Any power domain reference obtained by this function must have a symmetric
call to \ :c:func:`intel_display_power_put`\  to release the reference again.

.. _`intel_display_power_put`:

intel_display_power_put
=======================

.. c:function:: void intel_display_power_put(struct drm_i915_private *dev_priv, enum intel_display_power_domain domain)

    release a power domain reference

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param domain:
        power domain to reference
    :type domain: enum intel_display_power_domain

.. _`intel_display_power_put.description`:

Description
-----------

This function drops the power domain reference obtained by
\ :c:func:`intel_display_power_get`\  and might power down the corresponding hardware
block right away if this is the last reference.

.. _`intel_power_domains_init`:

intel_power_domains_init
========================

.. c:function:: int intel_power_domains_init(struct drm_i915_private *dev_priv)

    initializes the power domain structures

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_power_domains_init.description`:

Description
-----------

Initializes the power domain structures for \ ``dev_priv``\  depending upon the
supported platform.

.. _`intel_power_domains_cleanup`:

intel_power_domains_cleanup
===========================

.. c:function:: void intel_power_domains_cleanup(struct drm_i915_private *dev_priv)

    clean up power domains resources

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_power_domains_cleanup.description`:

Description
-----------

Release any resources acquired by \ :c:func:`intel_power_domains_init`\ 

.. _`intel_power_domains_init_hw`:

intel_power_domains_init_hw
===========================

.. c:function:: void intel_power_domains_init_hw(struct drm_i915_private *dev_priv, bool resume)

    initialize hardware power domain state

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param resume:
        Called from resume code paths or not
    :type resume: bool

.. _`intel_power_domains_init_hw.description`:

Description
-----------

This function initializes the hardware power domain state and enables all
power wells belonging to the INIT power domain. Power wells in other
domains (and not in the INIT domain) are referenced or disabled by
\ :c:func:`intel_modeset_readout_hw_state`\ . After that the reference count of each
power well must match its HW enabled state, see
\ :c:func:`intel_power_domains_verify_state`\ .

It will return with power domains disabled (to be enabled later by
\ :c:func:`intel_power_domains_enable`\ ) and must be paired with
\ :c:func:`intel_power_domains_fini_hw`\ .

.. _`intel_power_domains_fini_hw`:

intel_power_domains_fini_hw
===========================

.. c:function:: void intel_power_domains_fini_hw(struct drm_i915_private *dev_priv)

    deinitialize hw power domain state

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_power_domains_fini_hw.description`:

Description
-----------

De-initializes the display power domain HW state. It also ensures that the
device stays powered up so that the driver can be reloaded.

It must be called with power domains already disabled (after a call to
\ :c:func:`intel_power_domains_disable`\ ) and must be paired with
\ :c:func:`intel_power_domains_init_hw`\ .

.. _`intel_power_domains_enable`:

intel_power_domains_enable
==========================

.. c:function:: void intel_power_domains_enable(struct drm_i915_private *dev_priv)

    enable toggling of display power wells

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_power_domains_enable.description`:

Description
-----------

Enable the ondemand enabling/disabling of the display power wells. Note that
power wells not belonging to POWER_DOMAIN_INIT are allowed to be toggled
only at specific points of the display modeset sequence, thus they are not
affected by the \ :c:func:`intel_power_domains_enable`\ /disable() calls. The purpose
of these function is to keep the rest of power wells enabled until the end
of display HW readout (which will acquire the power references reflecting
the current HW state).

.. _`intel_power_domains_disable`:

intel_power_domains_disable
===========================

.. c:function:: void intel_power_domains_disable(struct drm_i915_private *dev_priv)

    disable toggling of display power wells

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_power_domains_disable.description`:

Description
-----------

Disable the ondemand enabling/disabling of the display power wells. See
\ :c:func:`intel_power_domains_enable`\  for which power wells this call controls.

.. _`intel_power_domains_suspend`:

intel_power_domains_suspend
===========================

.. c:function:: void intel_power_domains_suspend(struct drm_i915_private *dev_priv, enum i915_drm_suspend_mode suspend_mode)

    suspend power domain state

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param suspend_mode:
        specifies the target suspend state (idle, mem, hibernation)
    :type suspend_mode: enum i915_drm_suspend_mode

.. _`intel_power_domains_suspend.description`:

Description
-----------

This function prepares the hardware power domain state before entering
system suspend.

It must be called with power domains already disabled (after a call to
\ :c:func:`intel_power_domains_disable`\ ) and paired with \ :c:func:`intel_power_domains_resume`\ .

.. _`intel_power_domains_resume`:

intel_power_domains_resume
==========================

.. c:function:: void intel_power_domains_resume(struct drm_i915_private *dev_priv)

    resume power domain state

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_power_domains_resume.description`:

Description
-----------

This function resume the hardware power domain state during system resume.

It will return with power domain support disabled (to be enabled later by
\ :c:func:`intel_power_domains_enable`\ ) and must be paired with
\ :c:func:`intel_power_domains_suspend`\ .

.. _`intel_power_domains_verify_state`:

intel_power_domains_verify_state
================================

.. c:function:: void intel_power_domains_verify_state(struct drm_i915_private *dev_priv)

    verify the HW/SW state for all power wells

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_power_domains_verify_state.description`:

Description
-----------

Verify if the reference count of each power well matches its HW enabled
state and the total refcount of the domains it belongs to. This must be
called after modeset HW state sanitization, which is responsible for
acquiring reference counts for any power wells in use and disabling the
ones left on by BIOS but not required by any active output.

.. _`intel_runtime_pm_get`:

intel_runtime_pm_get
====================

.. c:function:: void intel_runtime_pm_get(struct drm_i915_private *dev_priv)

    grab a runtime pm reference

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_runtime_pm_get.description`:

Description
-----------

This function grabs a device-level runtime pm reference (mostly used for GEM
code to ensure the GTT or GT is on) and ensures that it is powered up.

Any runtime pm reference obtained by this function must have a symmetric
call to \ :c:func:`intel_runtime_pm_put`\  to release the reference again.

.. _`intel_runtime_pm_get_if_in_use`:

intel_runtime_pm_get_if_in_use
==============================

.. c:function:: bool intel_runtime_pm_get_if_in_use(struct drm_i915_private *dev_priv)

    grab a runtime pm reference if device in use

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_runtime_pm_get_if_in_use.description`:

Description
-----------

This function grabs a device-level runtime pm reference if the device is
already in use and ensures that it is powered up. It is illegal to try
and access the HW should \ :c:func:`intel_runtime_pm_get_if_in_use`\  report failure.

Any runtime pm reference obtained by this function must have a symmetric
call to \ :c:func:`intel_runtime_pm_put`\  to release the reference again.

.. _`intel_runtime_pm_get_if_in_use.return`:

Return
------

True if the wakeref was acquired, or False otherwise.

.. _`intel_runtime_pm_get_noresume`:

intel_runtime_pm_get_noresume
=============================

.. c:function:: void intel_runtime_pm_get_noresume(struct drm_i915_private *dev_priv)

    grab a runtime pm reference

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_runtime_pm_get_noresume.description`:

Description
-----------

This function grabs a device-level runtime pm reference (mostly used for GEM
code to ensure the GTT or GT is on).

It will _not_ power up the device but instead only check that it's powered
on.  Therefore it is only valid to call this functions from contexts where
the device is known to be powered up and where trying to power it up would
result in hilarity and deadlocks. That pretty much means only the system
suspend/resume code where this is used to grab runtime pm references for
delayed setup down in work items.

Any runtime pm reference obtained by this function must have a symmetric
call to \ :c:func:`intel_runtime_pm_put`\  to release the reference again.

.. _`intel_runtime_pm_put`:

intel_runtime_pm_put
====================

.. c:function:: void intel_runtime_pm_put(struct drm_i915_private *dev_priv)

    release a runtime pm reference

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_runtime_pm_put.description`:

Description
-----------

This function drops the device-level runtime pm reference obtained by
\ :c:func:`intel_runtime_pm_get`\  and might power down the corresponding
hardware block right away if this is the last reference.

.. _`intel_runtime_pm_enable`:

intel_runtime_pm_enable
=======================

.. c:function:: void intel_runtime_pm_enable(struct drm_i915_private *dev_priv)

    enable runtime pm

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_runtime_pm_enable.description`:

Description
-----------

This function enables runtime pm at the end of the driver load sequence.

Note that this function does currently not enable runtime pm for the
subordinate display power domains. That is done by
\ :c:func:`intel_power_domains_enable`\ .

.. This file was automatic generated / don't edit.

