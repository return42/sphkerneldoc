.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/mv_cesa.c

.. _`req_progress`:

struct req_progress
===================

.. c:type:: struct req_progress

    used for every crypt request

.. _`req_progress.definition`:

Definition
----------

.. code-block:: c

    struct req_progress {
        struct sg_mapping_iter src_sg_it;
        struct sg_mapping_iter dst_sg_it;
        void (*complete)(void);
        void (*process)(int is_first);
        int sg_src_left;
        int src_start;
        int crypt_len;
        int hw_nbytes;
        int copy_back;
        int sg_dst_left;
        int dst_start;
        int hw_processed_bytes;
    }

.. _`req_progress.members`:

Members
-------

src_sg_it
    sg iterator for src

dst_sg_it
    sg iterator for dst

complete
    *undescribed*

process
    *undescribed*

sg_src_left
    bytes left in src to process (scatter list)

src_start
    offset to add to src start position (scatter list)

crypt_len
    length of current hw crypt/hash process

hw_nbytes
    total bytes to process in hw for this request

copy_back
    whether to copy data back (crypt) or not (hash)

sg_dst_left
    bytes left dst to process in this scatter list

dst_start
    offset to add to dst start position (scatter list)

hw_processed_bytes
    number of bytes processed by hw (request).

.. _`req_progress.description`:

Description
-----------

sg helper are used to iterate over the scatterlist. Since the size of the
SRAM may be less than the scatter size, this struct struct is used to keep
track of progress within current scatterlist.

.. This file was automatic generated / don't edit.

