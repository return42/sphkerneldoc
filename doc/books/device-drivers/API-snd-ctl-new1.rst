.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ctl-new1:

============
snd_ctl_new1
============

*man snd_ctl_new1(9)*

*4.6.0-rc5*

create a control instance from the template


Synopsis
========

.. c:function:: struct snd_kcontrol * snd_ctl_new1( const struct snd_kcontrol_new * ncontrol, void * private_data )

Arguments
=========

``ncontrol``
    the initialization record

``private_data``
    the private data to set


Description
===========

Allocates a new struct snd_kcontrol instance and initialize from the
given template. When the access field of ncontrol is 0, it's assumed as
READWRITE access. When the count field is 0, it's assumes as one.


Return
======

The pointer of the newly generated instance, or ``NULL`` on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
