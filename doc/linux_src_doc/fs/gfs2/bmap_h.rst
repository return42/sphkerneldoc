.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/bmap.h

.. _`gfs2_write_calc_reserv`:

gfs2_write_calc_reserv
======================

.. c:function:: void gfs2_write_calc_reserv(const struct gfs2_inode *ip, unsigned int len, unsigned int *data_blocks, unsigned int *ind_blocks)

    calculate number of blocks needed to write to a file

    :param const struct gfs2_inode \*ip:
        the file

    :param unsigned int len:
        the number of bytes to be written to the file

    :param unsigned int \*data_blocks:
        returns the number of data blocks required

    :param unsigned int \*ind_blocks:
        returns the number of indirect blocks required

.. This file was automatic generated / don't edit.

