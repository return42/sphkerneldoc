.. -*- coding: utf-8; mode: rst -*-

.. _API-nand-setup-read-retry:

=====================
nand_setup_read_retry
=====================

*man nand_setup_read_retry(9)*

*4.6.0-rc5*

[INTERN] Set the READ RETRY mode


Synopsis
========

.. c:function:: int nand_setup_read_retry( struct mtd_info * mtd, int retry_mode )

Arguments
=========

``mtd``
    MTD device structure

``retry_mode``
    the retry mode to use


Description
===========

Some vendors supply a special command to shift the Vt threshold, to be
used when there are too many bitflips in a page (i.e., ECC error). After
setting a new threshold, the host should retry reading the page.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
