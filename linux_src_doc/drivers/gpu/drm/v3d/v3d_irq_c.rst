.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/v3d/v3d_irq.c

.. _`interrupt-management-for-the-v3d-engine`:

Interrupt management for the V3D engine
=======================================

When we take a binning or rendering flush done interrupt, we need
to signal the fence for that job so that the scheduler can queue up
the next one and unblock any waiters.

When we take the binner out of memory interrupt, we need to
allocate some new memory and pass it to the binner so that the
current job can make progress.

.. This file was automatic generated / don't edit.

