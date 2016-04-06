
.. _API-i915-parse-cmds:

===============
i915_parse_cmds
===============

*man i915_parse_cmds(9)*

*4.6.0-rc1*

parse a submitted batch buffer for privilege violations


Synopsis
========

.. c:function:: int i915_parse_cmds( struct intel_engine_cs * ring, struct drm_i915_gem_object * batch_obj, struct drm_i915_gem_object * shadow_batch_obj, u32 batch_start_offset, u32 batch_len, bool is_master )

Arguments
=========

``ring``
    the ring on which the batch is to execute

``batch_obj``
    the batch buffer in question

``shadow_batch_obj``
    copy of the batch buffer in question

``batch_start_offset``
    byte offset in the batch at which execution starts

``batch_len``
    length of the commands in batch_obj

``is_master``
    is the submitting process the drm master?


Description
===========

Parses the specified batch buffer looking for privilege violations as described in the overview.


Return
======

non-zero if the parser finds violations or otherwise fails; -EACCES if the batch appears legal but should use hardware parsing
