.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_wopcm.h

.. _`intel_wopcm`:

struct intel_wopcm
==================

.. c:type:: struct intel_wopcm

    Overall WOPCM info and WOPCM regions.

.. _`intel_wopcm.definition`:

Definition
----------

.. code-block:: c

    struct intel_wopcm {
        u32 size;
        struct {
            u32 base;
            u32 size;
        } guc;
    }

.. _`intel_wopcm.members`:

Members
-------

size
    Size of overall WOPCM.

guc
    GuC WOPCM Region info.

guc.base
    GuC WOPCM base which is offset from WOPCM base.

guc.size
    Size of the GuC WOPCM region.

.. This file was automatic generated / don't edit.

