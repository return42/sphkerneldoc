.. -*- coding: utf-8; mode: rst -*-

=====
mtd.h
=====


.. _`mtd_oob_ops`:

struct mtd_oob_ops
==================

.. c:type:: mtd_oob_ops

    oob operation operands


.. _`mtd_oob_ops.definition`:

Definition
----------

.. code-block:: c

  struct mtd_oob_ops {
    unsigned int mode;
    size_t len;
    size_t retlen;
    size_t ooblen;
    size_t oobretlen;
    uint32_t ooboffs;
    uint8_t * datbuf;
    uint8_t * oobbuf;
  };


.. _`mtd_oob_ops.members`:

Members
-------

:``mode``:
    operation mode

:``len``:
    number of data bytes to write/read

:``retlen``:
    number of data bytes written/read

:``ooblen``:
    number of oob bytes to write/read

:``oobretlen``:
    number of oob bytes written/read

:``ooboffs``:
    offset of oob data in the oob area (only relevant when
    mode = MTD_OPS_PLACE_OOB or MTD_OPS_RAW)

:``datbuf``:
    data buffer - if NULL only oob data are read/written

:``oobbuf``:
    oob data buffer




.. _`mtd_oob_ops.description`:

Description
-----------

Note, it is allowed to read more than one OOB area at one go, but not write.
The interface assumes that the OOB write requests program only one page's
OOB area.

