.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_cmd_parser.c

.. _`i915_cmd_parser_init_ring`:

i915_cmd_parser_init_ring
=========================

.. c:function:: int i915_cmd_parser_init_ring(struct intel_engine_cs *engine)

    set cmd parser related fields for a ringbuffer

    :param struct intel_engine_cs \*engine:
        *undescribed*

.. _`i915_cmd_parser_init_ring.description`:

Description
-----------

Optionally initializes fields related to batch buffer command parsing in the
struct intel_engine_cs based on whether the platform requires software
command parsing.

.. _`i915_cmd_parser_init_ring.return`:

Return
------

non-zero if initialization fails

.. _`i915_cmd_parser_fini_ring`:

i915_cmd_parser_fini_ring
=========================

.. c:function:: void i915_cmd_parser_fini_ring(struct intel_engine_cs *engine)

    clean up cmd parser related fields

    :param struct intel_engine_cs \*engine:
        *undescribed*

.. _`i915_cmd_parser_fini_ring.description`:

Description
-----------

Releases any resources related to command parsing that may have been
initialized for the specified ring.

.. _`i915_needs_cmd_parser`:

i915_needs_cmd_parser
=====================

.. c:function:: bool i915_needs_cmd_parser(struct intel_engine_cs *engine)

    should a given ring use software command parsing?

    :param struct intel_engine_cs \*engine:
        *undescribed*

.. _`i915_needs_cmd_parser.description`:

Description
-----------

Only certain platforms require software batch buffer command parsing, and
only when enabled via module parameter.

.. _`i915_needs_cmd_parser.return`:

Return
------

true if the ring requires software command parsing

.. _`i915_parse_cmds`:

i915_parse_cmds
===============

.. c:function:: int i915_parse_cmds(struct intel_engine_cs *engine, struct drm_i915_gem_object *batch_obj, struct drm_i915_gem_object *shadow_batch_obj, u32 batch_start_offset, u32 batch_len, bool is_master)

    parse a submitted batch buffer for privilege violations

    :param struct intel_engine_cs \*engine:
        *undescribed*

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

.. _`i915_parse_cmds.description`:

Description
-----------

Parses the specified batch buffer looking for privilege violations as
described in the overview.

.. _`i915_parse_cmds.return`:

Return
------

non-zero if the parser finds violations or otherwise fails; -EACCES
if the batch appears legal but should use hardware parsing

.. _`i915_cmd_parser_get_version`:

i915_cmd_parser_get_version
===========================

.. c:function:: int i915_cmd_parser_get_version( void)

    get the cmd parser version number

    :param  void:
        no arguments

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

