
.. _API-unregister-sound-midi:

=====================
unregister_sound_midi
=====================

*man unregister_sound_midi(9)*

*4.6.0-rc1*

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

Release a sound device that was allocated with ``register_sound_midi``. The unit passed is the return value from the register function.
