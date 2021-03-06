.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/fcx.c

.. _`tcw_get_intrg`:

tcw_get_intrg
=============

.. c:function:: struct tcw *tcw_get_intrg(struct tcw *tcw)

    return pointer to associated interrogate tcw

    :param tcw:
        pointer to the original tcw
    :type tcw: struct tcw \*

.. _`tcw_get_intrg.description`:

Description
-----------

Return a pointer to the interrogate tcw associated with the specified tcw
or \ ``NULL``\  if there is no associated interrogate tcw.

.. _`tcw_get_data`:

tcw_get_data
============

.. c:function:: void *tcw_get_data(struct tcw *tcw)

    return pointer to input/output data associated with tcw

    :param tcw:
        pointer to the tcw
    :type tcw: struct tcw \*

.. _`tcw_get_data.description`:

Description
-----------

Return the input or output data address specified in the tcw depending
on whether the r-bit or the w-bit is set. If neither bit is set, return
\ ``NULL``\ .

.. _`tcw_get_tccb`:

tcw_get_tccb
============

.. c:function:: struct tccb *tcw_get_tccb(struct tcw *tcw)

    return pointer to tccb associated with tcw

    :param tcw:
        pointer to the tcw
    :type tcw: struct tcw \*

.. _`tcw_get_tccb.description`:

Description
-----------

Return pointer to the tccb associated with this tcw.

.. _`tcw_get_tsb`:

tcw_get_tsb
===========

.. c:function:: struct tsb *tcw_get_tsb(struct tcw *tcw)

    return pointer to tsb associated with tcw

    :param tcw:
        pointer to the tcw
    :type tcw: struct tcw \*

.. _`tcw_get_tsb.description`:

Description
-----------

Return pointer to the tsb associated with this tcw.

.. _`tcw_init`:

tcw_init
========

.. c:function:: void tcw_init(struct tcw *tcw, int r, int w)

    initialize tcw data structure

    :param tcw:
        pointer to the tcw to be initialized
    :type tcw: struct tcw \*

    :param r:
        initial value of the r-bit
    :type r: int

    :param w:
        initial value of the w-bit
    :type w: int

.. _`tcw_init.description`:

Description
-----------

Initialize all fields of the specified tcw data structure with zero and
fill in the format, flags, r and w fields.

.. _`tcw_finalize`:

tcw_finalize
============

.. c:function:: void tcw_finalize(struct tcw *tcw, int num_tidaws)

    finalize tcw length fields and tidaw list

    :param tcw:
        pointer to the tcw
    :type tcw: struct tcw \*

    :param num_tidaws:
        the number of tidaws used to address input/output data or zero
        if no tida is used
    :type num_tidaws: int

.. _`tcw_finalize.description`:

Description
-----------

Calculate the input-/output-count and tccbl field in the tcw, add a
tcat the tccb and terminate the data tidaw list if used.

.. _`tcw_finalize.note`:

Note
----

in case input- or output-tida is used, the tidaw-list must be stored
in contiguous storage (no ttic). The tcal field in the tccb must be
up-to-date.

.. _`tcw_set_intrg`:

tcw_set_intrg
=============

.. c:function:: void tcw_set_intrg(struct tcw *tcw, struct tcw *intrg_tcw)

    set the interrogate tcw address of a tcw

    :param tcw:
        the tcw address
    :type tcw: struct tcw \*

    :param intrg_tcw:
        the address of the interrogate tcw
    :type intrg_tcw: struct tcw \*

.. _`tcw_set_intrg.description`:

Description
-----------

Set the address of the interrogate tcw in the specified tcw.

.. _`tcw_set_data`:

tcw_set_data
============

.. c:function:: void tcw_set_data(struct tcw *tcw, void *data, int use_tidal)

    set data address and tida flag of a tcw

    :param tcw:
        the tcw address
    :type tcw: struct tcw \*

    :param data:
        the data address
    :type data: void \*

    :param use_tidal:
        zero of the data address specifies a contiguous block of data,
        non-zero if it specifies a list if tidaws.
    :type use_tidal: int

.. _`tcw_set_data.description`:

Description
-----------

Set the input/output data address of a tcw (depending on the value of the
r-flag and w-flag). If \ ``use_tidal``\  is non-zero, the corresponding tida flag
is set as well.

.. _`tcw_set_tccb`:

tcw_set_tccb
============

.. c:function:: void tcw_set_tccb(struct tcw *tcw, struct tccb *tccb)

    set tccb address of a tcw

    :param tcw:
        the tcw address
    :type tcw: struct tcw \*

    :param tccb:
        the tccb address
    :type tccb: struct tccb \*

.. _`tcw_set_tccb.description`:

Description
-----------

Set the address of the tccb in the specified tcw.

.. _`tcw_set_tsb`:

tcw_set_tsb
===========

.. c:function:: void tcw_set_tsb(struct tcw *tcw, struct tsb *tsb)

    set tsb address of a tcw

    :param tcw:
        the tcw address
    :type tcw: struct tcw \*

    :param tsb:
        the tsb address
    :type tsb: struct tsb \*

.. _`tcw_set_tsb.description`:

Description
-----------

Set the address of the tsb in the specified tcw.

.. _`tccb_init`:

tccb_init
=========

.. c:function:: void tccb_init(struct tccb *tccb, size_t size, u32 sac)

    initialize tccb

    :param tccb:
        the tccb address
    :type tccb: struct tccb \*

    :param size:
        the maximum size of the tccb
    :type size: size_t

    :param sac:
        the service-action-code to be user
    :type sac: u32

.. _`tccb_init.description`:

Description
-----------

Initialize the header of the specified tccb by resetting all values to zero
and filling in defaults for format, sac and initial tcal fields.

.. _`tsb_init`:

tsb_init
========

.. c:function:: void tsb_init(struct tsb *tsb)

    initialize tsb

    :param tsb:
        the tsb address
    :type tsb: struct tsb \*

.. _`tsb_init.description`:

Description
-----------

Initialize the specified tsb by resetting all values to zero.

.. _`tccb_add_dcw`:

tccb_add_dcw
============

.. c:function:: struct dcw *tccb_add_dcw(struct tccb *tccb, size_t tccb_size, u8 cmd, u8 flags, void *cd, u8 cd_count, u32 count)

    add a dcw to the tccb

    :param tccb:
        the tccb address
    :type tccb: struct tccb \*

    :param tccb_size:
        the maximum tccb size
    :type tccb_size: size_t

    :param cmd:
        the dcw command
    :type cmd: u8

    :param flags:
        flags for the dcw
    :type flags: u8

    :param cd:
        pointer to control data for this dcw or NULL if none is required
    :type cd: void \*

    :param cd_count:
        number of control data bytes for this dcw
    :type cd_count: u8

    :param count:
        number of data bytes for this dcw
    :type count: u32

.. _`tccb_add_dcw.description`:

Description
-----------

Add a new dcw to the specified tccb by writing the dcw information specified
by \ ``cmd``\ , \ ``flags``\ , \ ``cd``\ , \ ``cd_count``\  and \ ``count``\  to the tca of the tccb. Return
a pointer to the newly added dcw on success or -%ENOSPC if the new dcw
would exceed the available space as defined by \ ``tccb_size``\ .

.. _`tccb_add_dcw.note`:

Note
----

the tcal field of the tccb header will be updates to reflect added
content.

.. _`tcw_add_tidaw`:

tcw_add_tidaw
=============

.. c:function:: struct tidaw *tcw_add_tidaw(struct tcw *tcw, int num_tidaws, u8 flags, void *addr, u32 count)

    add a tidaw to a tcw

    :param tcw:
        the tcw address
    :type tcw: struct tcw \*

    :param num_tidaws:
        the current number of tidaws
    :type num_tidaws: int

    :param flags:
        flags for the new tidaw
    :type flags: u8

    :param addr:
        address value for the new tidaw
    :type addr: void \*

    :param count:
        count value for the new tidaw
    :type count: u32

.. _`tcw_add_tidaw.description`:

Description
-----------

Add a new tidaw to the input/output data tidaw-list of the specified tcw
(depending on the value of the r-flag and w-flag) and return a pointer to
the new tidaw.

.. _`tcw_add_tidaw.note`:

Note
----

the tidaw-list is assumed to be contiguous with no ttics. The caller
must ensure that there is enough space for the new tidaw. The last-tidaw
flag for the last tidaw in the list will be set by tcw_finalize.

.. This file was automatic generated / don't edit.

