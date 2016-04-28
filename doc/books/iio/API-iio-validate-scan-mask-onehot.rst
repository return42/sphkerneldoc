.. -*- coding: utf-8; mode: rst -*-

.. _API-iio-validate-scan-mask-onehot:

=============================
iio_validate_scan_mask_onehot
=============================

*man iio_validate_scan_mask_onehot(9)*

*4.6.0-rc5*

Validates that exactly one channel is selected


Synopsis
========

.. c:function:: bool iio_validate_scan_mask_onehot( struct iio_dev * indio_dev, const unsigned long * mask )

Arguments
=========

``indio_dev``
    the iio device

``mask``
    scan mask to be checked


Description
===========

Return true if exactly one bit is set in the scan mask, false otherwise.
It can be used for devices where only one channel can be active for
sampling at a time.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
