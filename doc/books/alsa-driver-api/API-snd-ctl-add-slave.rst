
.. _API-snd-ctl-add-slave:

=================
snd_ctl_add_slave
=================

*man snd_ctl_add_slave(9)*

*4.6.0-rc1*

Add a virtual slave control


Synopsis
========

.. c:function:: int snd_ctl_add_slave( struct snd_kcontrol * master, struct snd_kcontrol * slave )

Arguments
=========

``master``
    vmaster element

``slave``
    slave element to add


Description
===========

Add a virtual slave control to the given master element created via ``snd_ctl_create_virtual_master`` beforehand.

All slaves must be the same type (returning the same information via info callback). The function doesn't check it, so it's your responsibility.

Also, some additional limitations: at most two channels, logarithmic volume control (dB level) thus no linear volume, master can only attenuate the volume without gain


Return
======

Zero if successful or a negative error code.
