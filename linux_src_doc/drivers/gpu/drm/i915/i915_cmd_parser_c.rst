.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_cmd_parser.c

.. _`intel_engine_init_cmd_parser`:

intel_engine_init_cmd_parser
============================

.. c:function:: void intel_engine_init_cmd_parser(struct intel_engine_cs *engine)

    set cmd parser related fields for an engine

    :param struct intel_engine_cs \*engine:
        the engine to initialize

.. _`intel_engine_init_cmd_parser.description`:

Description
-----------

Optionally initializes fields related to batch buffer command parsing in the
struct intel_engine_cs based on whether the platform requires software
command parsing.

.. _`intel_engine_cleanup_cmd_parser`:

intel_engine_cleanup_cmd_parser
===============================

.. c:function:: void intel_engine_cleanup_cmd_parser(struct intel_engine_cs *engine)

    clean up cmd parser related fields

    :param struct intel_engine_cs \*engine:
        the engine to clean up

.. _`intel_engine_cleanup_cmd_parser.description`:

Description
-----------

Releases any resources related to command parsing that may have been
initialized for the specified engine.

.. _`intel_engine_cmd_parser`:

intel_engine_cmd_parser
=======================

.. c:function:: int intel_engine_cmd_parser(struct intel_engine_cs *engine, struct drm_i915_gem_object *batch_obj, struct drm_i915_gem_object *shadow_batch_obj, u32 batch_start_offset, u32 batch_len, bool is_master)

    parse a submitted batch buffer for privilege violations

    :param struct intel_engine_cs \*engine:
        the engine on which the batch is to execute

    :param struct drm_i915_gem_object \*batch_obj:
        the batch buffer in question

    :param struct drm_i915_gem_object \*shadow_batch_obj:
        copy of the batch buffer in question

    :param u32 batch_start_offset:
        byte offset in the batch at which execution starts

    :param u32 batch_len:
        length of the commands in batch_obj

    :param bool is_master:
        is the submitting process the drm master?

.. _`intel_engine_cmd_parser.description`:

Description
-----------

Parses the specified batch buffer looking for privilege violations as
described in the overview.

.. _`intel_engine_cmd_parser.return`:

Return
------

non-zero if the parser finds violations or otherwise fails; -EACCES
if the batch appears legal but should use hardware parsing

.. _`i915_cmd_parser_get_version`:

i915_cmd_parser_get_version
===========================

.. c:function:: int i915_cmd_parser_get_version(struct drm_i915_private *dev_priv)

    get the cmd parser version number

    :param struct drm_i915_private \*dev_priv:
        i915 device private

.. _`i915_cmd_parser_get_version.description`:

Description
-----------

The cmd parser maintains a simple increasing integer version number suitable
for passing to userspace clients to determine what operations are permitted.

.. _`i915_cmd_parser_get_version.return`:

Return
------

the current version number of the cmd parser

.. This file was automatic generated / don't edit.

