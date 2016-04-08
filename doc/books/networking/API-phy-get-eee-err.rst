
.. _API-phy-get-eee-err:

===============
phy_get_eee_err
===============

*man phy_get_eee_err(9)*

*4.6.0-rc1*

report the EEE wake error count


Synopsis
========

.. c:function:: int phy_get_eee_err( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

it is to report the number of time where the PHY failed to complete its normal wake sequence.
