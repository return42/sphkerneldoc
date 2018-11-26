.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/gfs2/glock.h

.. _`gfs2_glock_nq_init`:

gfs2_glock_nq_init
==================

.. c:function:: int gfs2_glock_nq_init(struct gfs2_glock *gl, unsigned int state, u16 flags, struct gfs2_holder *gh)

    initialize a holder and enqueue it on a glock

    :param gl:
        the glock
    :type gl: struct gfs2_glock \*

    :param state:
        the state we're requesting
    :type state: unsigned int

    :param flags:
        the modifier flags
    :type flags: u16

    :param gh:
        the holder structure
    :type gh: struct gfs2_holder \*

.. _`gfs2_glock_nq_init.return`:

Return
------

0, GLR\_\*, or errno

.. _`glock_set_object`:

glock_set_object
================

.. c:function:: void glock_set_object(struct gfs2_glock *gl, void *object)

    set the gl_object field of a glock

    :param gl:
        the glock
    :type gl: struct gfs2_glock \*

    :param object:
        the object
    :type object: void \*

.. _`glock_clear_object`:

glock_clear_object
==================

.. c:function:: void glock_clear_object(struct gfs2_glock *gl, void *object)

    clear the gl_object field of a glock

    :param gl:
        the glock
    :type gl: struct gfs2_glock \*

    :param object:
        the object
    :type object: void \*

.. _`glock_clear_object.description`:

Description
-----------

I'd love to similarly add this:
else if (gfs2_assert_warn(gl->gl_sbd, gl->gl_object == object))
gfs2_dump_glock(NULL, gl);
Unfortunately, that's not possible because as soon as gfs2_delete_inode
frees the block in the rgrp, another process can reassign it for an I_NEW
inode in gfs2_create_inode because that calls new_inode, not gfs2_iget.
That means gfs2_delete_inode may subsequently try to call this function
for a glock that's already pointing to a brand new inode. If we clear the
new inode's gl_object, we'll introduce metadata corruption. Function
gfs2_delete_inode calls clear_inode which calls gfs2_clear_inode which also
tries to clear gl_object, so it's more than just gfs2_delete_inode.

.. This file was automatic generated / don't edit.

