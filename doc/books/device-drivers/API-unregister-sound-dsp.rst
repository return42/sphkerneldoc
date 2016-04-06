
.. _API-unregister-sound-dsp:

====================
unregister_sound_dsp
====================

*man unregister_sound_dsp(9)*

*4.6.0-rc1*

unregister a DSP device


Synopsis
========

.. c:function:: void unregister_sound_dsp( int unit )

Arguments
=========

``unit``
    unit number to allocate


Description
===========

Release a sound device that was allocated with ``register_sound_dsp``. The unit passed is the return value from the register function.

Both of the allocated units are released together automatically.
