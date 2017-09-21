.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_fifo_underrun.c

.. _`fifo-underrun-handling`:

fifo underrun handling
======================

The i915 driver checks for display fifo underruns using the interrupt signals
provided by the hardware. This is enabled by default and fairly useful to
debug display issues, especially watermark settings.

If an underrun is detected this is logged into dmesg. To avoid flooding logs
and occupying the cpu underrun interrupts are disabled after the first
occurrence until the next modeset on a given pipe.

Note that underrun detection on gmch platforms is a bit more ugly since there
is no interrupt (despite that the signalling bit is in the PIPESTAT pipe
interrupt register). Also on some other platforms underrun interrupts are
shared, which means that if we detect an underrun we need to disable underrun
reporting on all pipes.

The code also supports underrun detection on the PCH transcoder.

.. _`intel_set_cpu_fifo_underrun_reporting`:

intel_set_cpu_fifo_underrun_reporting
=====================================

.. c:function:: bool intel_set_cpu_fifo_underrun_reporting(struct drm_i915_private *dev_priv, enum pipe pipe, bool enable)

    set cpu fifo underrrun reporting state

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum pipe pipe:
        (CPU) pipe to set state for

    :param bool enable:
        whether underruns should be reported or not

.. _`intel_set_cpu_fifo_underrun_reporting.description`:

Description
-----------

This function sets the fifo underrun state for \ ``pipe``\ . It is used in the
modeset code to avoid false positives since on many platforms underruns are
expected when disabling or enabling the pipe.

Notice that on some platforms disabling underrun reports for one pipe
disables for all due to shared interrupts. Actual reporting is still per-pipe
though.

Returns the previous state of underrun reporting.

.. _`intel_set_pch_fifo_underrun_reporting`:

intel_set_pch_fifo_underrun_reporting
=====================================

.. c:function:: bool intel_set_pch_fifo_underrun_reporting(struct drm_i915_private *dev_priv, enum pipe pch_transcoder, bool enable)

    set PCH fifo underrun reporting state

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum pipe pch_transcoder:
        the PCH transcoder (same as pipe on IVB and older)

    :param bool enable:
        whether underruns should be reported or not

.. _`intel_set_pch_fifo_underrun_reporting.description`:

Description
-----------

This function makes us disable or enable PCH fifo underruns for a specific
PCH transcoder. Notice that on some PCHs (e.g. CPT/PPT), disabling FIFO
underrun reporting for one transcoder may also disable all the other PCH
error interruts for the other transcoders, due to the fact that there's just
one interrupt mask/enable bit for all the transcoders.

Returns the previous state of underrun reporting.

.. _`intel_cpu_fifo_underrun_irq_handler`:

intel_cpu_fifo_underrun_irq_handler
===================================

.. c:function:: void intel_cpu_fifo_underrun_irq_handler(struct drm_i915_private *dev_priv, enum pipe pipe)

    handle CPU fifo underrun interrupt

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum pipe pipe:
        (CPU) pipe to set state for

.. _`intel_cpu_fifo_underrun_irq_handler.description`:

Description
-----------

This handles a CPU fifo underrun interrupt, generating an underrun warning
into dmesg if underrun reporting is enabled and then disables the underrun
interrupt to avoid an irq storm.

.. _`intel_pch_fifo_underrun_irq_handler`:

intel_pch_fifo_underrun_irq_handler
===================================

.. c:function:: void intel_pch_fifo_underrun_irq_handler(struct drm_i915_private *dev_priv, enum pipe pch_transcoder)

    handle PCH fifo underrun interrupt

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum pipe pch_transcoder:
        the PCH transcoder (same as pipe on IVB and older)

.. _`intel_pch_fifo_underrun_irq_handler.description`:

Description
-----------

This handles a PCH fifo underrun interrupt, generating an underrun warning
into dmesg if underrun reporting is enabled and then disables the underrun
interrupt to avoid an irq storm.

.. _`intel_check_cpu_fifo_underruns`:

intel_check_cpu_fifo_underruns
==============================

.. c:function:: void intel_check_cpu_fifo_underruns(struct drm_i915_private *dev_priv)

    check for CPU fifo underruns immediately

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

.. _`intel_check_cpu_fifo_underruns.description`:

Description
-----------

Check for CPU fifo underruns immediately. Useful on IVB/HSW where the shared
error interrupt may have been disabled, and so CPU fifo underruns won't
necessarily raise an interrupt, and on GMCH platforms where underruns never
raise an interrupt.

.. _`intel_check_pch_fifo_underruns`:

intel_check_pch_fifo_underruns
==============================

.. c:function:: void intel_check_pch_fifo_underruns(struct drm_i915_private *dev_priv)

    check for PCH fifo underruns immediately

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

.. _`intel_check_pch_fifo_underruns.description`:

Description
-----------

Check for PCH fifo underruns immediately. Useful on CPT/PPT where the shared
error interrupt may have been disabled, and so PCH fifo underruns won't
necessarily raise an interrupt.

.. This file was automatic generated / don't edit.

