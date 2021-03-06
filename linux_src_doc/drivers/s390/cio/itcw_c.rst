.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/itcw.c

.. _`itcw_get_tcw`:

itcw_get_tcw
============

.. c:function:: struct tcw *itcw_get_tcw(struct itcw *itcw)

    return pointer to tcw associated with the itcw

    :param itcw:
        address of the itcw
    :type itcw: struct itcw \*

.. _`itcw_get_tcw.description`:

Description
-----------

Return pointer to the tcw associated with the itcw.

.. _`itcw_calc_size`:

itcw_calc_size
==============

.. c:function:: size_t itcw_calc_size(int intrg, int max_tidaws, int intrg_max_tidaws)

    return the size of an itcw with the given parameters

    :param intrg:
        if non-zero, add an interrogate tcw
    :type intrg: int

    :param max_tidaws:
        maximum number of tidaws to be used for data addressing or zero
        if no tida is to be used.
    :type max_tidaws: int

    :param intrg_max_tidaws:
        maximum number of tidaws to be used for data addressing
        by the interrogate tcw, if specified
    :type intrg_max_tidaws: int

.. _`itcw_calc_size.description`:

Description
-----------

Calculate and return the number of bytes required to hold an itcw with the
given parameters and assuming tccbs with maximum size.

Note that the resulting size also contains bytes needed for alignment
padding as well as padding to ensure that data structures don't cross a
4k-boundary where required.

.. _`itcw_init`:

itcw_init
=========

.. c:function:: struct itcw *itcw_init(void *buffer, size_t size, int op, int intrg, int max_tidaws, int intrg_max_tidaws)

    initialize incremental tcw data structure

    :param buffer:
        address of buffer to use for data structures
    :type buffer: void \*

    :param size:
        number of bytes in buffer
    :type size: size_t

    :param op:
        \ ``ITCW_OP_READ``\  for a read operation tcw, \ ``ITCW_OP_WRITE``\  for a write
        operation tcw
    :type op: int

    :param intrg:
        if non-zero, add and initialize an interrogate tcw
    :type intrg: int

    :param max_tidaws:
        maximum number of tidaws to be used for data addressing or zero
        if no tida is to be used.
    :type max_tidaws: int

    :param intrg_max_tidaws:
        maximum number of tidaws to be used for data addressing
        by the interrogate tcw, if specified
    :type intrg_max_tidaws: int

.. _`itcw_init.description`:

Description
-----------

Prepare the specified buffer to be used as an incremental tcw, i.e. a
helper data structure that can be used to construct a valid tcw by
successive calls to other helper functions. Note: the buffer needs to be
located below the 2G address limit. The resulting tcw has the following

.. _`itcw_init.restrictions`:

restrictions
------------

- no tccb tidal
- input/output tidal is contiguous (no ttic)
- total data should not exceed 4k
- tcw specifies either read or write operation

On success, return pointer to the resulting incremental tcw data structure,
ERR_PTR otherwise.

.. _`itcw_add_dcw`:

itcw_add_dcw
============

.. c:function:: struct dcw *itcw_add_dcw(struct itcw *itcw, u8 cmd, u8 flags, void *cd, u8 cd_count, u32 count)

    add a dcw to the itcw

    :param itcw:
        address of the itcw
    :type itcw: struct itcw \*

    :param cmd:
        the dcw command
    :type cmd: u8

    :param flags:
        flags for the dcw
    :type flags: u8

    :param cd:
        address of control data for this dcw or NULL if none is required
    :type cd: void \*

    :param cd_count:
        number of control data bytes for this dcw
    :type cd_count: u8

    :param count:
        number of data bytes for this dcw
    :type count: u32

.. _`itcw_add_dcw.description`:

Description
-----------

Add a new dcw to the specified itcw by writing the dcw information specified
by \ ``cmd``\ , \ ``flags``\ , \ ``cd``\ , \ ``cd_count``\  and \ ``count``\  to the tca of the tccb. Return
a pointer to the newly added dcw on success or -%ENOSPC if the new dcw
would exceed the available space.

.. _`itcw_add_dcw.note`:

Note
----

the tcal field of the tccb header will be updated to reflect added
content.

.. _`itcw_add_tidaw`:

itcw_add_tidaw
==============

.. c:function:: struct tidaw *itcw_add_tidaw(struct itcw *itcw, u8 flags, void *addr, u32 count)

    add a tidaw to the itcw

    :param itcw:
        address of the itcw
    :type itcw: struct itcw \*

    :param flags:
        flags for the new tidaw
    :type flags: u8

    :param addr:
        address value for the new tidaw
    :type addr: void \*

    :param count:
        count value for the new tidaw
    :type count: u32

.. _`itcw_add_tidaw.description`:

Description
-----------

Add a new tidaw to the input/output data tidaw-list of the specified itcw
(depending on the value of the r-flag and w-flag). Return a pointer to
the new tidaw on success or -%ENOSPC if the new tidaw would exceed the
available space.

.. _`itcw_add_tidaw.note`:

Note
----

TTIC tidaws are automatically added when needed, so explicitly calling
this interface with the TTIC flag is not supported. The last-tidaw flag
for the last tidaw in the list will be set by itcw_finalize.

.. _`itcw_set_data`:

itcw_set_data
=============

.. c:function:: void itcw_set_data(struct itcw *itcw, void *addr, int use_tidal)

    set data address and tida flag of the itcw

    :param itcw:
        address of the itcw
    :type itcw: struct itcw \*

    :param addr:
        the data address
    :type addr: void \*

    :param use_tidal:
        zero of the data address specifies a contiguous block of data,
        non-zero if it specifies a list if tidaws.
    :type use_tidal: int

.. _`itcw_set_data.description`:

Description
-----------

Set the input/output data address of the itcw (depending on the value of the
r-flag and w-flag). If \ ``use_tidal``\  is non-zero, the corresponding tida flag
is set as well.

.. _`itcw_finalize`:

itcw_finalize
=============

.. c:function:: void itcw_finalize(struct itcw *itcw)

    calculate length and count fields of the itcw

    :param itcw:
        address of the itcw
    :type itcw: struct itcw \*

.. _`itcw_finalize.description`:

Description
-----------

Calculate tcw input-/output-count and tccbl fields and add a tcat the tccb.
In case input- or output-tida is used, the tidaw-list must be stored in
continuous storage (no ttic). The tcal field in the tccb must be
up-to-date.

.. This file was automatic generated / don't edit.

