
.. _API-spi-finalize-current-message:

============================
spi_finalize_current_message
============================

*man spi_finalize_current_message(9)*

*4.6.0-rc1*

the current message is complete


Synopsis
========

.. c:function:: void spi_finalize_current_message( struct spi_master * master )

Arguments
=========

``master``
    the master to return the message to


Description
===========

Called by the driver to notify the core that the message in the front of the queue is complete and can be removed from the queue.
