.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-finalize-current-message:

============================
spi_finalize_current_message
============================

*man spi_finalize_current_message(9)*

*4.6.0-rc5*

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

Called by the driver to notify the core that the message in the front of
the queue is complete and can be removed from the queue.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
