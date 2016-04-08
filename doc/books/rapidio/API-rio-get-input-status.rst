
.. _API-rio-get-input-status:

====================
rio_get_input_status
====================

*man rio_get_input_status(9)*

*4.6.0-rc1*

Sends a Link-Request/Input-Status control symbol and returns link-response (if requested).


Synopsis
========

.. c:function:: int rio_get_input_status( struct rio_dev * rdev, int pnum, u32 * lnkresp )

Arguments
=========

``rdev``
    RIO devive to issue Input-status command

``pnum``
    Device port number to issue the command

``lnkresp``
    Response from a link partner
