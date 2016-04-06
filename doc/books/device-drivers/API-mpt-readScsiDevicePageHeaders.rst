
.. _API-mpt-readScsiDevicePageHeaders:

=============================
mpt_readScsiDevicePageHeaders
=============================

*man mpt_readScsiDevicePageHeaders(9)*

*4.6.0-rc1*

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
