
.. _API-snd-soc-kcontrol-platform:

=========================
snd_soc_kcontrol_platform
=========================

*man snd_soc_kcontrol_platform(9)*

*4.6.0-rc1*

Returns the platform that registered the control


Synopsis
========

.. c:function:: struct snd_soc_platform ⋆ snd_soc_kcontrol_platform( struct snd_kcontrol * kcontrol )

Arguments
=========

``kcontrol``
    The control for which to get the platform


Note
====

This function will only work correctly if the control has been registered with ``snd_soc_add_platform_controls`` or via table based setup of a snd_soc_platform_driver. Otherwise
the behavior is undefined.
