.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_workarounds.c

.. _`hardware-workarounds`:

Hardware workarounds
====================

This file is intended as a central place to implement most [1]_ of the
required workarounds for hardware to work as originally intended. They fall
in five basic categories depending on how/when they are applied:

- Workarounds that touch registers that are saved/restored to/from the HW
  context image. The list is emitted (via Load Register Immediate commands)
  everytime a new context is created.
- GT workarounds. The list of these WAs is applied whenever these registers
  revert to default values (on GPU reset, suspend/resume [2]_, etc..).
- Display workarounds. The list is applied during display clock-gating
  initialization.
- Workarounds that whitelist a privileged register, so that UMDs can manage
  them directly. This is just a special case of a MMMIO workaround (as we
  write the list of these to/be-whitelisted registers to some special HW
  registers).
- Workaround batchbuffers, that get executed automatically by the hardware
  on every HW context restore.

.. [1] Please notice that there are other WAs that, due to their nature,
   cannot be applied from a central place. Those are peppered around the rest
   of the code, as needed.

.. [2] Technically, some registers are powercontext saved & restored, so they
   survive a suspend/resume. In practice, writing them again is not too
   costly and simplifies things. We can revisit this in the future.

Layout
''''''

Keep things in this file ordered by WA type, as per the above (context, GT,
display, register whitelist, batchbuffer). Then, inside each type, keep the
following order:

- Infrastructure functions and macros
- WAs per platform in standard gen/chrono order
- Public functions to init or apply the given workaround type.

.. This file was automatic generated / don't edit.

