.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-notifier-call-chain:

=============================
regulator_notifier_call_chain
=============================

*man regulator_notifier_call_chain(9)*

*4.6.0-rc5*

call regulator event notifier


Synopsis
========

.. c:function:: int regulator_notifier_call_chain( struct regulator_dev * rdev, unsigned long event, void * data )

Arguments
=========

``rdev``
    regulator source

``event``
    notifier block

``data``
    callback-specific data.


Description
===========

Called by regulator drivers to notify clients a regulator event has
occurred. We also notify regulator clients downstream. Note lock must be
held by caller.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
