.. -*- coding: utf-8; mode: rst -*-

==========
dce_v8_0.c
==========


.. _`dce_v8_0_vblank_wait`:

dce_v8_0_vblank_wait
====================

.. c:function:: void dce_v8_0_vblank_wait (struct amdgpu_device *adev, int crtc)

    vblank wait asic callback.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param int crtc:
        crtc to wait for vblank on



.. _`dce_v8_0_vblank_wait.description`:

Description
-----------

Wait for vblank on the requested crtc (evergreen+).



.. _`dce_v8_0_page_flip`:

dce_v8_0_page_flip
==================

.. c:function:: void dce_v8_0_page_flip (struct amdgpu_device *adev, int crtc_id, u64 crtc_base)

    pageflip callback.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param int crtc_id:
        crtc to cleanup pageflip on

    :param u64 crtc_base:
        new address of the crtc (GPU MC address)



.. _`dce_v8_0_page_flip.description`:

Description
-----------

Triggers the actual pageflip by updating the primary
surface base address.



.. _`dce_v8_0_hpd_sense`:

dce_v8_0_hpd_sense
==================

.. c:function:: bool dce_v8_0_hpd_sense (struct amdgpu_device *adev, enum amdgpu_hpd_id hpd)

    hpd sense callback.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param enum amdgpu_hpd_id hpd:
        hpd (hotplug detect) pin



.. _`dce_v8_0_hpd_sense.description`:

Description
-----------

Checks if a digital monitor is connected (evergreen+).
Returns true if connected, false if not connected.



.. _`dce_v8_0_hpd_set_polarity`:

dce_v8_0_hpd_set_polarity
=========================

.. c:function:: void dce_v8_0_hpd_set_polarity (struct amdgpu_device *adev, enum amdgpu_hpd_id hpd)

    hpd set polarity callback.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param enum amdgpu_hpd_id hpd:
        hpd (hotplug detect) pin



.. _`dce_v8_0_hpd_set_polarity.description`:

Description
-----------

Set the polarity of the hpd pin (evergreen+).



.. _`dce_v8_0_hpd_init`:

dce_v8_0_hpd_init
=================

.. c:function:: void dce_v8_0_hpd_init (struct amdgpu_device *adev)

    hpd setup callback.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer



.. _`dce_v8_0_hpd_init.description`:

Description
-----------

Setup the hpd pins used by the card (evergreen+).
Enable the pin, set the polarity, and enable the hpd interrupts.



.. _`dce_v8_0_hpd_fini`:

dce_v8_0_hpd_fini
=================

.. c:function:: void dce_v8_0_hpd_fini (struct amdgpu_device *adev)

    hpd tear down callback.

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer



.. _`dce_v8_0_hpd_fini.description`:

Description
-----------

Tear down the hpd pins used by the card (evergreen+).
Disable the hpd interrupts.



.. _`dce_v8_0_line_buffer_adjust`:

dce_v8_0_line_buffer_adjust
===========================

.. c:function:: u32 dce_v8_0_line_buffer_adjust (struct amdgpu_device *adev, struct amdgpu_crtc *amdgpu_crtc, struct drm_display_mode *mode)

    Set up the line buffer

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_crtc \*amdgpu_crtc:
        the selected display controller

    :param struct drm_display_mode \*mode:
        the current display mode on the selected display
        controller



.. _`dce_v8_0_line_buffer_adjust.description`:

Description
-----------

Setup up the line buffer allocation for
the selected display controller (CIK).
Returns the line buffer size in pixels.



.. _`cik_get_number_of_dram_channels`:

cik_get_number_of_dram_channels
===============================

.. c:function:: u32 cik_get_number_of_dram_channels (struct amdgpu_device *adev)

    get the number of dram channels

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer



.. _`cik_get_number_of_dram_channels.description`:

Description
-----------

Look up the number of video ram channels (CIK).
Used for display watermark bandwidth calculations
Returns the number of dram channels



.. _`dce_v8_0_dram_bandwidth`:

dce_v8_0_dram_bandwidth
=======================

.. c:function:: u32 dce_v8_0_dram_bandwidth (struct dce8_wm_params *wm)

    get the dram bandwidth

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce_v8_0_dram_bandwidth.description`:

Description
-----------

Calculate the raw dram bandwidth (CIK).
Used for display watermark bandwidth calculations
Returns the dram bandwidth in MBytes/s



.. _`dce_v8_0_dram_bandwidth_for_display`:

dce_v8_0_dram_bandwidth_for_display
===================================

.. c:function:: u32 dce_v8_0_dram_bandwidth_for_display (struct dce8_wm_params *wm)

    get the dram bandwidth for display

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce_v8_0_dram_bandwidth_for_display.description`:

Description
-----------

Calculate the dram bandwidth used for display (CIK).
Used for display watermark bandwidth calculations
Returns the dram bandwidth for display in MBytes/s



.. _`dce_v8_0_data_return_bandwidth`:

dce_v8_0_data_return_bandwidth
==============================

.. c:function:: u32 dce_v8_0_data_return_bandwidth (struct dce8_wm_params *wm)

    get the data return bandwidth

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce_v8_0_data_return_bandwidth.description`:

Description
-----------

Calculate the data return bandwidth used for display (CIK).
Used for display watermark bandwidth calculations
Returns the data return bandwidth in MBytes/s



.. _`dce_v8_0_dmif_request_bandwidth`:

dce_v8_0_dmif_request_bandwidth
===============================

.. c:function:: u32 dce_v8_0_dmif_request_bandwidth (struct dce8_wm_params *wm)

    get the dmif bandwidth

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce_v8_0_dmif_request_bandwidth.description`:

Description
-----------

Calculate the dmif bandwidth used for display (CIK).
Used for display watermark bandwidth calculations
Returns the dmif bandwidth in MBytes/s



.. _`dce_v8_0_available_bandwidth`:

dce_v8_0_available_bandwidth
============================

.. c:function:: u32 dce_v8_0_available_bandwidth (struct dce8_wm_params *wm)

    get the min available bandwidth

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce_v8_0_available_bandwidth.description`:

Description
-----------

Calculate the min available bandwidth used for display (CIK).
Used for display watermark bandwidth calculations
Returns the min available bandwidth in MBytes/s



.. _`dce_v8_0_average_bandwidth`:

dce_v8_0_average_bandwidth
==========================

.. c:function:: u32 dce_v8_0_average_bandwidth (struct dce8_wm_params *wm)

    get the average available bandwidth

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce_v8_0_average_bandwidth.description`:

Description
-----------

Calculate the average available bandwidth used for display (CIK).
Used for display watermark bandwidth calculations
Returns the average available bandwidth in MBytes/s



.. _`dce_v8_0_latency_watermark`:

dce_v8_0_latency_watermark
==========================

.. c:function:: u32 dce_v8_0_latency_watermark (struct dce8_wm_params *wm)

    get the latency watermark

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce_v8_0_latency_watermark.description`:

Description
-----------

Calculate the latency watermark (CIK).
Used for display watermark bandwidth calculations
Returns the latency watermark in ns



.. _`dce_v8_0_average_bandwidth_vs_dram_bandwidth_for_display`:

dce_v8_0_average_bandwidth_vs_dram_bandwidth_for_display
========================================================

.. c:function:: bool dce_v8_0_average_bandwidth_vs_dram_bandwidth_for_display (struct dce8_wm_params *wm)

    check average and available dram bandwidth

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce_v8_0_average_bandwidth_vs_dram_bandwidth_for_display.description`:

Description
-----------

Check if the display average bandwidth fits in the display
dram bandwidth (CIK).
Used for display watermark bandwidth calculations
Returns true if the display fits, false if not.



.. _`dce_v8_0_average_bandwidth_vs_available_bandwidth`:

dce_v8_0_average_bandwidth_vs_available_bandwidth
=================================================

.. c:function:: bool dce_v8_0_average_bandwidth_vs_available_bandwidth (struct dce8_wm_params *wm)

    check average and available bandwidth

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce_v8_0_average_bandwidth_vs_available_bandwidth.description`:

Description
-----------

Check if the display average bandwidth fits in the display
available bandwidth (CIK).
Used for display watermark bandwidth calculations
Returns true if the display fits, false if not.



.. _`dce_v8_0_check_latency_hiding`:

dce_v8_0_check_latency_hiding
=============================

.. c:function:: bool dce_v8_0_check_latency_hiding (struct dce8_wm_params *wm)

    check latency hiding

    :param struct dce8_wm_params \*wm:
        watermark calculation data



.. _`dce_v8_0_check_latency_hiding.description`:

Description
-----------

Check latency hiding (CIK).
Used for display watermark bandwidth calculations
Returns true if the display fits, false if not.



.. _`dce_v8_0_program_watermarks`:

dce_v8_0_program_watermarks
===========================

.. c:function:: void dce_v8_0_program_watermarks (struct amdgpu_device *adev, struct amdgpu_crtc *amdgpu_crtc, u32 lb_size, u32 num_heads)

    program display watermarks

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer

    :param struct amdgpu_crtc \*amdgpu_crtc:
        the selected display controller

    :param u32 lb_size:
        line buffer size

    :param u32 num_heads:
        number of display controllers in use



.. _`dce_v8_0_program_watermarks.description`:

Description
-----------

Calculate and program the display watermarks for the
selected display controller (CIK).



.. _`dce_v8_0_bandwidth_update`:

dce_v8_0_bandwidth_update
=========================

.. c:function:: void dce_v8_0_bandwidth_update (struct amdgpu_device *adev)

    program display watermarks

    :param struct amdgpu_device \*adev:
        amdgpu_device pointer



.. _`dce_v8_0_bandwidth_update.description`:

Description
-----------

Calculate and program the display watermarks and line
buffer allocation (CIK).



.. _`dce_v8_0_pick_pll`:

dce_v8_0_pick_pll
=================

.. c:function:: u32 dce_v8_0_pick_pll (struct drm_crtc *crtc)

    Allocate a PPLL for use by the crtc.

    :param struct drm_crtc \*crtc:
        drm crtc



.. _`dce_v8_0_pick_pll.description`:

Description
-----------

Returns the PPLL (Pixel PLL) to be used by the crtc.  For DP monitors
a single PPLL can be used for all DP crtcs/encoders.  For non-DP
monitors a dedicated PPLL must be used.  If a particular board has
an external DP PLL, return ATOM_PPLL_INVALID to skip PLL programming
as there is no need to program the PLL itself.  If we are not able to
allocate a PLL, return ATOM_PPLL_INVALID to skip PLL programming to
avoid messing up an existing monitor.

Asic specific PLL information

DCE 8.x
KB/KV
- PPLL1, PPLL2 are available for all UNIPHY (both DP and non-DP)
CI
- PPLL0, PPLL1, PPLL2 are available for all UNIPHY (both DP and non-DP) and DAC

