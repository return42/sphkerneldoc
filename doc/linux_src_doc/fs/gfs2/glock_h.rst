.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/glock.h

.. _`gfs2_glock_nq_init`:

gfs2_glock_nq_init
==================

.. c:function:: int gfs2_glock_nq_init(struct gfs2_glock *gl, unsigned int state, u16 flags, struct gfs2_holder *gh)

    initialize a holder and enqueue it on a glock

    :param struct gfs2_glock \*gl:
        the glock

    :param unsigned int state:
        the state we're requesting

    :param u16 flags:
        the modifier flags

    :param struct gfs2_holder \*gh:
        the holder structure

.. _`gfs2_glock_nq_init.return`:

Return
------

0, GLR\_\*, or errno

.. This file was automatic generated / don't edit.

