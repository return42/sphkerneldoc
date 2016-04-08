
.. _API-ata-dev-set-feature:

===================
ata_dev_set_feature
===================

*man ata_dev_set_feature(9)*

*4.6.0-rc1*

Issue SET FEATURES - SATA FEATURES


Synopsis
========

.. c:function:: unsigned int ata_dev_set_feature( struct ata_device * dev, u8 enable, u8 feature )

Arguments
=========

``dev``
    Device to which command will be sent

``enable``
    Whether to enable or disable the feature

``feature``
    The sector count represents the feature to set


Description
===========

Issue SET FEATURES - SATA FEATURES command to device ``dev`` on port ``ap`` with sector count


LOCKING
=======

PCI/etc. bus probe sem.


RETURNS
=======

0 on success, AC_ERR_⋆ mask otherwise.
