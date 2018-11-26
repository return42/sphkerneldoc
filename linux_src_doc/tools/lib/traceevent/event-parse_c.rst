.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/lib/traceevent/event-parse.c

.. _`tep_buffer_init`:

tep_buffer_init
===============

.. c:function:: void tep_buffer_init(const char *buf, unsigned long long size)

    init buffer for parsing

    :param buf:
        buffer to parse
    :type buf: const char \*

    :param size:
        the size of the buffer
    :type size: unsigned long long

.. _`tep_buffer_init.description`:

Description
-----------

For use with \ :c:func:`tep_read_token`\ , this initializes the internal
buffer that \ :c:func:`tep_read_token`\  will parse.

.. _`tep_pid_is_registered`:

tep_pid_is_registered
=====================

.. c:function:: int tep_pid_is_registered(struct tep_handle *pevent, int pid)

    return if a pid has a cmdline registered

    :param pevent:
        handle for the pevent
    :type pevent: struct tep_handle \*

    :param pid:
        The pid to check if it has a cmdline registered with.
    :type pid: int

.. _`tep_pid_is_registered.description`:

Description
-----------

Returns 1 if the pid has a cmdline mapped to it
0 otherwise.

.. _`tep_register_comm`:

tep_register_comm
=================

.. c:function:: int tep_register_comm(struct tep_handle *pevent, const char *comm, int pid)

    register a pid / comm mapping

    :param pevent:
        handle for the pevent
    :type pevent: struct tep_handle \*

    :param comm:
        the command line to register
    :type comm: const char \*

    :param pid:
        the pid to map the command line to
    :type pid: int

.. _`tep_register_comm.description`:

Description
-----------

This adds a mapping to search for command line names with
a given pid. The comm is duplicated.

.. _`tep_set_function_resolver`:

tep_set_function_resolver
=========================

.. c:function:: int tep_set_function_resolver(struct tep_handle *pevent, tep_func_resolver_t *func, void *priv)

    set an alternative function resolver

    :param pevent:
        handle for the pevent
    :type pevent: struct tep_handle \*

    :param func:
        *undescribed*
    :type func: tep_func_resolver_t \*

    :param priv:
        resolver function private state.
    :type priv: void \*

.. _`tep_set_function_resolver.description`:

Description
-----------

Some tools may have already a way to resolve kernel functions, allow them to
keep using it instead of duplicating all the entries inside
pevent->funclist.

.. _`tep_reset_function_resolver`:

tep_reset_function_resolver
===========================

.. c:function:: void tep_reset_function_resolver(struct tep_handle *pevent)

    reset alternative function resolver

    :param pevent:
        handle for the pevent
    :type pevent: struct tep_handle \*

.. _`tep_reset_function_resolver.description`:

Description
-----------

Stop using whatever alternative resolver was set, use the default
one instead.

.. _`tep_find_function`:

tep_find_function
=================

.. c:function:: const char *tep_find_function(struct tep_handle *pevent, unsigned long long addr)

    find a function by a given address

    :param pevent:
        handle for the pevent
    :type pevent: struct tep_handle \*

    :param addr:
        the address to find the function with
    :type addr: unsigned long long

.. _`tep_find_function.description`:

Description
-----------

Returns a pointer to the function stored that has the given
address. Note, the address does not have to be exact, it
will select the function that would contain the address.

.. _`tep_find_function_address`:

tep_find_function_address
=========================

.. c:function:: unsigned long long tep_find_function_address(struct tep_handle *pevent, unsigned long long addr)

    find a function address by a given address

    :param pevent:
        handle for the pevent
    :type pevent: struct tep_handle \*

    :param addr:
        the address to find the function with
    :type addr: unsigned long long

.. _`tep_find_function_address.description`:

Description
-----------

Returns the address the function starts at. This can be used in
conjunction with tep_find_function to print both the function
name and the function offset.

.. _`tep_register_function`:

tep_register_function
=====================

.. c:function:: int tep_register_function(struct tep_handle *pevent, char *func, unsigned long long addr, char *mod)

    register a function with a given address

    :param pevent:
        handle for the pevent
    :type pevent: struct tep_handle \*

    :param func:
        *undescribed*
    :type func: char \*

    :param addr:
        the address the function starts at
    :type addr: unsigned long long

    :param mod:
        the kernel module the function may be in (NULL for none)
    :type mod: char \*

.. _`tep_register_function.description`:

Description
-----------

This registers a function name with an address and module.
The \ ``func``\  passed in is duplicated.

.. _`tep_print_funcs`:

tep_print_funcs
===============

.. c:function:: void tep_print_funcs(struct tep_handle *pevent)

    print out the stored functions

    :param pevent:
        handle for the pevent
    :type pevent: struct tep_handle \*

.. _`tep_print_funcs.description`:

Description
-----------

This prints out the stored functions.

.. _`tep_register_print_string`:

tep_register_print_string
=========================

.. c:function:: int tep_register_print_string(struct tep_handle *pevent, const char *fmt, unsigned long long addr)

    register a string by its address

    :param pevent:
        handle for the pevent
    :type pevent: struct tep_handle \*

    :param fmt:
        the string format to register
    :type fmt: const char \*

    :param addr:
        the address the string was located at
    :type addr: unsigned long long

.. _`tep_register_print_string.description`:

Description
-----------

This registers a string by the address it was stored in the kernel.
The \ ``fmt``\  passed in is duplicated.

.. _`tep_print_printk`:

tep_print_printk
================

.. c:function:: void tep_print_printk(struct tep_handle *pevent)

    print out the stored strings

    :param pevent:
        handle for the pevent
    :type pevent: struct tep_handle \*

.. _`tep_print_printk.description`:

Description
-----------

This prints the string formats that were stored.

.. _`tep_peek_char`:

tep_peek_char
=============

.. c:function:: int tep_peek_char( void)

    peek at the next character that will be read

    :param void:
        no arguments
    :type void: 

.. _`tep_peek_char.description`:

Description
-----------

Returns the next character read, or -1 if end of buffer.

.. _`tep_read_token`:

tep_read_token
==============

.. c:function:: enum tep_event_type tep_read_token(char **tok)

    access to utilites to use the pevent parser

    :param tok:
        The token to return
    :type tok: char \*\*

.. _`tep_read_token.description`:

Description
-----------

This will parse tokens from the string given by
\ :c:func:`tep_init_data`\ .

Returns the token type.

.. _`tep_free_token`:

tep_free_token
==============

.. c:function:: void tep_free_token(char *token)

    free a token returned by tep_read_token

    :param token:
        the token to free
    :type token: char \*

.. _`tep_find_common_field`:

tep_find_common_field
=====================

.. c:function:: struct tep_format_field *tep_find_common_field(struct tep_event_format *event, const char *name)

    return a common field by event

    :param event:
        handle for the event
    :type event: struct tep_event_format \*

    :param name:
        the name of the common field to return
    :type name: const char \*

.. _`tep_find_common_field.description`:

Description
-----------

Returns a common field from the event by the given \ ``name``\ .
This only searchs the common fields and not all field.

.. _`tep_find_field`:

tep_find_field
==============

.. c:function:: struct tep_format_field *tep_find_field(struct tep_event_format *event, const char *name)

    find a non-common field

    :param event:
        handle for the event
    :type event: struct tep_event_format \*

    :param name:
        the name of the non-common field
    :type name: const char \*

.. _`tep_find_field.description`:

Description
-----------

Returns a non-common field by the given \ ``name``\ .
This does not search common fields.

.. _`tep_find_any_field`:

tep_find_any_field
==================

.. c:function:: struct tep_format_field *tep_find_any_field(struct tep_event_format *event, const char *name)

    find any field by name

    :param event:
        handle for the event
    :type event: struct tep_event_format \*

    :param name:
        the name of the field
    :type name: const char \*

.. _`tep_find_any_field.description`:

Description
-----------

Returns a field by the given \ ``name``\ .
This searchs the common field names first, then
the non-common ones if a common one was not found.

.. _`tep_read_number`:

tep_read_number
===============

.. c:function:: unsigned long long tep_read_number(struct tep_handle *pevent, const void *ptr, int size)

    read a number from data

    :param pevent:
        handle for the pevent
    :type pevent: struct tep_handle \*

    :param ptr:
        the raw data
    :type ptr: const void \*

    :param size:
        the size of the data that holds the number
    :type size: int

.. _`tep_read_number.description`:

Description
-----------

Returns the number (converted to host) from the
raw data.

.. _`tep_read_number_field`:

tep_read_number_field
=====================

.. c:function:: int tep_read_number_field(struct tep_format_field *field, const void *data, unsigned long long *value)

    read a number from data

    :param field:
        a handle to the field
    :type field: struct tep_format_field \*

    :param data:
        the raw data to read
    :type data: const void \*

    :param value:
        the value to place the number in
    :type value: unsigned long long \*

.. _`tep_read_number_field.description`:

Description
-----------

Reads raw data according to a field offset and size,
and translates it into \ ``value``\ .

Returns 0 on success, -1 otherwise.

.. _`tep_find_event`:

tep_find_event
==============

.. c:function:: struct tep_event_format *tep_find_event(struct tep_handle *pevent, int id)

    find an event by given id

    :param pevent:
        a handle to the pevent
    :type pevent: struct tep_handle \*

    :param id:
        the id of the event
    :type id: int

.. _`tep_find_event.description`:

Description
-----------

Returns an event that has a given \ ``id``\ .

.. _`tep_find_event_by_name`:

tep_find_event_by_name
======================

.. c:function:: struct tep_event_format *tep_find_event_by_name(struct tep_handle *pevent, const char *sys, const char *name)

    find an event by given name

    :param pevent:
        a handle to the pevent
    :type pevent: struct tep_handle \*

    :param sys:
        the system name to search for
    :type sys: const char \*

    :param name:
        the name of the event to search for
    :type name: const char \*

.. _`tep_find_event_by_name.description`:

Description
-----------

This returns an event with a given \ ``name``\  and under the system
\ ``sys``\ . If \ ``sys``\  is NULL the first event with \ ``name``\  is returned.

.. _`tep_data_lat_fmt`:

tep_data_lat_fmt
================

.. c:function:: void tep_data_lat_fmt(struct tep_handle *pevent, struct trace_seq *s, struct tep_record *record)

    parse the data for the latency format

    :param pevent:
        a handle to the pevent
    :type pevent: struct tep_handle \*

    :param s:
        the trace_seq to write to
    :type s: struct trace_seq \*

    :param record:
        the record to read from
    :type record: struct tep_record \*

.. _`tep_data_lat_fmt.description`:

Description
-----------

This parses out the Latency format (interrupts disabled,
need rescheduling, in hard/soft interrupt, preempt count
and lock depth) and places it into the trace_seq.

.. _`tep_data_type`:

tep_data_type
=============

.. c:function:: int tep_data_type(struct tep_handle *pevent, struct tep_record *rec)

    parse out the given event type

    :param pevent:
        a handle to the pevent
    :type pevent: struct tep_handle \*

    :param rec:
        the record to read from
    :type rec: struct tep_record \*

.. _`tep_data_type.description`:

Description
-----------

This returns the event id from the \ ``rec``\ .

.. _`tep_data_event_from_type`:

tep_data_event_from_type
========================

.. c:function:: struct tep_event_format *tep_data_event_from_type(struct tep_handle *pevent, int type)

    find the event by a given type

    :param pevent:
        a handle to the pevent
    :type pevent: struct tep_handle \*

    :param type:
        the type of the event.
    :type type: int

.. _`tep_data_event_from_type.description`:

Description
-----------

This returns the event form a given \ ``type``\ ;

.. _`tep_data_pid`:

tep_data_pid
============

.. c:function:: int tep_data_pid(struct tep_handle *pevent, struct tep_record *rec)

    parse the PID from record

    :param pevent:
        a handle to the pevent
    :type pevent: struct tep_handle \*

    :param rec:
        the record to parse
    :type rec: struct tep_record \*

.. _`tep_data_pid.description`:

Description
-----------

This returns the PID from a record.

.. _`tep_data_preempt_count`:

tep_data_preempt_count
======================

.. c:function:: int tep_data_preempt_count(struct tep_handle *pevent, struct tep_record *rec)

    parse the preempt count from the record

    :param pevent:
        a handle to the pevent
    :type pevent: struct tep_handle \*

    :param rec:
        the record to parse
    :type rec: struct tep_record \*

.. _`tep_data_preempt_count.description`:

Description
-----------

This returns the preempt count from a record.

.. _`tep_data_flags`:

tep_data_flags
==============

.. c:function:: int tep_data_flags(struct tep_handle *pevent, struct tep_record *rec)

    parse the latency flags from the record

    :param pevent:
        a handle to the pevent
    :type pevent: struct tep_handle \*

    :param rec:
        the record to parse
    :type rec: struct tep_record \*

.. _`tep_data_flags.description`:

Description
-----------

This returns the latency flags from a record.

Use trace_flag_type enum for the flags (see event-parse.h).

.. _`tep_data_comm_from_pid`:

tep_data_comm_from_pid
======================

.. c:function:: const char *tep_data_comm_from_pid(struct tep_handle *pevent, int pid)

    return the command line from PID

    :param pevent:
        a handle to the pevent
    :type pevent: struct tep_handle \*

    :param pid:
        the PID of the task to search for
    :type pid: int

.. _`tep_data_comm_from_pid.description`:

Description
-----------

This returns a pointer to the command line that has the given
\ ``pid``\ .

.. _`tep_data_pid_from_comm`:

tep_data_pid_from_comm
======================

.. c:function:: struct cmdline *tep_data_pid_from_comm(struct tep_handle *pevent, const char *comm, struct cmdline *next)

    return the pid from a given comm

    :param pevent:
        a handle to the pevent
    :type pevent: struct tep_handle \*

    :param comm:
        the cmdline to find the pid from
    :type comm: const char \*

    :param next:
        the cmdline structure to find the next comm
    :type next: struct cmdline \*

.. _`tep_data_pid_from_comm.description`:

Description
-----------

This returns the cmdline structure that holds a pid for a given
comm, or NULL if none found. As there may be more than one pid for
a given comm, the result of this call can be passed back into
a recurring call in the \ ``next``\  paramater, and then it will find the
next pid.
Also, it does a linear seach, so it may be slow.

.. _`tep_cmdline_pid`:

tep_cmdline_pid
===============

.. c:function:: int tep_cmdline_pid(struct tep_handle *pevent, struct cmdline *cmdline)

    return the pid associated to a given cmdline

    :param pevent:
        *undescribed*
    :type pevent: struct tep_handle \*

    :param cmdline:
        The cmdline structure to get the pid from
    :type cmdline: struct cmdline \*

.. _`tep_cmdline_pid.description`:

Description
-----------

Returns the pid for a give cmdline. If \ ``cmdline``\  is NULL, then
-1 is returned.

.. _`tep_event_info`:

tep_event_info
==============

.. c:function:: void tep_event_info(struct trace_seq *s, struct tep_event_format *event, struct tep_record *record)

    parse the data into the print format

    :param s:
        the trace_seq to write to
    :type s: struct trace_seq \*

    :param event:
        the handle to the event
    :type event: struct tep_event_format \*

    :param record:
        the record to read from
    :type record: struct tep_record \*

.. _`tep_event_info.description`:

Description
-----------

This parses the raw \ ``data``\  using the given \ ``event``\  information and
writes the print format into the trace_seq.

.. _`tep_find_event_by_record`:

tep_find_event_by_record
========================

.. c:function:: struct tep_event_format *tep_find_event_by_record(struct tep_handle *pevent, struct tep_record *record)

    return the event from a given record

    :param pevent:
        a handle to the pevent
    :type pevent: struct tep_handle \*

    :param record:
        The record to get the event from
    :type record: struct tep_record \*

.. _`tep_find_event_by_record.description`:

Description
-----------

Returns the associated event for a given record, or NULL if non is
is found.

.. _`tep_print_event_task`:

tep_print_event_task
====================

.. c:function:: void tep_print_event_task(struct tep_handle *pevent, struct trace_seq *s, struct tep_event_format *event, struct tep_record *record)

    Write the event task comm, pid and CPU

    :param pevent:
        a handle to the pevent
    :type pevent: struct tep_handle \*

    :param s:
        the trace_seq to write to
    :type s: struct trace_seq \*

    :param event:
        the handle to the record's event
    :type event: struct tep_event_format \*

    :param record:
        The record to get the event from
    :type record: struct tep_record \*

.. _`tep_print_event_task.description`:

Description
-----------

Writes the tasks comm, pid and CPU to \ ``s``\ .

.. _`tep_print_event_time`:

tep_print_event_time
====================

.. c:function:: void tep_print_event_time(struct tep_handle *pevent, struct trace_seq *s, struct tep_event_format *event, struct tep_record *record, bool use_trace_clock)

    Write the event timestamp

    :param pevent:
        a handle to the pevent
    :type pevent: struct tep_handle \*

    :param s:
        the trace_seq to write to
    :type s: struct trace_seq \*

    :param event:
        the handle to the record's event
    :type event: struct tep_event_format \*

    :param record:
        The record to get the event from
    :type record: struct tep_record \*

    :param use_trace_clock:
        Set to parse according to the \ ``pevent->trace_clock``\ 
    :type use_trace_clock: bool

.. _`tep_print_event_time.description`:

Description
-----------

Writes the timestamp of the record into \ ``s``\ .

.. _`tep_print_event_data`:

tep_print_event_data
====================

.. c:function:: void tep_print_event_data(struct tep_handle *pevent, struct trace_seq *s, struct tep_event_format *event, struct tep_record *record)

    Write the event data section

    :param pevent:
        a handle to the pevent
    :type pevent: struct tep_handle \*

    :param s:
        the trace_seq to write to
    :type s: struct trace_seq \*

    :param event:
        the handle to the record's event
    :type event: struct tep_event_format \*

    :param record:
        The record to get the event from
    :type record: struct tep_record \*

.. _`tep_print_event_data.description`:

Description
-----------

Writes the parsing of the record's data to \ ``s``\ .

.. _`tep_event_common_fields`:

tep_event_common_fields
=======================

.. c:function:: struct tep_format_field **tep_event_common_fields(struct tep_event_format *event)

    return a list of common fields for an event

    :param event:
        the event to return the common fields of.
    :type event: struct tep_event_format \*

.. _`tep_event_common_fields.description`:

Description
-----------

Returns an allocated array of fields. The last item in the array is NULL.
The array must be freed with \ :c:func:`free`\ .

.. _`tep_event_fields`:

tep_event_fields
================

.. c:function:: struct tep_format_field **tep_event_fields(struct tep_event_format *event)

    return a list of event specific fields for an event

    :param event:
        the event to return the fields of.
    :type event: struct tep_event_format \*

.. _`tep_event_fields.description`:

Description
-----------

Returns an allocated array of fields. The last item in the array is NULL.
The array must be freed with \ :c:func:`free`\ .

.. _`tep_parse_header_page`:

tep_parse_header_page
=====================

.. c:function:: int tep_parse_header_page(struct tep_handle *pevent, char *buf, unsigned long size, int long_size)

    parse the data stored in the header page

    :param pevent:
        the handle to the pevent
    :type pevent: struct tep_handle \*

    :param buf:
        the buffer storing the header page format string
    :type buf: char \*

    :param size:
        the size of \ ``buf``\ 
    :type size: unsigned long

    :param long_size:
        the long size to use if there is no header
    :type long_size: int

.. _`tep_parse_header_page.description`:

Description
-----------

This parses the header page format for information on the
ring buffer used. The \ ``buf``\  should be copied from

/sys/kernel/debug/tracing/events/header_page

.. _`__tep_parse_format`:

\__tep_parse_format
===================

.. c:function:: enum tep_errno __tep_parse_format(struct tep_event_format **eventp, struct tep_handle *pevent, const char *buf, unsigned long size, const char *sys)

    parse the event format

    :param eventp:
        *undescribed*
    :type eventp: struct tep_event_format \*\*

    :param pevent:
        *undescribed*
    :type pevent: struct tep_handle \*

    :param buf:
        the buffer storing the event format string
    :type buf: const char \*

    :param size:
        the size of \ ``buf``\ 
    :type size: unsigned long

    :param sys:
        the system the event belongs to
    :type sys: const char \*

.. _`__tep_parse_format.description`:

Description
-----------

This parses the event format and creates an event structure
to quickly parse raw data for a given event.

.. _`__tep_parse_format.these-files-currently-come-from`:

These files currently come from
-------------------------------


/sys/kernel/debug/tracing/events/.../.../format

.. _`tep_parse_format`:

tep_parse_format
================

.. c:function:: enum tep_errno tep_parse_format(struct tep_handle *pevent, struct tep_event_format **eventp, const char *buf, unsigned long size, const char *sys)

    parse the event format

    :param pevent:
        the handle to the pevent
    :type pevent: struct tep_handle \*

    :param eventp:
        returned format
    :type eventp: struct tep_event_format \*\*

    :param buf:
        the buffer storing the event format string
    :type buf: const char \*

    :param size:
        the size of \ ``buf``\ 
    :type size: unsigned long

    :param sys:
        the system the event belongs to
    :type sys: const char \*

.. _`tep_parse_format.description`:

Description
-----------

This parses the event format and creates an event structure
to quickly parse raw data for a given event.

.. _`tep_parse_format.these-files-currently-come-from`:

These files currently come from
-------------------------------


/sys/kernel/debug/tracing/events/.../.../format

.. _`tep_parse_event`:

tep_parse_event
===============

.. c:function:: enum tep_errno tep_parse_event(struct tep_handle *pevent, const char *buf, unsigned long size, const char *sys)

    parse the event format

    :param pevent:
        the handle to the pevent
    :type pevent: struct tep_handle \*

    :param buf:
        the buffer storing the event format string
    :type buf: const char \*

    :param size:
        the size of \ ``buf``\ 
    :type size: unsigned long

    :param sys:
        the system the event belongs to
    :type sys: const char \*

.. _`tep_parse_event.description`:

Description
-----------

This parses the event format and creates an event structure
to quickly parse raw data for a given event.

.. _`tep_parse_event.these-files-currently-come-from`:

These files currently come from
-------------------------------


/sys/kernel/debug/tracing/events/.../.../format

.. _`tep_get_field_raw`:

tep_get_field_raw
=================

.. c:function:: void *tep_get_field_raw(struct trace_seq *s, struct tep_event_format *event, const char *name, struct tep_record *record, int *len, int err)

    return the raw pointer into the data field

    :param s:
        The seq to print to on error
    :type s: struct trace_seq \*

    :param event:
        the event that the field is for
    :type event: struct tep_event_format \*

    :param name:
        The name of the field
    :type name: const char \*

    :param record:
        The record with the field name.
    :type record: struct tep_record \*

    :param len:
        place to store the field length.
    :type len: int \*

    :param err:
        print default error if failed.
    :type err: int

.. _`tep_get_field_raw.description`:

Description
-----------

Returns a pointer into record->data of the field and places
the length of the field in \ ``len``\ .

On failure, it returns NULL.

.. _`tep_get_field_val`:

tep_get_field_val
=================

.. c:function:: int tep_get_field_val(struct trace_seq *s, struct tep_event_format *event, const char *name, struct tep_record *record, unsigned long long *val, int err)

    find a field and return its value

    :param s:
        The seq to print to on error
    :type s: struct trace_seq \*

    :param event:
        the event that the field is for
    :type event: struct tep_event_format \*

    :param name:
        The name of the field
    :type name: const char \*

    :param record:
        The record with the field name.
    :type record: struct tep_record \*

    :param val:
        place to store the value of the field.
    :type val: unsigned long long \*

    :param err:
        print default error if failed.
    :type err: int

.. _`tep_get_field_val.description`:

Description
-----------

Returns 0 on success -1 on field not found.

.. _`tep_get_common_field_val`:

tep_get_common_field_val
========================

.. c:function:: int tep_get_common_field_val(struct trace_seq *s, struct tep_event_format *event, const char *name, struct tep_record *record, unsigned long long *val, int err)

    find a common field and return its value

    :param s:
        The seq to print to on error
    :type s: struct trace_seq \*

    :param event:
        the event that the field is for
    :type event: struct tep_event_format \*

    :param name:
        The name of the field
    :type name: const char \*

    :param record:
        The record with the field name.
    :type record: struct tep_record \*

    :param val:
        place to store the value of the field.
    :type val: unsigned long long \*

    :param err:
        print default error if failed.
    :type err: int

.. _`tep_get_common_field_val.description`:

Description
-----------

Returns 0 on success -1 on field not found.

.. _`tep_get_any_field_val`:

tep_get_any_field_val
=====================

.. c:function:: int tep_get_any_field_val(struct trace_seq *s, struct tep_event_format *event, const char *name, struct tep_record *record, unsigned long long *val, int err)

    find a any field and return its value

    :param s:
        The seq to print to on error
    :type s: struct trace_seq \*

    :param event:
        the event that the field is for
    :type event: struct tep_event_format \*

    :param name:
        The name of the field
    :type name: const char \*

    :param record:
        The record with the field name.
    :type record: struct tep_record \*

    :param val:
        place to store the value of the field.
    :type val: unsigned long long \*

    :param err:
        print default error if failed.
    :type err: int

.. _`tep_get_any_field_val.description`:

Description
-----------

Returns 0 on success -1 on field not found.

.. _`tep_print_num_field`:

tep_print_num_field
===================

.. c:function:: int tep_print_num_field(struct trace_seq *s, const char *fmt, struct tep_event_format *event, const char *name, struct tep_record *record, int err)

    print a field and a format

    :param s:
        The seq to print to
    :type s: struct trace_seq \*

    :param fmt:
        The printf format to print the field with.
    :type fmt: const char \*

    :param event:
        the event that the field is for
    :type event: struct tep_event_format \*

    :param name:
        The name of the field
    :type name: const char \*

    :param record:
        The record with the field name.
    :type record: struct tep_record \*

    :param err:
        print default error if failed.
    :type err: int

.. _`tep_print_num_field.return`:

Return
------

0 on success, -1 field not found, or 1 if buffer is full.

.. _`tep_print_func_field`:

tep_print_func_field
====================

.. c:function:: int tep_print_func_field(struct trace_seq *s, const char *fmt, struct tep_event_format *event, const char *name, struct tep_record *record, int err)

    print a field and a format for function pointers

    :param s:
        The seq to print to
    :type s: struct trace_seq \*

    :param fmt:
        The printf format to print the field with.
    :type fmt: const char \*

    :param event:
        the event that the field is for
    :type event: struct tep_event_format \*

    :param name:
        The name of the field
    :type name: const char \*

    :param record:
        The record with the field name.
    :type record: struct tep_record \*

    :param err:
        print default error if failed.
    :type err: int

.. _`tep_print_func_field.return`:

Return
------

0 on success, -1 field not found, or 1 if buffer is full.

.. _`tep_register_print_function`:

tep_register_print_function
===========================

.. c:function:: int tep_register_print_function(struct tep_handle *pevent, tep_func_handler func, enum tep_func_arg_type ret_type, char *name,  ...)

    register a helper function

    :param pevent:
        the handle to the pevent
    :type pevent: struct tep_handle \*

    :param func:
        the function to process the helper function
    :type func: tep_func_handler

    :param ret_type:
        the return type of the helper function
    :type ret_type: enum tep_func_arg_type

    :param name:
        the name of the helper function
    :type name: char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`tep_register_print_function.description`:

Description
-----------

Some events may have helper functions in the print format arguments.
This allows a plugin to dynamically create a way to process one
of these functions.

The \ ``parameters``\  is a variable list of tep_func_arg_type enums that
must end with TEP_FUNC_ARG_VOID.

.. _`tep_unregister_print_function`:

tep_unregister_print_function
=============================

.. c:function:: int tep_unregister_print_function(struct tep_handle *pevent, tep_func_handler func, char *name)

    unregister a helper function

    :param pevent:
        the handle to the pevent
    :type pevent: struct tep_handle \*

    :param func:
        the function to process the helper function
    :type func: tep_func_handler

    :param name:
        the name of the helper function
    :type name: char \*

.. _`tep_unregister_print_function.description`:

Description
-----------

This function removes existing print handler for function \ ``name``\ .

Returns 0 if the handler was removed successully, -1 otherwise.

.. _`tep_register_event_handler`:

tep_register_event_handler
==========================

.. c:function:: int tep_register_event_handler(struct tep_handle *pevent, int id, const char *sys_name, const char *event_name, tep_event_handler_func func, void *context)

    register a way to parse an event

    :param pevent:
        the handle to the pevent
    :type pevent: struct tep_handle \*

    :param id:
        the id of the event to register
    :type id: int

    :param sys_name:
        the system name the event belongs to
    :type sys_name: const char \*

    :param event_name:
        the name of the event
    :type event_name: const char \*

    :param func:
        the function to call to parse the event information
    :type func: tep_event_handler_func

    :param context:
        the data to be passed to \ ``func``\ 
    :type context: void \*

.. _`tep_register_event_handler.description`:

Description
-----------

This function allows a developer to override the parsing of
a given event. If for some reason the default print format
is not sufficient, this function will register a function
for an event to be used to parse the data instead.

If \ ``id``\  is >= 0, then it is used to find the event.
else \ ``sys_name``\  and \ ``event_name``\  are used.

.. _`tep_unregister_event_handler`:

tep_unregister_event_handler
============================

.. c:function:: int tep_unregister_event_handler(struct tep_handle *pevent, int id, const char *sys_name, const char *event_name, tep_event_handler_func func, void *context)

    unregister an existing event handler

    :param pevent:
        the handle to the pevent
    :type pevent: struct tep_handle \*

    :param id:
        the id of the event to unregister
    :type id: int

    :param sys_name:
        the system name the handler belongs to
    :type sys_name: const char \*

    :param event_name:
        the name of the event handler
    :type event_name: const char \*

    :param func:
        the function to call to parse the event information
    :type func: tep_event_handler_func

    :param context:
        the data to be passed to \ ``func``\ 
    :type context: void \*

.. _`tep_unregister_event_handler.description`:

Description
-----------

This function removes existing event handler (parser).

If \ ``id``\  is >= 0, then it is used to find the event.
else \ ``sys_name``\  and \ ``event_name``\  are used.

Returns 0 if handler was removed successfully, -1 if event was not found.

.. _`tep_alloc`:

tep_alloc
=========

.. c:function:: struct tep_handle *tep_alloc( void)

    create a pevent handle

    :param void:
        no arguments
    :type void: 

.. _`tep_free`:

tep_free
========

.. c:function:: void tep_free(struct tep_handle *pevent)

    free a pevent handle

    :param pevent:
        the pevent handle to free
    :type pevent: struct tep_handle \*

.. This file was automatic generated / don't edit.

