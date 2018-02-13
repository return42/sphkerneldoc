.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/lib/traceevent/event-parse.c

.. _`pevent_buffer_init`:

pevent_buffer_init
==================

.. c:function:: void pevent_buffer_init(const char *buf, unsigned long long size)

    init buffer for parsing

    :param const char \*buf:
        buffer to parse

    :param unsigned long long size:
        the size of the buffer

.. _`pevent_buffer_init.description`:

Description
-----------

For use with \ :c:func:`pevent_read_token`\ , this initializes the internal
buffer that \ :c:func:`pevent_read_token`\  will parse.

.. _`pevent_pid_is_registered`:

pevent_pid_is_registered
========================

.. c:function:: int pevent_pid_is_registered(struct pevent *pevent, int pid)

    return if a pid has a cmdline registered

    :param struct pevent \*pevent:
        handle for the pevent

    :param int pid:
        The pid to check if it has a cmdline registered with.

.. _`pevent_pid_is_registered.description`:

Description
-----------

Returns 1 if the pid has a cmdline mapped to it
0 otherwise.

.. _`pevent_register_comm`:

pevent_register_comm
====================

.. c:function:: int pevent_register_comm(struct pevent *pevent, const char *comm, int pid)

    register a pid / comm mapping

    :param struct pevent \*pevent:
        handle for the pevent

    :param const char \*comm:
        the command line to register

    :param int pid:
        the pid to map the command line to

.. _`pevent_register_comm.description`:

Description
-----------

This adds a mapping to search for command line names with
a given pid. The comm is duplicated.

.. _`pevent_set_function_resolver`:

pevent_set_function_resolver
============================

.. c:function:: int pevent_set_function_resolver(struct pevent *pevent, pevent_func_resolver_t *func, void *priv)

    set an alternative function resolver

    :param struct pevent \*pevent:
        handle for the pevent

    :param pevent_func_resolver_t \*func:
        *undescribed*

    :param void \*priv:
        resolver function private state.

.. _`pevent_set_function_resolver.description`:

Description
-----------

Some tools may have already a way to resolve kernel functions, allow them to
keep using it instead of duplicating all the entries inside
pevent->funclist.

.. _`pevent_reset_function_resolver`:

pevent_reset_function_resolver
==============================

.. c:function:: void pevent_reset_function_resolver(struct pevent *pevent)

    reset alternative function resolver

    :param struct pevent \*pevent:
        handle for the pevent

.. _`pevent_reset_function_resolver.description`:

Description
-----------

Stop using whatever alternative resolver was set, use the default
one instead.

.. _`pevent_find_function`:

pevent_find_function
====================

.. c:function:: const char *pevent_find_function(struct pevent *pevent, unsigned long long addr)

    find a function by a given address

    :param struct pevent \*pevent:
        handle for the pevent

    :param unsigned long long addr:
        the address to find the function with

.. _`pevent_find_function.description`:

Description
-----------

Returns a pointer to the function stored that has the given
address. Note, the address does not have to be exact, it
will select the function that would contain the address.

.. _`pevent_find_function_address`:

pevent_find_function_address
============================

.. c:function:: unsigned long long pevent_find_function_address(struct pevent *pevent, unsigned long long addr)

    find a function address by a given address

    :param struct pevent \*pevent:
        handle for the pevent

    :param unsigned long long addr:
        the address to find the function with

.. _`pevent_find_function_address.description`:

Description
-----------

Returns the address the function starts at. This can be used in
conjunction with pevent_find_function to print both the function
name and the function offset.

.. _`pevent_register_function`:

pevent_register_function
========================

.. c:function:: int pevent_register_function(struct pevent *pevent, char *func, unsigned long long addr, char *mod)

    register a function with a given address

    :param struct pevent \*pevent:
        handle for the pevent

    :param char \*func:
        *undescribed*

    :param unsigned long long addr:
        the address the function starts at

    :param char \*mod:
        the kernel module the function may be in (NULL for none)

.. _`pevent_register_function.description`:

Description
-----------

This registers a function name with an address and module.
The \ ``func``\  passed in is duplicated.

.. _`pevent_print_funcs`:

pevent_print_funcs
==================

.. c:function:: void pevent_print_funcs(struct pevent *pevent)

    print out the stored functions

    :param struct pevent \*pevent:
        handle for the pevent

.. _`pevent_print_funcs.description`:

Description
-----------

This prints out the stored functions.

.. _`pevent_register_print_string`:

pevent_register_print_string
============================

.. c:function:: int pevent_register_print_string(struct pevent *pevent, const char *fmt, unsigned long long addr)

    register a string by its address

    :param struct pevent \*pevent:
        handle for the pevent

    :param const char \*fmt:
        the string format to register

    :param unsigned long long addr:
        the address the string was located at

.. _`pevent_register_print_string.description`:

Description
-----------

This registers a string by the address it was stored in the kernel.
The \ ``fmt``\  passed in is duplicated.

.. _`pevent_print_printk`:

pevent_print_printk
===================

.. c:function:: void pevent_print_printk(struct pevent *pevent)

    print out the stored strings

    :param struct pevent \*pevent:
        handle for the pevent

.. _`pevent_print_printk.description`:

Description
-----------

This prints the string formats that were stored.

.. _`pevent_peek_char`:

pevent_peek_char
================

.. c:function:: int pevent_peek_char( void)

    peek at the next character that will be read

    :param  void:
        no arguments

.. _`pevent_peek_char.description`:

Description
-----------

Returns the next character read, or -1 if end of buffer.

.. _`pevent_read_token`:

pevent_read_token
=================

.. c:function:: enum event_type pevent_read_token(char **tok)

    access to utilites to use the pevent parser

    :param char \*\*tok:
        The token to return

.. _`pevent_read_token.description`:

Description
-----------

This will parse tokens from the string given by
\ :c:func:`pevent_init_data`\ .

Returns the token type.

.. _`pevent_free_token`:

pevent_free_token
=================

.. c:function:: void pevent_free_token(char *token)

    free a token returned by pevent_read_token

    :param char \*token:
        the token to free

.. _`pevent_find_common_field`:

pevent_find_common_field
========================

.. c:function:: struct format_field *pevent_find_common_field(struct event_format *event, const char *name)

    return a common field by event

    :param struct event_format \*event:
        handle for the event

    :param const char \*name:
        the name of the common field to return

.. _`pevent_find_common_field.description`:

Description
-----------

Returns a common field from the event by the given \ ``name``\ .
This only searchs the common fields and not all field.

.. _`pevent_find_field`:

pevent_find_field
=================

.. c:function:: struct format_field *pevent_find_field(struct event_format *event, const char *name)

    find a non-common field

    :param struct event_format \*event:
        handle for the event

    :param const char \*name:
        the name of the non-common field

.. _`pevent_find_field.description`:

Description
-----------

Returns a non-common field by the given \ ``name``\ .
This does not search common fields.

.. _`pevent_find_any_field`:

pevent_find_any_field
=====================

.. c:function:: struct format_field *pevent_find_any_field(struct event_format *event, const char *name)

    find any field by name

    :param struct event_format \*event:
        handle for the event

    :param const char \*name:
        the name of the field

.. _`pevent_find_any_field.description`:

Description
-----------

Returns a field by the given \ ``name``\ .
This searchs the common field names first, then
the non-common ones if a common one was not found.

.. _`pevent_read_number`:

pevent_read_number
==================

.. c:function:: unsigned long long pevent_read_number(struct pevent *pevent, const void *ptr, int size)

    read a number from data

    :param struct pevent \*pevent:
        handle for the pevent

    :param const void \*ptr:
        the raw data

    :param int size:
        the size of the data that holds the number

.. _`pevent_read_number.description`:

Description
-----------

Returns the number (converted to host) from the
raw data.

.. _`pevent_read_number_field`:

pevent_read_number_field
========================

.. c:function:: int pevent_read_number_field(struct format_field *field, const void *data, unsigned long long *value)

    read a number from data

    :param struct format_field \*field:
        a handle to the field

    :param const void \*data:
        the raw data to read

    :param unsigned long long \*value:
        the value to place the number in

.. _`pevent_read_number_field.description`:

Description
-----------

Reads raw data according to a field offset and size,
and translates it into \ ``value``\ .

Returns 0 on success, -1 otherwise.

.. _`pevent_find_event`:

pevent_find_event
=================

.. c:function:: struct event_format *pevent_find_event(struct pevent *pevent, int id)

    find an event by given id

    :param struct pevent \*pevent:
        a handle to the pevent

    :param int id:
        the id of the event

.. _`pevent_find_event.description`:

Description
-----------

Returns an event that has a given \ ``id``\ .

.. _`pevent_find_event_by_name`:

pevent_find_event_by_name
=========================

.. c:function:: struct event_format *pevent_find_event_by_name(struct pevent *pevent, const char *sys, const char *name)

    find an event by given name

    :param struct pevent \*pevent:
        a handle to the pevent

    :param const char \*sys:
        the system name to search for

    :param const char \*name:
        the name of the event to search for

.. _`pevent_find_event_by_name.description`:

Description
-----------

This returns an event with a given \ ``name``\  and under the system
\ ``sys``\ . If \ ``sys``\  is NULL the first event with \ ``name``\  is returned.

.. _`pevent_data_lat_fmt`:

pevent_data_lat_fmt
===================

.. c:function:: void pevent_data_lat_fmt(struct pevent *pevent, struct trace_seq *s, struct pevent_record *record)

    parse the data for the latency format

    :param struct pevent \*pevent:
        a handle to the pevent

    :param struct trace_seq \*s:
        the trace_seq to write to

    :param struct pevent_record \*record:
        the record to read from

.. _`pevent_data_lat_fmt.description`:

Description
-----------

This parses out the Latency format (interrupts disabled,
need rescheduling, in hard/soft interrupt, preempt count
and lock depth) and places it into the trace_seq.

.. _`pevent_data_type`:

pevent_data_type
================

.. c:function:: int pevent_data_type(struct pevent *pevent, struct pevent_record *rec)

    parse out the given event type

    :param struct pevent \*pevent:
        a handle to the pevent

    :param struct pevent_record \*rec:
        the record to read from

.. _`pevent_data_type.description`:

Description
-----------

This returns the event id from the \ ``rec``\ .

.. _`pevent_data_event_from_type`:

pevent_data_event_from_type
===========================

.. c:function:: struct event_format *pevent_data_event_from_type(struct pevent *pevent, int type)

    find the event by a given type

    :param struct pevent \*pevent:
        a handle to the pevent

    :param int type:
        the type of the event.

.. _`pevent_data_event_from_type.description`:

Description
-----------

This returns the event form a given \ ``type``\ ;

.. _`pevent_data_pid`:

pevent_data_pid
===============

.. c:function:: int pevent_data_pid(struct pevent *pevent, struct pevent_record *rec)

    parse the PID from record

    :param struct pevent \*pevent:
        a handle to the pevent

    :param struct pevent_record \*rec:
        the record to parse

.. _`pevent_data_pid.description`:

Description
-----------

This returns the PID from a record.

.. _`pevent_data_preempt_count`:

pevent_data_preempt_count
=========================

.. c:function:: int pevent_data_preempt_count(struct pevent *pevent, struct pevent_record *rec)

    parse the preempt count from the record

    :param struct pevent \*pevent:
        a handle to the pevent

    :param struct pevent_record \*rec:
        the record to parse

.. _`pevent_data_preempt_count.description`:

Description
-----------

This returns the preempt count from a record.

.. _`pevent_data_flags`:

pevent_data_flags
=================

.. c:function:: int pevent_data_flags(struct pevent *pevent, struct pevent_record *rec)

    parse the latency flags from the record

    :param struct pevent \*pevent:
        a handle to the pevent

    :param struct pevent_record \*rec:
        the record to parse

.. _`pevent_data_flags.description`:

Description
-----------

This returns the latency flags from a record.

Use trace_flag_type enum for the flags (see event-parse.h).

.. _`pevent_data_comm_from_pid`:

pevent_data_comm_from_pid
=========================

.. c:function:: const char *pevent_data_comm_from_pid(struct pevent *pevent, int pid)

    return the command line from PID

    :param struct pevent \*pevent:
        a handle to the pevent

    :param int pid:
        the PID of the task to search for

.. _`pevent_data_comm_from_pid.description`:

Description
-----------

This returns a pointer to the command line that has the given
\ ``pid``\ .

.. _`pevent_data_pid_from_comm`:

pevent_data_pid_from_comm
=========================

.. c:function:: struct cmdline *pevent_data_pid_from_comm(struct pevent *pevent, const char *comm, struct cmdline *next)

    return the pid from a given comm

    :param struct pevent \*pevent:
        a handle to the pevent

    :param const char \*comm:
        the cmdline to find the pid from

    :param struct cmdline \*next:
        the cmdline structure to find the next comm

.. _`pevent_data_pid_from_comm.description`:

Description
-----------

This returns the cmdline structure that holds a pid for a given
comm, or NULL if none found. As there may be more than one pid for
a given comm, the result of this call can be passed back into
a recurring call in the \ ``next``\  paramater, and then it will find the
next pid.
Also, it does a linear seach, so it may be slow.

.. _`pevent_cmdline_pid`:

pevent_cmdline_pid
==================

.. c:function:: int pevent_cmdline_pid(struct pevent *pevent, struct cmdline *cmdline)

    return the pid associated to a given cmdline

    :param struct pevent \*pevent:
        *undescribed*

    :param struct cmdline \*cmdline:
        The cmdline structure to get the pid from

.. _`pevent_cmdline_pid.description`:

Description
-----------

Returns the pid for a give cmdline. If \ ``cmdline``\  is NULL, then
-1 is returned.

.. _`pevent_event_info`:

pevent_event_info
=================

.. c:function:: void pevent_event_info(struct trace_seq *s, struct event_format *event, struct pevent_record *record)

    parse the data into the print format

    :param struct trace_seq \*s:
        the trace_seq to write to

    :param struct event_format \*event:
        the handle to the event

    :param struct pevent_record \*record:
        the record to read from

.. _`pevent_event_info.description`:

Description
-----------

This parses the raw \ ``data``\  using the given \ ``event``\  information and
writes the print format into the trace_seq.

.. _`pevent_find_event_by_record`:

pevent_find_event_by_record
===========================

.. c:function:: struct event_format *pevent_find_event_by_record(struct pevent *pevent, struct pevent_record *record)

    return the event from a given record

    :param struct pevent \*pevent:
        a handle to the pevent

    :param struct pevent_record \*record:
        The record to get the event from

.. _`pevent_find_event_by_record.description`:

Description
-----------

Returns the associated event for a given record, or NULL if non is
is found.

.. _`pevent_print_event_task`:

pevent_print_event_task
=======================

.. c:function:: void pevent_print_event_task(struct pevent *pevent, struct trace_seq *s, struct event_format *event, struct pevent_record *record)

    Write the event task comm, pid and CPU

    :param struct pevent \*pevent:
        a handle to the pevent

    :param struct trace_seq \*s:
        the trace_seq to write to

    :param struct event_format \*event:
        the handle to the record's event

    :param struct pevent_record \*record:
        The record to get the event from

.. _`pevent_print_event_task.description`:

Description
-----------

Writes the tasks comm, pid and CPU to \ ``s``\ .

.. _`pevent_print_event_time`:

pevent_print_event_time
=======================

.. c:function:: void pevent_print_event_time(struct pevent *pevent, struct trace_seq *s, struct event_format *event, struct pevent_record *record, bool use_trace_clock)

    Write the event timestamp

    :param struct pevent \*pevent:
        a handle to the pevent

    :param struct trace_seq \*s:
        the trace_seq to write to

    :param struct event_format \*event:
        the handle to the record's event

    :param struct pevent_record \*record:
        The record to get the event from

    :param bool use_trace_clock:
        Set to parse according to the \ ``pevent``\ ->trace_clock

.. _`pevent_print_event_time.description`:

Description
-----------

Writes the timestamp of the record into \ ``s``\ .

.. _`pevent_print_event_data`:

pevent_print_event_data
=======================

.. c:function:: void pevent_print_event_data(struct pevent *pevent, struct trace_seq *s, struct event_format *event, struct pevent_record *record)

    Write the event data section

    :param struct pevent \*pevent:
        a handle to the pevent

    :param struct trace_seq \*s:
        the trace_seq to write to

    :param struct event_format \*event:
        the handle to the record's event

    :param struct pevent_record \*record:
        The record to get the event from

.. _`pevent_print_event_data.description`:

Description
-----------

Writes the parsing of the record's data to \ ``s``\ .

.. _`pevent_event_common_fields`:

pevent_event_common_fields
==========================

.. c:function:: struct format_field **pevent_event_common_fields(struct event_format *event)

    return a list of common fields for an event

    :param struct event_format \*event:
        the event to return the common fields of.

.. _`pevent_event_common_fields.description`:

Description
-----------

Returns an allocated array of fields. The last item in the array is NULL.
The array must be freed with \ :c:func:`free`\ .

.. _`pevent_event_fields`:

pevent_event_fields
===================

.. c:function:: struct format_field **pevent_event_fields(struct event_format *event)

    return a list of event specific fields for an event

    :param struct event_format \*event:
        the event to return the fields of.

.. _`pevent_event_fields.description`:

Description
-----------

Returns an allocated array of fields. The last item in the array is NULL.
The array must be freed with \ :c:func:`free`\ .

.. _`pevent_parse_header_page`:

pevent_parse_header_page
========================

.. c:function:: int pevent_parse_header_page(struct pevent *pevent, char *buf, unsigned long size, int long_size)

    parse the data stored in the header page

    :param struct pevent \*pevent:
        the handle to the pevent

    :param char \*buf:
        the buffer storing the header page format string

    :param unsigned long size:
        the size of \ ``buf``\ 

    :param int long_size:
        the long size to use if there is no header

.. _`pevent_parse_header_page.description`:

Description
-----------

This parses the header page format for information on the
ring buffer used. The \ ``buf``\  should be copied from

/sys/kernel/debug/tracing/events/header_page

.. _`__pevent_parse_format`:

\__pevent_parse_format
======================

.. c:function:: enum pevent_errno __pevent_parse_format(struct event_format **eventp, struct pevent *pevent, const char *buf, unsigned long size, const char *sys)

    parse the event format

    :param struct event_format \*\*eventp:
        *undescribed*

    :param struct pevent \*pevent:
        *undescribed*

    :param const char \*buf:
        the buffer storing the event format string

    :param unsigned long size:
        the size of \ ``buf``\ 

    :param const char \*sys:
        the system the event belongs to

.. _`__pevent_parse_format.description`:

Description
-----------

This parses the event format and creates an event structure
to quickly parse raw data for a given event.

.. _`__pevent_parse_format.these-files-currently-come-from`:

These files currently come from
-------------------------------


/sys/kernel/debug/tracing/events/.../.../format

.. _`pevent_parse_format`:

pevent_parse_format
===================

.. c:function:: enum pevent_errno pevent_parse_format(struct pevent *pevent, struct event_format **eventp, const char *buf, unsigned long size, const char *sys)

    parse the event format

    :param struct pevent \*pevent:
        the handle to the pevent

    :param struct event_format \*\*eventp:
        returned format

    :param const char \*buf:
        the buffer storing the event format string

    :param unsigned long size:
        the size of \ ``buf``\ 

    :param const char \*sys:
        the system the event belongs to

.. _`pevent_parse_format.description`:

Description
-----------

This parses the event format and creates an event structure
to quickly parse raw data for a given event.

.. _`pevent_parse_format.these-files-currently-come-from`:

These files currently come from
-------------------------------


/sys/kernel/debug/tracing/events/.../.../format

.. _`pevent_parse_event`:

pevent_parse_event
==================

.. c:function:: enum pevent_errno pevent_parse_event(struct pevent *pevent, const char *buf, unsigned long size, const char *sys)

    parse the event format

    :param struct pevent \*pevent:
        the handle to the pevent

    :param const char \*buf:
        the buffer storing the event format string

    :param unsigned long size:
        the size of \ ``buf``\ 

    :param const char \*sys:
        the system the event belongs to

.. _`pevent_parse_event.description`:

Description
-----------

This parses the event format and creates an event structure
to quickly parse raw data for a given event.

.. _`pevent_parse_event.these-files-currently-come-from`:

These files currently come from
-------------------------------


/sys/kernel/debug/tracing/events/.../.../format

.. _`pevent_get_field_raw`:

pevent_get_field_raw
====================

.. c:function:: void *pevent_get_field_raw(struct trace_seq *s, struct event_format *event, const char *name, struct pevent_record *record, int *len, int err)

    return the raw pointer into the data field

    :param struct trace_seq \*s:
        The seq to print to on error

    :param struct event_format \*event:
        the event that the field is for

    :param const char \*name:
        The name of the field

    :param struct pevent_record \*record:
        The record with the field name.

    :param int \*len:
        place to store the field length.

    :param int err:
        print default error if failed.

.. _`pevent_get_field_raw.description`:

Description
-----------

Returns a pointer into record->data of the field and places
the length of the field in \ ``len``\ .

On failure, it returns NULL.

.. _`pevent_get_field_val`:

pevent_get_field_val
====================

.. c:function:: int pevent_get_field_val(struct trace_seq *s, struct event_format *event, const char *name, struct pevent_record *record, unsigned long long *val, int err)

    find a field and return its value

    :param struct trace_seq \*s:
        The seq to print to on error

    :param struct event_format \*event:
        the event that the field is for

    :param const char \*name:
        The name of the field

    :param struct pevent_record \*record:
        The record with the field name.

    :param unsigned long long \*val:
        place to store the value of the field.

    :param int err:
        print default error if failed.

.. _`pevent_get_field_val.description`:

Description
-----------

Returns 0 on success -1 on field not found.

.. _`pevent_get_common_field_val`:

pevent_get_common_field_val
===========================

.. c:function:: int pevent_get_common_field_val(struct trace_seq *s, struct event_format *event, const char *name, struct pevent_record *record, unsigned long long *val, int err)

    find a common field and return its value

    :param struct trace_seq \*s:
        The seq to print to on error

    :param struct event_format \*event:
        the event that the field is for

    :param const char \*name:
        The name of the field

    :param struct pevent_record \*record:
        The record with the field name.

    :param unsigned long long \*val:
        place to store the value of the field.

    :param int err:
        print default error if failed.

.. _`pevent_get_common_field_val.description`:

Description
-----------

Returns 0 on success -1 on field not found.

.. _`pevent_get_any_field_val`:

pevent_get_any_field_val
========================

.. c:function:: int pevent_get_any_field_val(struct trace_seq *s, struct event_format *event, const char *name, struct pevent_record *record, unsigned long long *val, int err)

    find a any field and return its value

    :param struct trace_seq \*s:
        The seq to print to on error

    :param struct event_format \*event:
        the event that the field is for

    :param const char \*name:
        The name of the field

    :param struct pevent_record \*record:
        The record with the field name.

    :param unsigned long long \*val:
        place to store the value of the field.

    :param int err:
        print default error if failed.

.. _`pevent_get_any_field_val.description`:

Description
-----------

Returns 0 on success -1 on field not found.

.. _`pevent_print_num_field`:

pevent_print_num_field
======================

.. c:function:: int pevent_print_num_field(struct trace_seq *s, const char *fmt, struct event_format *event, const char *name, struct pevent_record *record, int err)

    print a field and a format

    :param struct trace_seq \*s:
        The seq to print to

    :param const char \*fmt:
        The printf format to print the field with.

    :param struct event_format \*event:
        the event that the field is for

    :param const char \*name:
        The name of the field

    :param struct pevent_record \*record:
        The record with the field name.

    :param int err:
        print default error if failed.

.. _`pevent_print_num_field.return`:

Return
------

0 on success, -1 field not found, or 1 if buffer is full.

.. _`pevent_print_func_field`:

pevent_print_func_field
=======================

.. c:function:: int pevent_print_func_field(struct trace_seq *s, const char *fmt, struct event_format *event, const char *name, struct pevent_record *record, int err)

    print a field and a format for function pointers

    :param struct trace_seq \*s:
        The seq to print to

    :param const char \*fmt:
        The printf format to print the field with.

    :param struct event_format \*event:
        the event that the field is for

    :param const char \*name:
        The name of the field

    :param struct pevent_record \*record:
        The record with the field name.

    :param int err:
        print default error if failed.

.. _`pevent_print_func_field.return`:

Return
------

0 on success, -1 field not found, or 1 if buffer is full.

.. _`pevent_register_print_function`:

pevent_register_print_function
==============================

.. c:function:: int pevent_register_print_function(struct pevent *pevent, pevent_func_handler func, enum pevent_func_arg_type ret_type, char *name,  ...)

    register a helper function

    :param struct pevent \*pevent:
        the handle to the pevent

    :param pevent_func_handler func:
        the function to process the helper function

    :param enum pevent_func_arg_type ret_type:
        the return type of the helper function

    :param char \*name:
        the name of the helper function

    :param ellipsis ellipsis:
        variable arguments

.. _`pevent_register_print_function.description`:

Description
-----------

Some events may have helper functions in the print format arguments.
This allows a plugin to dynamically create a way to process one
of these functions.

The \ ``parameters``\  is a variable list of pevent_func_arg_type enums that
must end with PEVENT_FUNC_ARG_VOID.

.. _`pevent_unregister_print_function`:

pevent_unregister_print_function
================================

.. c:function:: int pevent_unregister_print_function(struct pevent *pevent, pevent_func_handler func, char *name)

    unregister a helper function

    :param struct pevent \*pevent:
        the handle to the pevent

    :param pevent_func_handler func:
        the function to process the helper function

    :param char \*name:
        the name of the helper function

.. _`pevent_unregister_print_function.description`:

Description
-----------

This function removes existing print handler for function \ ``name``\ .

Returns 0 if the handler was removed successully, -1 otherwise.

.. _`pevent_register_event_handler`:

pevent_register_event_handler
=============================

.. c:function:: int pevent_register_event_handler(struct pevent *pevent, int id, const char *sys_name, const char *event_name, pevent_event_handler_func func, void *context)

    register a way to parse an event

    :param struct pevent \*pevent:
        the handle to the pevent

    :param int id:
        the id of the event to register

    :param const char \*sys_name:
        the system name the event belongs to

    :param const char \*event_name:
        the name of the event

    :param pevent_event_handler_func func:
        the function to call to parse the event information

    :param void \*context:
        the data to be passed to \ ``func``\ 

.. _`pevent_register_event_handler.description`:

Description
-----------

This function allows a developer to override the parsing of
a given event. If for some reason the default print format
is not sufficient, this function will register a function
for an event to be used to parse the data instead.

If \ ``id``\  is >= 0, then it is used to find the event.
else \ ``sys_name``\  and \ ``event_name``\  are used.

.. _`pevent_unregister_event_handler`:

pevent_unregister_event_handler
===============================

.. c:function:: int pevent_unregister_event_handler(struct pevent *pevent, int id, const char *sys_name, const char *event_name, pevent_event_handler_func func, void *context)

    unregister an existing event handler

    :param struct pevent \*pevent:
        the handle to the pevent

    :param int id:
        the id of the event to unregister

    :param const char \*sys_name:
        the system name the handler belongs to

    :param const char \*event_name:
        the name of the event handler

    :param pevent_event_handler_func func:
        the function to call to parse the event information

    :param void \*context:
        the data to be passed to \ ``func``\ 

.. _`pevent_unregister_event_handler.description`:

Description
-----------

This function removes existing event handler (parser).

If \ ``id``\  is >= 0, then it is used to find the event.
else \ ``sys_name``\  and \ ``event_name``\  are used.

Returns 0 if handler was removed successfully, -1 if event was not found.

.. _`pevent_alloc`:

pevent_alloc
============

.. c:function:: struct pevent *pevent_alloc( void)

    create a pevent handle

    :param  void:
        no arguments

.. _`pevent_free`:

pevent_free
===========

.. c:function:: void pevent_free(struct pevent *pevent)

    free a pevent handle

    :param struct pevent \*pevent:
        the pevent handle to free

.. This file was automatic generated / don't edit.

