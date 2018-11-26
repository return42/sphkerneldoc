.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/lib/traceevent/parse-filter.c

.. _`tep_filter_alloc`:

tep_filter_alloc
================

.. c:function:: struct tep_event_filter *tep_filter_alloc(struct tep_handle *pevent)

    create a new event filter

    :param pevent:
        The pevent that this filter is associated with
    :type pevent: struct tep_handle \*

.. _`tep_filter_add_filter_str`:

tep_filter_add_filter_str
=========================

.. c:function:: enum tep_errno tep_filter_add_filter_str(struct tep_event_filter *filter, const char *filter_str)

    add a new filter

    :param filter:
        the event filter to add to
    :type filter: struct tep_event_filter \*

    :param filter_str:
        the filter string that contains the filter
    :type filter_str: const char \*

.. _`tep_filter_add_filter_str.description`:

Description
-----------

Returns 0 if the filter was successfully added or a
negative error code.  Use \ :c:func:`tep_filter_strerror`\  to see
actual error message in case of error.

.. _`tep_filter_strerror`:

tep_filter_strerror
===================

.. c:function:: int tep_filter_strerror(struct tep_event_filter *filter, enum tep_errno err, char *buf, size_t buflen)

    fill error message in a buffer

    :param filter:
        the event filter contains error
    :type filter: struct tep_event_filter \*

    :param err:
        the error code
    :type err: enum tep_errno

    :param buf:
        the buffer to be filled in
    :type buf: char \*

    :param buflen:
        the size of the buffer
    :type buflen: size_t

.. _`tep_filter_strerror.description`:

Description
-----------

Returns 0 if message was filled successfully, -1 if error

.. _`tep_filter_remove_event`:

tep_filter_remove_event
=======================

.. c:function:: int tep_filter_remove_event(struct tep_event_filter *filter, int event_id)

    remove a filter for an event

    :param filter:
        the event filter to remove from
    :type filter: struct tep_event_filter \*

    :param event_id:
        the event to remove a filter for
    :type event_id: int

.. _`tep_filter_remove_event.description`:

Description
-----------

Removes the filter saved for an event defined by \ ``event_id``\ 
from the \ ``filter``\ .

.. _`tep_filter_remove_event.returns-1`:

Returns 1
---------

if an event was removed
0: if the event was not found

.. _`tep_filter_reset`:

tep_filter_reset
================

.. c:function:: void tep_filter_reset(struct tep_event_filter *filter)

    clear all filters in a filter

    :param filter:
        the event filter to reset
    :type filter: struct tep_event_filter \*

.. _`tep_filter_reset.description`:

Description
-----------

Removes all filters from a filter and resets it.

.. _`tep_filter_copy`:

tep_filter_copy
===============

.. c:function:: int tep_filter_copy(struct tep_event_filter *dest, struct tep_event_filter *source)

    copy a filter using another filter \ ``dest``\  - the filter to copy to \ ``source``\  - the filter to copy from

    :param dest:
        *undescribed*
    :type dest: struct tep_event_filter \*

    :param source:
        *undescribed*
    :type source: struct tep_event_filter \*

.. _`tep_filter_copy.description`:

Description
-----------

Returns 0 on success and -1 if not all filters were copied

.. _`tep_update_trivial`:

tep_update_trivial
==================

.. c:function:: int tep_update_trivial(struct tep_event_filter *dest, struct tep_event_filter *source, enum tep_filter_trivial_type type)

    update the trivial filters with the given filter \ ``dest``\  - the filter to update \ ``source``\  - the filter as the source of the update \ ``type``\  - the type of trivial filter to update.

    :param dest:
        *undescribed*
    :type dest: struct tep_event_filter \*

    :param source:
        *undescribed*
    :type source: struct tep_event_filter \*

    :param type:
        *undescribed*
    :type type: enum tep_filter_trivial_type

.. _`tep_update_trivial.description`:

Description
-----------

Scan dest for trivial events matching \ ``type``\  to replace with the source.

Returns 0 on success and -1 if there was a problem updating, but
events may have still been updated on error.

.. _`tep_filter_clear_trivial`:

tep_filter_clear_trivial
========================

.. c:function:: int tep_filter_clear_trivial(struct tep_event_filter *filter, enum tep_filter_trivial_type type)

    clear TRUE and FALSE filters

    :param filter:
        the filter to remove trivial filters from
    :type filter: struct tep_event_filter \*

    :param type:
        remove only true, false, or both
    :type type: enum tep_filter_trivial_type

.. _`tep_filter_clear_trivial.description`:

Description
-----------

Removes filters that only contain a TRUE or FALES boolean arg.

Returns 0 on success and -1 if there was a problem.

.. _`tep_filter_event_has_trivial`:

tep_filter_event_has_trivial
============================

.. c:function:: int tep_filter_event_has_trivial(struct tep_event_filter *filter, int event_id, enum tep_filter_trivial_type type)

    return true event contains trivial filter

    :param filter:
        the filter with the information
    :type filter: struct tep_event_filter \*

    :param event_id:
        the id of the event to test
    :type event_id: int

    :param type:
        trivial type to test for (TRUE, FALSE, EITHER)
    :type type: enum tep_filter_trivial_type

.. _`tep_filter_event_has_trivial.description`:

Description
-----------

Returns 1 if the event contains a matching trivial type
otherwise 0.

.. _`tep_event_filtered`:

tep_event_filtered
==================

.. c:function:: int tep_event_filtered(struct tep_event_filter *filter, int event_id)

    return true if event has filter

    :param filter:
        filter struct with filter information
    :type filter: struct tep_event_filter \*

    :param event_id:
        event id to test if filter exists
    :type event_id: int

.. _`tep_event_filtered.description`:

Description
-----------

Returns 1 if filter found for \ ``event_id``\ 
otherwise 0;

.. _`tep_filter_match`:

tep_filter_match
================

.. c:function:: enum tep_errno tep_filter_match(struct tep_event_filter *filter, struct tep_record *record)

    test if a record matches a filter

    :param filter:
        filter struct with filter information
    :type filter: struct tep_event_filter \*

    :param record:
        the record to test against the filter
    :type record: struct tep_record \*

.. _`tep_filter_match.return`:

Return
------

match result or error code (prefixed with TEP_ERRNO__)
FILTER_MATCH - filter found for event and \ ``record``\  matches
FILTER_MISS  - filter found for event and \ ``record``\  does not match
FILTER_NOT_FOUND - no filter found for \ ``record``\ 's event
NO_FILTER - if no filters exist
otherwise - error occurred during test

.. _`tep_filter_make_string`:

tep_filter_make_string
======================

.. c:function:: char *tep_filter_make_string(struct tep_event_filter *filter, int event_id)

    return a string showing the filter

    :param filter:
        filter struct with filter information
    :type filter: struct tep_event_filter \*

    :param event_id:
        the event id to return the filter string with
    :type event_id: int

.. _`tep_filter_make_string.description`:

Description
-----------

Returns a string that displays the filter contents.
This string must be freed with free(str).
NULL is returned if no filter is found or allocation failed.

.. _`tep_filter_compare`:

tep_filter_compare
==================

.. c:function:: int tep_filter_compare(struct tep_event_filter *filter1, struct tep_event_filter *filter2)

    compare two filters and return if they are the same

    :param filter1:
        Filter to compare with \ ``filter2``\ 
    :type filter1: struct tep_event_filter \*

    :param filter2:
        Filter to compare with \ ``filter1``\ 
    :type filter2: struct tep_event_filter \*

.. _`tep_filter_compare.return`:

Return
------

1 if the two filters hold the same content.
0 if they do not.

.. This file was automatic generated / don't edit.

