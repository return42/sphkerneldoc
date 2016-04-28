.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dapm-new-controls:

=========================
snd_soc_dapm_new_controls
=========================

*man snd_soc_dapm_new_controls(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
