
.. _API-spi-get-next-queued-message:

===========================
spi_get_next_queued_message
===========================

*man spi_get_next_queued_message(9)*

*4.6.0-rc1*

called by driver to check for queued messages


Synopsis
========

.. c:function:: struct spi_message ⋆ spi_get_next_queued_message( struct spi_master * master )

Arguments
=========

``master``
    the master to check for queued messages


Description
===========

If there are more messages in the queue, the next message is returned from this call.


Return
======

the next message in the queue, else NULL if the queue is empty.
