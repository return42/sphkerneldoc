
.. _API-snd-jack-add-new-kctl:

=====================
snd_jack_add_new_kctl
=====================

*man snd_jack_add_new_kctl(9)*

*4.6.0-rc1*

Create a new snd_jack_kctl and add it to jack


Synopsis
========

.. c:function:: int snd_jack_add_new_kctl( struct snd_jack * jack, const char * name, int mask )

Arguments
=========

``jack``
    the jack instance which the kctl will attaching to

``name``
    the name for the snd_kcontrol object

``mask``
    a bitmask of enum snd_jack_type values that can be detected by this snd_jack_kctl object.


Description
===========

Creates a new snd_kcontrol object and adds it to the jack kctl_list.


Return
======

Zero if successful, or a negative error code on failure.
