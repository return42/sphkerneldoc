.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/moduleparam.h

.. _`module_param`:

module_param
============

.. c:function::  module_param( name,  type,  perm)

    typesafe helper for a module/cmdline parameter

    :param  name:
        *undescribed*

    :param  type:
        the type of the parameter

    :param  perm:
        visibility in sysfs.

.. _`module_param.description`:

Description
-----------

\ ``value``\  becomes the module parameter, or (prefixed by KBUILD_MODNAME and a
".") the kernel commandline parameter.  Note that - is changed to _, so
the user can use "foo-bar=1" even for variable "foo_bar".

\ ``perm``\  is 0 if the the variable is not to appear in sysfs, or 0444
for world-readable, 0644 for root-writable, etc.  Note that if it
is writable, you may need to use \ :c:func:`kernel_param_lock`\  around
accesses (esp. charp, which can be kfreed when it changes).

The \ ``type``\  is simply pasted to refer to a param_ops_##type and a
param_check_##type: for convenience many standard types are provided but
you can create your own by defining those variables.

.. _`module_param.standard-types-are`:

Standard types are
------------------

byte, short, ushort, int, uint, long, ulong

.. _`module_param.charp`:

charp
-----

a character pointer

.. _`module_param.bool`:

bool
----

a bool, values 0/1, y/n, Y/N.

.. _`module_param.invbool`:

invbool
-------

the above, only sense-reversed (N = true).

.. _`module_param_unsafe`:

module_param_unsafe
===================

.. c:function::  module_param_unsafe( name,  type,  perm)

    same as module_param but taints kernel

    :param  name:
        *undescribed*

    :param  type:
        *undescribed*

    :param  perm:
        *undescribed*

.. _`module_param_named`:

module_param_named
==================

.. c:function::  module_param_named( name,  value,  type,  perm)

    typesafe helper for a renamed module/cmdline parameter

    :param  name:
        a valid C identifier which is the parameter name.

    :param  value:
        the actual lvalue to alter.

    :param  type:
        the type of the parameter

    :param  perm:
        visibility in sysfs.

.. _`module_param_named.description`:

Description
-----------

Usually it's a good idea to have variable names and user-exposed names the
same, but that's harder if the variable must be non-static or is inside a
structure.  This allows exposure under a different name.

.. _`module_param_named_unsafe`:

module_param_named_unsafe
=========================

.. c:function::  module_param_named_unsafe( name,  value,  type,  perm)

    same as module_param_named but taints kernel

    :param  name:
        *undescribed*

    :param  value:
        *undescribed*

    :param  type:
        *undescribed*

    :param  perm:
        *undescribed*

.. _`module_param_cb`:

module_param_cb
===============

.. c:function::  module_param_cb( name,  ops,  arg,  perm)

    general callback for a module/cmdline parameter

    :param  name:
        a valid C identifier which is the parameter name.

    :param  ops:
        the set & get operations for this parameter.

    :param  arg:
        *undescribed*

    :param  perm:
        visibility in sysfs.

.. _`module_param_cb.description`:

Description
-----------

The ops can have NULL set or get functions.

.. _`core_param`:

core_param
==========

.. c:function::  core_param( name,  var,  type,  perm)

    define a historical core kernel parameter.

    :param  name:
        the name of the cmdline and sysfs parameter (often the same as var)

    :param  var:
        the variable

    :param  type:
        the type of the parameter

    :param  perm:
        visibility in sysfs

.. _`core_param.description`:

Description
-----------

core_param is just like \ :c:func:`module_param`\ , but cannot be modular and
doesn't add a prefix (such as "printk.").  This is for compatibility
with \\ :c:func:`__setup`\ , and it makes sense as truly core parameters aren't
tied to the particular file they're in.

.. _`core_param_unsafe`:

core_param_unsafe
=================

.. c:function::  core_param_unsafe( name,  var,  type,  perm)

    same as core_param but taints kernel

    :param  name:
        *undescribed*

    :param  var:
        *undescribed*

    :param  type:
        *undescribed*

    :param  perm:
        *undescribed*

.. _`module_param_string`:

module_param_string
===================

.. c:function::  module_param_string( name,  string,  len,  perm)

    a char array parameter

    :param  name:
        the name of the parameter

    :param  string:
        the string variable

    :param  len:
        the maximum length of the string, incl. terminator

    :param  perm:
        visibility in sysfs.

.. _`module_param_string.description`:

Description
-----------

This actually copies the string when it's set (unlike type charp).
\ ``len``\  is usually just sizeof(string).

.. _`parameq`:

parameq
=======

.. c:function:: bool parameq(const char *name1, const char *name2)

    checks if two parameter names match

    :param const char \*name1:
        parameter name 1

    :param const char \*name2:
        parameter name 2

.. _`parameq.description`:

Description
-----------

Returns true if the two parameter names are equal.
Dashes (-) are considered equal to underscores (_).

.. _`parameqn`:

parameqn
========

.. c:function:: bool parameqn(const char *name1, const char *name2, size_t n)

    checks if two parameter names match

    :param const char \*name1:
        parameter name 1

    :param const char \*name2:
        parameter name 2

    :param size_t n:
        the length to compare

.. _`parameqn.description`:

Description
-----------

Similar to \ :c:func:`parameq`\ , except it compares \ ``n``\  characters.

.. _`module_param_array`:

module_param_array
==================

.. c:function::  module_param_array( name,  type,  nump,  perm)

    a parameter which is an array of some type

    :param  name:
        the name of the array variable

    :param  type:
        the type, as per \ :c:func:`module_param`\ 

    :param  nump:
        optional pointer filled in with the number written

    :param  perm:
        visibility in sysfs

.. _`module_param_array.description`:

Description
-----------

Input and output are as comma-separated values.  Commas inside values
don't work properly (eg. an array of charp).

ARRAY_SIZE(\ ``name``\ ) is used to determine the number of elements in the
array, so the definition must be visible.

.. _`module_param_array_named`:

module_param_array_named
========================

.. c:function::  module_param_array_named( name,  array,  type,  nump,  perm)

    renamed parameter which is an array of some type

    :param  name:
        a valid C identifier which is the parameter name

    :param  array:
        the name of the array variable

    :param  type:
        the type, as per \ :c:func:`module_param`\ 

    :param  nump:
        optional pointer filled in with the number written

    :param  perm:
        visibility in sysfs

.. _`module_param_array_named.description`:

Description
-----------

This exposes a different name than the actual variable name.  See
\ :c:func:`module_param_named`\  for why this might be necessary.

.. This file was automatic generated / don't edit.

