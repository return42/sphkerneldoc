.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_dpio_phy.c

.. _`dpio`:

DPIO
====

VLV, CHV and BXT have slightly peculiar display PHYs for driving DP/HDMI
ports. DPIO is the name given to such a display PHY. These PHYs
don't follow the standard programming model using direct MMIO
registers, and instead their registers must be accessed trough IOSF
sideband. VLV has one such PHY for driving ports B and C, and CHV
adds another PHY for driving port D. Each PHY responds to specific
IOSF-SB port.

Each display PHY is made up of one or two channels. Each channel
houses a common lane part which contains the PLL and other common
logic. CH0 common lane also contains the IOSF-SB logic for the
Common Register Interface (CRI) ie. the DPIO registers. CRI clock
must be running when any DPIO registers are accessed.

In addition to having their own registers, the PHYs are also
controlled through some dedicated signals from the display
controller. These include PLL reference clock enable, PLL enable,
and CRI clock selection, for example.

Eeach channel also has two splines (also called data lanes), and
each spline is made up of one Physical Access Coding Sub-Layer
(PCS) block and two TX lanes. So each channel has two PCS blocks
and four TX lanes. The TX lanes are used as DP lanes or TMDS
data/clock pairs depending on the output type.

Additionally the PHY also contains an AUX lane with AUX blocks
for each channel. This is used for DP AUX communication, but
this fact isn't really relevant for the driver since AUX is
controlled from the display controller side. No DPIO registers
need to be accessed during AUX communication,

Generally on VLV/CHV the common lane corresponds to the pipe and
the spline (PCS/TX) corresponds to the port.

For dual channel PHY (VLV/CHV):

 pipe A == CMN/PLL/REF CH0

 pipe B == CMN/PLL/REF CH1

 port B == PCS/TX CH0

 port C == PCS/TX CH1

This is especially important when we cross the streams
ie. drive port B with pipe B, or port C with pipe A.

For single channel PHY (CHV):

 pipe C == CMN/PLL/REF CH0

 port D == PCS/TX CH0

On BXT the entire PHY channel corresponds to the port. That means
the PLL is also now associated with the port rather than the pipe,
and so the clock needs to be routed to the appropriate transcoder.
Port A PLL is directly connected to transcoder EDP and port B/C
PLLs can be routed to any transcoder A/B/C.

Note: DDI0 is digital port B, DD1 is digital port C, and DDI2 is
digital port D (CHV) or port A (BXT). ::


    Dual channel PHY (VLV/CHV/BXT)
    ---------------------------------
    |      CH0      |      CH1      |
    |  CMN/PLL/REF  |  CMN/PLL/REF  |
    |---------------|---------------| Display PHY
    | PCS01 | PCS23 | PCS01 | PCS23 |
    |-------|-------|-------|-------|
    |TX0|TX1|TX2|TX3|TX0|TX1|TX2|TX3|
    ---------------------------------
    |     DDI0      |     DDI1      | DP/HDMI ports
    ---------------------------------

    Single channel PHY (CHV/BXT)
    -----------------
    |      CH0      |
    |  CMN/PLL/REF  |
    |---------------| Display PHY
    | PCS01 | PCS23 |
    |-------|-------|
    |TX0|TX1|TX2|TX3|
    -----------------
    |     DDI2      | DP/HDMI port
    -----------------

.. _`bxt_ddi_phy_info`:

struct bxt_ddi_phy_info
=======================

.. c:type:: struct bxt_ddi_phy_info

    Hold info for a broxton DDI phy

.. _`bxt_ddi_phy_info.definition`:

Definition
----------

.. code-block:: c

    struct bxt_ddi_phy_info {
        bool dual_channel;
        enum dpio_phy rcomp_phy;
        int reset_delay;
        u32 pwron_mask;
        struct {
            enum port port;
        } channel[2];
    }

.. _`bxt_ddi_phy_info.members`:

Members
-------

dual_channel
    true if this phy has a second channel.

rcomp_phy
    If -1, indicates this phy has its own rcomp resistor.Otherwise the GRC value will be copied from the phy indicated by
    this field.

reset_delay
    delay in us to wait before setting the common resetbit in BXT_PHY_CTL_FAMILY, which effectively enables the phy.

pwron_mask
    Mask with the appropriate bit set that would cause thepunit to power this phy if written to BXT_P_CR_GT_DISP_PWRON.

channel
    struct containing per channel information.

channel.port
    which port maps to this channel.

.. This file was automatic generated / don't edit.

