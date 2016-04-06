
.. _API-input-ff-create:

===============
input_ff_create
===============

*man input_ff_create(9)*

*4.6.0-rc1*

create force-feedback device


Synopsis
========

.. c:function:: int input_ff_create( struct input_dev * dev, unsigned int max_effects )

Arguments
=========

``dev``
    input device supporting force-feedback

``max_effects``
    maximum number of effects supported by the device


Description
===========

This function allocates all necessary memory for a force feedback portion of an input device and installs all default handlers. ``dev``->ffbit should be already set up before
calling this function. Once ff device is created you need to setup its upload, erase, playback and other handlers before registering input device
