.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/bmap.h

.. _`gfs2_write_calc_reserv`:

gfs2_write_calc_reserv
======================

.. c:function:: void gfs2_write_calc_reserv(const struct gfs2_inode *ip, unsigned int len, unsigned int *data_blocks, unsigned int *ind_blocks)

    calculate number of blocks needed to write to a file

    :param ip:
        the file
    :type ip: const struct gfs2_inode \*

    :param len:
        the number of bytes to be written to the file
    :type len: unsigned int

    :param data_blocks:
        returns the number of data blocks required
    :type data_blocks: unsigned int \*

    :param ind_blocks:
        returns the number of indirect blocks required
    :type ind_blocks: unsigned int \*

.. This file was automatic generated / don't edit.

