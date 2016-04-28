.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-BUG:

=======
snd_BUG
=======

*man snd_BUG(9)*

*4.6.0-rc5*

give a BUG warning message and stack trace


Synopsis
========

.. c:function:: snd_BUG(  )

Arguments
=========

None


Description
===========

Calls ``WARN`` if CONFIG_SND_DEBUG is set. Ignored when
CONFIG_SND_DEBUG is not set.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
