.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-driver-register:

===================
phy_driver_register
===================

*man phy_driver_register(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
