.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-readScsiDevicePageHeaders:

=============================
mpt_readScsiDevicePageHeaders
=============================

*man mpt_readScsiDevicePageHeaders(9)*

*4.6.0-rc5*

save version and length of SDP1


Synopsis
========

.. c:function:: int mpt_readScsiDevicePageHeaders( MPT_ADAPTER * ioc, int portnum )

Arguments
=========

``ioc``
    Pointer to a Adapter Strucutre

``portnum``
    IOC port number


Return
======

-EFAULT if read of config page header fails or 0 if success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
