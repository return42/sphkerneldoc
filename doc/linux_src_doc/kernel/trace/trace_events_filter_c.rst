.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/trace_events_filter.c

.. _`filter_parse_regex`:

filter_parse_regex
==================

.. c:function:: enum regex_type filter_parse_regex(char *buff, int len, char **search, int *not)

    parse a basic regex

    :param char \*buff:
        the raw regex

    :param int len:
        length of the regex

    :param char \*\*search:
        will point to the beginning of the string to compare

    :param int \*not:
        tell whether the match will have to be inverted

.. _`filter_parse_regex.description`:

Description
-----------

This passes in a buffer containing a regex and this function will
set search to point to the search part of the buffer and
return the type of search it is (see enum above).
This does modify buff.

Returns enum type.
search returns the pointer to use for comparison.
not returns 1 if buff started with a '!'
0 otherwise.

.. _`create_filter`:

create_filter
=============

.. c:function:: int create_filter(struct trace_event_call *call, char *filter_str, bool set_str, struct event_filter **filterp)

    create a filter for a trace_event_call

    :param struct trace_event_call \*call:
        trace_event_call to create a filter for

    :param char \*filter_str:
        filter string

    :param bool set_str:
        remember \ ``filter_str``\  and enable detailed error in filter

    :param struct event_filter \*\*filterp:
        out param for created filter (always updated on return)

.. _`create_filter.description`:

Description
-----------

Creates a filter for \ ``call``\  with \ ``filter_str``\ .  If \ ``set_str``\  is \ ``true``\ ,
\ ``filter_str``\  is copied and recorded in the new filter.

On success, returns 0 and \*\ ``filterp``\  points to the new filter.  On
failure, returns -errno and \*\ ``filterp``\  may point to \ ``NULL``\  or to a new
filter.  In the latter case, the returned filter contains error
information if \ ``set_str``\  is \ ``true``\  and the caller is responsible for
freeing it.

.. _`create_system_filter`:

create_system_filter
====================

.. c:function:: int create_system_filter(struct trace_subsystem_dir *dir, struct trace_array *tr, char *filter_str, struct event_filter **filterp)

    create a filter for an event_subsystem

    :param struct trace_subsystem_dir \*dir:
        *undescribed*

    :param struct trace_array \*tr:
        *undescribed*

    :param char \*filter_str:
        filter string

    :param struct event_filter \*\*filterp:
        out param for created filter (always updated on return)

.. _`create_system_filter.description`:

Description
-----------

Identical to \ :c:func:`create_filter`\  except that it creates a subsystem filter
and always remembers \ ``filter_str``\ .

.. This file was automatic generated / don't edit.

