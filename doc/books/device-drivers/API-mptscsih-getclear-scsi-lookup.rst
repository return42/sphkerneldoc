.. -*- coding: utf-8; mode: rst -*-

.. _API-mptscsih-getclear-scsi-lookup:

=============================
mptscsih_getclear_scsi_lookup
=============================

*man mptscsih_getclear_scsi_lookup(9)*

*4.6.0-rc5*

retrieves and clears scmd entry from ScsiLookup[] array list


Synopsis
========

.. c:function:: struct scsi_cmnd * mptscsih_getclear_scsi_lookup( MPT_ADAPTER * ioc, int i )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``i``
    index into the array


Description
===========

Returns the scsi_cmd pointer


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
