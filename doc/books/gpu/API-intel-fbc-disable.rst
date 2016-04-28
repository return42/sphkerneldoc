.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-fbc-disable:

=================
intel_fbc_disable
=================

*man intel_fbc_disable(9)*

*4.6.0-rc5*

disable FBC if it's associated with crtc


Synopsis
========

.. c:function:: void intel_fbc_disable( struct intel_crtc * crtc )

Arguments
=========

``crtc``
    the CRTC


Description
===========

This function disables FBC if it's associated with the provided CRTC.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
