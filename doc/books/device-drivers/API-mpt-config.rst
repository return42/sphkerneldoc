
.. _API-mpt-config:

==========
mpt_config
==========

*man mpt_config(9)*

*4.6.0-rc1*

Generic function to issue config message


Synopsis
========

.. c:function:: int mpt_config( MPT_ADAPTER * ioc, CONFIGPARMS * pCfg )

Arguments
=========

``ioc``
    Pointer to an adapter structure

``pCfg``
    Pointer to a configuration structure. Struct contains action, page address, direction, physical address and pointer to a configuration page header Page header is updated.


Description
===========

Returns 0 for success -EPERM if not allowed due to ISR context -EAGAIN if no msg frames currently available -EFAULT for non-successful reply or no reply (timeout)
