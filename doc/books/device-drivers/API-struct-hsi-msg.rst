.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-hsi-msg:

==============
struct hsi_msg
==============

*man struct hsi_msg(9)*

*4.6.0-rc5*

HSI message descriptor


Synopsis
========

.. code-block:: c

    struct hsi_msg {
      struct list_head link;
      struct hsi_client * cl;
      struct sg_table sgt;
      void * context;
      void (* complete) (struct hsi_msg *msg);
      void (* destructor) (struct hsi_msg *msg);
      int status;
      unsigned int actual_len;
      unsigned int channel;
      unsigned int ttype:1;
      unsigned int break_frame:1;
    };


Members
=======

link
    Free to use by the current descriptor owner

cl
    HSI device client that issues the transfer

sgt
    Head of the scatterlist array

context
    Client context data associated to the transfer

complete
    Transfer completion callback

destructor
    Destructor to free resources when flushing

status
    Status of the transfer when completed

actual_len
    Actual length of data transferred on completion

channel
    Channel were to TX/RX the message

ttype
    Transfer type (TX if set, RX otherwise)

break_frame
    if true HSI will send/receive a break frame. Data buffers are
    ignored in the request.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
