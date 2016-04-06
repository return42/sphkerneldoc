
.. _API-i915-cmd-parser-get-version:

===========================
i915_cmd_parser_get_version
===========================

*man i915_cmd_parser_get_version(9)*

*4.6.0-rc1*

get the cmd parser version number


Synopsis
========

.. c:function:: int i915_cmd_parser_get_version( void )

Arguments
=========

``void``
    no arguments


Description
===========

The cmd parser maintains a simple increasing integer version number suitable for passing to userspace clients to determine what operations are permitted.


Return
======

the current version number of the cmd parser
