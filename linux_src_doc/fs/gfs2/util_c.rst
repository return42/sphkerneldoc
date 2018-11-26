.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/util.c

.. _`gfs2_assert_withdraw_i`:

gfs2_assert_withdraw_i
======================

.. c:function:: int gfs2_assert_withdraw_i(struct gfs2_sbd *sdp, char *assertion, const char *function, char *file, unsigned int line)

    Cause the machine to withdraw if \ ``assertion``\  is false

    :param sdp:
        *undescribed*
    :type sdp: struct gfs2_sbd \*

    :param assertion:
        *undescribed*
    :type assertion: char \*

    :param function:
        *undescribed*
    :type function: const char \*

    :param file:
        *undescribed*
    :type file: char \*

    :param line:
        *undescribed*
    :type line: unsigned int

.. _`gfs2_assert_withdraw_i.return`:

Return
------

-1 if this call withdrew the machine,
-2 if it was already withdrawn

.. _`gfs2_assert_warn_i`:

gfs2_assert_warn_i
==================

.. c:function:: int gfs2_assert_warn_i(struct gfs2_sbd *sdp, char *assertion, const char *function, char *file, unsigned int line)

    Print a message to the console if \ ``assertion``\  is false

    :param sdp:
        *undescribed*
    :type sdp: struct gfs2_sbd \*

    :param assertion:
        *undescribed*
    :type assertion: char \*

    :param function:
        *undescribed*
    :type function: const char \*

    :param file:
        *undescribed*
    :type file: char \*

    :param line:
        *undescribed*
    :type line: unsigned int

.. _`gfs2_assert_warn_i.return`:

Return
------

-1 if we printed something
-2 if we didn't

.. _`gfs2_consist_i`:

gfs2_consist_i
==============

.. c:function:: int gfs2_consist_i(struct gfs2_sbd *sdp, int cluster_wide, const char *function, char *file, unsigned int line)

    Flag a filesystem consistency error and withdraw

    :param sdp:
        *undescribed*
    :type sdp: struct gfs2_sbd \*

    :param cluster_wide:
        *undescribed*
    :type cluster_wide: int

    :param function:
        *undescribed*
    :type function: const char \*

    :param file:
        *undescribed*
    :type file: char \*

    :param line:
        *undescribed*
    :type line: unsigned int

.. _`gfs2_consist_i.return`:

Return
------

-1 if this call withdrew the machine,
0 if it was already withdrawn

.. _`gfs2_consist_inode_i`:

gfs2_consist_inode_i
====================

.. c:function:: int gfs2_consist_inode_i(struct gfs2_inode *ip, int cluster_wide, const char *function, char *file, unsigned int line)

    Flag an inode consistency error and withdraw

    :param ip:
        *undescribed*
    :type ip: struct gfs2_inode \*

    :param cluster_wide:
        *undescribed*
    :type cluster_wide: int

    :param function:
        *undescribed*
    :type function: const char \*

    :param file:
        *undescribed*
    :type file: char \*

    :param line:
        *undescribed*
    :type line: unsigned int

.. _`gfs2_consist_inode_i.return`:

Return
------

-1 if this call withdrew the machine,
0 if it was already withdrawn

.. _`gfs2_consist_rgrpd_i`:

gfs2_consist_rgrpd_i
====================

.. c:function:: int gfs2_consist_rgrpd_i(struct gfs2_rgrpd *rgd, int cluster_wide, const char *function, char *file, unsigned int line)

    Flag a RG consistency error and withdraw

    :param rgd:
        *undescribed*
    :type rgd: struct gfs2_rgrpd \*

    :param cluster_wide:
        *undescribed*
    :type cluster_wide: int

    :param function:
        *undescribed*
    :type function: const char \*

    :param file:
        *undescribed*
    :type file: char \*

    :param line:
        *undescribed*
    :type line: unsigned int

.. _`gfs2_consist_rgrpd_i.return`:

Return
------

-1 if this call withdrew the machine,
0 if it was already withdrawn

.. _`gfs2_meta_check_ii`:

gfs2_meta_check_ii
==================

.. c:function:: int gfs2_meta_check_ii(struct gfs2_sbd *sdp, struct buffer_head *bh, const char *type, const char *function, char *file, unsigned int line)

    Flag a magic number consistency error and withdraw

    :param sdp:
        *undescribed*
    :type sdp: struct gfs2_sbd \*

    :param bh:
        *undescribed*
    :type bh: struct buffer_head \*

    :param type:
        *undescribed*
    :type type: const char \*

    :param function:
        *undescribed*
    :type function: const char \*

    :param file:
        *undescribed*
    :type file: char \*

    :param line:
        *undescribed*
    :type line: unsigned int

.. _`gfs2_meta_check_ii.return`:

Return
------

-1 if this call withdrew the machine,
-2 if it was already withdrawn

.. _`gfs2_metatype_check_ii`:

gfs2_metatype_check_ii
======================

.. c:function:: int gfs2_metatype_check_ii(struct gfs2_sbd *sdp, struct buffer_head *bh, u16 type, u16 t, const char *function, char *file, unsigned int line)

    Flag a metadata type consistency error and withdraw

    :param sdp:
        *undescribed*
    :type sdp: struct gfs2_sbd \*

    :param bh:
        *undescribed*
    :type bh: struct buffer_head \*

    :param type:
        *undescribed*
    :type type: u16

    :param t:
        *undescribed*
    :type t: u16

    :param function:
        *undescribed*
    :type function: const char \*

    :param file:
        *undescribed*
    :type file: char \*

    :param line:
        *undescribed*
    :type line: unsigned int

.. _`gfs2_metatype_check_ii.return`:

Return
------

-1 if this call withdrew the machine,
-2 if it was already withdrawn

.. _`gfs2_io_error_i`:

gfs2_io_error_i
===============

.. c:function:: int gfs2_io_error_i(struct gfs2_sbd *sdp, const char *function, char *file, unsigned int line)

    Flag an I/O error and withdraw

    :param sdp:
        *undescribed*
    :type sdp: struct gfs2_sbd \*

    :param function:
        *undescribed*
    :type function: const char \*

    :param file:
        *undescribed*
    :type file: char \*

    :param line:
        *undescribed*
    :type line: unsigned int

.. _`gfs2_io_error_i.return`:

Return
------

-1 if this call withdrew the machine,
0 if it was already withdrawn

.. _`gfs2_io_error_bh_i`:

gfs2_io_error_bh_i
==================

.. c:function:: void gfs2_io_error_bh_i(struct gfs2_sbd *sdp, struct buffer_head *bh, const char *function, char *file, unsigned int line, bool withdraw)

    Flag a buffer I/O error

    :param sdp:
        *undescribed*
    :type sdp: struct gfs2_sbd \*

    :param bh:
        *undescribed*
    :type bh: struct buffer_head \*

    :param function:
        *undescribed*
    :type function: const char \*

    :param file:
        *undescribed*
    :type file: char \*

    :param line:
        *undescribed*
    :type line: unsigned int

    :param withdraw:
        withdraw the filesystem
    :type withdraw: bool

.. This file was automatic generated / don't edit.

