
.. _API-snd-soc-limit-volume:

====================
snd_soc_limit_volume
====================

*man snd_soc_limit_volume(9)*

*4.6.0-rc1*

Set new limit to an existing volume control.


Synopsis
========

.. c:function:: int snd_soc_limit_volume( struct snd_soc_card * card, const char * name, int max )

Arguments
=========

``card``
    where to look for the control

``name``
    Name of the control

``max``
    new maximum limit


Description
===========

Return 0 for success, else error.
