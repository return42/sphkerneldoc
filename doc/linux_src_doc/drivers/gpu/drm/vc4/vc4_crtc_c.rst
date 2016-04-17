.. -*- coding: utf-8; mode: rst -*-

==========
vc4_crtc.c
==========


.. _`vc4-crtc-module`:

VC4 CRTC module
===============

In VC4, the Pixel Valve is what most closely corresponds to the
DRM's concept of a CRTC.  The PV generates video timings from the
output's clock plus its configuration.  It pulls scaled pixels from
the HVS at that timing, and feeds it to the encoder.

However, the DRM CRTC also collects the configuration of all the
DRM planes attached to it.  As a result, this file also manages
setup of the VC4 HVS's display elements on the CRTC.

The 2835 has 3 different pixel valves.  pv0 in the audio power
domain feeds DSI0 or DPI, while pv1 feeds DS1 or SMI.  pv2 in the
image domain can feed either HDMI or the SDTV controller.  The
pixel valve chooses from the CPRMAN clocks (HSM for HDMI, VEC for
SDTV, etc.) according to which output type is chosen in the mux.

For power management, the pixel valve's registers are all clocked
by the AXI clock, while the timings and FIFOs make use of the
output-specific clock.  Since the encoders also directly consume
the CPRMAN clocks, and know what timings they need, they are the
ones that set the clock.

