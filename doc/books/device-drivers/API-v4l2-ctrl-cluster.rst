.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-ctrl-cluster:

=================
v4l2_ctrl_cluster
=================

*man v4l2_ctrl_cluster(9)*

*4.6.0-rc5*

Mark all controls in the cluster as belonging to that cluster.


Synopsis
========

.. c:function:: void v4l2_ctrl_cluster( unsigned ncontrols, struct v4l2_ctrl ** controls )

Arguments
=========

``ncontrols``
    The number of controls in this cluster.

``controls``
    The cluster control array of size ``ncontrols``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
