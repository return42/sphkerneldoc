
.. _API-struct-drm-dp-aux-msg:

=====================
struct drm_dp_aux_msg
=====================

*man struct drm_dp_aux_msg(9)*

*4.6.0-rc1*

DisplayPort AUX channel transaction


Synopsis
========

.. code-block:: c

    struct drm_dp_aux_msg {
      unsigned int address;
      u8 request;
      u8 reply;
      void * buffer;
      size_t size;
    };


Members
=======

address
    address of the (first) register to access

request
    contains the type of transaction (see DP_AUX_⋆ macros)

reply
    upon completion, contains the reply type of the transaction

buffer
    pointer to a transmission or reception buffer

size
    size of ``buffer``
