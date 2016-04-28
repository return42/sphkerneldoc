.. -*- coding: utf-8; mode: rst -*-

.. _API-unregister-sound-special:

========================
unregister_sound_special
========================

*man unregister_sound_special(9)*

*4.6.0-rc5*

unregister a special sound device


Synopsis
========

.. c:function:: void unregister_sound_special( int unit )

Arguments
=========

``unit``
    unit number to allocate


Description
===========

Release a sound device that was allocated with
``register_sound_special``. The unit passed is the return value from the
register function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
