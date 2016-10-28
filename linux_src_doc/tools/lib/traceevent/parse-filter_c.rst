.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/lib/traceevent/parse-filter.c

.. _`pevent_filter_alloc`:

pevent_filter_alloc
===================

.. c:function:: struct event_filter *pevent_filter_alloc(struct pevent *pevent)

    create a new event filter

    :param struct pevent \*pevent:
        The pevent that this filter is associated with

.. _`pevent_filter_add_filter_str`:

pevent_filter_add_filter_str
============================

.. c:function:: enum pevent_errno pevent_filter_add_filter_str(struct event_filter *filter, const char *filter_str)

    add a new filter

    :param struct event_filter \*filter:
        the event filter to add to

    :param const char \*filter_str:
        the filter string that contains the filter

.. _`pevent_filter_add_filter_str.description`:

Description
-----------

Returns 0 if the filter was successfully added or a
negative error code.  Use \ :c:func:`pevent_filter_strerror`\  to see
actual error message in case of error.

.. _`pevent_filter_strerror`:

pevent_filter_strerror
======================

.. c:function:: int pevent_filter_strerror(struct event_filter *filter, enum pevent_errno err, char *buf, size_t buflen)

    fill error message in a buffer

    :param struct event_filter \*filter:
        the event filter contains error

    :param enum pevent_errno err:
        the error code

    :param char \*buf:
        the buffer to be filled in

    :param size_t buflen:
        the size of the buffer

.. _`pevent_filter_strerror.description`:

Description
-----------

Returns 0 if message was filled successfully, -1 if error

.. _`pevent_filter_remove_event`:

pevent_filter_remove_event
==========================

.. c:function:: int pevent_filter_remove_event(struct event_filter *filter, int event_id)

    remove a filter for an event

    :param struct event_filter \*filter:
        the event filter to remove from

    :param int event_id:
        the event to remove a filter for

.. _`pevent_filter_remove_event.description`:

Description
-----------

Removes the filter saved for an event defined by \ ``event_id``\ 
from the \ ``filter``\ .

.. _`pevent_filter_remove_event.returns-1`:

Returns 1
---------

if an event was removed
0: if the event was not found

.. _`pevent_filter_reset`:

pevent_filter_reset
===================

.. c:function:: void pevent_filter_reset(struct event_filter *filter)

    clear all filters in a filter

    :param struct event_filter \*filter:
        the event filter to reset

.. _`pevent_filter_reset.description`:

Description
-----------

Removes all filters from a filter and resets it.

.. _`pevent_filter_copy`:

pevent_filter_copy
==================

.. c:function:: int pevent_filter_copy(struct event_filter *dest, struct event_filter *source)

    copy a filter using another filter \ ``dest``\  - the filter to copy to \ ``source``\  - the filter to copy from

    :param struct event_filter \*dest:
        *undescribed*

    :param struct event_filter \*source:
        *undescribed*

.. _`pevent_filter_copy.description`:

Description
-----------

Returns 0 on success and -1 if not all filters were copied

.. _`pevent_update_trivial`:

pevent_update_trivial
=====================

.. c:function:: int pevent_update_trivial(struct event_filter *dest, struct event_filter *source, enum filter_trivial_type type)

    update the trivial filters with the given filter \ ``dest``\  - the filter to update \ ``source``\  - the filter as the source of the update \ ``type``\  - the type of trivial filter to update.

    :param struct event_filter \*dest:
        *undescribed*

    :param struct event_filter \*source:
        *undescribed*

    :param enum filter_trivial_type type:
        *undescribed*

.. _`pevent_update_trivial.description`:

Description
-----------

Scan dest for trivial events matching \ ``type``\  to replace with the source.

Returns 0 on success and -1 if there was a problem updating, but
events may have still been updated on error.

.. _`pevent_filter_clear_trivial`:

pevent_filter_clear_trivial
===========================

.. c:function:: int pevent_filter_clear_trivial(struct event_filter *filter, enum filter_trivial_type type)

    clear TRUE and FALSE filters

    :param struct event_filter \*filter:
        the filter to remove trivial filters from

    :param enum filter_trivial_type type:
        remove only true, false, or both

.. _`pevent_filter_clear_trivial.description`:

Description
-----------

Removes filters that only contain a TRUE or FALES boolean arg.

Returns 0 on success and -1 if there was a problem.

.. _`pevent_filter_event_has_trivial`:

pevent_filter_event_has_trivial
===============================

.. c:function:: int pevent_filter_event_has_trivial(struct event_filter *filter, int event_id, enum filter_trivial_type type)

    return true event contains trivial filter

    :param struct event_filter \*filter:
        the filter with the information

    :param int event_id:
        the id of the event to test

    :param enum filter_trivial_type type:
        trivial type to test for (TRUE, FALSE, EITHER)

.. _`pevent_filter_event_has_trivial.description`:

Description
-----------

Returns 1 if the event contains a matching trivial type
otherwise 0.

.. _`pevent_event_filtered`:

pevent_event_filtered
=====================

.. c:function:: int pevent_event_filtered(struct event_filter *filter, int event_id)

    return true if event has filter

    :param struct event_filter \*filter:
        filter struct with filter information

    :param int event_id:
        event id to test if filter exists

.. _`pevent_event_filtered.description`:

Description
-----------

Returns 1 if filter found for \ ``event_id``\ 
otherwise 0;

.. _`pevent_filter_match`:

pevent_filter_match
===================

.. c:function:: enum pevent_errno pevent_filter_match(struct event_filter *filter, struct pevent_record *record)

    test if a record matches a filter

    :param struct event_filter \*filter:
        filter struct with filter information

    :param struct pevent_record \*record:
        the record to test against the filter

.. _`pevent_filter_match.return`:

Return
------

match result or error code (prefixed with PEVENT_ERRNO__)
FILTER_MATCH - filter found for event and \ ``record``\  matches
FILTER_MISS  - filter found for event and \ ``record``\  does not match
FILTER_NOT_FOUND - no filter found for \ ``record``\ 's event
NO_FILTER - if no filters exist
otherwise - error occurred during test

.. _`pevent_filter_make_string`:

pevent_filter_make_string
=========================

.. c:function:: char *pevent_filter_make_string(struct event_filter *filter, int event_id)

    return a string showing the filter

    :param struct event_filter \*filter:
        filter struct with filter information

    :param int event_id:
        the event id to return the filter string with

.. _`pevent_filter_make_string.description`:

Description
-----------

Returns a string that displays the filter contents.
This string must be freed with free(str).
NULL is returned if no filter is found or allocation failed.

.. _`pevent_filter_compare`:

pevent_filter_compare
=====================

.. c:function:: int pevent_filter_compare(struct event_filter *filter1, struct event_filter *filter2)

    compare two filters and return if they are the same

    :param struct event_filter \*filter1:
        Filter to compare with \ ``filter2``\ 

    :param struct event_filter \*filter2:
        Filter to compare with \ ``filter1``\ 

.. _`pevent_filter_compare.return`:

Return
------

1 if the two filters hold the same content.
0 if they do not.

.. This file was automatic generated / don't edit.

