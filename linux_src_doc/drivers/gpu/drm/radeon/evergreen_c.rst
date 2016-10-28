.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/evergreen.c

.. _`evergreen_get_allowed_info_register`:

evergreen_get_allowed_info_register
===================================

.. c:function:: int evergreen_get_allowed_info_register(struct radeon_device *rdev, u32 reg, u32 *val)

    fetch the register for the info ioctl

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param u32 reg:
        register offset in bytes

    :param u32 \*val:
        register value

.. _`evergreen_get_allowed_info_register.description`:

Description
-----------

Returns 0 for success or -EINVAL for an invalid register

.. _`dce4_wait_for_vblank`:

dce4_wait_for_vblank
====================

.. c:function:: void dce4_wait_for_vblank(struct radeon_device *rdev, int crtc)

    vblank wait asic callback.

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param int crtc:
        crtc to wait for vblank on

.. _`dce4_wait_for_vblank.description`:

Description
-----------

Wait for vblank on the requested crtc (evergreen+).

.. _`evergreen_page_flip`:

evergreen_page_flip
===================

.. c:function:: void evergreen_page_flip(struct radeon_device *rdev, int crtc_id, u64 crtc_base, bool async)

    pageflip callback.

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param int crtc_id:
        crtc to cleanup pageflip on

    :param u64 crtc_base:
        new address of the crtc (GPU MC address)

    :param bool async:
        *undescribed*

.. _`evergreen_page_flip.description`:

Description
-----------

Triggers the actual pageflip by updating the primary
surface base address (evergreen+).

.. _`evergreen_page_flip_pending`:

evergreen_page_flip_pending
===========================

.. c:function:: bool evergreen_page_flip_pending(struct radeon_device *rdev, int crtc_id)

    check if page flip is still pending

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param int crtc_id:
        crtc to check

.. _`evergreen_page_flip_pending.description`:

Description
-----------

Returns the current update pending status.

.. _`sumo_pm_init_profile`:

sumo_pm_init_profile
====================

.. c:function:: void sumo_pm_init_profile(struct radeon_device *rdev)

    Initialize power profiles callback.

    :param struct radeon_device \*rdev:
        radeon_device pointer

.. _`sumo_pm_init_profile.description`:

Description
-----------

Initialize the power states used in profile mode
(sumo, trinity, SI).
Used for profile mode only.

.. _`btc_pm_init_profile`:

btc_pm_init_profile
===================

.. c:function:: void btc_pm_init_profile(struct radeon_device *rdev)

    Initialize power profiles callback.

    :param struct radeon_device \*rdev:
        radeon_device pointer

.. _`btc_pm_init_profile.description`:

Description
-----------

Initialize the power states used in profile mode
(BTC, cayman).
Used for profile mode only.

.. _`evergreen_pm_misc`:

evergreen_pm_misc
=================

.. c:function:: void evergreen_pm_misc(struct radeon_device *rdev)

    set additional pm hw parameters callback.

    :param struct radeon_device \*rdev:
        radeon_device pointer

.. _`evergreen_pm_misc.description`:

Description
-----------

Set non-clock parameters associated with a power state
(voltage, etc.) (evergreen+).

.. _`evergreen_pm_prepare`:

evergreen_pm_prepare
====================

.. c:function:: void evergreen_pm_prepare(struct radeon_device *rdev)

    pre-power state change callback.

    :param struct radeon_device \*rdev:
        radeon_device pointer

.. _`evergreen_pm_prepare.description`:

Description
-----------

Prepare for a power state change (evergreen+).

.. _`evergreen_pm_finish`:

evergreen_pm_finish
===================

.. c:function:: void evergreen_pm_finish(struct radeon_device *rdev)

    post-power state change callback.

    :param struct radeon_device \*rdev:
        radeon_device pointer

.. _`evergreen_pm_finish.description`:

Description
-----------

Clean up after a power state change (evergreen+).

.. _`evergreen_hpd_sense`:

evergreen_hpd_sense
===================

.. c:function:: bool evergreen_hpd_sense(struct radeon_device *rdev, enum radeon_hpd_id hpd)

    hpd sense callback.

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param enum radeon_hpd_id hpd:
        hpd (hotplug detect) pin

.. _`evergreen_hpd_sense.description`:

Description
-----------

Checks if a digital monitor is connected (evergreen+).
Returns true if connected, false if not connected.

.. _`evergreen_hpd_set_polarity`:

evergreen_hpd_set_polarity
==========================

.. c:function:: void evergreen_hpd_set_polarity(struct radeon_device *rdev, enum radeon_hpd_id hpd)

    hpd set polarity callback.

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param enum radeon_hpd_id hpd:
        hpd (hotplug detect) pin

.. _`evergreen_hpd_set_polarity.description`:

Description
-----------

Set the polarity of the hpd pin (evergreen+).

.. _`evergreen_hpd_init`:

evergreen_hpd_init
==================

.. c:function:: void evergreen_hpd_init(struct radeon_device *rdev)

    hpd setup callback.

    :param struct radeon_device \*rdev:
        radeon_device pointer

.. _`evergreen_hpd_init.description`:

Description
-----------

Setup the hpd pins used by the card (evergreen+).
Enable the pin, set the polarity, and enable the hpd interrupts.

.. _`evergreen_hpd_fini`:

evergreen_hpd_fini
==================

.. c:function:: void evergreen_hpd_fini(struct radeon_device *rdev)

    hpd tear down callback.

    :param struct radeon_device \*rdev:
        radeon_device pointer

.. _`evergreen_hpd_fini.description`:

Description
-----------

Tear down the hpd pins used by the card (evergreen+).
Disable the hpd interrupts.

.. _`evergreen_bandwidth_update`:

evergreen_bandwidth_update
==========================

.. c:function:: void evergreen_bandwidth_update(struct radeon_device *rdev)

    update display watermarks callback.

    :param struct radeon_device \*rdev:
        radeon_device pointer

.. _`evergreen_bandwidth_update.description`:

Description
-----------

Update the display watermarks based on the requested mode(s)
(evergreen+).

.. _`evergreen_mc_wait_for_idle`:

evergreen_mc_wait_for_idle
==========================

.. c:function:: int evergreen_mc_wait_for_idle(struct radeon_device *rdev)

    wait for MC idle callback.

    :param struct radeon_device \*rdev:
        radeon_device pointer

.. _`evergreen_mc_wait_for_idle.description`:

Description
-----------

Wait for the MC (memory controller) to be idle.
(evergreen+).
Returns 0 if the MC is idle, -1 if not.

.. _`evergreen_gfx_is_lockup`:

evergreen_gfx_is_lockup
=======================

.. c:function:: bool evergreen_gfx_is_lockup(struct radeon_device *rdev, struct radeon_ring *ring)

    Check if the GFX engine is locked up

    :param struct radeon_device \*rdev:
        radeon_device pointer

    :param struct radeon_ring \*ring:
        radeon_ring structure holding ring information

.. _`evergreen_gfx_is_lockup.description`:

Description
-----------

Check if the GFX engine is locked up.
Returns true if the engine appears to be locked up, false if not.

.. This file was automatic generated / don't edit.

