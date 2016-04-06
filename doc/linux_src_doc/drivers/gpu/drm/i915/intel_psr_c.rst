.. -*- coding: utf-8; mode: rst -*-

===========
intel_psr.c
===========



.. _xref_intel_psr_enable:

intel_psr_enable
================

.. c:function:: void intel_psr_enable (struct intel_dp * intel_dp)

    Enable PSR

    :param struct intel_dp * intel_dp:
        Intel DP



Description
-----------

This function can only be called after the pipe is fully trained and enabled.




.. _xref_intel_psr_disable:

intel_psr_disable
=================

.. c:function:: void intel_psr_disable (struct intel_dp * intel_dp)

    Disable PSR

    :param struct intel_dp * intel_dp:
        Intel DP



Description
-----------

This function needs to be called before disabling pipe.




.. _xref_intel_psr_single_frame_update:

intel_psr_single_frame_update
=============================

.. c:function:: void intel_psr_single_frame_update (struct drm_device * dev, unsigned frontbuffer_bits)

    Single Frame Update

    :param struct drm_device * dev:
        DRM device

    :param unsigned frontbuffer_bits:
        frontbuffer plane tracking bits



Description
-----------

Some platforms support a single frame update feature that is used to
send and update only one frame on Remote Frame Buffer.
So far it is only implemented for Valleyview and Cherryview because
hardware requires this to be done before a page flip.




.. _xref_intel_psr_invalidate:

intel_psr_invalidate
====================

.. c:function:: void intel_psr_invalidate (struct drm_device * dev, unsigned frontbuffer_bits)

    Invalidade PSR

    :param struct drm_device * dev:
        DRM device

    :param unsigned frontbuffer_bits:
        frontbuffer plane tracking bits



Description
-----------

Since the hardware frontbuffer tracking has gaps we need to integrate
with the software frontbuffer tracking. This function gets called every
time frontbuffer rendering starts and a buffer gets dirtied. PSR must be
disabled if the frontbuffer mask contains a buffer relevant to PSR.


Dirty frontbuffers relevant to PSR are tracked in busy_frontbuffer_bits."




.. _xref_intel_psr_flush:

intel_psr_flush
===============

.. c:function:: void intel_psr_flush (struct drm_device * dev, unsigned frontbuffer_bits, enum fb_op_origin origin)

    Flush PSR

    :param struct drm_device * dev:
        DRM device

    :param unsigned frontbuffer_bits:
        frontbuffer plane tracking bits

    :param enum fb_op_origin origin:
        which operation caused the flush



Description
-----------

Since the hardware frontbuffer tracking has gaps we need to integrate
with the software frontbuffer tracking. This function gets called every
time frontbuffer rendering has completed and flushed out to memory. PSR
can be enabled again if no other frontbuffer relevant to PSR is dirty.


Dirty frontbuffers relevant to PSR are tracked in busy_frontbuffer_bits.




.. _xref_intel_psr_init:

intel_psr_init
==============

.. c:function:: void intel_psr_init (struct drm_device * dev)

    Init basic PSR work and mutex.

    :param struct drm_device * dev:
        DRM device



Description
-----------

This function is  called only once at driver load to initialize basic
PSR stuff.


