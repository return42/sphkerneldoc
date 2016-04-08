
.. _API-phy-driver-register:

===================
phy_driver_register
===================

*man phy_driver_register(9)*

*4.6.0-rc1*

register a phy_driver with the PHY layer


Synopsis
========

.. c:function:: int phy_driver_register( struct phy_driver * new_driver, struct module * owner )

Arguments
=========

``new_driver``
    new phy_driver to register

``owner``
    module owning this PHY
