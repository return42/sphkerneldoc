.. -*- coding: utf-8; mode: rst -*-

.. _API-unregister-sound-midi:

=====================
unregister_sound_midi
=====================

*man unregister_sound_midi(9)*

*4.6.0-rc5*

unregister a midi device


Synopsis
========

.. c:function:: void unregister_sound_midi( int unit )

Arguments
=========

``unit``
    unit number to allocate


Description
===========

Release a sound device that was allocated with ``register_sound_midi``.
The unit passed is the return value from the register function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
