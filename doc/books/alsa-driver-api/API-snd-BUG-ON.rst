.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-BUG-ON:

==========
snd_BUG_ON
==========

*man snd_BUG_ON(9)*

*4.6.0-rc5*

debugging check macro


Synopsis
========

.. c:function:: snd_BUG_ON( cond )

Arguments
=========

``cond``
    condition to evaluate


Description
===========

Has the same behavior as WARN_ON when CONFIG_SND_DEBUG is set,
otherwise just evaluates the conditional and returns the value.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
