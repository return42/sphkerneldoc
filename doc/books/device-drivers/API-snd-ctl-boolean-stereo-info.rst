.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ctl-boolean-stereo-info:

===========================
snd_ctl_boolean_stereo_info
===========================

*man snd_ctl_boolean_stereo_info(9)*

*4.6.0-rc5*

Helper function for a standard boolean info callback with stereo two
channels


Synopsis
========

.. c:function:: int snd_ctl_boolean_stereo_info( struct snd_kcontrol * kcontrol, struct snd_ctl_elem_info * uinfo )

Arguments
=========

``kcontrol``
    the kcontrol instance

``uinfo``
    info to store


Description
===========

This is a function that can be used as info callback for a standard
boolean control with stereo two channels.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
