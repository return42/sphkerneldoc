.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/zip/zip_device.h

.. _`zip_state`:

struct zip_state
================

.. c:type:: struct zip_state

    Structure representing the required information related to a command

.. _`zip_state.definition`:

Definition
----------

.. code-block:: c

    struct zip_state {
        union zip_inst_s zip_cmd;
        union zip_zres_s result;
        union zip_zptr_s *ctx;
        union zip_zptr_s *history;
        struct sg_info sginfo;
    }

.. _`zip_state.members`:

Members
-------

zip_cmd
    Pointer to zip instruction structure

result
    Pointer to zip result structure

ctx
    Context pointer for inflate

history
    Decompression history pointer

sginfo
    Scatter-gather info structure

.. This file was automatic generated / don't edit.

