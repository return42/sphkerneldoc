.. -*- coding: utf-8; mode: rst -*-

.. _API-ata-dev-init-params:

===================
ata_dev_init_params
===================

*man ata_dev_init_params(9)*

*4.6.0-rc5*

Issue INIT DEV PARAMS command


Synopsis
========

.. c:function:: unsigned int ata_dev_init_params( struct ata_device * dev, u16 heads, u16 sectors )

Arguments
=========

``dev``
    Device to which command will be sent

``heads``
    Number of heads (taskfile parameter)

``sectors``
    Number of sectors (taskfile parameter)


LOCKING
=======

Kernel thread context (may sleep)


RETURNS
=======

0 on success, AC_ERR_* mask otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
