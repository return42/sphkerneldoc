
.. _API-netdev-increment-features:

=========================
netdev_increment_features
=========================

*man netdev_increment_features(9)*

*4.6.0-rc1*

increment feature set by one


Synopsis
========

.. c:function:: netdev_features_t netdev_increment_features( netdev_features_t all, netdev_features_t one, netdev_features_t mask )

Arguments
=========

``all``
    current feature set

``one``
    new feature set

``mask``
    mask feature set


Description
===========

Computes a new feature set after adding a device with feature set ``one`` to the master device with current feature set ``all``. Will not enable anything that is off in ``mask``.
Returns the new feature set.
