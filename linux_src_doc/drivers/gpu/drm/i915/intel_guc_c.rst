.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_guc.c

.. _`intel_guc_auth_huc`:

intel_guc_auth_huc
==================

.. c:function:: int intel_guc_auth_huc(struct intel_guc *guc, u32 rsa_offset)

    Send action to GuC to authenticate HuC ucode

    :param struct intel_guc \*guc:
        intel_guc structure

    :param u32 rsa_offset:
        rsa offset w.r.t ggtt base of huc vma

.. _`intel_guc_auth_huc.description`:

Description
-----------

Triggers a HuC firmware authentication request to the GuC via intel_guc_send
INTEL_GUC_ACTION_AUTHENTICATE_HUC interface. This function is invoked by
\ :c:func:`intel_huc_auth`\ .

.. _`intel_guc_auth_huc.return`:

Return
------

non-zero code on error

.. _`intel_guc_suspend`:

intel_guc_suspend
=================

.. c:function:: int intel_guc_suspend(struct intel_guc *guc)

    notify GuC entering suspend state

    :param struct intel_guc \*guc:
        the guc

.. _`intel_guc_reset_engine`:

intel_guc_reset_engine
======================

.. c:function:: int intel_guc_reset_engine(struct intel_guc *guc, struct intel_engine_cs *engine)

    ask GuC to reset an engine

    :param struct intel_guc \*guc:
        intel_guc structure

    :param struct intel_engine_cs \*engine:
        engine to be reset

.. _`intel_guc_resume`:

intel_guc_resume
================

.. c:function:: int intel_guc_resume(struct intel_guc *guc)

    notify GuC resuming from suspend state

    :param struct intel_guc \*guc:
        the guc

.. _`guc-address-space`:

GuC Address Space
=================

The layout of GuC address space is shown below:

::

    +==============> +====================+ <== GUC_GGTT_TOP
    ^                |                    |
    |                |                    |
    |                |        DRAM        |
    |                |       Memory       |
    |                |                    |
   GuC               |                    |
 Address  +========> +====================+ <== WOPCM Top
  Space   ^          |   HW contexts RSVD |
    |     |          |        WOPCM       |
    |     |     +==> +--------------------+ <== GuC WOPCM Top
    |    GuC    ^    |                    |
    |    GGTT   |    |                    |
    |    Pin   GuC   |        GuC         |
    |    Bias WOPCM  |       WOPCM        |
    |     |    Size  |                    |
    |     |     |    |                    |
    v     v     v    |                    |
    +=====+=====+==> +====================+ <== GuC WOPCM Base
                     |   Non-GuC WOPCM    |
                     |   (HuC/Reserved)   |
                     +====================+ <== WOPCM Base

The lower part of GuC Address Space [0, ggtt_pin_bias) is mapped to WOPCM
while upper part of GuC Address Space [ggtt_pin_bias, GUC_GGTT_TOP) is mapped
to DRAM. The value of the GuC ggtt_pin_bias is determined by WOPCM size and
actual GuC WOPCM size.

.. _`intel_guc_init_ggtt_pin_bias`:

intel_guc_init_ggtt_pin_bias
============================

.. c:function:: void intel_guc_init_ggtt_pin_bias(struct intel_guc *guc)

    Initialize the GuC ggtt_pin_bias value.

    :param struct intel_guc \*guc:
        intel_guc structure.

.. _`intel_guc_init_ggtt_pin_bias.description`:

Description
-----------

This function will calculate and initialize the ggtt_pin_bias value based on
overall WOPCM size and GuC WOPCM size.

.. _`intel_guc_allocate_vma`:

intel_guc_allocate_vma
======================

.. c:function:: struct i915_vma *intel_guc_allocate_vma(struct intel_guc *guc, u32 size)

    Allocate a GGTT VMA for GuC usage

    :param struct intel_guc \*guc:
        the guc

    :param u32 size:
        size of area to allocate (both virtual space and memory)

.. _`intel_guc_allocate_vma.description`:

Description
-----------

This is a wrapper to create an object for use with the GuC. In order to
use it inside the GuC, an object needs to be pinned lifetime, so we allocate
both some backing storage and a range inside the Global GTT. We must pin
it in the GGTT somewhere other than than [0, GUC ggtt_pin_bias) because that
range is reserved inside GuC.

.. _`intel_guc_allocate_vma.return`:

Return
------

A i915_vma if successful, otherwise an ERR_PTR.

.. This file was automatic generated / don't edit.

