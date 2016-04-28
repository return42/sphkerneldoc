.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ctl-make-virtual-master:

===========================
snd_ctl_make_virtual_master
===========================

*man snd_ctl_make_virtual_master(9)*

*4.6.0-rc5*

Create a virtual master control


Synopsis
========

.. c:function:: struct snd_kcontrol * snd_ctl_make_virtual_master( char * name, const unsigned int * tlv )

Arguments
=========

``name``
    name string of the control element to create

``tlv``
    optional TLV int array for dB information


Description
===========

Creates a virtual master control with the given name string.

After creating a vmaster element, you can add the slave controls via
``snd_ctl_add_slave`` or ``snd_ctl_add_slave_uncached``.

The optional argument ``tlv`` can be used to specify the TLV information
for dB scale of the master control. It should be a single element with
#SNDRV_CTL_TLVT_DB_SCALE, #SNDRV_CTL_TLV_DB_MINMAX or
#SNDRV_CTL_TLVT_DB_MINMAX_MUTE type, and should be the max 0dB.


Return
======

The created control element, or ``NULL`` for errors (ENOMEM).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
