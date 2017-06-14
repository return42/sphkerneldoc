.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vc4/vc4_irq.c

.. _`interrupt-management-for-the-v3d-engine`:

Interrupt management for the V3D engine
=======================================

We have an interrupt status register (V3D_INTCTL) which reports
interrupts, and where writing 1 bits clears those interrupts.
There are also a pair of interrupt registers
(V3D_INTENA/V3D_INTDIS) where writing a 1 to their bits enables or
disables that specific interrupt, and 0s written are ignored
(reading either one returns the set of enabled interrupts).

When we take a binning flush done interrupt, we need to submit the
next frame for binning and move the finished frame to the render
thread.

When we take a render frame interrupt, we need to wake the
processes waiting for some frame to be done, and get the next frame
submitted ASAP (so the hardware doesn't sit idle when there's work
to do).

When we take the binner out of memory interrupt, we need to
allocate some new memory and pass it to the binner so that the
current job can make progress.

.. This file was automatic generated / don't edit.

