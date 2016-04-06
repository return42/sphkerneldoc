
.. _API-snd-ctl-remove:

==============
snd_ctl_remove
==============

*man snd_ctl_remove(9)*

*4.6.0-rc1*

remove the control from the card and release it


Synopsis
========

.. c:function:: int snd_ctl_remove( struct snd_card * card, struct snd_kcontrol * kcontrol )

Arguments
=========

``card``
    the card instance

``kcontrol``
    the control instance to remove


Description
===========

Removes the control from the card and then releases the instance. You don't need to call ``snd_ctl_free_one``. You must be in the write lock -
down_write( ``card``->controls_rwsem).


Return
======

0 if successful, or a negative error code on failure.
