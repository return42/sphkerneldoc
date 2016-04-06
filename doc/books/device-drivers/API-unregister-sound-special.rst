
.. _API-unregister-sound-special:

========================
unregister_sound_special
========================

*man unregister_sound_special(9)*

*4.6.0-rc1*

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

Release a sound device that was allocated with ``register_sound_special``. The unit passed is the return value from the register function.
