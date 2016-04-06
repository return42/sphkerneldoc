
.. _API-unregister-sound-mixer:

======================
unregister_sound_mixer
======================

*man unregister_sound_mixer(9)*

*4.6.0-rc1*

unregister a mixer


Synopsis
========

.. c:function:: void unregister_sound_mixer( int unit )

Arguments
=========

``unit``
    unit number to allocate


Description
===========

Release a sound device that was allocated with ``register_sound_mixer``. The unit passed is the return value from the register function.
