
.. _API-wimax-msg:

=========
wimax_msg
=========

*man wimax_msg(9)*

*4.6.0-rc1*

Send a message to user space


Synopsis
========

.. c:function:: int wimax_msg( struct wimax_dev * wimax_dev, const char * pipe_name, const void * buf, size_t size, gfp_t gfp_flags )

Arguments
=========

``wimax_dev``
    WiMAX device descriptor (properly referenced)

``pipe_name``
    "named pipe" the message will be sent to

``buf``
    pointer to the message to send.

``size``
    size of the buffer pointed to by ``buf`` (in bytes).

``gfp_flags``
    flags for memory allocation.


Returns
=======

``0`` if ok, negative errno code on error.


Description
===========

Sends a free-form message to user space on the device ``wimax_dev``.


NOTES
=====

Once the ``skb`` is given to this function, who will own it and will release it when done (unless it returns error).
