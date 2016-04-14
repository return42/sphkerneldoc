.. -*- coding: utf-8; mode: rst -*-

==================
intel_runtime_pm.c
==================

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

.. c:function:: bool __intel_display_power_is_enabled (struct drm_i915_private *dev_priv, enum intel_display_power_domain domain)

    unlocked check for a power domain

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum intel_display_power_domain domain:
        power domain to check


.. _`__intel_display_power_is_enabled.description`:

Description
-----------

This is the unlocked version of :c:func:`intel_display_power_is_enabled` and should
only be used from error capture and recovery code where deadlocks are
possible.

Returns:
True when the power domain is enabled, false otherwise.


.. _`intel_display_power_is_enabled`:

intel_display_power_is_enabled
==============================

.. c:function:: bool intel_display_power_is_enabled (struct drm_i915_private *dev_priv, enum intel_display_power_domain domain)

    check for a power domain

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum intel_display_power_domain domain:
        power domain to check


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

Returns:
True when the power domain is enabled, false otherwise.


.. _`intel_display_set_init_power`:

intel_display_set_init_power
============================

.. c:function:: void intel_display_set_init_power (struct drm_i915_private *dev_priv, bool enable)

    set the initial power domain state

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param bool enable:
        whether to enable or disable the initial power domain state


.. _`intel_display_set_init_power.description`:

Description
-----------

For simplicity our driver load/unload and system suspend/resume code assumes
that all power domains are always enabled. This functions controls the state
of this little hack. While the initial power domain state is enabled runtime
pm is effectively disabled.


.. _`intel_display_power_get`:

intel_display_power_get
=======================

.. c:function:: void intel_display_power_get (struct drm_i915_private *dev_priv, enum intel_display_power_domain domain)

    grab a power domain reference

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum intel_display_power_domain domain:
        power domain to reference


.. _`intel_display_power_get.description`:

Description
-----------

This function grabs a power domain reference for ``domain`` and ensures that the
power domain and all its parents are powered up. Therefore users should only
grab a reference to the innermost power domain they need.

Any power domain reference obtained by this function must have a symmetric
call to :c:func:`intel_display_power_put` to release the reference again.


.. _`intel_display_power_get_if_enabled`:

intel_display_power_get_if_enabled
==================================

.. c:function:: bool intel_display_power_get_if_enabled (struct drm_i915_private *dev_priv, enum intel_display_power_domain domain)

    grab a reference for an enabled display power domain

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum intel_display_power_domain domain:
        power domain to reference


.. _`intel_display_power_get_if_enabled.description`:

Description
-----------

This function grabs a power domain reference for ``domain`` and ensures that the
power domain and all its parents are powered up. Therefore users should only
grab a reference to the innermost power domain they need.

Any power domain reference obtained by this function must have a symmetric
call to :c:func:`intel_display_power_put` to release the reference again.


.. _`intel_display_power_put`:

intel_display_power_put
=======================

.. c:function:: void intel_display_power_put (struct drm_i915_private *dev_priv, enum intel_display_power_domain domain)

    release a power domain reference

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum intel_display_power_domain domain:
        power domain to reference


.. _`intel_display_power_put.description`:

Description
-----------

This function drops the power domain reference obtained by
:c:func:`intel_display_power_get` and might power down the corresponding hardware
block right away if this is the last reference.


.. _`intel_power_domains_init`:

intel_power_domains_init
========================

.. c:function:: int intel_power_domains_init (struct drm_i915_private *dev_priv)

    initializes the power domain structures

    :param struct drm_i915_private \*dev_priv:
        i915 device instance


.. _`intel_power_domains_init.description`:

Description
-----------

Initializes the power domain structures for ``dev_priv`` depending upon the
supported platform.


.. _`intel_power_domains_fini`:

intel_power_domains_fini
========================

.. c:function:: void intel_power_domains_fini (struct drm_i915_private *dev_priv)

    finalizes the power domain structures

    :param struct drm_i915_private \*dev_priv:
        i915 device instance


.. _`intel_power_domains_fini.description`:

Description
-----------

Finalizes the power domain structures for ``dev_priv`` depending upon the
supported platform. This function also disables runtime pm and ensures that
the device stays powered up so that the driver can be reloaded.


.. _`intel_power_domains_init_hw`:

intel_power_domains_init_hw
===========================

.. c:function:: void intel_power_domains_init_hw (struct drm_i915_private *dev_priv, bool resume)

    initialize hardware power domain state

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param bool resume:

        *undescribed*


.. _`intel_power_domains_init_hw.description`:

Description
-----------

This function initializes the hardware power domain state and enables all
power domains using :c:func:`intel_display_set_init_power`.


.. _`intel_power_domains_suspend`:

intel_power_domains_suspend
===========================

.. c:function:: void intel_power_domains_suspend (struct drm_i915_private *dev_priv)

    suspend power domain state

    :param struct drm_i915_private \*dev_priv:
        i915 device instance


.. _`intel_power_domains_suspend.description`:

Description
-----------

This function prepares the hardware power domain state before entering
system suspend. It must be paired with :c:func:`intel_power_domains_init_hw`.


.. _`intel_runtime_pm_get`:

intel_runtime_pm_get
====================

.. c:function:: void intel_runtime_pm_get (struct drm_i915_private *dev_priv)

    grab a runtime pm reference

    :param struct drm_i915_private \*dev_priv:
        i915 device instance


.. _`intel_runtime_pm_get.description`:

Description
-----------

This function grabs a device-level runtime pm reference (mostly used for GEM
code to ensure the GTT or GT is on) and ensures that it is powered up.

Any runtime pm reference obtained by this function must have a symmetric
call to :c:func:`intel_runtime_pm_put` to release the reference again.


.. _`intel_runtime_pm_get_if_in_use`:

intel_runtime_pm_get_if_in_use
==============================

.. c:function:: bool intel_runtime_pm_get_if_in_use (struct drm_i915_private *dev_priv)

    grab a runtime pm reference if device in use

    :param struct drm_i915_private \*dev_priv:
        i915 device instance


.. _`intel_runtime_pm_get_if_in_use.description`:

Description
-----------

This function grabs a device-level runtime pm reference if the device is
already in use and ensures that it is powered up.

Any runtime pm reference obtained by this function must have a symmetric
call to :c:func:`intel_runtime_pm_put` to release the reference again.


.. _`intel_runtime_pm_get_noresume`:

intel_runtime_pm_get_noresume
=============================

.. c:function:: void intel_runtime_pm_get_noresume (struct drm_i915_private *dev_priv)

    grab a runtime pm reference

    :param struct drm_i915_private \*dev_priv:
        i915 device instance


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
call to :c:func:`intel_runtime_pm_put` to release the reference again.


.. _`intel_runtime_pm_put`:

intel_runtime_pm_put
====================

.. c:function:: void intel_runtime_pm_put (struct drm_i915_private *dev_priv)

    release a runtime pm reference

    :param struct drm_i915_private \*dev_priv:
        i915 device instance


.. _`intel_runtime_pm_put.description`:

Description
-----------

This function drops the device-level runtime pm reference obtained by
:c:func:`intel_runtime_pm_get` and might power down the corresponding
hardware block right away if this is the last reference.


.. _`intel_runtime_pm_enable`:

intel_runtime_pm_enable
=======================

.. c:function:: void intel_runtime_pm_enable (struct drm_i915_private *dev_priv)

    enable runtime pm

    :param struct drm_i915_private \*dev_priv:
        i915 device instance


.. _`intel_runtime_pm_enable.description`:

Description
-----------

This function enables runtime pm at the end of the driver load sequence.

Note that this function does currently not enable runtime pm for the
subordinate display power domains. That is only done on the first modeset
using :c:func:`intel_display_set_init_power`.

