.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-res-release:

===============
spi_res_release
===============

*man spi_res_release(9)*

*4.6.0-rc5*

release all spi resources for this message


Synopsis
========

.. c:function:: void spi_res_release( struct spi_master * master, struct spi_message * message )

Arguments
=========

``master``
    the ``spi_master``

``message``
    the ``spi_message``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
