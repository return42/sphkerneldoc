
.. _API-i915-needs-cmd-parser:

=====================
i915_needs_cmd_parser
=====================

*man i915_needs_cmd_parser(9)*

*4.6.0-rc1*

should a given ring use software command parsing?


Synopsis
========

.. c:function:: bool i915_needs_cmd_parser( struct intel_engine_cs * ring )

Arguments
=========

``ring``
    the ring in question


Description
===========

Only certain platforms require software batch buffer command parsing, and only when enabled via module parameter.


Return
======

true if the ring requires software command parsing
