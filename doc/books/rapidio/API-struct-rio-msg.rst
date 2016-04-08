
.. _API-struct-rio-msg:

==============
struct rio_msg
==============

*man struct rio_msg(9)*

*4.6.0-rc1*

RIO message event


Synopsis
========

.. code-block:: c

    struct rio_msg {
      struct resource * res;
      void (* mcback) (struct rio_mport * mport, void *dev_id, int mbox, int slot);
    };


Members
=======

res
    Mailbox resource

mcback
    Message event callback
