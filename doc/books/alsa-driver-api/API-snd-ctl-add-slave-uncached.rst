.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ctl-add-slave-uncached:

==========================
snd_ctl_add_slave_uncached
==========================

*man snd_ctl_add_slave_uncached(9)*

*4.6.0-rc5*

Add a virtual slave control


Synopsis
========

.. c:function:: int snd_ctl_add_slave_uncached( struct snd_kcontrol * master, struct snd_kcontrol * slave )

Arguments
=========

``master``
    vmaster element

``slave``
    slave element to add


Description
===========

Add a virtual slave control to the given master. Unlike
``snd_ctl_add_slave``, the element added via this function is supposed
to have volatile values, and get callback is called at each time queried
from the master.

When the control peeks the hardware values directly and the value can be
changed by other means than the put callback of the element, this
function should be used to keep the value always up-to-date.


Return
======

Zero if successful or a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
