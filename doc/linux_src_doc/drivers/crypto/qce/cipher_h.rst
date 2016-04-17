.. -*- coding: utf-8; mode: rst -*-

========
cipher.h
========


.. _`qce_cipher_reqctx`:

struct qce_cipher_reqctx
========================

.. c:type:: qce_cipher_reqctx

    holds private cipher objects per request


.. _`qce_cipher_reqctx.definition`:

Definition
----------

.. code-block:: c

  struct qce_cipher_reqctx {
    unsigned long flags;
    u8 * iv;
    unsigned int ivsize;
    int src_nents;
    int dst_nents;
    struct scatterlist result_sg;
    struct sg_table dst_tbl;
    struct scatterlist * dst_sg;
    struct sg_table src_tbl;
    struct scatterlist * src_sg;
    unsigned int cryptlen;
  };


.. _`qce_cipher_reqctx.members`:

Members
-------

:``flags``:
    operation flags

:``iv``:
    pointer to the IV

:``ivsize``:
    IV size

:``src_nents``:
    source entries

:``dst_nents``:
    destination entries

:``result_sg``:
    scatterlist used for result buffer

:``dst_tbl``:
    destination sg table

:``dst_sg``:
    destination sg pointer table beginning

:``src_tbl``:
    source sg table

:``src_sg``:
    source sg pointer table beginning;

:``cryptlen``:
    crypto length


