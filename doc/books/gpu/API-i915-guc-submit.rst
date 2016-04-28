.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-guc-submit:

===============
i915_guc_submit
===============

*man i915_guc_submit(9)*

*4.6.0-rc5*

Submit commands through GuC


Synopsis
========

.. c:function:: int i915_guc_submit( struct i915_guc_client * client, struct drm_i915_gem_request * rq )

Arguments
=========

``client``
    the guc client where commands will go through

``rq``
    request associated with the commands


Return
======

0 if succeed


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
