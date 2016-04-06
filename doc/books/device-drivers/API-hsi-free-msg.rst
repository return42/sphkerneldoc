
.. _API-hsi-free-msg:

============
hsi_free_msg
============

*man hsi_free_msg(9)*

*4.6.0-rc1*

Free an HSI message


Synopsis
========

.. c:function:: void hsi_free_msg( struct hsi_msg * msg )

Arguments
=========

``msg``
    Pointer to the HSI message


Description
===========

Client is responsible to free the buffers pointed by the scatterlists.
