.. -*- coding: utf-8; mode: rst -*-

===============
atombios_crtc.c
===============


.. _`radeon_get_pll_use_mask`:

radeon_get_pll_use_mask
=======================

.. c:function:: u32 radeon_get_pll_use_mask (struct drm_crtc *crtc)

    look up a mask of which pplls are in use

    :param struct drm_crtc \*crtc:
        drm crtc



.. _`radeon_get_pll_use_mask.description`:

Description
-----------

Returns the mask of which PPLLs (Pixel PLLs) are in use.



.. _`radeon_get_shared_dp_ppll`:

radeon_get_shared_dp_ppll
=========================

.. c:function:: int radeon_get_shared_dp_ppll (struct drm_crtc *crtc)

    return the PPLL used by another crtc for DP

    :param struct drm_crtc \*crtc:
        drm crtc



.. _`radeon_get_shared_dp_ppll.description`:

Description
-----------

Returns the PPLL (Pixel PLL) used by another crtc/encoder which is
also in DP mode.  For DP, a single PPLL can be used for all DP
crtcs/encoders.



.. _`radeon_get_shared_nondp_ppll`:

radeon_get_shared_nondp_ppll
============================

.. c:function:: int radeon_get_shared_nondp_ppll (struct drm_crtc *crtc)

    return the PPLL used by another non-DP crtc

    :param struct drm_crtc \*crtc:
        drm crtc



.. _`radeon_get_shared_nondp_ppll.description`:

Description
-----------

Returns the PPLL (Pixel PLL) used by another non-DP crtc/encoder which can
be shared (i.e., same clock).



.. _`radeon_atom_pick_pll`:

radeon_atom_pick_pll
====================

.. c:function:: int radeon_atom_pick_pll (struct drm_crtc *crtc)

    Allocate a PPLL for use by the crtc.

    :param struct drm_crtc \*crtc:
        drm crtc



.. _`radeon_atom_pick_pll.description`:

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

DCE 6.1
- PPLL2 is only available to UNIPHYA (both DP and non-DP)
- PPLL0, PPLL1 are available for UNIPHYB/C/D/E/F (both DP and non-DP)

DCE 6.0
- PPLL0 is available to all UNIPHY (DP only)
- PPLL1, PPLL2 are available for all UNIPHY (both DP and non-DP) and DAC

DCE 5.0
- DCPLL is available to all UNIPHY (DP only)
- PPLL1, PPLL2 are available for all UNIPHY (both DP and non-DP) and DAC

DCE 3.0/4.0/4.1
- PPLL1, PPLL2 are available for all UNIPHY (both DP and non-DP) and DAC

