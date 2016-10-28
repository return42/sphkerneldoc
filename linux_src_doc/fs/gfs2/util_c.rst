.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/util.c

.. _`gfs2_assert_withdraw_i`:

gfs2_assert_withdraw_i
======================

.. c:function:: int gfs2_assert_withdraw_i(struct gfs2_sbd *sdp, char *assertion, const char *function, char *file, unsigned int line)

    Cause the machine to withdraw if \ ``assertion``\  is false

    :param struct gfs2_sbd \*sdp:
        *undescribed*

    :param char \*assertion:
        *undescribed*

    :param const char \*function:
        *undescribed*

    :param char \*file:
        *undescribed*

    :param unsigned int line:
        *undescribed*

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

    :param struct gfs2_sbd \*sdp:
        *undescribed*

    :param char \*assertion:
        *undescribed*

    :param const char \*function:
        *undescribed*

    :param char \*file:
        *undescribed*

    :param unsigned int line:
        *undescribed*

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

    :param struct gfs2_sbd \*sdp:
        *undescribed*

    :param int cluster_wide:
        *undescribed*

    :param const char \*function:
        *undescribed*

    :param char \*file:
        *undescribed*

    :param unsigned int line:
        *undescribed*

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

    :param struct gfs2_inode \*ip:
        *undescribed*

    :param int cluster_wide:
        *undescribed*

    :param const char \*function:
        *undescribed*

    :param char \*file:
        *undescribed*

    :param unsigned int line:
        *undescribed*

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

    :param struct gfs2_rgrpd \*rgd:
        *undescribed*

    :param int cluster_wide:
        *undescribed*

    :param const char \*function:
        *undescribed*

    :param char \*file:
        *undescribed*

    :param unsigned int line:
        *undescribed*

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

    :param struct gfs2_sbd \*sdp:
        *undescribed*

    :param struct buffer_head \*bh:
        *undescribed*

    :param const char \*type:
        *undescribed*

    :param const char \*function:
        *undescribed*

    :param char \*file:
        *undescribed*

    :param unsigned int line:
        *undescribed*

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

    :param struct gfs2_sbd \*sdp:
        *undescribed*

    :param struct buffer_head \*bh:
        *undescribed*

    :param u16 type:
        *undescribed*

    :param u16 t:
        *undescribed*

    :param const char \*function:
        *undescribed*

    :param char \*file:
        *undescribed*

    :param unsigned int line:
        *undescribed*

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

    :param struct gfs2_sbd \*sdp:
        *undescribed*

    :param const char \*function:
        *undescribed*

    :param char \*file:
        *undescribed*

    :param unsigned int line:
        *undescribed*

.. _`gfs2_io_error_i.return`:

Return
------

-1 if this call withdrew the machine,
0 if it was already withdrawn

.. _`gfs2_io_error_bh_i`:

gfs2_io_error_bh_i
==================

.. c:function:: int gfs2_io_error_bh_i(struct gfs2_sbd *sdp, struct buffer_head *bh, const char *function, char *file, unsigned int line)

    Flag a buffer I/O error and withdraw

    :param struct gfs2_sbd \*sdp:
        *undescribed*

    :param struct buffer_head \*bh:
        *undescribed*

    :param const char \*function:
        *undescribed*

    :param char \*file:
        *undescribed*

    :param unsigned int line:
        *undescribed*

.. _`gfs2_io_error_bh_i.return`:

Return
------

-1 if this call withdrew the machine,
0 if it was already withdrawn

.. This file was automatic generated / don't edit.

