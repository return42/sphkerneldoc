.. -*- coding: utf-8; mode: rst -*-

==========
vc4_hdmi.c
==========


.. _`vc4-falcon-hdmi-module`:

VC4 Falcon HDMI module
======================

The HDMI core has a state machine and a PHY.  Most of the unit
operates off of the HSM clock from CPRMAN.  It also internally uses
the PLLH_PIX clock for the PHY.

