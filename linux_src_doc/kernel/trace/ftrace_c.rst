.. -*- coding: utf-8; mode: rst -*-
.. src-file: kernel/trace/ftrace.c

.. _`ftrace_nr_registered_ops`:

ftrace_nr_registered_ops
========================

.. c:function:: int ftrace_nr_registered_ops( void)

    return number of ops registered

    :param  void:
        no arguments

.. _`ftrace_nr_registered_ops.description`:

Description
-----------

Returns the number of ftrace_ops registered and tracing functions

.. _`clear_ftrace_function`:

clear_ftrace_function
=====================

.. c:function:: void clear_ftrace_function( void)

    reset the ftrace function

    :param  void:
        no arguments

.. _`clear_ftrace_function.description`:

Description
-----------

This NULLs the ftrace function and in essence stops
tracing.  There may be lag

.. _`ftrace_lookup_ip`:

ftrace_lookup_ip
================

.. c:function:: struct ftrace_func_entry *ftrace_lookup_ip(struct ftrace_hash *hash, unsigned long ip)

    Test to see if an ip exists in an ftrace_hash

    :param struct ftrace_hash \*hash:
        The hash to look at

    :param unsigned long ip:
        The instruction pointer to test

.. _`ftrace_lookup_ip.description`:

Description
-----------

Search a given \ ``hash``\  to see if a given instruction pointer (@ip)
exists in it.

Returns the entry that holds the \ ``ip``\  if found. NULL otherwise.

.. _`ftrace_location_range`:

ftrace_location_range
=====================

.. c:function:: unsigned long ftrace_location_range(unsigned long start, unsigned long end)

    return the first address of a traced location if it touches the given ip range

    :param unsigned long start:
        start of range to search.

    :param unsigned long end:
        end of range to search (inclusive). \ ``end``\  points to the last byte
        to check.

.. _`ftrace_location_range.description`:

Description
-----------

Returns rec->ip if the related ftrace location is a least partly within
the given address range. That is, the first address of the instruction
that is either a NOP or call to the function tracer. It checks the ftrace
internal tables to determine if the address belongs or not.

.. _`ftrace_location`:

ftrace_location
===============

.. c:function:: unsigned long ftrace_location(unsigned long ip)

    return true if the ip giving is a traced location

    :param unsigned long ip:
        the instruction pointer to check

.. _`ftrace_location.description`:

Description
-----------

Returns rec->ip if \ ``ip``\  given is a pointer to a ftrace location.
That is, the instruction that is either a NOP or call to
the function tracer. It checks the ftrace internal tables to
determine if the address belongs or not.

.. _`ftrace_text_reserved`:

ftrace_text_reserved
====================

.. c:function:: int ftrace_text_reserved(const void *start, const void *end)

    return true if range contains an ftrace location

    :param const void \*start:
        start of range to search

    :param const void \*end:
        end of range to search (inclusive). \ ``end``\  points to the last byte to check.

.. _`ftrace_text_reserved.description`:

Description
-----------

Returns 1 if \ ``start``\  and \ ``end``\  contains a ftrace location.
That is, the instruction that is either a NOP or call to
the function tracer. It checks the ftrace internal tables to
determine if the address belongs or not.

.. _`ftrace_bug`:

ftrace_bug
==========

.. c:function:: void ftrace_bug(int failed, struct dyn_ftrace *rec)

    report and shutdown function tracer

    :param int failed:
        The failed type (EFAULT, EINVAL, EPERM)

    :param struct dyn_ftrace \*rec:
        The record that failed

.. _`ftrace_bug.description`:

Description
-----------

The arch code that enables or disables the function tracing
can call \ :c:func:`ftrace_bug`\  when it has detected a problem in
modifying the code. \ ``failed``\  should be one of either:
EFAULT - if the problem happens on reading the \ ``ip``\  address
EINVAL - if what is read at \ ``ip``\  is not what was expected
EPERM - if the problem happens on writting to the \ ``ip``\  address

.. _`ftrace_update_record`:

ftrace_update_record
====================

.. c:function:: int ftrace_update_record(struct dyn_ftrace *rec, int enable)

    :param struct dyn_ftrace \*rec:
        the record to update

    :param int enable:
        set to 1 if the record is tracing, zero to force disable

.. _`ftrace_update_record.description`:

Description
-----------

The records that represent all functions that can be traced need
to be updated when tracing has been enabled.

.. _`ftrace_test_record`:

ftrace_test_record
==================

.. c:function:: int ftrace_test_record(struct dyn_ftrace *rec, int enable)

    :param struct dyn_ftrace \*rec:
        the record to test

    :param int enable:
        set to 1 to check if enabled, 0 if it is disabled

.. _`ftrace_test_record.description`:

Description
-----------

The arch code may need to test if a record is already set to
tracing to determine how to modify the function code that it
represents.

.. _`ftrace_get_addr_new`:

ftrace_get_addr_new
===================

.. c:function:: unsigned long ftrace_get_addr_new(struct dyn_ftrace *rec)

    Get the call address to set to

    :param struct dyn_ftrace \*rec:
        The ftrace record descriptor

.. _`ftrace_get_addr_new.description`:

Description
-----------

If the record has the FTRACE_FL_REGS set, that means that it
wants to convert to a callback that saves all regs. If FTRACE_FL_REGS
is not not set, then it wants to convert to the normal callback.

Returns the address of the trampoline to set to

.. _`ftrace_get_addr_curr`:

ftrace_get_addr_curr
====================

.. c:function:: unsigned long ftrace_get_addr_curr(struct dyn_ftrace *rec)

    Get the call address that is already there

    :param struct dyn_ftrace \*rec:
        The ftrace record descriptor

.. _`ftrace_get_addr_curr.description`:

Description
-----------

The FTRACE_FL_REGS_EN is set when the record already points to
a function that saves all the regs. Basically the '_EN' version
represents the current state of the function.

Returns the address of the trampoline that is currently being called

.. _`ftrace_rec_iter_start`:

ftrace_rec_iter_start
=====================

.. c:function:: struct ftrace_rec_iter *ftrace_rec_iter_start( void)

    :param  void:
        no arguments

.. _`ftrace_rec_iter_start.description`:

Description
-----------

Returns an iterator handle that is used to iterate over all
the records that represent address locations where functions
are traced.

May return NULL if no records are available.

.. _`ftrace_rec_iter_next`:

ftrace_rec_iter_next
====================

.. c:function:: struct ftrace_rec_iter *ftrace_rec_iter_next(struct ftrace_rec_iter *iter)

    :param struct ftrace_rec_iter \*iter:
        The handle to the iterator.

.. _`ftrace_rec_iter_next.description`:

Description
-----------

Returns the next iterator after the given iterator \ ``iter``\ .

.. _`ftrace_rec_iter_record`:

ftrace_rec_iter_record
======================

.. c:function:: struct dyn_ftrace *ftrace_rec_iter_record(struct ftrace_rec_iter *iter)

    :param struct ftrace_rec_iter \*iter:
        The current iterator location

.. _`ftrace_rec_iter_record.description`:

Description
-----------

Returns the record that the current \ ``iter``\  is at.

.. _`ftrace_run_stop_machine`:

ftrace_run_stop_machine
=======================

.. c:function:: void ftrace_run_stop_machine(int command)

    :param int command:
        The command to tell ftrace what to do

.. _`ftrace_run_stop_machine.description`:

Description
-----------

If an arch needs to fall back to the stop machine method, the
it can call this function.

.. _`arch_ftrace_update_code`:

arch_ftrace_update_code
=======================

.. c:function:: void arch_ftrace_update_code(int command)

    :param int command:
        The command that needs to be done

.. _`arch_ftrace_update_code.description`:

Description
-----------

Archs can override this function if it does not need to
run \ :c:func:`stop_machine`\  to modify code.

.. _`ftrace_regex_open`:

ftrace_regex_open
=================

.. c:function:: int ftrace_regex_open(struct ftrace_ops *ops, int flag, struct inode *inode, struct file *file)

    initialize function tracer filter files

    :param struct ftrace_ops \*ops:
        The ftrace_ops that hold the hash filters

    :param int flag:
        The type of filter to process

    :param struct inode \*inode:
        The inode, usually passed in to your open routine

    :param struct file \*file:
        The file, usually passed in to your open routine

.. _`ftrace_regex_open.description`:

Description
-----------

ftrace_regex_open() initializes the filter files for the
\ ``ops``\ . Depending on \ ``flag``\  it may process the filter hash or
the notrace hash of \ ``ops``\ . With this called from the open
routine, you can use \ :c:func:`ftrace_filter_write`\  for the write
routine if \ ``flag``\  has FTRACE_ITER_FILTER set, or
\ :c:func:`ftrace_notrace_write`\  if \ ``flag``\  has FTRACE_ITER_NOTRACE set.
\ :c:func:`tracing_lseek`\  should be used as the lseek routine, and
release must call \ :c:func:`ftrace_regex_release`\ .

.. _`allocate_ftrace_func_mapper`:

allocate_ftrace_func_mapper
===========================

.. c:function:: struct ftrace_func_mapper *allocate_ftrace_func_mapper( void)

    allocate a new ftrace_func_mapper

    :param  void:
        no arguments

.. _`allocate_ftrace_func_mapper.description`:

Description
-----------

Returns a ftrace_func_mapper descriptor that can be used to map ips to data.

.. _`ftrace_func_mapper_find_ip`:

ftrace_func_mapper_find_ip
==========================

.. c:function:: void **ftrace_func_mapper_find_ip(struct ftrace_func_mapper *mapper, unsigned long ip)

    Find some data mapped to an ip

    :param struct ftrace_func_mapper \*mapper:
        The mapper that has the ip maps

    :param unsigned long ip:
        the instruction pointer to find the data for

.. _`ftrace_func_mapper_find_ip.description`:

Description
-----------

Returns the data mapped to \ ``ip``\  if found otherwise NULL. The return
is actually the address of the mapper data pointer. The address is
returned for use cases where the data is no bigger than a long, and
the user can use the data pointer as its data instead of having to
allocate more memory for the reference.

.. _`ftrace_func_mapper_add_ip`:

ftrace_func_mapper_add_ip
=========================

.. c:function:: int ftrace_func_mapper_add_ip(struct ftrace_func_mapper *mapper, unsigned long ip, void *data)

    Map some data to an ip

    :param struct ftrace_func_mapper \*mapper:
        The mapper that has the ip maps

    :param unsigned long ip:
        The instruction pointer address to map \ ``data``\  to

    :param void \*data:
        The data to map to \ ``ip``\ 

.. _`ftrace_func_mapper_add_ip.description`:

Description
-----------

Returns 0 on succes otherwise an error.

.. _`ftrace_func_mapper_remove_ip`:

ftrace_func_mapper_remove_ip
============================

.. c:function:: void *ftrace_func_mapper_remove_ip(struct ftrace_func_mapper *mapper, unsigned long ip)

    Remove an ip from the mapping

    :param struct ftrace_func_mapper \*mapper:
        The mapper that has the ip maps

    :param unsigned long ip:
        The instruction pointer address to remove the data from

.. _`ftrace_func_mapper_remove_ip.description`:

Description
-----------

Returns the data if it is found, otherwise NULL.
Note, if the data pointer is used as the data itself, (see
\ :c:func:`ftrace_func_mapper_find_ip`\ , then the return value may be meaningless,
if the data pointer was set to zero.

.. _`free_ftrace_func_mapper`:

free_ftrace_func_mapper
=======================

.. c:function:: void free_ftrace_func_mapper(struct ftrace_func_mapper *mapper, ftrace_mapper_func free_func)

    free a mapping of ips and data

    :param struct ftrace_func_mapper \*mapper:
        The mapper that has the ip maps

    :param ftrace_mapper_func free_func:
        A function to be called on each data item.

.. _`free_ftrace_func_mapper.description`:

Description
-----------

This is used to free the function mapper. The \ ``free_func``\  is optional
and can be used if the data needs to be freed as well.

.. _`ftrace_set_filter_ip`:

ftrace_set_filter_ip
====================

.. c:function:: int ftrace_set_filter_ip(struct ftrace_ops *ops, unsigned long ip, int remove, int reset)

    set a function to filter on in ftrace by address \ ``ops``\  - the ops to set the filter with \ ``ip``\  - the address to add to or remove from the filter. \ ``remove``\  - non zero to remove the ip from the filter \ ``reset``\  - non zero to reset all filters before applying this filter.

    :param struct ftrace_ops \*ops:
        *undescribed*

    :param unsigned long ip:
        *undescribed*

    :param int remove:
        *undescribed*

    :param int reset:
        *undescribed*

.. _`ftrace_set_filter_ip.description`:

Description
-----------

Filters denote which functions should be enabled when tracing is enabled
If \ ``ip``\  is NULL, it failes to update filter.

.. _`ftrace_ops_set_global_filter`:

ftrace_ops_set_global_filter
============================

.. c:function:: void ftrace_ops_set_global_filter(struct ftrace_ops *ops)

    setup ops to use global filters \ ``ops``\  - the ops which will use the global filters

    :param struct ftrace_ops \*ops:
        *undescribed*

.. _`ftrace_ops_set_global_filter.description`:

Description
-----------

ftrace users who need global function trace filtering should call this.
It can set the global filter only if ops were not initialized before.

.. _`ftrace_set_filter`:

ftrace_set_filter
=================

.. c:function:: int ftrace_set_filter(struct ftrace_ops *ops, unsigned char *buf, int len, int reset)

    set a function to filter on in ftrace \ ``ops``\  - the ops to set the filter with \ ``buf``\  - the string that holds the function filter text. \ ``len``\  - the length of the string. \ ``reset``\  - non zero to reset all filters before applying this filter.

    :param struct ftrace_ops \*ops:
        *undescribed*

    :param unsigned char \*buf:
        *undescribed*

    :param int len:
        *undescribed*

    :param int reset:
        *undescribed*

.. _`ftrace_set_filter.description`:

Description
-----------

Filters denote which functions should be enabled when tracing is enabled.
If \ ``buf``\  is NULL and reset is set, all functions will be enabled for tracing.

.. _`ftrace_set_notrace`:

ftrace_set_notrace
==================

.. c:function:: int ftrace_set_notrace(struct ftrace_ops *ops, unsigned char *buf, int len, int reset)

    set a function to not trace in ftrace \ ``ops``\  - the ops to set the notrace filter with \ ``buf``\  - the string that holds the function notrace text. \ ``len``\  - the length of the string. \ ``reset``\  - non zero to reset all filters before applying this filter.

    :param struct ftrace_ops \*ops:
        *undescribed*

    :param unsigned char \*buf:
        *undescribed*

    :param int len:
        *undescribed*

    :param int reset:
        *undescribed*

.. _`ftrace_set_notrace.description`:

Description
-----------

Notrace Filters denote which functions should not be enabled when tracing
is enabled. If \ ``buf``\  is NULL and reset is set, all functions will be enabled
for tracing.

.. _`ftrace_set_global_filter`:

ftrace_set_global_filter
========================

.. c:function:: void ftrace_set_global_filter(unsigned char *buf, int len, int reset)

    set a function to filter on with global tracers \ ``buf``\  - the string that holds the function filter text. \ ``len``\  - the length of the string. \ ``reset``\  - non zero to reset all filters before applying this filter.

    :param unsigned char \*buf:
        *undescribed*

    :param int len:
        *undescribed*

    :param int reset:
        *undescribed*

.. _`ftrace_set_global_filter.description`:

Description
-----------

Filters denote which functions should be enabled when tracing is enabled.
If \ ``buf``\  is NULL and reset is set, all functions will be enabled for tracing.

.. _`ftrace_set_global_notrace`:

ftrace_set_global_notrace
=========================

.. c:function:: void ftrace_set_global_notrace(unsigned char *buf, int len, int reset)

    set a function to not trace with global tracers \ ``buf``\  - the string that holds the function notrace text. \ ``len``\  - the length of the string. \ ``reset``\  - non zero to reset all filters before applying this filter.

    :param unsigned char \*buf:
        *undescribed*

    :param int len:
        *undescribed*

    :param int reset:
        *undescribed*

.. _`ftrace_set_global_notrace.description`:

Description
-----------

Notrace Filters denote which functions should not be enabled when tracing
is enabled. If \ ``buf``\  is NULL and reset is set, all functions will be enabled
for tracing.

.. _`ftrace_ops_get_func`:

ftrace_ops_get_func
===================

.. c:function:: ftrace_func_t ftrace_ops_get_func(struct ftrace_ops *ops)

    get the function a trampoline should call

    :param struct ftrace_ops \*ops:
        the ops to get the function for

.. _`ftrace_ops_get_func.description`:

Description
-----------

Normally the mcount trampoline will call the ops->func, but there
are times that it should not. For example, if the ops does not
have its own recursion protection, then it should call the
\ :c:func:`ftrace_ops_assist_func`\  instead.

Returns the function that the trampoline should call for \ ``ops``\ .

.. _`ftrace_kill`:

ftrace_kill
===========

.. c:function:: void ftrace_kill( void)

    kill ftrace

    :param  void:
        no arguments

.. _`ftrace_kill.description`:

Description
-----------

This function should be used by panic code. It stops ftrace
but in a not so nice way. If you need to simply kill ftrace
from a non-atomic section, use ftrace_kill.

.. _`ftrace_is_dead`:

ftrace_is_dead
==============

.. c:function:: int ftrace_is_dead( void)

    :param  void:
        no arguments

.. _`register_ftrace_function`:

register_ftrace_function
========================

.. c:function:: int register_ftrace_function(struct ftrace_ops *ops)

    register a function for profiling \ ``ops``\  - ops structure that holds the function for profiling.

    :param struct ftrace_ops \*ops:
        *undescribed*

.. _`register_ftrace_function.description`:

Description
-----------

Register a function to be called by all functions in the
kernel.

.. _`register_ftrace_function.note`:

Note
----

@ops->func and all the functions it calls must be labeled
with "notrace", otherwise it will go into a
recursive loop.

.. _`unregister_ftrace_function`:

unregister_ftrace_function
==========================

.. c:function:: int unregister_ftrace_function(struct ftrace_ops *ops)

    unregister a function for profiling. \ ``ops``\  - ops structure that holds the function to unregister

    :param struct ftrace_ops \*ops:
        *undescribed*

.. _`unregister_ftrace_function.description`:

Description
-----------

Unregister a function that was added to be called by ftrace profiling.

.. This file was automatic generated / don't edit.

