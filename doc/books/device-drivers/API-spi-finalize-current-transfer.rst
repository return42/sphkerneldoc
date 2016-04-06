
.. _API-spi-finalize-current-transfer:

=============================
spi_finalize_current_transfer
=============================

*man spi_finalize_current_transfer(9)*

*4.6.0-rc1*

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

Called by SPI drivers using the core ``transfer_one_message`` implementation to notify it that the current interrupt driven transfer has finished and the next one may be scheduled.
