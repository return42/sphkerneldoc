.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-register:

==================
regulator_register
==================

*man regulator_register(9)*

*4.6.0-rc5*

register regulator


Synopsis
========

.. c:function:: struct regulator_dev * regulator_register( const struct regulator_desc * regulator_desc, const struct regulator_config * cfg )

Arguments
=========

``regulator_desc``
    regulator to register

``cfg``
    runtime configuration for regulator


Description
===========

Called by regulator drivers to register a regulator. Returns a valid
pointer to struct regulator_dev on success or an ``ERR_PTR`` on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
