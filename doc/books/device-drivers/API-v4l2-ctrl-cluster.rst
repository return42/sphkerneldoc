
.. _API-v4l2-ctrl-cluster:

=================
v4l2_ctrl_cluster
=================

*man v4l2_ctrl_cluster(9)*

*4.6.0-rc1*

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
