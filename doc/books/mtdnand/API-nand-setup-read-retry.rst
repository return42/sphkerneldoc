
.. _API-nand-setup-read-retry:

=====================
nand_setup_read_retry
=====================

*man nand_setup_read_retry(9)*

*4.6.0-rc1*

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

Some vendors supply a special command to shift the Vt threshold, to be used when there are too many bitflips in a page (i.e., ECC error). After setting a new threshold, the host
should retry reading the page.
