.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/trace_events_filter.c

.. _`update_preds`:

update_preds
============

.. c:function:: void update_preds(struct prog_entry *prog, int N, int invert)

    assign a program entry a label target

    :param prog:
        The program array
    :type prog: struct prog_entry \*

    :param N:
        The index of the current entry in \ ``prog``\ 
    :type N: int

    :param invert:
        *undescribed*
    :type invert: int

.. _`update_preds.description`:

Description
-----------

The program entry at \ ``N``\  has a target that points to the index of a program
entry that can have its target and when_to_branch fields updated.
Update the current program entry denoted by index \ ``N``\  target field to be
that of the updated entry. This will denote the entry to update if
we are processing an "\|\|" after an "&&"

.. _`filter_parse_regex`:

filter_parse_regex
==================

.. c:function:: enum regex_type filter_parse_regex(char *buff, int len, char **search, int *not)

    parse a basic regex

    :param buff:
        the raw regex
    :type buff: char \*

    :param len:
        length of the regex
    :type len: int

    :param search:
        will point to the beginning of the string to compare
    :type search: char \*\*

    :param not:
        tell whether the match will have to be inverted
    :type not: int \*

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

.. c:function:: int create_filter(struct trace_event_call *call, char *filter_string, bool set_str, struct event_filter **filterp)

    create a filter for a trace_event_call

    :param call:
        trace_event_call to create a filter for
    :type call: struct trace_event_call \*

    :param filter_string:
        *undescribed*
    :type filter_string: char \*

    :param set_str:
        remember \ ``filter_str``\  and enable detailed error in filter
    :type set_str: bool

    :param filterp:
        out param for created filter (always updated on return)
        Must be a pointer that references a NULL pointer.
    :type filterp: struct event_filter \*\*

.. _`create_filter.description`:

Description
-----------

Creates a filter for \ ``call``\  with \ ``filter_str``\ .  If \ ``set_str``\  is \ ``true``\ ,
\ ``filter_str``\  is copied and recorded in the new filter.

On success, returns 0 and \*@filterp points to the new filter.  On
failure, returns -errno and \*@filterp may point to \ ``NULL``\  or to a new
filter.  In the latter case, the returned filter contains error
information if \ ``set_str``\  is \ ``true``\  and the caller is responsible for
freeing it.

.. _`create_system_filter`:

create_system_filter
====================

.. c:function:: int create_system_filter(struct trace_subsystem_dir *dir, struct trace_array *tr, char *filter_str, struct event_filter **filterp)

    create a filter for an event_subsystem

    :param dir:
        *undescribed*
    :type dir: struct trace_subsystem_dir \*

    :param tr:
        *undescribed*
    :type tr: struct trace_array \*

    :param filter_str:
        filter string
    :type filter_str: char \*

    :param filterp:
        out param for created filter (always updated on return)
    :type filterp: struct event_filter \*\*

.. _`create_system_filter.description`:

Description
-----------

Identical to \ :c:func:`create_filter`\  except that it creates a subsystem filter
and always remembers \ ``filter_str``\ .

.. This file was automatic generated / don't edit.

