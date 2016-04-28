.. -*- coding: utf-8; mode: rst -*-

.. _API-maple-driver-unregister:

=======================
maple_driver_unregister
=======================

*man maple_driver_unregister(9)*

*4.6.0-rc5*

unregister a maple driver.


Synopsis
========

.. c:function:: void maple_driver_unregister( struct maple_driver * drv )

Arguments
=========

``drv``
    maple driver to unregister.


Description
===========

Cleans up after ``maple_driver_register``. To be invoked in the exit
path of any module drivers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
