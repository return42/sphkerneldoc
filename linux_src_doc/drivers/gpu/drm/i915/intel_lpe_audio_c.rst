.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_lpe_audio.c

.. _`lpe-audio-integration-for-hdmi-or-dp-playback`:

LPE Audio integration for HDMI or DP playback
=============================================

Motivation:
Atom platforms (e.g. valleyview and cherryTrail) integrates a DMA-based
interface as an alternative to the traditional HDaudio path. While this
mode is unrelated to the LPE aka SST audio engine, the documentation refers
to this mode as LPE so we keep this notation for the sake of consistency.

The interface is handled by a separate standalone driver maintained in the
ALSA subsystem for simplicity. To minimize the interaction between the two
subsystems, a bridge is setup between the hdmi-lpe-audio and i915:
1. Create a platform device to share MMIO/IRQ resources
2. Make the platform device child of i915 device for runtime PM.
3. Create IRQ chip to forward the LPE audio irqs.
the hdmi-lpe-audio driver probes the lpe audio device and creates a new
sound card

Threats:
Due to the restriction in Linux platform device model, user need manually
uninstall the hdmi-lpe-audio driver before uninstalling i915 module,
otherwise we might run into use-after-free issues after i915 removes the
platform device: even though hdmi-lpe-audio driver is released, the modules
is still in "installed" status.

Implementation:
The MMIO/REG platform resources are created according to the registers
specification.
When forwarding LPE audio irqs, the flow control handler selection depends
on the platform, for example on valleyview handle_simple_irq is enough.

.. _`intel_lpe_audio_irq_handler`:

intel_lpe_audio_irq_handler
===========================

.. c:function:: void intel_lpe_audio_irq_handler(struct drm_i915_private *dev_priv)

    forwards the LPE audio irq

    :param struct drm_i915_private \*dev_priv:
        the i915 drm device private data

.. _`intel_lpe_audio_irq_handler.description`:

Description
-----------

the LPE Audio irq is forwarded to the irq handler registered by LPE audio
driver.

.. _`intel_lpe_audio_init`:

intel_lpe_audio_init
====================

.. c:function:: int intel_lpe_audio_init(struct drm_i915_private *dev_priv)

    detect and setup the bridge between HDMI LPE Audio driver and i915

    :param struct drm_i915_private \*dev_priv:
        the i915 drm device private data

.. _`intel_lpe_audio_init.return`:

Return
------

0 if successful. non-zero if detection or
llocation/initialization fails

.. _`intel_lpe_audio_teardown`:

intel_lpe_audio_teardown
========================

.. c:function:: void intel_lpe_audio_teardown(struct drm_i915_private *dev_priv)

    destroy the bridge between HDMI LPE audio driver and i915

    :param struct drm_i915_private \*dev_priv:
        the i915 drm device private data

.. _`intel_lpe_audio_teardown.description`:

Description
-----------

release all the resources for LPE audio <-> i915 bridge.

.. _`intel_lpe_audio_notify`:

intel_lpe_audio_notify
======================

.. c:function:: void intel_lpe_audio_notify(struct drm_i915_private *dev_priv, void *eld, int port, int pipe, int tmds_clk_speed, bool dp_output, int link_rate)

    notify lpe audio event audio driver and i915

    :param struct drm_i915_private \*dev_priv:
        the i915 drm device private data

    :param void \*eld:
        ELD data

    :param int port:
        port id

    :param int pipe:
        pipe id

    :param int tmds_clk_speed:
        tmds clock frequency in Hz

    :param bool dp_output:
        *undescribed*

    :param int link_rate:
        *undescribed*

.. _`intel_lpe_audio_notify.description`:

Description
-----------

Notify lpe audio driver of eld change.

.. This file was automatic generated / don't edit.

