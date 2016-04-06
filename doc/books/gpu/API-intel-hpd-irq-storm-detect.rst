
.. _API-intel-hpd-irq-storm-detect:

==========================
intel_hpd_irq_storm_detect
==========================

*man intel_hpd_irq_storm_detect(9)*

*4.6.0-rc1*

gather stats and detect HPD irq storm on a pin


Synopsis
========

.. c:function:: bool intel_hpd_irq_storm_detect( struct drm_i915_private * dev_priv, enum hpd_pin pin )

Arguments
=========

``dev_priv``
    private driver data pointer

``pin``
    the pin to gather stats on


Description
===========

Gather stats about HPD irqs from the specified ``pin``, and detect irq storms. Only the pin specific stats and state are changed, the caller is responsible for further action.

``HPD_STORM_THRESHOLD`` irqs are allowed within ``HPD_STORM_DETECT_PERIOD`` ms, otherwise it's considered an irq storm, and the irq state is set to ``HPD_MARK_DISABLED``.

Return true if an irq storm was detected on ``pin``.
