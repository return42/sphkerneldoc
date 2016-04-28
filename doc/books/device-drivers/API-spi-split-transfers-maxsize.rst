.. -*- coding: utf-8; mode: rst -*-

.. _API-spi-split-transfers-maxsize:

===========================
spi_split_transfers_maxsize
===========================

*man spi_split_transfers_maxsize(9)*

*4.6.0-rc5*

split spi transfers into multiple transfers when an individual transfer
exceeds a certain size


Synopsis
========

.. c:function:: int spi_split_transfers_maxsize( struct spi_master * master, struct spi_message * msg, size_t maxsize, gfp_t gfp )

Arguments
=========

``master``
    the ``spi_master`` for this transfer

``msg``
    the ``spi_message`` to transform

``maxsize``
    the maximum when to apply this

``gfp``
    GFP allocation flags


Return
======

status of transformation


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
