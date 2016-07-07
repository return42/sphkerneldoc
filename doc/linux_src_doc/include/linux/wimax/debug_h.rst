.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/wimax/debug.h

.. _`d_modulename`:

D_MODULENAME
============

.. c:function::  D_MODULENAME()

    Name of the current module

.. _`d_modulename.description`:

Description
-----------

#define in your module's debug-levels.h, making sure it is
unique. This has to be a legal C identifier.

.. _`d_master`:

D_MASTER
========

.. c:function::  D_MASTER()

    Compile time maximum debug level

.. _`d_master.description`:

Description
-----------

#define in your debug-levels.h file to the maximum debug level the
runtime code will be allowed to have. This allows you to provide a
main knob.

Anything above that level will be optimized out of the compile.

Defaults to zero (no debug code compiled in).

Maximum one definition per module (at the debug-levels.h file).

.. _`d_submodule`:

D_SUBMODULE
===========

.. c:function::  D_SUBMODULE()

    Name of the current submodule

.. _`d_submodule.description`:

Description
-----------

#define in your submodule .c file before #including debug-levels.h
to the name of the current submodule as previously declared and
defined with \ :c:func:`D_SUBMODULE_DECLARE`\  (in your module's
debug-levels.h) and \ :c:func:`D_SUBMODULE_DEFINE`\ .

This is used to provide runtime-control over the debug levels.

Maximum one per .c file! Can be shared among different .c files
(meaning they belong to the same submodule categorization).

.. _`d_submodule_declare`:

D_SUBMODULE_DECLARE
===================

.. c:function::  D_SUBMODULE_DECLARE( _name)

    Declare a submodule for runtime debug level control

    :param  _name:
        name of the submodule, restricted to the chars that make up a
        valid C identifier ([a-zA-Z0-9_]).

.. _`d_submodule_declare.description`:

Description
-----------

Declare in the module's debug-levels.h header file as:

enum d_module {
D_SUBMODULE_DECLARE(submodule_1),
D_SUBMODULE_DECLARE(submodule_2),
D_SUBMODULE_DECLARE(submodule_3),
};

Some corresponding .c file needs to have a matching
\ :c:func:`D_SUBMODULE_DEFINE`\ .

.. _`d_submodule_define`:

D_SUBMODULE_DEFINE
==================

.. c:function::  D_SUBMODULE_DEFINE( _name)

    Define a submodule for runtime debug level control

    :param  _name:
        name of the submodule, restricted to the chars that make up a
        valid C identifier ([a-zA-Z0-9_]).

.. _`d_submodule_define.description`:

Description
-----------

Use once per module (in some .c file) as:

static
struct d_level d_level_SUBMODULENAME[] = {
D_SUBMODULE_DEFINE(submodule_1),
D_SUBMODULE_DEFINE(submodule_2),
D_SUBMODULE_DEFINE(submodule_3),
};
size_t d_level_size_SUBDMODULENAME = ARRAY_SIZE(d_level_SUBDMODULENAME);

Matching \ :c:func:`D_SUBMODULE_DECLARE`\ s have to be present in a
debug-levels.h header file.

.. _`d_test`:

d_test
======

.. c:function::  d_test( l)

    Returns true if debugging should be enabled

    :param  l:
        intended debug level (unsigned)

.. _`d_test.description`:

Description
-----------

If the master debug switch is enabled and the current settings are
higher or equal to the requested level, then debugging
output/actions should be enabled.

.. _`d_test.note`:

NOTE
----


This needs to be coded so that it can be evaluated in compile
time; this is why the ugly \ :c:func:`BUG_ON`\  is placed in there, so the
D_MASTER evaluation compiles all out if it is compile-time false.

.. _`d_fnstart`:

d_fnstart
=========

.. c:function::  d_fnstart( l,  _dev,  f,  a...)

    log message at function start if debugging enabled

    :param  l:
        intended debug level

    :param  _dev:
        'struct device' pointer, NULL if none (for context)

    :param  f:
        printf-like format and arguments

    :param  a...:
        variable arguments

.. _`d_fnend`:

d_fnend
=======

.. c:function::  d_fnend( l,  _dev,  f,  a...)

    log message at function end if debugging enabled

    :param  l:
        intended debug level

    :param  _dev:
        'struct device' pointer, NULL if none (for context)

    :param  f:
        printf-like format and arguments

    :param  a...:
        variable arguments

.. _`d_printf`:

d_printf
========

.. c:function::  d_printf( l,  _dev,  f,  a...)

    log message if debugging enabled

    :param  l:
        intended debug level

    :param  _dev:
        'struct device' pointer, NULL if none (for context)

    :param  f:
        printf-like format and arguments

    :param  a...:
        variable arguments

.. _`d_dump`:

d_dump
======

.. c:function::  d_dump( l,  dev,  ptr,  size)

    log buffer hex dump if debugging enabled

    :param  l:
        intended debug level

    :param  dev:
        *undescribed*

    :param  ptr:
        *undescribed*

    :param  size:
        *undescribed*

.. _`d_level_register_debugfs`:

d_level_register_debugfs
========================

.. c:function::  d_level_register_debugfs( prefix,  name,  parent)

    :param  prefix:
        string to prefix the name with

    :param  name:
        *undescribed*

    :param  parent:
        *undescribed*

.. _`d_level_register_debugfs.return`:

Return
------

0 if ok, < 0 errno on error.

For removing, just use \ :c:func:`debugfs_remove_recursive`\  on the parent.

.. _`d_parse_params`:

d_parse_params
==============

.. c:function:: void d_parse_params(struct d_level *d_level, size_t d_level_size, const char *_params, const char *tag)

    Parse a string with debug parameters from the command line

    :param struct d_level \*d_level:
        level structure (D_LEVEL)

    :param size_t d_level_size:
        number of items in the level structure
        (D_LEVEL_SIZE).

    :param const char \*_params:
        string with the parameters; this is a space (not tab!)
        separated list of NAME:VALUE, where value is the debug level
        and NAME is the name of the submodule.

    :param const char \*tag:
        string for error messages (example: MODULE.ARGNAME).

.. This file was automatic generated / don't edit.

