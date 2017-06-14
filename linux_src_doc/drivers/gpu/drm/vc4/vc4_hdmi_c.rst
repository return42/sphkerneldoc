.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vc4/vc4_hdmi.c

.. _`vc4-falcon-hdmi-module`:

VC4 Falcon HDMI module
======================

The HDMI core has a state machine and a PHY.  On BCM2835, most of
the unit operates off of the HSM clock from CPRMAN.  It also
internally uses the PLLH_PIX clock for the PHY.

HDMI infoframes are kept within a small packet ram, where each
packet can be individually enabled for including in a frame.

HDMI audio is implemented entirely within the HDMI IP block.  A
register in the HDMI encoder takes SPDIF frames from the DMA engine
and transfers them over an internal MAI (multi-channel audio
interconnect) bus to the encoder side for insertion into the video
blank regions.

The driver's HDMI encoder does not yet support power management.
The HDMI encoder's power domain and the HSM/pixel clocks are kept
continuously running, and only the HDMI logic and packet ram are
powered off/on at disable/enable time.

The driver does not yet support CEC control, though the HDMI
encoder block has CEC support.

.. This file was automatic generated / don't edit.

