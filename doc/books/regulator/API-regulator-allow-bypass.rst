.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-allow-bypass:

======================
regulator_allow_bypass
======================

*man regulator_allow_bypass(9)*

*4.6.0-rc5*

allow the regulator to go into bypass mode


Synopsis
========

.. c:function:: int regulator_allow_bypass( struct regulator * regulator, bool enable )

Arguments
=========

``regulator``
    Regulator to configure

``enable``
    enable or disable bypass mode


Description
===========

Allow the regulator to go into bypass mode if all other consumers for
the regulator also enable bypass mode and the machine constraints allow
this. Bypass mode means that the regulator is simply passing the input
directly to the output with no regulation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
