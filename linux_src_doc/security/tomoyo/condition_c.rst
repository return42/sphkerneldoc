.. -*- coding: utf-8; mode: rst -*-
.. src-file: security/tomoyo/condition.c

.. _`tomoyo_argv`:

tomoyo_argv
===========

.. c:function:: bool tomoyo_argv(const unsigned int index, const char *arg_ptr, const int argc, const struct tomoyo_argv *argv, u8 *checked)

    Check argv[] in "struct linux_binbrm".

    :param index:
        Index number of \ ``arg_ptr``\ .
    :type index: const unsigned int

    :param arg_ptr:
        Contents of argv[@index].
    :type arg_ptr: const char \*

    :param argc:
        Length of \ ``argv``\ .
    :type argc: const int

    :param argv:
        Pointer to "struct tomoyo_argv".
    :type argv: const struct tomoyo_argv \*

    :param checked:
        Set to true if \ ``argv``\ [@index] was found.
    :type checked: u8 \*

.. _`tomoyo_argv.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_envp`:

tomoyo_envp
===========

.. c:function:: bool tomoyo_envp(const char *env_name, const char *env_value, const int envc, const struct tomoyo_envp *envp, u8 *checked)

    Check envp[] in "struct linux_binbrm".

    :param env_name:
        The name of environment variable.
    :type env_name: const char \*

    :param env_value:
        The value of environment variable.
    :type env_value: const char \*

    :param envc:
        Length of \ ``envp``\ .
    :type envc: const int

    :param envp:
        Pointer to "struct tomoyo_envp".
    :type envp: const struct tomoyo_envp \*

    :param checked:
        Set to true if \ ``envp``\ [@env_name] was found.
    :type checked: u8 \*

.. _`tomoyo_envp.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_scan_bprm`:

tomoyo_scan_bprm
================

.. c:function:: bool tomoyo_scan_bprm(struct tomoyo_execve *ee, const u16 argc, const struct tomoyo_argv *argv, const u16 envc, const struct tomoyo_envp *envp)

    Scan "struct linux_binprm".

    :param ee:
        Pointer to "struct tomoyo_execve".
    :type ee: struct tomoyo_execve \*

    :param argc:
        Length of \ ``argc``\ .
    :type argc: const u16

    :param argv:
        Pointer to "struct tomoyo_argv".
    :type argv: const struct tomoyo_argv \*

    :param envc:
        Length of \ ``envp``\ .
    :type envc: const u16

    :param envp:
        Poiner to "struct tomoyo_envp".
    :type envp: const struct tomoyo_envp \*

.. _`tomoyo_scan_bprm.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_scan_exec_realpath`:

tomoyo_scan_exec_realpath
=========================

.. c:function:: bool tomoyo_scan_exec_realpath(struct file *file, const struct tomoyo_name_union *ptr, const bool match)

    Check "exec.realpath" parameter of "struct tomoyo_condition".

    :param file:
        Pointer to "struct file".
    :type file: struct file \*

    :param ptr:
        Pointer to "struct tomoyo_name_union".
    :type ptr: const struct tomoyo_name_union \*

    :param match:
        True if "exec.realpath=", false if "exec.realpath!=".
    :type match: const bool

.. _`tomoyo_scan_exec_realpath.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_get_dqword`:

tomoyo_get_dqword
=================

.. c:function:: const struct tomoyo_path_info *tomoyo_get_dqword(char *start)

    \ :c:func:`tomoyo_get_name`\  for a quoted string.

    :param start:
        String to save.
    :type start: char \*

.. _`tomoyo_get_dqword.description`:

Description
-----------

Returns pointer to "struct tomoyo_path_info" on success, NULL otherwise.

.. _`tomoyo_parse_name_union_quoted`:

tomoyo_parse_name_union_quoted
==============================

.. c:function:: bool tomoyo_parse_name_union_quoted(struct tomoyo_acl_param *param, struct tomoyo_name_union *ptr)

    Parse a quoted word.

    :param param:
        Pointer to "struct tomoyo_acl_param".
    :type param: struct tomoyo_acl_param \*

    :param ptr:
        Pointer to "struct tomoyo_name_union".
    :type ptr: struct tomoyo_name_union \*

.. _`tomoyo_parse_name_union_quoted.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_parse_argv`:

tomoyo_parse_argv
=================

.. c:function:: bool tomoyo_parse_argv(char *left, char *right, struct tomoyo_argv *argv)

    Parse an argv[] condition part.

    :param left:
        Lefthand value.
    :type left: char \*

    :param right:
        Righthand value.
    :type right: char \*

    :param argv:
        Pointer to "struct tomoyo_argv".
    :type argv: struct tomoyo_argv \*

.. _`tomoyo_parse_argv.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_parse_envp`:

tomoyo_parse_envp
=================

.. c:function:: bool tomoyo_parse_envp(char *left, char *right, struct tomoyo_envp *envp)

    Parse an envp[] condition part.

    :param left:
        Lefthand value.
    :type left: char \*

    :param right:
        Righthand value.
    :type right: char \*

    :param envp:
        Pointer to "struct tomoyo_envp".
    :type envp: struct tomoyo_envp \*

.. _`tomoyo_parse_envp.description`:

Description
-----------

Returns true on success, false otherwise.

.. _`tomoyo_same_condition`:

tomoyo_same_condition
=====================

.. c:function:: bool tomoyo_same_condition(const struct tomoyo_condition *a, const struct tomoyo_condition *b)

    Check for duplicated "struct tomoyo_condition" entry.

    :param a:
        Pointer to "struct tomoyo_condition".
    :type a: const struct tomoyo_condition \*

    :param b:
        Pointer to "struct tomoyo_condition".
    :type b: const struct tomoyo_condition \*

.. _`tomoyo_same_condition.description`:

Description
-----------

Returns true if \ ``a``\  == \ ``b``\ , false otherwise.

.. _`tomoyo_condition_type`:

tomoyo_condition_type
=====================

.. c:function:: u8 tomoyo_condition_type(const char *word)

    Get condition type.

    :param word:
        Keyword string.
    :type word: const char \*

.. _`tomoyo_condition_type.description`:

Description
-----------

Returns one of values in "enum tomoyo_conditions_index" on success,
TOMOYO_MAX_CONDITION_KEYWORD otherwise.

.. _`tomoyo_commit_condition`:

tomoyo_commit_condition
=======================

.. c:function:: struct tomoyo_condition *tomoyo_commit_condition(struct tomoyo_condition *entry)

    Commit "struct tomoyo_condition".

    :param entry:
        Pointer to "struct tomoyo_condition".
    :type entry: struct tomoyo_condition \*

.. _`tomoyo_commit_condition.description`:

Description
-----------

Returns pointer to "struct tomoyo_condition" on success, NULL otherwise.

This function merges duplicated entries. This function returns NULL if
\ ``entry``\  is not duplicated but memory quota for policy has exceeded.

.. _`tomoyo_get_transit_preference`:

tomoyo_get_transit_preference
=============================

.. c:function:: char *tomoyo_get_transit_preference(struct tomoyo_acl_param *param, struct tomoyo_condition *e)

    Parse domain transition preference for \ :c:func:`execve`\ .

    :param param:
        Pointer to "struct tomoyo_acl_param".
    :type param: struct tomoyo_acl_param \*

    :param e:
        Pointer to "struct tomoyo_condition".
    :type e: struct tomoyo_condition \*

.. _`tomoyo_get_transit_preference.description`:

Description
-----------

Returns the condition string part.

.. _`tomoyo_get_condition`:

tomoyo_get_condition
====================

.. c:function:: struct tomoyo_condition *tomoyo_get_condition(struct tomoyo_acl_param *param)

    Parse condition part.

    :param param:
        Pointer to "struct tomoyo_acl_param".
    :type param: struct tomoyo_acl_param \*

.. _`tomoyo_get_condition.description`:

Description
-----------

Returns pointer to "struct tomoyo_condition" on success, NULL otherwise.

.. _`tomoyo_get_attributes`:

tomoyo_get_attributes
=====================

.. c:function:: void tomoyo_get_attributes(struct tomoyo_obj_info *obj)

    Revalidate "struct inode".

    :param obj:
        Pointer to "struct tomoyo_obj_info".
    :type obj: struct tomoyo_obj_info \*

.. _`tomoyo_get_attributes.description`:

Description
-----------

Returns nothing.

.. _`tomoyo_condition`:

tomoyo_condition
================

.. c:function:: bool tomoyo_condition(struct tomoyo_request_info *r, const struct tomoyo_condition *cond)

    Check condition part.

    :param r:
        Pointer to "struct tomoyo_request_info".
    :type r: struct tomoyo_request_info \*

    :param cond:
        Pointer to "struct tomoyo_condition". Maybe NULL.
    :type cond: const struct tomoyo_condition \*

.. _`tomoyo_condition.description`:

Description
-----------

Returns true on success, false otherwise.

Caller holds \ :c:func:`tomoyo_read_lock`\ .

.. This file was automatic generated / don't edit.

