.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-ctrl-auto-cluster:

======================
v4l2_ctrl_auto_cluster
======================

*man v4l2_ctrl_auto_cluster(9)*

*4.6.0-rc5*

Mark all controls in the cluster as belonging to that cluster and set it
up for autofoo/foo-type handling.


Synopsis
========

.. c:function:: void v4l2_ctrl_auto_cluster( unsigned ncontrols, struct v4l2_ctrl ** controls, u8 manual_val, bool set_volatile )

Arguments
=========

``ncontrols``
    The number of controls in this cluster.

``controls``
    The cluster control array of size ``ncontrols``. The first control
    must be the 'auto' control (e.g. autogain, autoexposure, etc.)

``manual_val``
    The value for the first control in the cluster that equals the
    manual setting.

``set_volatile``
    If true, then all controls except the first auto control will be
    volatile.


Description
===========

Use for control groups where one control selects some automatic feature
and the other controls are only active whenever the automatic feature is
turned off (manual mode). Typical examples: autogain vs gain,
auto-whitebalance vs red and blue balance, etc.


The behavior of such controls is as follows
===========================================

When the autofoo control is set to automatic, then any manual controls
are set to inactive and any reads will call g_volatile_ctrl (if the
control was marked volatile).

When the autofoo control is set to manual, then any manual controls will
be marked active, and any reads will just return the current value
without going through g_volatile_ctrl.

In addition, this function will set the V4L2_CTRL_FLAG_UPDATE flag on
the autofoo control and V4L2_CTRL_FLAG_INACTIVE on the foo control(s)
if autofoo is in auto mode.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
