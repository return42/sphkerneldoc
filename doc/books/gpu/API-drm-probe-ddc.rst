
.. _API-drm-probe-ddc:

=============
drm_probe_ddc
=============

*man drm_probe_ddc(9)*

*4.6.0-rc1*

probe DDC presence


Synopsis
========

.. c:function:: bool drm_probe_ddc( struct i2c_adapter * adapter )

Arguments
=========

``adapter``
    I2C adapter to probe


Return
======

True on success, false on failure.
