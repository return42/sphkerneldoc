
.. _API-snd-soc-dapm-new-controls:

=========================
snd_soc_dapm_new_controls
=========================

*man snd_soc_dapm_new_controls(9)*

*4.6.0-rc1*

create new dapm controls


Synopsis
========

.. c:function:: int snd_soc_dapm_new_controls( struct snd_soc_dapm_context * dapm, const struct snd_soc_dapm_widget * widget, int num )

Arguments
=========

``dapm``
    DAPM context

``widget``
    widget array

``num``
    number of widgets


Description
===========

Creates new DAPM controls based upon the templates.

Returns 0 for success else error.
