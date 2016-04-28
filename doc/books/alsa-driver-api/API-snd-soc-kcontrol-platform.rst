.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-kcontrol-platform:

=========================
snd_soc_kcontrol_platform
=========================

*man snd_soc_kcontrol_platform(9)*

*4.6.0-rc5*

Returns the platform that registered the control


Synopsis
========

.. c:function:: struct snd_soc_platform * snd_soc_kcontrol_platform( struct snd_kcontrol * kcontrol )

Arguments
=========

``kcontrol``
    The control for which to get the platform


Note
====

This function will only work correctly if the control has been
registered with ``snd_soc_add_platform_controls`` or via table based
setup of a snd_soc_platform_driver. Otherwise the behavior is
undefined.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
