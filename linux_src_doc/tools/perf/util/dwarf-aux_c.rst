.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/perf/util/dwarf-aux.c

.. _`cu_find_realpath`:

cu_find_realpath
================

.. c:function:: const char *cu_find_realpath(Dwarf_Die *cu_die, const char *fname)

    Find the realpath of the target file

    :param Dwarf_Die \*cu_die:
        A DIE(dwarf information entry) of CU(compilation Unit)

    :param const char \*fname:
        The tail filename of the target file

.. _`cu_find_realpath.description`:

Description
-----------

Find the real(long) path of \ ``fname``\  in \ ``cu_die``\ .

.. _`cu_get_comp_dir`:

cu_get_comp_dir
===============

.. c:function:: const char *cu_get_comp_dir(Dwarf_Die *cu_die)

    Get the path of compilation directory

    :param Dwarf_Die \*cu_die:
        a CU DIE

.. _`cu_get_comp_dir.description`:

Description
-----------

Get the path of compilation directory of given \ ``cu_die``\ .
Since this depends on DW_AT_comp_dir, older gcc will not
embedded it. In that case, this returns NULL.

.. _`cu_find_lineinfo`:

cu_find_lineinfo
================

.. c:function:: int cu_find_lineinfo(Dwarf_Die *cu_die, unsigned long addr, const char **fname, int *lineno)

    Get a line number and file name for given address

    :param Dwarf_Die \*cu_die:
        a CU DIE

    :param unsigned long addr:
        An address

    :param const char \*\*fname:
        a pointer which returns the file name string

    :param int \*lineno:
        a pointer which returns the line number

.. _`cu_find_lineinfo.description`:

Description
-----------

Find a line number and file name for \ ``addr``\  in \ ``cu_die``\ .

.. _`cu_walk_functions_at`:

cu_walk_functions_at
====================

.. c:function:: int cu_walk_functions_at(Dwarf_Die *cu_die, Dwarf_Addr addr, int (*callback)(Dwarf_Die *, void *), void *data)

    Walk on function DIEs at given address

    :param Dwarf_Die \*cu_die:
        A CU DIE

    :param Dwarf_Addr addr:
        An address

    :param int (\*callback)(Dwarf_Die \*, void \*):
        A callback which called with found DIEs

    :param void \*data:
        A user data

.. _`cu_walk_functions_at.description`:

Description
-----------

Walk on function DIEs at given \ ``addr``\  in \ ``cu_die``\ . Passed DIEs
should be subprogram or inlined-subroutines.

.. _`die_get_linkage_name`:

die_get_linkage_name
====================

.. c:function:: const char *die_get_linkage_name(Dwarf_Die *dw_die)

    Get the linkage name of the object

    :param Dwarf_Die \*dw_die:
        A DIE of the object

.. _`die_get_linkage_name.description`:

Description
-----------

Get the linkage name attiribute of given \ ``dw_die``\ .
For C++ binary, the linkage name will be the mangled symbol.

.. _`die_compare_name`:

die_compare_name
================

.. c:function:: bool die_compare_name(Dwarf_Die *dw_die, const char *tname)

    Compare diename and tname

    :param Dwarf_Die \*dw_die:
        a DIE

    :param const char \*tname:
        a string of target name

.. _`die_compare_name.description`:

Description
-----------

Compare the name of \ ``dw_die``\  and \ ``tname``\ . Return false if \ ``dw_die``\  has no name.

.. _`die_match_name`:

die_match_name
==============

.. c:function:: bool die_match_name(Dwarf_Die *dw_die, const char *glob)

    Match diename/linkage name and glob

    :param Dwarf_Die \*dw_die:
        a DIE

    :param const char \*glob:
        a string of target glob pattern

.. _`die_match_name.description`:

Description
-----------

Glob matching the name of \ ``dw_die``\  and \ ``glob``\ . Return false if matching fail.
This also match linkage name.

.. _`die_get_call_lineno`:

die_get_call_lineno
===================

.. c:function:: int die_get_call_lineno(Dwarf_Die *in_die)

    Get callsite line number of inline-function instance

    :param Dwarf_Die \*in_die:
        a DIE of an inlined function instance

.. _`die_get_call_lineno.description`:

Description
-----------

Get call-site line number of \ ``in_die``\ . This means from where the inline
function is called.

.. _`die_get_type`:

die_get_type
============

.. c:function:: Dwarf_Die *die_get_type(Dwarf_Die *vr_die, Dwarf_Die *die_mem)

    Get type DIE

    :param Dwarf_Die \*vr_die:
        a DIE of a variable

    :param Dwarf_Die \*die_mem:
        where to store a type DIE

.. _`die_get_type.description`:

Description
-----------

Get a DIE of the type of given variable (@vr_die), and store
it to die_mem. Return NULL if fails to get a type DIE.

.. _`die_get_real_type`:

die_get_real_type
=================

.. c:function:: Dwarf_Die *die_get_real_type(Dwarf_Die *vr_die, Dwarf_Die *die_mem)

    Get a type die, but skip qualifiers and typedef

    :param Dwarf_Die \*vr_die:
        a DIE of a variable

    :param Dwarf_Die \*die_mem:
        where to store a type DIE

.. _`die_get_real_type.description`:

Description
-----------

Get a DIE of the type of given variable (@vr_die), and store
it to die_mem. Return NULL if fails to get a type DIE.
If the type is qualifiers (e.g. const) or typedef, this skips it
and tries to find real type (structure or basic types, e.g. int).

.. _`die_is_signed_type`:

die_is_signed_type
==================

.. c:function:: bool die_is_signed_type(Dwarf_Die *tp_die)

    Check whether a type DIE is signed or not

    :param Dwarf_Die \*tp_die:
        a DIE of a type

.. _`die_is_signed_type.description`:

Description
-----------

Get the encoding of \ ``tp_die``\  and return true if the encoding
is signed.

.. _`die_is_func_def`:

die_is_func_def
===============

.. c:function:: bool die_is_func_def(Dwarf_Die *dw_die)

    Ensure that this DIE is a subprogram and definition

    :param Dwarf_Die \*dw_die:
        a DIE

.. _`die_is_func_def.description`:

Description
-----------

Ensure that this DIE is a subprogram and NOT a declaration. This
returns true if \ ``dw_die``\  is a function definition.

.. _`die_is_func_instance`:

die_is_func_instance
====================

.. c:function:: bool die_is_func_instance(Dwarf_Die *dw_die)

    Ensure that this DIE is an instance of a subprogram

    :param Dwarf_Die \*dw_die:
        a DIE

.. _`die_is_func_instance.description`:

Description
-----------

Ensure that this DIE is an instance (which has an entry address).
This returns true if \ ``dw_die``\  is a function instance. If not, you need to
call \ :c:func:`die_walk_instances`\  to find actual instances.

.. _`die_get_data_member_location`:

die_get_data_member_location
============================

.. c:function:: int die_get_data_member_location(Dwarf_Die *mb_die, Dwarf_Word *offs)

    Get the data-member offset

    :param Dwarf_Die \*mb_die:
        a DIE of a member of a data structure

    :param Dwarf_Word \*offs:
        The offset of the member in the data structure

.. _`die_get_data_member_location.description`:

Description
-----------

Get the offset of \ ``mb_die``\  in the data structure including \ ``mb_die``\ , and
stores result offset to \ ``offs``\ . If any error occurs this returns errno.

.. _`die_get_call_file`:

die_get_call_file
=================

.. c:function:: const char *die_get_call_file(Dwarf_Die *in_die)

    Get callsite file name of inlined function instance

    :param Dwarf_Die \*in_die:
        a DIE of an inlined function instance

.. _`die_get_call_file.description`:

Description
-----------

Get call-site file name of \ ``in_die``\ . This means from which file the inline
function is called.

.. _`die_find_child`:

die_find_child
==============

.. c:function:: Dwarf_Die *die_find_child(Dwarf_Die *rt_die, int (*callback)(Dwarf_Die *, void *), void *data, Dwarf_Die *die_mem)

    Generic DIE search function in DIE tree

    :param Dwarf_Die \*rt_die:
        a root DIE

    :param int (\*callback)(Dwarf_Die \*, void \*):
        a callback function

    :param void \*data:
        a user data passed to the callback function

    :param Dwarf_Die \*die_mem:
        a buffer for result DIE

.. _`die_find_child.description`:

Description
-----------

Trace DIE tree from \ ``rt_die``\  and call \ ``callback``\  for each child DIE.
If \ ``callback``\  returns DIE_FIND_CB_END, this stores the DIE into
\ ``die_mem``\  and returns it. If \ ``callback``\  returns DIE_FIND_CB_CONTINUE,
this continues to trace the tree. Optionally, \ ``callback``\  can return
DIE_FIND_CB_CHILD and DIE_FIND_CB_SIBLING, those means trace only
the children and trace only the siblings respectively.
Returns NULL if \ ``callback``\  can't find any appropriate DIE.

.. _`die_find_tailfunc`:

die_find_tailfunc
=================

.. c:function:: Dwarf_Die *die_find_tailfunc(Dwarf_Die *cu_die, Dwarf_Addr addr, Dwarf_Die *die_mem)

    Search for a non-inlined function with tail call at given address

    :param Dwarf_Die \*cu_die:
        a CU DIE which including \ ``addr``\ 

    :param Dwarf_Addr addr:
        target address

    :param Dwarf_Die \*die_mem:
        a buffer for result DIE

.. _`die_find_tailfunc.description`:

Description
-----------

Search for a non-inlined function DIE with tail call at \ ``addr``\ . Stores the
DIE to \ ``die_mem``\  and returns it if found. Returns NULL if failed.

.. _`die_find_realfunc`:

die_find_realfunc
=================

.. c:function:: Dwarf_Die *die_find_realfunc(Dwarf_Die *cu_die, Dwarf_Addr addr, Dwarf_Die *die_mem)

    Search a non-inlined function at given address

    :param Dwarf_Die \*cu_die:
        a CU DIE which including \ ``addr``\ 

    :param Dwarf_Addr addr:
        target address

    :param Dwarf_Die \*die_mem:
        a buffer for result DIE

.. _`die_find_realfunc.description`:

Description
-----------

Search a non-inlined function DIE which includes \ ``addr``\ . Stores the
DIE to \ ``die_mem``\  and returns it if found. Returns NULL if failed.

.. _`die_find_top_inlinefunc`:

die_find_top_inlinefunc
=======================

.. c:function:: Dwarf_Die *die_find_top_inlinefunc(Dwarf_Die *sp_die, Dwarf_Addr addr, Dwarf_Die *die_mem)

    Search the top inlined function at given address

    :param Dwarf_Die \*sp_die:
        a subprogram DIE which including \ ``addr``\ 

    :param Dwarf_Addr addr:
        target address

    :param Dwarf_Die \*die_mem:
        a buffer for result DIE

.. _`die_find_top_inlinefunc.description`:

Description
-----------

Search an inlined function DIE which includes \ ``addr``\ . Stores the
DIE to \ ``die_mem``\  and returns it if found. Returns NULL if failed.
Even if several inlined functions are expanded recursively, this
doesn't trace it down, and returns the topmost one.

.. _`die_find_inlinefunc`:

die_find_inlinefunc
===================

.. c:function:: Dwarf_Die *die_find_inlinefunc(Dwarf_Die *sp_die, Dwarf_Addr addr, Dwarf_Die *die_mem)

    Search an inlined function at given address

    :param Dwarf_Die \*sp_die:
        a subprogram DIE which including \ ``addr``\ 

    :param Dwarf_Addr addr:
        target address

    :param Dwarf_Die \*die_mem:
        a buffer for result DIE

.. _`die_find_inlinefunc.description`:

Description
-----------

Search an inlined function DIE which includes \ ``addr``\ . Stores the
DIE to \ ``die_mem``\  and returns it if found. Returns NULL if failed.
If several inlined functions are expanded recursively, this trace
it down and returns deepest one.

.. _`die_walk_instances`:

die_walk_instances
==================

.. c:function:: int die_walk_instances(Dwarf_Die *or_die, int (*callback)(Dwarf_Die *, void *), void *data)

    Walk on instances of given DIE

    :param Dwarf_Die \*or_die:
        an abstract original DIE

    :param int (\*callback)(Dwarf_Die \*, void \*):
        a callback function which is called with instance DIE

    :param void \*data:
        user data

.. _`die_walk_instances.description`:

Description
-----------

Walk on the instances of give \ ``in_die``\ . \ ``in_die``\  must be an inlined function
declartion. This returns the return value of \ ``callback``\  if it returns
non-zero value, or -ENOENT if there is no instance.

.. _`die_walk_lines`:

die_walk_lines
==============

.. c:function:: int die_walk_lines(Dwarf_Die *rt_die, line_walk_callback_t callback, void *data)

    Walk on lines inside given DIE

    :param Dwarf_Die \*rt_die:
        a root DIE (CU, subprogram or inlined_subroutine)

    :param line_walk_callback_t callback:
        callback routine

    :param void \*data:
        user data

.. _`die_walk_lines.description`:

Description
-----------

Walk on all lines inside given \ ``rt_die``\  and call \ ``callback``\  on each line.
If the \ ``rt_die``\  is a function, walk only on the lines inside the function,
otherwise \ ``rt_die``\  must be a CU DIE.
Note that this walks not only dwarf line list, but also function entries
and inline call-site.

.. _`die_find_variable_at`:

die_find_variable_at
====================

.. c:function:: Dwarf_Die *die_find_variable_at(Dwarf_Die *sp_die, const char *name, Dwarf_Addr addr, Dwarf_Die *die_mem)

    Find a given name variable at given address

    :param Dwarf_Die \*sp_die:
        a function DIE

    :param const char \*name:
        variable name

    :param Dwarf_Addr addr:
        address

    :param Dwarf_Die \*die_mem:
        a buffer for result DIE

.. _`die_find_variable_at.description`:

Description
-----------

Find a variable DIE called \ ``name``\  at \ ``addr``\  in \ ``sp_die``\ .

.. _`die_find_member`:

die_find_member
===============

.. c:function:: Dwarf_Die *die_find_member(Dwarf_Die *st_die, const char *name, Dwarf_Die *die_mem)

    Find a given name member in a data structure

    :param Dwarf_Die \*st_die:
        a data structure type DIE

    :param const char \*name:
        member name

    :param Dwarf_Die \*die_mem:
        a buffer for result DIE

.. _`die_find_member.description`:

Description
-----------

Find a member DIE called \ ``name``\  in \ ``st_die``\ .

.. _`die_get_typename`:

die_get_typename
================

.. c:function:: int die_get_typename(Dwarf_Die *vr_die, struct strbuf *buf)

    Get the name of given variable DIE

    :param Dwarf_Die \*vr_die:
        a variable DIE

    :param struct strbuf \*buf:
        a strbuf for result type name

.. _`die_get_typename.description`:

Description
-----------

Get the name of \ ``vr_die``\  and stores it to \ ``buf``\ . Return 0 if succeeded.
and Return -ENOENT if failed to find type name.
Note that the result will stores typedef name if possible, and stores
"\*(function_type)" if the type is a function pointer.

.. _`die_get_varname`:

die_get_varname
===============

.. c:function:: int die_get_varname(Dwarf_Die *vr_die, struct strbuf *buf)

    Get the name and type of given variable DIE

    :param Dwarf_Die \*vr_die:
        a variable DIE

    :param struct strbuf \*buf:
        a strbuf for type and variable name

.. _`die_get_varname.description`:

Description
-----------

Get the name and type of \ ``vr_die``\  and stores it in \ ``buf``\  as "type\tname".

.. _`die_get_var_innermost_scope`:

die_get_var_innermost_scope
===========================

.. c:function:: int die_get_var_innermost_scope(Dwarf_Die *sp_die, Dwarf_Die *vr_die, struct strbuf *buf)

    Get innermost scope range of given variable DIE

    :param Dwarf_Die \*sp_die:
        a subprogram DIE

    :param Dwarf_Die \*vr_die:
        a variable DIE

    :param struct strbuf \*buf:
        a strbuf for variable byte offset range

.. _`die_get_var_innermost_scope.description`:

Description
-----------

Get the innermost scope range of \ ``vr_die``\  and stores it in \ ``buf``\  as
"@<function_name+[NN-NN,NN-NN]>".

.. _`die_get_var_range`:

die_get_var_range
=================

.. c:function:: int die_get_var_range(Dwarf_Die *sp_die, Dwarf_Die *vr_die, struct strbuf *buf)

    Get byte offset range of given variable DIE

    :param Dwarf_Die \*sp_die:
        a subprogram DIE

    :param Dwarf_Die \*vr_die:
        a variable DIE

    :param struct strbuf \*buf:
        a strbuf for type and variable name and byte offset range

.. _`die_get_var_range.description`:

Description
-----------

Get the byte offset range of \ ``vr_die``\  and stores it in \ ``buf``\  as
"@<function_name+[NN-NN,NN-NN]>".

.. This file was automatic generated / don't edit.

