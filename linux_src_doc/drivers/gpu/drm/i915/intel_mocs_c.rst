.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_mocs.c

.. _`get_mocs_settings`:

get_mocs_settings
=================

.. c:function:: bool get_mocs_settings(struct drm_i915_private *dev_priv, struct drm_i915_mocs_table *table)

    :param dev_priv:
        i915 device.
    :type dev_priv: struct drm_i915_private \*

    :param table:
        Output table that will be made to point at appropriate
        MOCS values for the device.
    :type table: struct drm_i915_mocs_table \*

.. _`get_mocs_settings.description`:

Description
-----------

This function will return the values of the MOCS table that needs to
be programmed for the platform. It will return the values that need
to be programmed and if they need to be programmed.

.. _`get_mocs_settings.return`:

Return
------

true if there are applicable MOCS settings for the device.

.. _`intel_mocs_init_engine`:

intel_mocs_init_engine
======================

.. c:function:: void intel_mocs_init_engine(struct intel_engine_cs *engine)

    emit the mocs control table

    :param engine:
        The engine for whom to emit the registers.
    :type engine: struct intel_engine_cs \*

.. _`intel_mocs_init_engine.description`:

Description
-----------

This function simply emits a MI_LOAD_REGISTER_IMM command for the
given table starting at the given address.

.. _`emit_mocs_control_table`:

emit_mocs_control_table
=======================

.. c:function:: int emit_mocs_control_table(struct i915_request *rq, const struct drm_i915_mocs_table *table)

    emit the mocs control table

    :param rq:
        Request to set up the MOCS table for.
    :type rq: struct i915_request \*

    :param table:
        The values to program into the control regs.
    :type table: const struct drm_i915_mocs_table \*

.. _`emit_mocs_control_table.description`:

Description
-----------

This function simply emits a MI_LOAD_REGISTER_IMM command for the
given table starting at the given address.

.. _`emit_mocs_control_table.return`:

Return
------

0 on success, otherwise the error status.

.. _`emit_mocs_l3cc_table`:

emit_mocs_l3cc_table
====================

.. c:function:: int emit_mocs_l3cc_table(struct i915_request *rq, const struct drm_i915_mocs_table *table)

    emit the mocs control table

    :param rq:
        Request to set up the MOCS table for.
    :type rq: struct i915_request \*

    :param table:
        The values to program into the control regs.
    :type table: const struct drm_i915_mocs_table \*

.. _`emit_mocs_l3cc_table.description`:

Description
-----------

This function simply emits a MI_LOAD_REGISTER_IMM command for the
given table starting at the given address. This register set is
programmed in pairs.

.. _`emit_mocs_l3cc_table.return`:

Return
------

0 on success, otherwise the error status.

.. _`intel_mocs_init_l3cc_table`:

intel_mocs_init_l3cc_table
==========================

.. c:function:: void intel_mocs_init_l3cc_table(struct drm_i915_private *dev_priv)

    program the mocs control table

    :param dev_priv:
        i915 device private
    :type dev_priv: struct drm_i915_private \*

.. _`intel_mocs_init_l3cc_table.description`:

Description
-----------

This function simply programs the mocs registers for the given table
starting at the given address. This register set is  programmed in pairs.

These registers may get programmed more than once, it is simpler to
re-program 32 registers than maintain the state of when they were programmed.
We are always reprogramming with the same values and this only on context
start.

.. _`intel_mocs_init_l3cc_table.return`:

Return
------

Nothing.

.. _`intel_rcs_context_init_mocs`:

intel_rcs_context_init_mocs
===========================

.. c:function:: int intel_rcs_context_init_mocs(struct i915_request *rq)

    program the MOCS register.

    :param rq:
        Request to set up the MOCS tables for.
    :type rq: struct i915_request \*

.. _`intel_rcs_context_init_mocs.description`:

Description
-----------

This function will emit a batch buffer with the values required for
programming the MOCS register values for all the currently supported
rings.

These registers are partially stored in the RCS context, so they are
emitted at the same time so that when a context is created these registers
are set up. These registers have to be emitted into the start of the
context as setting the ELSP will re-init some of these registers back
to the hw values.

.. _`intel_rcs_context_init_mocs.return`:

Return
------

0 on success, otherwise the error status.

.. This file was automatic generated / don't edit.

