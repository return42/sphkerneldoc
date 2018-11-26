.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_wopcm.c

.. _`wopcm-layout`:

WOPCM Layout
============

The layout of the WOPCM will be fixed after writing to GuC WOPCM size and
offset registers whose values are calculated and determined by HuC/GuC
firmware size and set of hardware requirements/restrictions as shown below:

::

   +=========> +====================+ <== WOPCM Top
   ^           |  HW contexts RSVD  |
   |     +===> +====================+ <== GuC WOPCM Top
   |     ^     |                    |
   |     |     |                    |
   |     |     |                    |
   |    GuC    |                    |
   |   WOPCM   |                    |
   |    Size   +--------------------+
 WOPCM   |     |    GuC FW RSVD     |
   |     |     +--------------------+
   |     |     |   GuC Stack RSVD   |
   |     |     +------------------- +
   |     v     |   GuC WOPCM RSVD   |
   |     +===> +====================+ <== GuC WOPCM base
   |           |     WOPCM RSVD     |
   |           +------------------- + <== HuC Firmware Top
   v           |      HuC FW        |
   +=========> +====================+ <== WOPCM Base

GuC accessible WOPCM starts at GuC WOPCM base and ends at GuC WOPCM top.
The top part of the WOPCM is reserved for hardware contexts (e.g. RC6
context).

.. _`intel_wopcm_init_early`:

intel_wopcm_init_early
======================

.. c:function:: void intel_wopcm_init_early(struct intel_wopcm *wopcm)

    Early initialization of the WOPCM.

    :param wopcm:
        pointer to intel_wopcm.
    :type wopcm: struct intel_wopcm \*

.. _`intel_wopcm_init_early.description`:

Description
-----------

Setup the size of WOPCM which will be used by later on WOPCM partitioning.

.. _`intel_wopcm_init`:

intel_wopcm_init
================

.. c:function:: int intel_wopcm_init(struct intel_wopcm *wopcm)

    Initialize the WOPCM structure.

    :param wopcm:
        pointer to intel_wopcm.
    :type wopcm: struct intel_wopcm \*

.. _`intel_wopcm_init.description`:

Description
-----------

This function will partition WOPCM space based on GuC and HuC firmware sizes
and will allocate max remaining for use by GuC. This function will also
enforce platform dependent hardware restrictions on GuC WOPCM offset and
size. It will fail the WOPCM init if any of these checks were failed, so that
the following GuC firmware uploading would be aborted.

.. _`intel_wopcm_init.return`:

Return
------

0 on success, non-zero error code on failure.

.. _`intel_wopcm_init_hw`:

intel_wopcm_init_hw
===================

.. c:function:: int intel_wopcm_init_hw(struct intel_wopcm *wopcm)

    Setup GuC WOPCM registers.

    :param wopcm:
        pointer to intel_wopcm.
    :type wopcm: struct intel_wopcm \*

.. _`intel_wopcm_init_hw.description`:

Description
-----------

Setup the GuC WOPCM size and offset registers with the calculated values. It
will verify the register values to make sure the registers are locked with
correct values.

.. _`intel_wopcm_init_hw.return`:

Return
------

0 on success. -EIO if registers were locked with incorrect values.

.. This file was automatic generated / don't edit.

