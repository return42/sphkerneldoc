.. -*- coding: utf-8; mode: rst -*-

=================
i915_cmd_parser.c
=================



.. _xref_i915_cmd_parser_init_ring:

i915_cmd_parser_init_ring
=========================

.. c:function:: int i915_cmd_parser_init_ring (struct intel_engine_cs * ring)

    set cmd parser related fields for a ringbuffer

    :param struct intel_engine_cs * ring:
        the ringbuffer to initialize



Description
-----------

Optionally initializes fields related to batch buffer command parsing in the
struct intel_engine_cs based on whether the platform requires software
command parsing.



Return
------

non-zero if initialization fails




.. _xref_i915_cmd_parser_fini_ring:

i915_cmd_parser_fini_ring
=========================

.. c:function:: void i915_cmd_parser_fini_ring (struct intel_engine_cs * ring)

    clean up cmd parser related fields

    :param struct intel_engine_cs * ring:
        the ringbuffer to clean up



Description
-----------

Releases any resources related to command parsing that may have been
initialized for the specified ring.




.. _xref_i915_needs_cmd_parser:

i915_needs_cmd_parser
=====================

.. c:function:: bool i915_needs_cmd_parser (struct intel_engine_cs * ring)

    should a given ring use software command parsing?

    :param struct intel_engine_cs * ring:
        the ring in question



Description
-----------

Only certain platforms require software batch buffer command parsing, and
only when enabled via module parameter.



Return
------

true if the ring requires software command parsing




.. _xref_i915_parse_cmds:

i915_parse_cmds
===============

.. c:function:: int i915_parse_cmds (struct intel_engine_cs * ring, struct drm_i915_gem_object * batch_obj, struct drm_i915_gem_object * shadow_batch_obj, u32 batch_start_offset, u32 batch_len, bool is_master)

    parse a submitted batch buffer for privilege violations

    :param struct intel_engine_cs * ring:
        the ring on which the batch is to execute

    :param struct drm_i915_gem_object * batch_obj:
        the batch buffer in question

    :param struct drm_i915_gem_object * shadow_batch_obj:
        copy of the batch buffer in question

    :param u32 batch_start_offset:
        byte offset in the batch at which execution starts

    :param u32 batch_len:
        length of the commands in batch_obj

    :param bool is_master:
        is the submitting process the drm master?



Description
-----------

Parses the specified batch buffer looking for privilege violations as
described in the overview.



Return
------

non-zero if the parser finds violations or otherwise fails; -EACCES
if the batch appears legal but should use hardware parsing




.. _xref_i915_cmd_parser_get_version:

i915_cmd_parser_get_version
===========================

.. c:function:: int i915_cmd_parser_get_version ( void)

    get the cmd parser version number

    :param void:
        no arguments



Description
-----------



The cmd parser maintains a simple increasing integer version number suitable
for passing to userspace clients to determine what operations are permitted.



Return
------

the current version number of the cmd parser


