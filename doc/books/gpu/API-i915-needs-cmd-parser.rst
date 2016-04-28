.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-needs-cmd-parser:

=====================
i915_needs_cmd_parser
=====================

*man i915_needs_cmd_parser(9)*

*4.6.0-rc5*

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

Only certain platforms require software batch buffer command parsing,
and only when enabled via module parameter.


Return
======

true if the ring requires software command parsing


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
