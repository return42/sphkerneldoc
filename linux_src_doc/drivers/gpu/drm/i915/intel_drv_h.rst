.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_drv.h

.. _`__wait_for`:

\__wait_for
===========

.. c:function::  __wait_for( OP,  COND,  US,  Wmin,  Wmax)

    magic wait macro

    :param OP:
        *undescribed*
    :type OP: 

    :param COND:
        *undescribed*
    :type COND: 

    :param US:
        *undescribed*
    :type US: 

    :param Wmin:
        *undescribed*
    :type Wmin: 

    :param Wmax:
        *undescribed*
    :type Wmax: 

.. _`__wait_for.description`:

Description
-----------

Macro to help avoid open coding check/wait/timeout patterns. Note that it's
important that we check the condition again after having timed out, since the
timeout could be due to preemption or similar and we've never had a chance to
check the condition before the timeout.

.. _`disable_rpm_wakeref_asserts`:

disable_rpm_wakeref_asserts
===========================

.. c:function:: void disable_rpm_wakeref_asserts(struct drm_i915_private *dev_priv)

    disable the RPM assert checks

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`disable_rpm_wakeref_asserts.description`:

Description
-----------

This function disable asserts that check if we hold an RPM wakelock
reference, while keeping the device-not-suspended checks still enabled.
It's meant to be used only in special circumstances where our rule about
the wakelock refcount wrt. the device power state doesn't hold. According
to this rule at any point where we access the HW or want to keep the HW in
an active state we must hold an RPM wakelock reference acquired via one of
the \ :c:func:`intel_runtime_pm_get`\  helpers. Currently there are a few special spots
where this rule doesn't hold: the IRQ and suspend/resume handlers, the
forcewake release timer, and the GPU RPS and hangcheck works. All other
users should avoid using this function.

Any calls to this function must have a symmetric call to
\ :c:func:`enable_rpm_wakeref_asserts`\ .

.. _`enable_rpm_wakeref_asserts`:

enable_rpm_wakeref_asserts
==========================

.. c:function:: void enable_rpm_wakeref_asserts(struct drm_i915_private *dev_priv)

    re-enable the RPM assert checks

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`enable_rpm_wakeref_asserts.description`:

Description
-----------

This function re-enables the RPM assert checks after disabling them with
disable_rpm_wakeref_asserts. It's meant to be used only in special
circumstances otherwise its use should be avoided.

Any calls to this function must have a symmetric call to
\ :c:func:`disable_rpm_wakeref_asserts`\ .

.. This file was automatic generated / don't edit.

