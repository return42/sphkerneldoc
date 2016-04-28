.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-finalize-current-transfer:

=============================
spi_finalize_current_transfer
=============================

*man spi_finalize_current_transfer(9)*

*4.6.0-rc5*

report completion of a transfer


Synopsis
========

.. c:function:: void spi_finalize_current_transfer( struct spi_master * master )

Arguments
=========

``master``
    the master reporting completion


Description
===========

Called by SPI drivers using the core ``transfer_one_message``
implementation to notify it that the current interrupt driven transfer
has finished and the next one may be scheduled.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
